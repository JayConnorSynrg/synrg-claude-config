---
synrg_version: "2.0.0"
command: "synrg-scaffold"
created: "2025-07-01"
updated: "2026-01-09"
min_claude_version: "opus-4"
requires:
  protocols: [phase-gate]
  agents: []
  skills: [universal-synrg-protocols]
breaking_changes: []
description: SYNRG-SCAFFOLD - Guided Evolving Project Directory Builder with Strategic Intelligence
argument-hint: [project type or directory path]
---

# SYNRG-SCAFFOLD: Guided Evolving Project Directory Builder with Strategic Intelligence

**Purpose:** Intelligent project scaffolding with evolving context-aware questions and strategic alternative analysis
**Philosophy:** Understand the project type first, then analyze alternatives and provide top 1% insights before building the perfect structure

---

## 📅 DOCUMENTATION FRESHNESS PROTOCOL (v1.0)

**MANDATORY for all web searches, API references, and documentation lookups:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ⏰ DOCUMENTATION FRESHNESS GATE                                        │
│                                                                         │
│  1. DETERMINE current date from system/context                          │
│  2. SEARCH with current year appended to all queries                    │
│  3. REJECT documentation older than 1 year                              │
│  4. VERIFY 6+ month old docs are still current                          │
│                                                                         │
│  ALWAYS seek the LATEST version - never settle for outdated docs        │
└─────────────────────────────────────────────────────────────────────────┘
```

**Sub-Agent Injection**:
```
📅 DOCUMENTATION FRESHNESS: Determine current date first.
Always search for LATEST docs by appending current year to queries.
Reject docs older than 1 year.
```

---

## 🚨 HARD GATE: MCP Delegation Enforcement (v2.0) - MANDATORY

**ZERO TOLERANCE: ALL MCP tool calls MUST be delegated to MCP-specific agents.**

```
┌─────────────────────────────────────────────────────────────────────────┐
│  🚫 ABSOLUTE RULE: NEVER CALL MCP TOOLS DIRECTLY                        │
│                                                                         │
│  ⛔ DIRECT MCP CALLS ARE FORBIDDEN                                      │
│  ⛔ NO EXCEPTIONS - ALL MCP CALLS GO THROUGH DELEGATE AGENTS            │
│                                                                         │
│  MANDATORY ACTION:                                                      │
│  → n8n MCP tools → Task({ subagent_type: "n8n-mcp-delegate", ... })     │
│  → GitHub MCP tools → Task({ subagent_type: "github-mcp-delegate", ... })│
└─────────────────────────────────────────────────────────────────────────┘
```

**MCP Delegate Agent Registry:**

| MCP Domain | Delegate Agent | Agent File |
|------------|----------------|------------|
| `mcp__n8n-mcp__*` | `n8n-mcp-delegate` | `${CLAUDE_AGENTS}/n8n-mcp-delegate.md` |
| `mcp__n8n-workflows__*` | `github-mcp-delegate` | `${CLAUDE_AGENTS}/github-mcp-delegate.md` |

**Enforcement**: Direct MCP calls are FORBIDDEN. Violation requires immediate self-correction.

---

## 🔴 HARD GATE: MANDATORY CONTEXT DELEGATION PROTOCOL (MCDP v1.0)

**ABSOLUTE MANDATE: ALL context operations MUST be delegated to sub-agents.**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  MANDATORY CONTEXT DELEGATION - ZERO EXCEPTIONS                             │
│                                                                             │
│  1. LARGE DOCUMENT READS (>500 tokens expected)                             │
│     → Delegate to: Explore or general-purpose agent                         │
│     → Return: Summary + key findings + references                           │
│                                                                             │
│  2. ALL MCP TOOL CALLS → Covered by MCP Delegation Enforcement              │
│                                                                             │
│  3. ALL CONTEXT GATHERING OPERATIONS                                        │
│     → Delegate to: Explore, general-purpose, or specialized agents          │
│     → Return: Actionable summary, not raw content                           │
│                                                                             │
│  SCAFFOLD-SPECIFIC: Template analysis MUST be delegated to sub-agents       │
│                                                                             │
│  VIOLATION = IMMEDIATE SELF-CORRECTION REQUIRED                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Self-Enforcement Check** (Before EVERY operation):
```
□ MCP call?        → MUST delegate to MCP agent
□ Large file?      → MUST delegate to Explore/general-purpose
□ Context gather?  → MUST delegate to appropriate agent
□ >500 tokens?     → MUST delegate

ANY = YES → DELEGATE. No exceptions.
```

**Full Protocol**: See `${CLAUDE_SKILLS}/mandatory-context-delegation.md`

---

## 🔒 UNIVERSAL SYNRG PROTOCOLS (USP v1.0 - Compact)

**All gates apply. Full specs: `${CLAUDE_SKILLS}/universal-synrg-protocols.md`**

### PRE-IMPLEMENTATION GATES
```
GATE 1: ANTI-MEMORY    - READ existing project structure before scaffolding
GATE 2: GIT_STRATEGY   - Scaffolding = typically new project, init git
GATE 3: CERTAINTY      - High certainty for standard patterns
GATE 4: SECURITY       - No secrets in scaffold templates
GATE 5: USER_VERIFY    - Interactive questions provide verification
```

### POST-IMPLEMENTATION REVIEWS
```
REVIEW 1: OBJECTIVE    - All requested structure created?
REVIEW 2: SECURITY     - No hardcoded credentials in templates
REVIEW 3: DOCS (P5)    - README and architecture docs generated
REVIEW 4: COMMIT       - Initial commit with scaffold
REVIEW 5: QUALITY      - All gates passed → COMPLETE
```

---

## Overview

This command creates a comprehensive `.claude/` directory structure through guided context gathering that evolves based on your project type. **Unlike traditional scaffolding tools, this command analyzes your choices, evaluates alternatives, and provides strategic insights that top performers use but rarely share.**

After each decision point, you'll receive:
- ✅ **Your Choice Analysis** - Why your selection makes sense
- 🔍 **Alternative Probabilities** - What else exists and their tradeoffs
- 💡 **Top 1% Insight** - Strategic wisdom from industry leaders
- 🌐 **Ecosystem Perspective** - Macro trends, adoption, longevity
- ⚖️ **Tradeoff Matrix** - Quantified comparison of options
- ❓ **Recommendation** - Should you reconsider or proceed?

---

## Execution Flow

### Phase 1: Project Type Discovery (Foundation Questions)
### Phase 1.5: 🧠 STRATEGIC FOUNDATION ANALYSIS
### Phase 2: Adaptive Context Gathering (Evolves Based on Type)
### Phase 2.5: 🧠 ECOSYSTEM & ALTERNATIVE ANALYSIS
### Phase 3: Development Workflow & Standards
### Phase 3.5: 🧠 WORKFLOW OPTIMIZATION ANALYSIS
### Phase 4: SYNRG Integration Preferences
### Phase 4.5: 🧠 AUTOMATION STRATEGY VALIDATION
### Phase 5: Directory Scaffolding & Generation
### Phase 6: Validation & Next Steps

---

## PHASE 1: PROJECT TYPE DISCOVERY

**Purpose:** Establish the foundation that drives all subsequent questions

Use the AskUserQuestion tool to ask these critical foundation questions:

```javascript
AskUserQuestion({
  questions: [
    {
      question: "What type of project are you building?",
      header: "Project Type",
      multiSelect: false,
      options: [
        {
          label: "Web Application",
          description: "Full-stack web app, SPA, or traditional server-rendered site"
        },
        {
          label: "CLI Tool",
          description: "Command-line application or developer tool"
        },
        {
          label: "Library/Package",
          description: "Reusable library or package for distribution"
        },
        {
          label: "Mobile App",
          description: "iOS, Android, or cross-platform mobile application"
        },
        {
          label: "API/Backend Service",
          description: "REST API, GraphQL API, or microservice"
        },
        {
          label: "Desktop Application",
          description: "Native or Electron-based desktop app"
        },
        {
          label: "AI/ML Project",
          description: "Machine learning model, AI application, or data science project"
        },
        {
          label: "Automation/Script",
          description: "Automation scripts, workflow tools, or batch processing"
        }
      ]
    },
    {
      question: "What is the primary programming language or tech stack?",
      header: "Tech Stack",
      multiSelect: false,
      options: [
        {
          label: "JavaScript/TypeScript",
          description: "Node.js, React, Vue, Next.js, etc."
        },
        {
          label: "Python",
          description: "Django, Flask, FastAPI, data science, ML, etc."
        },
        {
          label: "Go",
          description: "Go-based services, CLIs, or backends"
        },
        {
          label: "Rust",
          description: "Systems programming, performance-critical apps"
        },
        {
          label: "Java/Kotlin",
          description: "Spring Boot, Android, enterprise applications"
        },
        {
          label: "C#/.NET",
          description: ".NET Core, ASP.NET, Unity, etc."
        },
        {
          label: "Ruby",
          description: "Rails, Sinatra, or Ruby scripts"
        },
        {
          label: "Swift/Objective-C",
          description: "iOS/macOS native development"
        }
      ]
    },
    {
      question: "What is the current project stage?",
      header: "Stage",
      multiSelect: false,
      options: [
        {
          label: "Brand New",
          description: "Starting from scratch, no code yet"
        },
        {
          label: "Early Development",
          description: "Some code exists, foundational work in progress"
        },
        {
          label: "Active Development",
          description: "Working codebase with ongoing feature development"
        },
        {
          label: "Mature/Production",
          description: "Production-ready or already deployed with users"
        }
      ]
    }
  ]
})
```

**Store the responses in context as:**
- `projectType` (e.g., "Web Application")
- `techStack` (e.g., "JavaScript/TypeScript")
- `projectStage` (e.g., "Brand New")

---

## PHASE 1.5: 🧠 STRATEGIC FOUNDATION ANALYSIS

**Purpose:** Analyze the strategic implications of foundational choices and provide top 1% insights

### Analysis Framework

After receiving Phase 1 answers, perform comprehensive strategic analysis:

```javascript
function analyzeFoundationChoices(projectType, techStack, projectStage) {
  const analysis = {
    choiceValidation: validateChoice(projectType, techStack, projectStage),
    alternatives: evaluateAlternatives(projectType, techStack),
    topPerformerInsights: getTop1PercentInsights(projectType, techStack),
    ecosystemPerspective: analyzeEcosystem(techStack, projectStage),
    tradeoffMatrix: buildTradeoffMatrix(techStack),
    recommendation: generateRecommendation(analysis)
  };

  return presentAnalysis(analysis);
}
```

### Strategic Analysis Template

Present findings in this format:

---

## 🧠 Strategic Foundation Analysis

### ✅ Your Choices

**Project Type:** [projectType]
**Tech Stack:** [techStack]
**Stage:** [projectStage]

**Why This Makes Sense:**
[Analyze why their combination is logical given industry trends]

---

### 🔍 Alternative Probabilities

Based on your project type, here are alternatives you might not have considered:

#### Alternative 1: [Alternative Stack/Approach]

**What it is:**
[Brief description]

**When it's superior:**
- [Scenario 1]
- [Scenario 2]
- [Scenario 3]

**When your choice is better:**
- [Scenario 1]
- [Scenario 2]

**Hidden costs of switching:**
[Learning curve, ecosystem maturity, hiring, etc.]

**Example:** [Real-world example of company using this alternative]

---

#### Alternative 2: [Another Alternative]

[Same structure as Alternative 1]

---

#### Alternative 3: [Third Alternative]

[Same structure as Alternative 1]

---

### 💡 Top 1% Performer Insights

**What Top Performers Know (But Don't Usually Tell You):**

#### For [projectType] + [techStack]:

1. **[Insight Title]**
   - **The Reality:** [What top performers actually do]
   - **Why It Matters:** [Business/technical impact]
   - **How To Apply:** [Actionable guidance]
   - **Who Does This:** [Examples: Vercel, Linear, Stripe, etc.]

2. **[Second Insight Title]**
   [Same structure]

3. **[Third Insight Title]**
   [Same structure]

**Strategic Decisions They Make Early:**
- [Decision 1 and rationale]
- [Decision 2 and rationale]
- [Decision 3 and rationale]

---

### 🌐 Ecosystem Perspective (Macro View)

#### Industry Adoption Trends

**[techStack] in 2024-2025:**
- **Market Share:** [Percentage or trend]
- **Growth Trajectory:** [Rising/Stable/Declining]
- **Enterprise Adoption:** [High/Medium/Low with examples]
- **Startup Preference:** [Percentage or trend]

**Longevity Indicators:**
- **Corporate Backing:** [Companies investing in this stack]
- **Community Size:** [GitHub stars, npm downloads, etc.]
- **Job Market:** [Demand trend, salary data]
- **Learning Resources:** [Availability and quality]

#### Vendor Lock-in Risk Analysis

**Your Choice ([techStack]):**
- **Lock-in Score:** [0-100, higher = more locked in]
- **Exit Strategy Complexity:** [Low/Medium/High]
- **Platform Dependencies:** [List if applicable]
- **Cost Escalation Risk:** [Free tier limitations, pricing tiers]

**Open Source Alternatives:**
[If applicable, list open source options that reduce vendor dependence]

#### Hidden Cost Analysis

**Subscription Services in Your Stack:**
- [Service 1]: $[monthly cost] → Open source alternative: [Name] (saves $X/year)
- [Service 2]: $[monthly cost] → Open source alternative: [Name] (saves $X/year)

**Total Potential Savings:** $[annual amount]

**When Paid Makes Sense:**
- [Scenario where convenience/features justify cost]
- [Break-even point analysis]

---

### ⚖️ Tradeoff Matrix

Quantified comparison of your choice vs alternatives:

| Criterion | Your Choice ([techStack]) | Alternative 1 | Alternative 2 | Alternative 3 |
|-----------|---------------------------|---------------|---------------|---------------|
| **Learning Curve** | [1-10] | [1-10] | [1-10] | [1-10] |
| **Performance** | [1-10] | [1-10] | [1-10] | [1-10] |
| **Developer Experience** | [1-10] | [1-10] | [1-10] | [1-10] |
| **Ecosystem Maturity** | [1-10] | [1-10] | [1-10] | [1-10] |
| **Hiring Availability** | [1-10] | [1-10] | [1-10] | [1-10] |
| **Long-term Viability** | [1-10] | [1-10] | [1-10] | [1-10] |
| **Total Cost (3 years)** | $[amount] | $[amount] | $[amount] | $[amount] |
| **Time to MVP** | [weeks] | [weeks] | [weeks] | [weeks] |
| **Scalability** | [1-10] | [1-10] | [1-10] | [1-10] |

**Score (Higher Better):**
- Your Choice: [Total/90]
- Alternative 1: [Total/90]
- Alternative 2: [Total/90]
- Alternative 3: [Total/90]

---

### ❓ Recommendation

**Assessment:** [Your choice is optimal/good/has risks/should reconsider]

**Proceed If:**
- [Condition 1 that makes sense to proceed]
- [Condition 2]
- [Condition 3]

**Reconsider If:**
- [Red flag 1]
- [Red flag 2]
- [Red flag 3]

**Suggested Hybrid Approach (Best of Both Worlds):**
[If applicable, suggest how to get benefits of alternatives while keeping primary choice]

**Examples:**
- Use [techStack] but adopt [specific practice from alternative]
- Start with [techStack] but architect for [future migration path]
- Combine [primary] with [complementary tool from alternative ecosystem]

---

**Do you want to:**
1. ✅ Proceed with current choices
2. 🔄 Reconsider tech stack based on analysis
3. 🤔 Tell me more about [specific alternative]

[Wait for user decision before proceeding to Phase 2]

---

## PHASE 2: ADAPTIVE CONTEXT GATHERING

**Purpose:** Ask intelligent follow-up questions that evolve based on project type

### Decision Tree: Select Question Set Based on Project Type

```javascript
function selectAdaptiveQuestions(projectType, techStack) {
  switch(projectType) {
    case "Web Application":
      return getWebAppQuestions(techStack);
    case "CLI Tool":
      return getCLIToolQuestions(techStack);
    case "Library/Package":
      return getLibraryQuestions(techStack);
    case "Mobile App":
      return getMobileAppQuestions(techStack);
    case "API/Backend Service":
      return getAPIQuestions(techStack);
    case "Desktop Application":
      return getDesktopAppQuestions(techStack);
    case "AI/ML Project":
      return getAIMLQuestions(techStack);
    case "Automation/Script":
      return getAutomationQuestions(techStack);
    default:
      return getGenericQuestions(techStack);
  }
}
```

---

### 2.1: Web Application Questions

If `projectType === "Web Application"`:

```javascript
AskUserQuestion({
  questions: [
    {
      question: "What is your web application architecture?",
      header: "Architecture",
      multiSelect: false,
      options: [
        {
          label: "Full-Stack (Monolith)",
          description: "Single codebase with frontend and backend together"
        },
        {
          label: "Full-Stack (Separate)",
          description: "Frontend and backend in separate directories/repos"
        },
        {
          label: "Frontend Only",
          description: "SPA or static site, backend is external/existing"
        },
        {
          label: "Backend Only",
          description: "API or server, frontend is external/existing"
        }
      ]
    },
    {
      question: "What frontend framework/library are you using?",
      header: "Frontend",
      multiSelect: false,
      options: [
        { label: "React", description: "React with or without framework" },
        { label: "Next.js", description: "React with SSR/SSG" },
        { label: "Vue.js", description: "Vue 3 or Vue 2" },
        { label: "Nuxt.js", description: "Vue with SSR/SSG" },
        { label: "Svelte/SvelteKit", description: "Svelte framework" },
        { label: "Angular", description: "Angular framework" },
        { label: "Vanilla JS", description: "No framework, plain JavaScript" },
        { label: "None", description: "Server-rendered templates only" }
      ]
    },
    {
      question: "What backend framework are you using (if applicable)?",
      header: "Backend",
      multiSelect: false,
      options: [
        { label: "Express.js", description: "Node.js with Express" },
        { label: "Next.js API Routes", description: "Built-in Next.js backend" },
        { label: "FastAPI", description: "Python FastAPI framework" },
        { label: "Django/Flask", description: "Python web frameworks" },
        { label: "NestJS", description: "TypeScript Node.js framework" },
        { label: "Rails", description: "Ruby on Rails" },
        { label: "Spring Boot", description: "Java/Kotlin framework" },
        { label: "None", description: "Frontend-only or external backend" }
      ]
    },
    {
      question: "What database(s) are you using?",
      header: "Database",
      multiSelect: true,
      options: [
        { label: "PostgreSQL", description: "Relational SQL database" },
        { label: "MySQL/MariaDB", description: "Relational SQL database" },
        { label: "MongoDB", description: "Document-based NoSQL" },
        { label: "SQLite", description: "Embedded SQL database" },
        { label: "Supabase", description: "PostgreSQL with backend services" },
        { label: "Firebase", description: "Google's backend platform" },
        { label: "Redis", description: "In-memory data store / cache" },
        { label: "None", description: "No database / external database" }
      ]
    },
    {
      question: "Where will this be deployed?",
      header: "Deployment",
      multiSelect: false,
      options: [
        { label: "Vercel", description: "Serverless platform for web apps" },
        { label: "Netlify", description: "JAMstack deployment platform" },
        { label: "AWS", description: "Amazon Web Services (EC2, Lambda, etc.)" },
        { label: "Railway/Render", description: "Modern deployment platforms" },
        { label: "Docker/Self-hosted", description: "Containerized deployment" },
        { label: "Traditional Server", description: "VPS or dedicated server" },
        { label: "Not Decided", description: "Still evaluating options" }
      ]
    }
  ]
})
```

**Store responses:**
- `architecture`
- `frontend`
- `backend`
- `databases` (array)
- `deployment`

---

### 2.2: CLI Tool Questions

If `projectType === "CLI Tool"`:

```javascript
AskUserQuestion({
  questions: [
    {
      question: "What is the primary purpose of your CLI tool?",
      header: "Purpose",
      multiSelect: false,
      options: [
        { label: "Developer Tool", description: "Build tools, code generators, linters" },
        { label: "System Utility", description: "File management, system operations" },
        { label: "Data Processing", description: "Data transformation, analysis, ETL" },
        { label: "API Client", description: "Interface for web services/APIs" },
        { label: "Automation", description: "Task automation, scripting workflows" }
      ]
    },
    {
      question: "How will users install your CLI?",
      header: "Distribution",
      multiSelect: true,
      options: [
        { label: "npm/npx", description: "Node Package Manager" },
        { label: "pip/pipx", description: "Python Package Index" },
        { label: "Homebrew", description: "macOS/Linux package manager" },
        { label: "Cargo", description: "Rust package manager" },
        { label: "Go install", description: "Go module installation" },
        { label: "Direct Binary", description: "Downloadable executables" }
      ]
    },
    {
      question: "Does your CLI need configuration files?",
      header: "Config",
      multiSelect: false,
      options: [
        { label: "Yes (JSON/YAML)", description: "Config files for user preferences" },
        { label: "Yes (dotenv)", description: "Environment variables only" },
        { label: "Yes (Both)", description: "Config files AND environment variables" },
        { label: "No", description: "All configuration via flags/arguments" }
      ]
    },
    {
      question: "What level of interactivity does it have?",
      header: "Interactivity",
      multiSelect: false,
      options: [
        { label: "Non-interactive", description: "Pure CLI flags and arguments" },
        { label: "Prompts", description: "Interactive questions when needed" },
        { label: "TUI", description: "Full terminal UI with navigation" },
        { label: "Mixed", description: "Both interactive and non-interactive modes" }
      ]
    }
  ]
})
```

**Store responses:**
- `cliPurpose`
- `distribution` (array)
- `configType`
- `interactivity`

---

### 2.3: Library/Package Questions

If `projectType === "Library/Package"`:

```javascript
AskUserQuestion({
  questions: [
    {
      question: "What type of library are you building?",
      header: "Library Type",
      multiSelect: false,
      options: [
        { label: "UI Components", description: "React/Vue components, design system" },
        { label: "Utility Library", description: "Helper functions, data manipulation" },
        { label: "Framework/Plugin", description: "Extension or plugin for existing framework" },
        { label: "API Client", description: "SDK for external API/service" },
        { label: "Data Structure", description: "Algorithms, data structures, math" }
      ]
    },
    {
      question: "Where will it be published?",
      header: "Registry",
      multiSelect: true,
      options: [
        { label: "npm", description: "Node Package Manager registry" },
        { label: "PyPI", description: "Python Package Index" },
        { label: "crates.io", description: "Rust package registry" },
        { label: "Maven Central", description: "Java/Kotlin packages" },
        { label: "NuGet", description: ".NET package manager" },
        { label: "GitHub Packages", description: "GitHub-hosted packages" },
        { label: "Private Registry", description: "Internal/private package registry" }
      ]
    },
    {
      question: "What's your versioning and release strategy?",
      header: "Versioning",
      multiSelect: false,
      options: [
        { label: "SemVer (Strict)", description: "Strict semantic versioning" },
        { label: "SemVer (Flexible)", description: "SemVer with breaking changes in minors" },
        { label: "CalVer", description: "Calendar-based versioning" },
        { label: "Manual", description: "Manual version numbers without system" }
      ]
    },
    {
      question: "How important is bundle size optimization?",
      header: "Bundle Size",
      multiSelect: false,
      options: [
        { label: "Critical", description: "Must be minimal, tree-shakeable" },
        { label: "Important", description: "Should be reasonable, some optimization" },
        { label: "Not Priority", description: "Functionality over size" }
      ]
    }
  ]
})
```

**Store responses:**
- `libraryType`
- `registries` (array)
- `versioning`
- `bundleSize`

---

### 2.4: Mobile App Questions

If `projectType === "Mobile App"`:

```javascript
AskUserQuestion({
  questions: [
    {
      question: "What platform(s) are you targeting?",
      header: "Platform",
      multiSelect: true,
      options: [
        { label: "iOS", description: "iPhone/iPad apps" },
        { label: "Android", description: "Android devices" },
        { label: "Both (Cross-platform)", description: "Single codebase for both" }
      ]
    },
    {
      question: "What mobile framework are you using?",
      header: "Framework",
      multiSelect: false,
      options: [
        { label: "React Native", description: "JavaScript/React cross-platform" },
        { label: "Flutter", description: "Dart-based cross-platform" },
        { label: "Native iOS", description: "Swift/SwiftUI or Objective-C" },
        { label: "Native Android", description: "Kotlin or Java" },
        { label: "Ionic/Capacitor", description: "Web-based hybrid apps" },
        { label: "Xamarin/.NET MAUI", description: "C# cross-platform" }
      ]
    },
    {
      question: "What state management solution are you using?",
      header: "State Mgmt",
      multiSelect: false,
      options: [
        { label: "Redux/Redux Toolkit", description: "Predictable state container" },
        { label: "MobX", description: "Observable state management" },
        { label: "Zustand/Jotai", description: "Lightweight state libraries" },
        { label: "Provider/Riverpod", description: "Flutter state management" },
        { label: "Context API", description: "React built-in state" },
        { label: "None/Local State", description: "Component-level state only" }
      ]
    },
    {
      question: "Does the app require authentication?",
      header: "Auth",
      multiSelect: false,
      options: [
        { label: "Yes (Social)", description: "OAuth, Google, Apple, Facebook login" },
        { label: "Yes (Email/Password)", description: "Traditional authentication" },
        { label: "Yes (Both)", description: "Social and traditional auth" },
        { label: "No", description: "No authentication needed" }
      ]
    }
  ]
})
```

**Store responses:**
- `mobilePlatforms` (array)
- `mobileFramework`
- `stateManagement`
- `authentication`

---

### 2.5: API/Backend Service Questions

If `projectType === "API/Backend Service"`:

```javascript
AskUserQuestion({
  questions: [
    {
      question: "What API architecture are you using?",
      header: "API Type",
      multiSelect: false,
      options: [
        { label: "REST API", description: "RESTful HTTP endpoints" },
        { label: "GraphQL", description: "GraphQL schema and resolvers" },
        { label: "gRPC", description: "High-performance RPC framework" },
        { label: "WebSocket", description: "Real-time bidirectional communication" },
        { label: "Mixed", description: "Combination of multiple types" }
      ]
    },
    {
      question: "What database(s) are you using?",
      header: "Database",
      multiSelect: true,
      options: [
        { label: "PostgreSQL", description: "Relational SQL database" },
        { label: "MongoDB", description: "Document-based NoSQL" },
        { label: "Redis", description: "In-memory cache/store" },
        { label: "MySQL", description: "Relational SQL database" },
        { label: "DynamoDB", description: "AWS NoSQL database" },
        { label: "Elasticsearch", description: "Search and analytics engine" }
      ]
    },
    {
      question: "What authentication strategy are you using?",
      header: "Auth",
      multiSelect: true,
      options: [
        { label: "JWT", description: "JSON Web Tokens" },
        { label: "OAuth 2.0", description: "OAuth protocol" },
        { label: "API Keys", description: "Simple API key authentication" },
        { label: "Session-based", description: "Server-side sessions" },
        { label: "None", description: "Public API, no authentication" }
      ]
    },
    {
      question: "How do you handle API documentation?",
      header: "Docs",
      multiSelect: false,
      options: [
        { label: "OpenAPI/Swagger", description: "Auto-generated from spec" },
        { label: "GraphQL Introspection", description: "Built-in GraphQL docs" },
        { label: "Manual Documentation", description: "README, custom docs" },
        { label: "API Blueprint/RAML", description: "Spec-first documentation" },
        { label: "Not Yet Decided", description: "Still planning" }
      ]
    }
  ]
})
```

**Store responses:**
- `apiType`
- `databases` (array)
- `authStrategies` (array)
- `apiDocs`

---

### 2.6: Desktop Application Questions

If `projectType === "Desktop Application"`:

```javascript
AskUserQuestion({
  questions: [
    {
      question: "What desktop framework are you using?",
      header: "Framework",
      multiSelect: false,
      options: [
        { label: "Electron", description: "Web technologies (Chromium + Node.js)" },
        { label: "Tauri", description: "Rust-based, smaller bundle size" },
        { label: "Qt", description: "Cross-platform C++ framework" },
        { label: "Native (Swift/Obj-C)", description: "macOS native" },
        { label: "Native (.NET/WPF)", description: "Windows native" },
        { label: "Native (GTK)", description: "Linux native" }
      ]
    },
    {
      question: "What platforms will you support?",
      header: "Platforms",
      multiSelect: true,
      options: [
        { label: "Windows", description: "Windows 10/11" },
        { label: "macOS", description: "macOS 10.15+" },
        { label: "Linux", description: "Ubuntu, Fedora, etc." }
      ]
    },
    {
      question: "Does your app need system-level access?",
      header: "System Access",
      multiSelect: true,
      options: [
        { label: "File System", description: "Read/write local files" },
        { label: "System Tray", description: "Background app in system tray" },
        { label: "Native Menus", description: "OS-native menu bar" },
        { label: "Notifications", description: "System notifications" },
        { label: "Auto-updates", description: "Built-in update mechanism" },
        { label: "None", description: "Sandboxed web app only" }
      ]
    }
  ]
})
```

**Store responses:**
- `desktopFramework`
- `desktopPlatforms` (array)
- `systemAccess` (array)

---

### 2.7: AI/ML Project Questions

If `projectType === "AI/ML Project"`:

```javascript
AskUserQuestion({
  questions: [
    {
      question: "What type of AI/ML project is this?",
      header: "AI Type",
      multiSelect: false,
      options: [
        { label: "Training Models", description: "Model development and training" },
        { label: "Inference/Serving", description: "Deploying trained models" },
        { label: "Data Pipeline", description: "ETL, preprocessing, feature engineering" },
        { label: "Experimentation", description: "Research, notebooks, analysis" },
        { label: "Full MLOps", description: "Complete ML lifecycle management" }
      ]
    },
    {
      question: "What ML framework(s) are you using?",
      header: "Framework",
      multiSelect: true,
      options: [
        { label: "PyTorch", description: "Deep learning framework" },
        { label: "TensorFlow/Keras", description: "ML/DL framework" },
        { label: "scikit-learn", description: "Traditional ML algorithms" },
        { label: "Hugging Face", description: "Transformers, NLP models" },
        { label: "XGBoost/LightGBM", description: "Gradient boosting" },
        { label: "JAX", description: "High-performance numerical computing" }
      ]
    },
    {
      question: "How do you track experiments and models?",
      header: "Tracking",
      multiSelect: true,
      options: [
        { label: "MLflow", description: "Experiment tracking and model registry" },
        { label: "Weights & Biases", description: "Experiment tracking platform" },
        { label: "TensorBoard", description: "TensorFlow visualization" },
        { label: "DVC", description: "Data version control" },
        { label: "Custom/Manual", description: "Custom tracking solution" },
        { label: "None", description: "No formal tracking yet" }
      ]
    },
    {
      question: "Where do you store and process data?",
      header: "Data Storage",
      multiSelect: true,
      options: [
        { label: "Local Files", description: "CSV, JSON, Parquet on disk" },
        { label: "Cloud Storage", description: "S3, GCS, Azure Blob" },
        { label: "Database", description: "PostgreSQL, MongoDB, etc." },
        { label: "Data Warehouse", description: "BigQuery, Snowflake, Redshift" },
        { label: "Feature Store", description: "Feast, Tecton, etc." }
      ]
    }
  ]
})
```

**Store responses:**
- `aiType`
- `mlFrameworks` (array)
- `experimentTracking` (array)
- `dataStorage` (array)

---

### 2.8: Automation/Script Questions

If `projectType === "Automation/Script"`:

```javascript
AskUserQuestion({
  questions: [
    {
      question: "What does your automation script do?",
      header: "Purpose",
      multiSelect: false,
      options: [
        { label: "Data Processing", description: "Transform, clean, analyze data" },
        { label: "CI/CD Pipeline", description: "Build, test, deploy automation" },
        { label: "System Administration", description: "Server management, backups, monitoring" },
        { label: "Web Scraping", description: "Extract data from websites" },
        { label: "Workflow Automation", description: "Business process automation" },
        { label: "Testing", description: "Automated testing scripts" }
      ]
    },
    {
      question: "How will the script be triggered?",
      header: "Execution",
      multiSelect: true,
      options: [
        { label: "Manual", description: "Run manually when needed" },
        { label: "Cron/Scheduled", description: "Time-based scheduling" },
        { label: "Event-driven", description: "Triggered by events (webhooks, file changes)" },
        { label: "CI/CD Pipeline", description: "Part of automated pipeline" }
      ]
    },
    {
      question: "Does it need external dependencies or APIs?",
      header: "Dependencies",
      multiSelect: false,
      options: [
        { label: "Yes (Many)", description: "Multiple external APIs/services" },
        { label: "Yes (Few)", description: "1-2 external dependencies" },
        { label: "No", description: "Self-contained, no external deps" }
      ]
    }
  ]
})
```

**Store responses:**
- `automationPurpose`
- `executionTriggers` (array)
- `externalDeps`

---

## PHASE 2.5: 🧠 ECOSYSTEM & ALTERNATIVE ANALYSIS

**Purpose:** Provide deep strategic insights into technology choices and ecosystem implications

After receiving Phase 2 answers, analyze each major technology choice:

### Analysis Structure (Per Technology Choice)

For each significant technology selected (e.g., database, framework, deployment platform), provide:

---

## 🧠 Ecosystem & Alternative Analysis: [Technology Category]

### ✅ Your Choice: [Selected Technology]

**Why This Is A Solid Choice:**
[Strengths analysis - when this technology excels]

**Market Position:**
- **Adoption:** [High/Medium/Low with data]
- **Trend:** [Growing/Stable/Declining]
- **Used By:** [Notable companies using this]

---

### 🔍 Alternative Analysis

#### Open Source vs Subscription Consideration

**Your Choice ([Technology]):**
- **Cost Structure:** [Free/Free tier + paid/Subscription only]
- **Monthly Cost at Scale:** $[estimate for typical production use]
- **Annual TCO (3 years):** $[total cost of ownership]

**Open Source Alternative: [Name]**
- **What it is:** [Brief description]
- **Cost Savings:** $[amount] per year
- **Setup Complexity:** [Hours/Days needed]
- **Maintenance Burden:** [Low/Medium/High]
- **Feature Parity:** [Percentage or description]

**When Paid Makes Sense:**
- Team < [number] engineers (setup time costs more than subscription)
- Need enterprise support/SLAs
- Compliance requirements require managed service
- Time to market is critical

**When Open Source Makes Sense:**
- Team > [number] engineers (can maintain in-house)
- Budget constraints
- Need full control over data/infrastructure
- Have specific customization requirements

---

#### Framework Support & Ecosystem Maturity

**Community Metrics:**
| Metric | Your Choice | Alternative 1 | Alternative 2 |
|--------|-------------|---------------|---------------|
| GitHub Stars | [number]K | [number]K | [number]K |
| npm Downloads/Month | [number]M | [number]M | [number]M |
| Stack Overflow Questions | [number]K | [number]K | [number]K |
| Active Contributors | [number] | [number] | [number] |
| Corporate Sponsors | [list] | [list] | [list] |
| Years Active | [number] | [number] | [number] |

**Support Quality:**
- **Documentation:** [Excellent/Good/Fair/Poor]
- **Tutorial Availability:** [Abundant/Adequate/Scarce]
- **Community Responsiveness:** [< 1 day / 1-3 days / Slow]
- **Breaking Changes Frequency:** [Rare/Occasional/Frequent]

---

### 💡 Top 1% Insight: [Technology Category]

#### What Elite Teams Actually Do

**[Insight #1 Title]**

**The Common Approach:**
[What most teams do - the conventional wisdom]

**What Top Performers Do Instead:**
[The unconventional but superior approach]

**Why It Matters:**
- **Performance Impact:** [Quantified improvement]
- **Cost Impact:** [Savings or efficiency gains]
- **Scalability Impact:** [How it affects growth]

**Real Example:**
[Stripe/Vercel/Linear/etc.] does [specific implementation] because [strategic reason]. This resulted in [measurable outcome].

**How To Implement:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Common Pitfalls To Avoid:**
- [Mistake 1 and why it happens]
- [Mistake 2 and why it happens]

---

**[Insight #2 Title]**

[Same structure as Insight #1]

---

#### Hidden Optimization Patterns

**Pattern 1: [Pattern Name]**
- **What:** [Description of pattern]
- **When:** [When to apply]
- **Impact:** [Measurable benefit]
- **Who Uses It:** [Companies]

**Pattern 2: [Pattern Name]**
[Same structure]

---

### 🌐 Ecosystem Perspective

#### Industry Direction (Next 2-3 Years)

**Current State:**
[Where the ecosystem is today]

**Emerging Trends:**
1. **[Trend 1]:** [Description and implications]
   - **Adoption Timeline:** [Months/Years to mainstream]
   - **Should You Adopt Now?** [Yes/No and why]

2. **[Trend 2]:** [Description]
   - **Adoption Timeline:** [Estimate]
   - **Should You Adopt Now?** [Recommendation]

**Declining Patterns:**
- [Pattern that's being phased out]
- [Migration path to new approach]

---

#### Vendor Lock-in Risk Assessment

**Lock-in Score: [0-100]**
- 0-30: Minimal lock-in, easy to migrate
- 31-60: Moderate lock-in, migration requires effort
- 61-100: High lock-in, migration is complex/costly

**Your Choice ([Technology]): [Score]/100**

**Lock-in Factors:**
- **Proprietary APIs:** [Yes/No - Details]
- **Data Export:** [Easy/Medium/Difficult]
- **Migration Path Exists:** [Yes/No]
- **Community Converters Available:** [Yes/No]

**Exit Strategy:**
If you needed to migrate in 1 year:
1. [Step 1 - Effort estimate]
2. [Step 2 - Effort estimate]
3. [Step 3 - Effort estimate]
**Total Migration Cost:** [Developer-weeks] + $[services cost]

**Hybrid Approach to Reduce Lock-in:**
- Use [abstraction layer/pattern] to isolate [vendor-specific code]
- Standardize on [open format/protocol] for [data/APIs]
- Keep [percentage]% of logic vendor-agnostic

---

#### Cost Trajectory Analysis

**Year 1 (Current):**
- Base cost: $[amount]/month
- Expected growth: [percentage] monthly
- Annual: $[amount]

**Year 2 (Projected):**
- Base cost: $[amount]/month (after tier changes)
- Growth cost: $[amount] (based on scale)
- Annual: $[amount]

**Year 3 (Projected):**
- Base cost: $[amount]/month
- Growth cost: $[amount]
- Annual: $[amount]

**3-Year TCO: $[total]**

**Alternative (Open Source) TCO:**
- Setup: $[one-time developer hours × rate]
- Hosting: $[infrastructure costs]
- Maintenance: $[annual developer time × rate]
**3-Year TCO: $[total]**

**Break-even Analysis:**
Open source becomes cheaper after [months/years] if team > [number] engineers.

---

#### Performance & Scalability Intel

**Your Choice Scales To:**
- **Requests/Second:** [number] (before optimization needed)
- **Database Size:** [TB] (before partitioning needed)
- **Concurrent Users:** [number] (before horizontal scaling)

**Known Scaling Challenges:**
1. **[Challenge]:** Hits at [scale point]
   - **Solution:** [How companies solve this]
   - **Cost:** [Additional infrastructure/dev time]

2. **[Challenge]:** Becomes issue at [scale point]
   - **Solution:** [Approach]
   - **Cost:** [Estimate]

**Who's Using It at Scale:**
- [Company]: [scale metrics - users, requests, data]
- [Company]: [scale metrics]
- [Company]: [scale metrics]

**Performance Benchmarks:**
| Operation | Your Choice | Alternative 1 | Alternative 2 |
|-----------|-------------|---------------|---------------|
| [Metric 1] | [value] | [value] | [value] |
| [Metric 2] | [value] | [value] | [value] |
| [Metric 3] | [value] | [value] | [value] |

---

### ⚖️ Technology-Specific Tradeoff Matrix

| Criterion | Your Choice | Alt 1 (Open Source) | Alt 2 (Different Approach) |
|-----------|-------------|---------------------|----------------------------|
| **Initial Setup Time** | [hours/days] | [hours/days] | [hours/days] |
| **Monthly Cost @ 10K Users** | $[amount] | $[amount] | $[amount] |
| **Monthly Cost @ 100K Users** | $[amount] | $[amount] | $[amount] |
| **Monthly Cost @ 1M Users** | $[amount] | $[amount] | $[amount] |
| **Performance** | [1-10] | [1-10] | [1-10] |
| **DX (Developer Experience)** | [1-10] | [1-10] | [1-10] |
| **Ease of Migration Away** | [1-10] | [1-10] | [1-10] |
| **Community Support** | [1-10] | [1-10] | [1-10] |
| **Future-Proofing** | [1-10] | [1-10] | [1-10] |

**Weighted Score (Higher Better):**
- Your Choice: [score]/100
- Alternative 1: [score]/100
- Alternative 2: [score]/100

---

### ❓ Recommendation: [Technology Category]

**Overall Assessment:** [Optimal/Good/Consider Alternatives/High Risk]

**Your Choice ([Technology]) Is Best If:**
- [Condition 1]
- [Condition 2]
- [Condition 3]

**Consider [Alternative] Instead If:**
- [Red flag 1]
- [Red flag 2]
- [Red flag 3]

**Hybrid Strategy (Best of Both Worlds):**
Use [your choice] but:
1. [Adopt specific practice from alternative to reduce lock-in]
2. [Implement abstraction layer for easier migration]
3. [Use open standard for data format]
4. [Keep critical path vendor-agnostic]

**Action Items Before Proceeding:**
- [ ] [Specific research or validation task]
- [ ] [Prototype or proof-of-concept]
- [ ] [Cost modeling for expected scale]

---

**Repeat this analysis for each major technology choice (frontend framework, database, deployment, etc.)**

---

**After all technology analyses, present summary:**

## 🎯 Overall Technology Stack Assessment

**Strengths:**
1. [Major strength of combined stack]
2. [Synergy between chosen technologies]
3. [Strategic advantage]

**Risks:**
1. [Identified risk across stack]
2. [Potential scaling challenge]
3. [Vendor dependence concern]

**Strategic Recommendations:**
1. [Action to mitigate risk 1]
2. [Optimization for better outcome]
3. [Future-proofing measure]

**Proceed to Phase 3?**
1. ✅ Yes, stack is validated
2. 🔄 Reconsider [specific technology]
3. 💬 Discuss [specific concern] first

[Wait for user decision]

---

## PHASE 3: DEVELOPMENT WORKFLOW & STANDARDS

**Purpose:** Universal questions about development practices (applies to all project types)

```javascript
AskUserQuestion({
  questions: [
    {
      question: "What testing approach will you use?",
      header: "Testing",
      multiSelect: true,
      options: [
        { label: "Unit Tests", description: "Function/component level tests" },
        { label: "Integration Tests", description: "Module interaction tests" },
        { label: "E2E Tests", description: "Full user flow testing" },
        { label: "Visual Regression", description: "Screenshot comparison tests" },
        { label: "Manual Testing Only", description: "No automated tests planned" },
        { label: "TDD", description: "Test-driven development approach" }
      ]
    },
    {
      question: "What code quality tools do you want configured?",
      header: "Quality Tools",
      multiSelect: true,
      options: [
        { label: "ESLint/Prettier", description: "JS/TS linting and formatting" },
        { label: "TypeScript", description: "Type checking" },
        { label: "Black/Ruff", description: "Python formatting and linting" },
        { label: "Clippy/Rustfmt", description: "Rust linting and formatting" },
        { label: "Pre-commit Hooks", description: "Git hooks for quality checks" },
        { label: "None", description: "No automated quality tools" }
      ]
    },
    {
      question: "What's your Git workflow preference?",
      header: "Git Workflow",
      multiSelect: false,
      options: [
        { label: "Trunk-based", description: "Main branch, short-lived feature branches" },
        { label: "Git Flow", description: "Main, develop, feature, release branches" },
        { label: "GitHub Flow", description: "Main + feature branches with PRs" },
        { label: "GitLab Flow", description: "Environment branches" },
        { label: "Flexible", description: "No strict workflow" }
      ]
    },
    {
      question: "Do you need CI/CD configuration?",
      header: "CI/CD",
      multiSelect: false,
      options: [
        { label: "Yes (GitHub Actions)", description: "GitHub Actions workflows" },
        { label: "Yes (GitLab CI)", description: "GitLab CI/CD pipelines" },
        { label: "Yes (CircleCI/Jenkins)", description: "Other CI platforms" },
        { label: "Later", description: "Not needed right now" },
        { label: "No", description: "No CI/CD planned" }
      ]
    }
  ]
})
```

**Store responses:**
- `testingApproach` (array)
- `qualityTools` (array)
- `gitWorkflow`
- `cicd`

---

## PHASE 3.5: 🧠 WORKFLOW OPTIMIZATION ANALYSIS

**Purpose:** Analyze workflow choices and suggest elite-level optimizations

---

## 🧠 Workflow Optimization Analysis

### ✅ Your Workflow Configuration

**Testing:** [testingApproach]
**Quality Tools:** [qualityTools]
**Git Workflow:** [gitWorkflow]
**CI/CD:** [cicd]

---

### 💡 Top 1% Workflow Insights

#### Testing Strategy Optimization

**Your Approach:** [testingApproach]

**What Most Teams Miss:**

1. **The Testing Pyramid Is Outdated**
   - **Old Wisdom:** 70% unit, 20% integration, 10% E2E
   - **What Top Teams Do:** [Adjusted ratio based on project type]
   - **Why:** [Modern reasoning - CI speed, reliability, ROI]
   - **Examples:**
     - [Company]: Uses [ratio] because [reason]
     - Result: [metric - deployment frequency, bug escape rate]

2. **Test Investment ROI Matrix**

   | Test Type | Setup Cost | Maintenance Cost | Bug Detection ROI | Speed |
   |-----------|-----------|------------------|-------------------|-------|
   | Unit | Low | Low | Medium | Fast |
   | Integration | Medium | Medium | High | Medium |
   | E2E | High | Very High | Very High | Slow |
   | Visual Regression | High | Low | High (UI bugs) | Medium |

   **Recommendation for [projectType]:**
   - Invest heavily in: [test type] - [reasoning]
   - Moderate investment: [test type] - [reasoning]
   - Minimal investment: [test type] - [reasoning]

3. **Flaky Test Elimination Strategy**
   - **Industry Average:** 15-30% of E2E tests are flaky
   - **Top Performers:** < 2% flaky rate
   - **How They Do It:**
     - [Technique 1 with example]
     - [Technique 2 with example]
     - [Technique 3 with example]

---

#### CI/CD Optimization

**Your Choice:** [cicd]

**Elite-Level Pipeline Architecture:**

1. **The 10-Minute Rule**
   - **Goal:** Feedback in < 10 minutes for 95% of commits
   - **How Top Teams Achieve This:**
     - Parallel job execution (save [percentage]% time)
     - Incremental testing (only affected tests)
     - Intelligent caching (reduce build from [X] to [Y] min)
     - Early failure detection (fail fast)

   **Your Current Estimated Pipeline Time:** [estimate based on choices]
   **Optimized Potential:** [optimized estimate]
   **Optimizations To Apply:**
   - [Specific optimization 1]
   - [Specific optimization 2]
   - [Specific optimization 3]

2. **Cost Optimization Secrets**

   **CI/CD Cost at Scale:**
   | Scale | Traditional Setup | Optimized Setup | Savings |
   |-------|-------------------|-----------------|---------|
   | 10 devs, 50 commits/day | $[amount]/month | $[amount]/month | [percentage]% |
   | 50 devs, 250 commits/day | $[amount]/month | $[amount]/month | [percentage]% |
   | 100 devs, 500 commits/day | $[amount]/month | $[amount]/month | [percentage]% |

   **Optimization Techniques:**
   - Self-hosted runners for [specific jobs]: Save $[amount]/mo
   - Matrix build optimization: Save [percentage]% compute time
   - Artifact caching strategy: Save [percentage]% redundant builds
   - Spot instances for [job types]: Save 60-80% on compute

3. **Deployment Frequency Multiplier**

   **Industry Data:**
   - Low performers: < 1 deploy/month
   - Medium performers: 1-4 deploys/month
   - High performers: 1+ deploys/day
   - Elite: Multiple deploys/day

   **Your Current Configuration Enables:** [estimate frequency]

   **To Reach Elite Level:**
   - [Capability to add]
   - [Process to streamline]
   - [Automation to implement]

---

#### Git Workflow Efficiency

**Your Choice:** [gitWorkflow]

**Why [gitWorkflow] May Not Be Optimal:**

**Workflow Comparison Matrix:**

| Workflow | Merge Frequency | Branch Lifespan | Merge Conflicts | Deployment Speed | Best For |
|----------|-----------------|-----------------|-----------------|------------------|----------|
| Trunk-based | Very High | Hours | Rare | Very Fast | High-trust teams |
| GitHub Flow | High | Days | Occasional | Fast | Small-medium teams |
| Git Flow | Low | Weeks | Frequent | Slow | Scheduled releases |
| GitLab Flow | Medium | Days | Occasional | Medium | Multi-env deploys |

**Your Workflow ([gitWorkflow]) Matches If:**
- [Condition 1]
- [Condition 2]
- [Condition 3]

**Consider [Alternative Workflow] If:**
- [Scenario where alternative is better]
- [Tradeoff analysis]

**Top Performer Secret:**
Most elite teams (Stripe, Vercel, Linear) use **trunk-based** with:
- Feature flags for long-running work
- Very short-lived branches (< 1 day)
- Small, atomic commits
- Automated rollback capability

**Migration Path:**
If you want to adopt trunk-based:
1. [Phase 1: Preparation]
2. [Phase 2: Gradual adoption]
3. [Phase 3: Full switch]
Estimated timeline: [weeks/months]

---

### 🌐 Workflow Ecosystem Perspective

#### Industry Benchmarks

**Your Configuration vs Industry:**

| Metric | Your Setup | Industry Average | Top 10% | Elite (Top 1%) |
|--------|-----------|------------------|---------|----------------|
| **Deploy Frequency** | [estimate] | Weekly | Daily | Multiple/day |
| **Lead Time (Commit→Prod)** | [estimate] | 1-4 weeks | < 1 day | < 1 hour |
| **MTTR (Mean Time to Restore)** | [estimate] | < 1 day | < 1 hour | < 5 min |
| **Change Failure Rate** | [estimate] | 15-30% | 5-10% | < 5% |
| **CI Pipeline Time** | [estimate] | 30-60 min | < 15 min | < 5 min |

**Your Current DORA Score:** [Based on configuration]
- Elite: [percentage match]
- High: [percentage match]
- Medium: [percentage match]
- Low: [percentage match]

**To Reach Elite:**
- [Gap 1 to close]
- [Gap 2 to close]
- [Gap 3 to close]

---

### ⚖️ Workflow Tradeoff Analysis

**Quality vs Speed:**
- Your configuration leans: [Quality-focused / Balanced / Speed-focused]
- Recommended for [projectType]: [Recommendation with reasoning]

**Automation vs Control:**
- Your configuration: [Highly automated / Balanced / Manual gates]
- Risk level: [Low / Medium / High]
- Recommended adjustment: [Suggestion]

**Cost vs Comprehensiveness:**
- Estimated CI/CD cost: $[amount]/month at scale
- Test coverage level: [Expected percentage]
- ROI assessment: [Good / Needs optimization / Over-investment]

---

### ❓ Workflow Recommendations

**Overall Assessment:** [Optimal / Good / Needs Adjustment / Suboptimal]

**Strengths:**
1. [What you got right]
2. [Good decision]
3. [Strategic advantage]

**Suggested Optimizations:**

**High-Impact (Do First):**
1. **[Optimization 1]**
   - Impact: [Metric improvement]
   - Effort: [Hours/days]
   - ROI: [High/Medium/Low]

2. **[Optimization 2]**
   [Same structure]

**Medium-Impact (Do Next):**
1. **[Optimization]**
   [Structure]

**Low-Impact (Nice-to-Have):**
1. **[Optimization]**
   [Structure]

---

**Proceed to Phase 4?**
1. ✅ Yes, workflow is validated
2. 🔄 Adjust [specific aspect]
3. 💬 Discuss [specific workflow question]

[Wait for user decision]

---

## PHASE 4: SYNRG INTEGRATION PREFERENCES

**Purpose:** Determine SYNRG orchestration capabilities for this project

```javascript
AskUserQuestion({
  questions: [
    {
      question: "Do you want SYNRG orchestration commands included in this project?",
      header: "SYNRG Commands",
      multiSelect: false,
      options: [
        {
          label: "Yes (Full Suite)",
          description: "Include /synrg, /synrg-guided, /synrg-refactor, etc."
        },
        {
          label: "Yes (Essential Only)",
          description: "Just /synrg and /synrg-guided"
        },
        {
          label: "No",
          description: "Skip SYNRG-specific commands"
        }
      ]
    },
    {
      question: "What level of automation should SYNRG use for this project?",
      header: "Automation",
      multiSelect: false,
      options: [
        {
          label: "Maximum Autonomy",
          description: "Auto-proceed on low-risk changes, minimal escalation"
        },
        {
          label: "Balanced",
          description: "Confirm medium-risk changes, auto-proceed on low-risk"
        },
        {
          label: "Conservative",
          description: "Confirm most changes, maximum safety"
        }
      ]
    },
    {
      question: "Should validation always require Playwright screenshots?",
      header: "Validation",
      multiSelect: false,
      options: [
        {
          label: "Yes (Always)",
          description: "Every change must be validated with screenshots"
        },
        {
          label: "UI Changes Only",
          description: "Only UI/frontend changes need screenshots"
        },
        {
          label: "Optional",
          description: "Screenshots when appropriate, not mandatory"
        }
      ]
    }
  ]
})
```

**Store responses:**
- `synrgCommands`
- `automationLevel`
- `screenshotValidation`

---

## PHASE 4.5: 🧠 AUTOMATION STRATEGY VALIDATION

**Purpose:** Validate automation choices against project needs and provide strategic guidance

---

## 🧠 Automation Strategy Validation

### ✅ Your Automation Configuration

**SYNRG Commands:** [synrgCommands]
**Automation Level:** [automationLevel]
**Screenshot Validation:** [screenshotValidation]

---

### 💡 Automation Strategy Insights

#### Automation Level Analysis

**Your Choice:** [automationLevel]

**Matches Your Project If:**
- Project stage: [projectStage]
- Team size: [estimate based on project type]
- Risk tolerance: [High/Medium/Low]

**Automation Level Breakdown:**

| Level | Auto-proceed Threshold | Escalation Rate | Deployment Frequency | Best For |
|-------|------------------------|-----------------|----------------------|----------|
| **Maximum Autonomy** | 70/100 | ~20% | Multiple/day | Mature teams, fast iteration |
| **Balanced** | 50/100 | ~40% | Daily | Most projects |
| **Conservative** | 30/100 | ~60% | Weekly | New projects, high stakes |

**Your Selection ([automationLevel]) Implies:**
- **Speed:** [Fast/Medium/Slow] iteration cycles
- **Oversight:** [Low/Medium/High] human validation required
- **Risk Acceptance:** [High/Medium/Low]
- **Team Maturity Needed:** [High/Medium/Low]

---

#### Screenshot Validation Strategy

**Your Choice:** [screenshotValidation]

**Cost-Benefit Analysis:**

| Validation Level | Setup Time | Maintenance | Bug Detection | CI Time Added | Best For |
|------------------|-----------|-------------|---------------|---------------|----------|
| **Always** | High | High | 95%+ UI bugs caught | +10-15 min | User-facing apps |
| **UI Only** | Medium | Medium | 80%+ UI bugs caught | +5-10 min | Mixed apps |
| **Optional** | Low | Low | 50%+ UI bugs caught | +0-5 min | Backend/CLI |

**For [projectType]:**
- **Recommended:** [Level]
- **Why:** [Reasoning based on project type]
- **Industry Standard:** [What similar projects do]

**Top Performer Insight:**
Companies like [examples] use screenshot validation for [specific scenarios] but avoid it for [other scenarios] to maintain [deployment frequency metric].

**Optimization Strategy:**
- Critical user flows: Always screenshot validate
- Admin/internal pages: Manual validation
- API/backend: No screenshots needed
- Non-visual changes: Skip screenshot validation

---

### 🌐 Automation Ecosystem Perspective

#### Industry Automation Trends

**Current State (2024-2025):**
- **Average Automation Level:** ~45% of changes auto-deployed
- **Elite Performers:** 70-80% auto-deployment
- **Trend:** Moving toward autonomous validation with AI-assisted verification

**Your Configuration:**
- **Automation Percentage:** [estimate based on automationLevel]
- **Relative Position:** [Below/At/Above] industry average
- **Growth Path:** [What needs to happen to increase automation]

---

#### Risk vs Speed Tradeoff

**Your Configuration Prioritizes:** [Speed / Balance / Safety]

**Tradeoff Analysis:**

```
Risk Tolerance ←―――――――――――――――→ Speed Priority
Conservative         Balanced         Maximum Autonomy
│                       │                      │
│                       │                      │
Low deployment    Moderate deployment    High deployment
frequency         frequency              frequency
│                       │                      │
High quality      Balanced quality       Quality through
through gates     through automation     rapid iteration
```

**Your Position:** [Mark on spectrum]

**Optimal for [projectType]:** [Position on spectrum]

**Adjustment Recommendation:**
[If misaligned, suggest moving toward optimal position with reasoning]

---

### ⚖️ Automation Configuration Matrix

| Aspect | Your Config | Alternative 1 (More Auto) | Alternative 2 (More Manual) |
|--------|-------------|---------------------------|-----------------------------|
| **Auto-proceed %** | [percentage] | [percentage] | [percentage] |
| **Daily Escalations** | [estimate] | [estimate] | [estimate] |
| **Deployment Frequency** | [frequency] | [frequency] | [frequency] |
| **Developer Interruptions** | [count/day] | [count/day] | [count/day] |
| **Bug Escape Rate** | [percentage] | [percentage] | [percentage] |
| **Time to Production** | [hours] | [hours] | [hours] |
| **Rollback Frequency** | [percentage] | [percentage] | [percentage] |

---

### ❓ Final Automation Recommendation

**Overall Assessment:** [Optimal / Good / Needs Tuning]

**Strengths:**
1. [Positive aspect of configuration]
2. [Good decision]

**Potential Adjustments:**

**Consider More Automation If:**
- You find yourself approving >80% of escalations
- Team is experienced with the stack
- Rollback capability is strong
- [Additional conditions]

**Consider More Conservative Approach If:**
- High stakes (financial, healthcare, critical infrastructure)
- Team is learning the stack
- Deployment rollback is complex
- [Additional conditions]

**Recommended Starting Point:**
For [projectStage] projects with [projectType]:
- **Automation Level:** [Recommended level]
- **Screenshot Validation:** [Recommended approach]
- **Rationale:** [Why this configuration]

**Evolution Path:**
1. **Month 1-3:** [Initial configuration]
2. **Month 4-6:** [Increase automation to X level as confidence grows]
3. **Month 7+:** [Mature automation configuration]

---

**Proceed to scaffolding?**
1. ✅ Yes, configuration validated
2. 🔄 Adjust automation level
3. 💬 Discuss specific concern

[Wait for user decision before Phase 5]

---

## PHASE 5: DIRECTORY SCAFFOLDING & GENERATION

[... Rest of the scaffolding implementation remains the same as original ...]

---

**Note:** The remainder of Phase 5 and Phase 6 implementation continues with the same comprehensive generation logic from the original command, but now informed by all the strategic insights gathered in phases 1.5, 2.5, 3.5, and 4.5.

---

## EXECUTION CHECKLIST

When this command is invoked:

- [ ] PHASE 1: Project Type Discovery (3 questions)
- [ ] PHASE 1.5: 🧠 Strategic Foundation Analysis
- [ ] PHASE 2: Adaptive Context Gathering (4-5 questions)
- [ ] PHASE 2.5: 🧠 Ecosystem & Alternative Analysis (per technology)
- [ ] PHASE 3: Development Workflow & Standards (4 questions)
- [ ] PHASE 3.5: 🧠 Workflow Optimization Analysis
- [ ] PHASE 4: SYNRG Integration Preferences (3 questions)
- [ ] PHASE 4.5: 🧠 Automation Strategy Validation
- [ ] PHASE 5: Directory Scaffolding & Generation (6+ files)
- [ ] PHASE 6: Validation & Summary Report

**Total:** ~14-17 adaptive questions + 4 strategic analysis phases, complete project setup with elite-level insights.

---

**Version:** 2.0.0
**Last Updated:** 2025-11-22
**Command:** `/synrg-scaffold`
**New in v2.0:** Strategic alternative analysis, top 1% performer insights, ecosystem perspective throughout
