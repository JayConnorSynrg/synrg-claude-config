#!/usr/bin/env node
/**
 * Minimal n8n-workflows MCP Server
 *
 * Only exposes the 3 tools actually used for n8n workflow development:
 * - search_repositories: Find workflow templates
 * - get_file_contents: Fetch workflow JSON files
 * - search_code: Search for node patterns in workflows
 *
 * Saves ~16K tokens by excluding 23 unused GitHub tools
 */

const { Server } = require("@modelcontextprotocol/sdk/server/index.js");
const { StdioServerTransport } = require("@modelcontextprotocol/sdk/server/stdio.js");
const {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} = require("@modelcontextprotocol/sdk/types.js");

const GITHUB_API = "https://api.github.com";
const DEFAULT_REPO = "Zie619/n8n-workflows";

// Get GitHub token from environment (optional, increases rate limit)
const GITHUB_TOKEN = process.env.GITHUB_TOKEN || "";

async function githubRequest(endpoint, options = {}) {
  const headers = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "n8n-workflows-mcp",
  };

  if (GITHUB_TOKEN) {
    headers["Authorization"] = `Bearer ${GITHUB_TOKEN}`;
  }

  const response = await fetch(`${GITHUB_API}${endpoint}`, {
    ...options,
    headers: { ...headers, ...options.headers },
  });

  if (!response.ok) {
    throw new Error(`GitHub API error: ${response.status} ${response.statusText}`);
  }

  return response.json();
}

// Only the 3 tools we actually use
const TOOLS = [
  {
    name: "search_repositories",
    description: "Search for GitHub repositories containing n8n workflows",
    inputSchema: {
      type: "object",
      properties: {
        query: {
          type: "string",
          description: "Search query (GitHub search syntax)"
        },
        perPage: {
          type: "number",
          description: "Results per page (default: 30, max: 100)"
        },
        page: {
          type: "number",
          description: "Page number (default: 1)"
        }
      },
      required: ["query"]
    }
  },
  {
    name: "get_file_contents",
    description: "Get contents of a file from a GitHub repository (typically n8n workflow JSON)",
    inputSchema: {
      type: "object",
      properties: {
        owner: {
          type: "string",
          description: "Repository owner (default: Zie619)"
        },
        repo: {
          type: "string",
          description: "Repository name (default: n8n-workflows)"
        },
        path: {
          type: "string",
          description: "Path to the file"
        },
        branch: {
          type: "string",
          description: "Branch name (optional)"
        }
      },
      required: ["path"]
    }
  },
  {
    name: "search_code",
    description: "Search for code patterns in GitHub repositories (e.g., find n8n node configurations)",
    inputSchema: {
      type: "object",
      properties: {
        q: {
          type: "string",
          description: "Search query (GitHub code search syntax)"
        },
        per_page: {
          type: "number",
          description: "Results per page (max: 100)"
        },
        page: {
          type: "number",
          description: "Page number"
        }
      },
      required: ["q"]
    }
  }
];

async function handleToolCall(name, args) {
  switch (name) {
    case "search_repositories": {
      const { query, perPage = 30, page = 1 } = args;
      const params = new URLSearchParams({
        q: query,
        per_page: Math.min(perPage, 100).toString(),
        page: page.toString()
      });
      return await githubRequest(`/search/repositories?${params}`);
    }

    case "get_file_contents": {
      const { owner = "Zie619", repo = "n8n-workflows", path, branch } = args;
      let endpoint = `/repos/${owner}/${repo}/contents/${path}`;
      if (branch) {
        endpoint += `?ref=${branch}`;
      }
      const result = await githubRequest(endpoint);

      // Decode base64 content if it's a file
      if (result.content && result.encoding === "base64") {
        result.decoded_content = Buffer.from(result.content, "base64").toString("utf-8");
      }

      return result;
    }

    case "search_code": {
      const { q, per_page = 30, page = 1 } = args;
      // Add default repo scope if not specified
      const query = q.includes("repo:") ? q : `${q} repo:${DEFAULT_REPO}`;
      const params = new URLSearchParams({
        q: query,
        per_page: Math.min(per_page, 100).toString(),
        page: page.toString()
      });
      return await githubRequest(`/search/code?${params}`);
    }

    default:
      throw new Error(`Unknown tool: ${name}`);
  }
}

async function main() {
  const server = new Server(
    {
      name: "n8n-workflows-minimal",
      version: "1.0.0",
    },
    {
      capabilities: {
        tools: {},
      },
    }
  );

  server.setRequestHandler(ListToolsRequestSchema, async () => ({
    tools: TOOLS,
  }));

  server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;

    try {
      const result = await handleToolCall(name, args || {});
      return {
        content: [
          {
            type: "text",
            text: JSON.stringify(result, null, 2),
          },
        ],
      };
    } catch (error) {
      return {
        content: [
          {
            type: "text",
            text: `Error: ${error.message}`,
          },
        ],
        isError: true,
      };
    }
  });

  const transport = new StdioServerTransport();
  await server.connect(transport);

  console.error("n8n-workflows-minimal MCP server running");
}

main().catch(console.error);
