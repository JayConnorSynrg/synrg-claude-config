# MANDATORY CONTEXT DELEGATION PROTOCOL (MCDP v1.0)

**Version**: 1.0.0
**Created**: 2025-01-09
**Authority**: ABSOLUTE - Zero Exceptions
**Scope**: ALL SYNRG Commands

---

## ABSOLUTE MANDATE

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ██████████████████████████████████████████████████████████████████████████│
│  █                                                                         █│
│  █  MANDATORY CONTEXT DELEGATION PROTOCOL                                  █│
│  █                                                                         █│
│  █  ALL of the following operations MUST be delegated to sub-agents:       █│
│  █                                                                         █│
│  █  1. LARGE DOCUMENT READS (>500 tokens expected response)                █│
│  █  2. ALL MCP TOOL CALLS (zero exceptions)                                █│
│  █  3. ALL CONTEXT GATHERING OPERATIONS                                    █│
│  █                                                                         █│
│  █  VIOLATION = IMMEDIATE SELF-CORRECTION REQUIRED                         █│
│  █                                                                         █│
│  ██████████████████████████████████████████████████████████████████████████│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. LARGE DOCUMENT DELEGATION

**Definition**: Any file read expected to return >500 tokens

**Trigger Detection**:
```javascript
// Before ANY file read operation, assess:
const shouldDelegate = {
  largeFiles: [
    '*.md > 5KB',           // Markdown documentation
    '*.json > 10KB',        // Large JSON configs
    '*.ts/*.js > 500 lines', // Large source files
    'package.json',         // Always delegate for dependency analysis
    'README.md',            // Always delegate for project context
    '*.log',                // Log files (always large)
  ],
  patterns: [
    /workflow.*\.json/i,    // n8n workflows
    /schema\.(ts|json)/i,   // Schema definitions
    /config\./i,            // Configuration files
    /\.claude\//,           // SYNRG command files
  ]
};
```

**MANDATORY DELEGATION**:
```javascript
// ❌ FORBIDDEN - Direct large file read
const content = await Read({ file_path: "large-file.md" });

// ✅ REQUIRED - Delegate to sub-agent
Task({
  subagent_type: "Explore",
  prompt: `Read and analyze ${file}. Return:
    - Summary (2-3 sentences)
    - Key sections/concepts
    - Specific data points needed: [specify]
    - References for follow-up`,
  model: "haiku"
});
```

**Sub-Agent Return Format**:
```javascript
{
  summary: "Brief 2-3 sentence overview",
  keyConcepts: ["concept1", "concept2"],
  extractedData: { /* Only requested data points */ },
  references: { /* Line numbers/sections for follow-up */ },
  contextReduction: "90%"  // How much context was saved
}
```

---

## 2. MCP TOOL DELEGATION (Zero Exceptions)

**Definition**: ANY tool call starting with `mcp__*`

**ABSOLUTE RULE**:
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  🚫 NEVER CALL ANY MCP TOOL DIRECTLY                                        │
│                                                                             │
│  mcp__n8n-mcp__*        → Task({ subagent_type: "n8n-mcp-delegate" })       │
│  mcp__n8n-workflows__*  → Task({ subagent_type: "github-mcp-delegate" })    │
│  mcp__*                 → Task({ subagent_type: appropriate-delegate })     │
│                                                                             │
│  NO EXCEPTIONS. EVER.                                                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

**MCP Delegate Agent Registry**:

| MCP Domain | Delegate Agent | Context Reduction |
|------------|----------------|-------------------|
| `mcp__n8n-mcp__*` | `n8n-mcp-delegate` | 70-96% |
| `mcp__n8n-workflows__*` | `github-mcp-delegate` | 70-90% |

**Delegation Template**:
```javascript
// For n8n MCP operations
Task({
  subagent_type: "n8n-mcp-delegate",
  prompt: `Execute MCP operation:
    Tool: mcp__n8n-mcp__${toolName}
    Parameters: ${JSON.stringify(params)}

    Return ONLY:
    - Summary of result (2-3 sentences)
    - Vital extracted data
    - Issues/warnings detected
    - IDs/references for follow-up

    DO NOT return raw JSON payloads.`,
  model: "haiku"
});

// For GitHub MCP operations
Task({
  subagent_type: "github-mcp-delegate",
  prompt: `Execute MCP operation:
    Tool: mcp__n8n-workflows__${toolName}
    Parameters: ${JSON.stringify(params)}

    Return ONLY:
    - Summary of findings
    - Key patterns/concepts
    - Actionable recommendations

    DO NOT return full file contents.`,
  model: "haiku"
});
```

---

## 3. CONTEXT GATHERING DELEGATION

**Definition**: Any operation that gathers information about:
- Codebase structure
- File contents/patterns
- Dependencies
- Configuration state
- Git history
- External documentation

**MANDATORY DELEGATION FOR**:

### 3.1 Codebase Exploration
```javascript
// ❌ FORBIDDEN - Direct exploration
const files = await Glob({ pattern: "**/*.ts" });
for (const file of files) {
  const content = await Read({ file_path: file });
  // Process...
}

// ✅ REQUIRED - Delegate to Explore agent
Task({
  subagent_type: "Explore",
  prompt: `Explore codebase to find: [objective]
    Return:
    - Relevant files with brief descriptions
    - Key patterns identified
    - Recommendations for [task]`,
  model: "haiku"  // or "sonnet" for complex exploration
});
```

### 3.2 Architecture Analysis
```javascript
// ✅ REQUIRED - Delegate architecture reconnaissance
Task({
  subagent_type: "general-purpose",
  prompt: `Analyze architecture for: [objective]
    Focus on:
    - Directory structure
    - Module boundaries
    - Dependency graph
    - Integration points

    Return distilled findings, not raw file contents.`,
  model: "sonnet"
});
```

### 3.3 Dependency Analysis
```javascript
// ✅ REQUIRED - Delegate dependency analysis
Task({
  subagent_type: "general-purpose",
  prompt: `Analyze dependencies:
    - Read package.json/requirements.txt
    - Map internal imports
    - Identify external packages
    - Flag security concerns

    Return summary with key findings only.`,
  model: "haiku"
});
```

### 3.4 Git History Analysis
```javascript
// ✅ REQUIRED - Delegate git analysis
Task({
  subagent_type: "general-purpose",
  prompt: `Analyze git history for: [objective]
    Execute: git log, git diff, git blame as needed
    Return:
    - Summary of changes
    - Key patterns
    - Relevant commits`,
  model: "haiku"
});
```

---

## DELEGATION DECISION FLOWCHART

```
                    ┌─────────────────────────┐
                    │  OPERATION DETECTED      │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  Is it an MCP call?      │
                    │  (mcp__*)               │
                    └───────────┬─────────────┘
                         YES    │    NO
                   ┌────────────┼────────────┐
                   │                         │
          ┌────────▼────────┐       ┌────────▼────────┐
          │ MUST DELEGATE   │       │ Is it a file    │
          │ to MCP-delegate │       │ read >500 tokens?│
          └─────────────────┘       └────────┬────────┘
                                        YES  │  NO
                                  ┌──────────┼──────────┐
                                  │                     │
                         ┌────────▼────────┐   ┌────────▼────────┐
                         │ MUST DELEGATE   │   │ Is it context   │
                         │ to Explore/     │   │ gathering?      │
                         │ general-purpose │   └────────┬────────┘
                         └─────────────────┘       YES  │  NO
                                             ┌─────────┼─────────┐
                                             │                   │
                                    ┌────────▼────────┐ ┌────────▼────────┐
                                    │ MUST DELEGATE   │ │ MAY execute     │
                                    │ to appropriate  │ │ directly        │
                                    │ sub-agent       │ │ (simple ops)    │
                                    └─────────────────┘ └─────────────────┘
```

---

## SELF-ENFORCEMENT PROTOCOL

**Before EVERY operation, perform this check**:

```javascript
function enforceDelegation(operation) {
  // CHECK 1: MCP Tools
  if (operation.startsWith('mcp__')) {
    throw new Error(`
      ⛔ DELEGATION VIOLATION DETECTED

      Operation: ${operation}
      Required: Task({ subagent_type: "${getMCPDelegate(operation)}" })

      STOP. Construct proper delegation.
    `);
  }

  // CHECK 2: Large File Reads
  if (operation === 'Read' && isLargeFile(params.file_path)) {
    throw new Error(`
      ⛔ DELEGATION VIOLATION DETECTED

      Operation: Read large file (${params.file_path})
      Required: Task({ subagent_type: "Explore" or "general-purpose" })

      STOP. Delegate document reading.
    `);
  }

  // CHECK 3: Context Gathering
  if (isContextGatheringOperation(operation)) {
    throw new Error(`
      ⛔ DELEGATION VIOLATION DETECTED

      Operation: ${operation}
      Required: Task({ subagent_type: "appropriate-agent" })

      STOP. Delegate context gathering.
    `);
  }

  return true; // Operation is compliant
}
```

---

## VIOLATION DETECTION & CORRECTION

**If a violation is detected (including self-detection)**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  VIOLATION DETECTED - MANDATORY CORRECTION SEQUENCE                         │
│                                                                             │
│  1. HALT current operation immediately                                      │
│  2. LOG violation type and operation                                        │
│  3. CONSTRUCT proper delegation                                             │
│  4. EXECUTE via Task() with appropriate agent                               │
│  5. CONTINUE only with delegated result                                     │
│                                                                             │
│  NO EXCEPTIONS. NO BYPASSES. NO JUSTIFICATIONS.                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## SUB-AGENT PROMPT INJECTION

**ALL sub-agents MUST include this delegation inheritance**:

```markdown
## DELEGATION INHERITANCE (MANDATORY)

You are a sub-agent operating under SYNRG's Mandatory Context Delegation Protocol.

**YOU MUST ALSO DELEGATE**:
- MCP tool calls → Create nested Task() calls to MCP delegates
- Large document reads → Return summaries, not full content
- Context gathering → Focus on distilled, actionable findings

**YOUR RETURN FORMAT**:
- Summary (2-3 sentences max)
- Key findings (bulleted, concise)
- Extracted data (only what was requested)
- References (for follow-up if needed)

**NEVER RETURN**:
- Full file contents
- Raw JSON payloads
- Verbose explanations
- Unrequested information
```

---

## CONTEXT EFFICIENCY METRICS

**Expected context reduction per delegation type**:

| Delegation Type | Raw Context | Delegated Return | Reduction |
|-----------------|-------------|------------------|-----------|
| MCP Tool Call | 10,000-50,000 tokens | 500-2,000 tokens | 70-96% |
| Large File Read | 2,000-20,000 tokens | 200-1,000 tokens | 85-95% |
| Codebase Explore | 5,000-50,000 tokens | 500-2,000 tokens | 80-96% |
| Git History | 2,000-10,000 tokens | 200-800 tokens | 85-92% |
| Architecture | 10,000-100,000 tokens | 1,000-3,000 tokens | 90-97% |

---

## COMMAND-SPECIFIC DELEGATION EXAMPLES

### /synrg (Director-Orchestrator)
```javascript
// Reconnaissance Phase - ALL delegated
const reconAgents = [
  Task({ subagent_type: "Explore", prompt: "Codebase structure..." }),
  Task({ subagent_type: "general-purpose", prompt: "Dependencies..." }),
  Task({ subagent_type: "general-purpose", prompt: "Quality metrics..." }),
];
await Promise.all(reconAgents); // Parallel execution
```

### /synrg-buildworkflow
```javascript
// ALL n8n operations - delegated
const workflowData = await Task({
  subagent_type: "n8n-mcp-delegate",
  prompt: "Get workflow structure and node configurations..."
});

const nodeSchemas = await Task({
  subagent_type: "n8n-mcp-delegate",
  prompt: "Get schemas for nodes: [list]..."
});
```

### /synrg-commit
```javascript
// Git analysis - delegated
const gitAnalysis = await Task({
  subagent_type: "general-purpose",
  prompt: "Analyze git diff, history, and context for commit decomposition..."
});
```

---

## ABSOLUTE RULES SUMMARY

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ABSOLUTE RULES - MEMORIZE AND ENFORCE                                      │
│                                                                             │
│  1. NEVER call mcp__* directly → ALWAYS delegate to MCP agents              │
│  2. NEVER read large docs directly → ALWAYS delegate and get summaries      │
│  3. NEVER gather context in main thread → ALWAYS spawn sub-agents           │
│  4. ALWAYS return distilled findings → NEVER raw payloads                   │
│  5. ALWAYS check before operations → NEVER assume compliance                │
│  6. ALWAYS self-correct violations → NEVER justify or bypass                │
│                                                                             │
│  THESE RULES ARE ABSOLUTE. ZERO EXCEPTIONS. ZERO TOLERANCE.                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

**MCDP v1.0 - Mandatory Context Delegation Protocol**
**Authority: SYNRG Orchestration System**
**Enforcement: Absolute**
