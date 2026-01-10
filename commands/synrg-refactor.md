---
synrg_version: "3.0.0"
command: "synrg-refactor"
created: "2025-06-01"
updated: "2026-01-09"
min_claude_version: "opus-4"
requires:
  protocols: [mcdp, sub-agent-spawn]
  agents: []
  skills: [certainty-gated-atomic-change]
breaking_changes: []
description: Execute SYNRG File Restructuring Agent with intelligent code quality elevation
argument-hint: [restructuring objective and scope]
---

# SYNRG-REFACTOR v3.0: Intelligent File Restructuring + Code Quality Orchestrator
## AI-Optimized Codebase Architecture with Robustness-First Refactoring

You are now executing the SYNRG File Restructuring Orchestrator v3.0 - a specialized multi-agent system for reorganizing codebases into intelligent, senior-developer-level structures optimized for AI agent navigation and context window efficiency, **with integrated code quality elevation through systematic refactoring**.

**CRITICAL**: This is an **EXECUTABLE ORCHESTRATOR**, not a specification document. You MUST use the Task tool to spawn actual sub-agents. This command coordinates multiple specialized agents using the Task tool with proper parallel execution and comprehensive error handling.

---

## 🎯 Core Mission

**Primary Objective**: Restructure code files into an organized structure that:
1. Optimizes for AI agent context window efficiency
2. Preserves complete project integrity (no broken imports, no runtime errors)
3. Follows senior developer architecture patterns **with active code quality elevation**
4. Eliminates code smells and technical debt during reorganization
5. Applies SOLID principles and design patterns where beneficial
6. Groups related functionality for minimal cross-domain dependencies
7. Enables easy navigation and understanding of code flow

**User Objective**: $ARGUMENTS

**Philosophy**: Following SYNRG v3.0 robustness-first approach:
- Take as long as needed for perfection
- No quick fixes or workarounds
- Production-ready from start
- Comprehensive quality gates
- Mandatory error analysis on all failures
- **🆕 Anti-Memory Protocol Active** (v4.1) - Never trust memory for known failure patterns

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
│  REFACTOR-SPECIFIC: Codebase analysis MUST be delegated to parallel agents  │
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
GATE 1: ANTI-MEMORY    - READ files, don't trust memory
GATE 2: GIT_STRATEGY   - Refactoring = ALWAYS feature branch or worktree
GATE 3: CERTAINTY      - Certainty = (Evidence + Understanding + Isolation) / 3
                         Level 4 (multi-file): >=90% | Level 5 (arch): >=95% + USER
GATE 4: SECURITY       - Secrets/OWASP/Privilege/Deps check on all changes
GATE 5: USER_VERIFY    - Get approval for refactoring scope
```

### POST-IMPLEMENTATION REVIEWS
```
REVIEW 1: OBJECTIVE    - Refactoring achieved? No broken imports/tests?
REVIEW 2: SECURITY     - Re-scan refactored files for vulnerabilities
REVIEW 3: DOCS (P5)    - Update architecture docs for structural changes
REVIEW 4: COMMIT       - Use /synrg-commit for atomic commits
REVIEW 5: QUALITY      - All gates passed → COMPLETE
```

**MCP Delegate Agent Registry:**

| MCP Domain | Delegate Agent | Agent File |
|------------|----------------|------------|
| `mcp__n8n-mcp__*` | `n8n-mcp-delegate` | `${CLAUDE_AGENTS}/n8n-mcp-delegate.md` |
| `mcp__n8n-workflows__*` | `github-mcp-delegate` | `${CLAUDE_AGENTS}/github-mcp-delegate.md` |

**Enforcement**: Direct MCP calls are FORBIDDEN. Violation requires immediate self-correction.

---

## 🔴 Anti-Memory Protocol for Refactoring (v4.1)

**CRITICAL**: Refactoring operations involve high-risk configuration patterns. Apply Anti-Memory Protocol.

### Known Failure Patterns in Refactoring Context

| Pattern | Risk | Protocol |
|---------|------|----------|
| Import path updates | Expression syntax contamination | READ n8n/tool docs before modifying |
| Config file edits | Environment variable format errors | COPY from documented reference |
| Build tool configs | Version-specific parameter formats | VALIDATE with tool's latest docs |
| Type definitions | Auto-generated file modifications | VERIFY if file is auto-generated first |

### Refactoring-Specific Memory Safety Rules

**Before ANY file modification**:
1. **CHECK** if file pattern matches Known Failure Points
2. **READ** relevant documentation if pattern matches
3. **VALIDATE** proposed changes against documented syntax
4. **VERIFY** changes don't introduce expression syntax contamination

**Sub-Agent Injection**: When spawning refactoring sub-agents, inject:
```
⚠️ ANTI-MEMORY PROTOCOL: This refactoring task may involve known failure patterns.
Before modifying configuration files, import statements, or type definitions:
- READ the documented reference (do not reconstruct from memory)
- VALIDATE syntax against tool documentation
- VERIFY no expression prefix contamination (e.g., "=data" vs "data")
```

---

## 🧠 CLAUDE TOOL SELECTION PROTOCOL (Reference: /synrg)

**BEFORE executing ANY refactoring task, select the optimal Claude tool type:**

| Tool Type | When to Use | Action |
|-----------|-------------|--------|
| **SUB-AGENTS** | Isolated context, parallel execution, >500 token responses | Task tool with agent type |
| **SLASH COMMANDS** | Multi-phase orchestration, command chaining | SlashCommand tool |
| **HOOKS** | Event-triggered automation (pre-commit, etc.) | Create in .claude/hooks/ |
| **SKILLS** | Reusable methodology across agents | Create in .claude/skills/ |
| **DIRECT TOOLS** | Simple one-shot operations (last resort) | Built-in tools |

**Refactoring-Specific Tool Selection:**
- Large file restructuring → SUB-AGENT (isolated context for diffs)
- Code quality analysis → SUB-AGENT (analysis patterns)
- Pre-commit validation → HOOK (event-triggered)
- Debugging methodology → SKILL (reusable across agents)

**Tool Creation Gate**: If optimal tool doesn't exist AND task is recurring → CREATE the tool first.

**Ecosystem Proliferation**: After improvements → PROPAGATE to ALL /synrg-* commands.

**Full Protocol**: See `/synrg` command for complete Tool Type Decision Matrix, Task Analysis Protocol, and examples.

---

## 🔴 MANDATORY: Sub-Agent Delegation Protocol (v4.3)

**BEFORE spawning refactoring agents, CHECK for existing specialized agents:**

```
┌─────────────────────────────────────────────────────────────┐
│  AGENT LIBRARY CHECK (MANDATORY)                            │
│                                                             │
│  1. CHECK ${CLAUDE_AGENTS}/ for relevant agents             │
│  2. USE existing agents instead of spawning generic ones    │
│  3. CREATE new agents if task type has no coverage          │
│  4. DOCUMENT new agents in agents-evolution.md              │
└─────────────────────────────────────────────────────────────┘
```

### Available Specialized Agents

Check `${CLAUDE_AGENTS}/` before spawning. Key agents:
- **N8N**: `n8n-node-validator`, `n8n-connection-fixer`, `n8n-expression-debugger`, `n8n-workflow-expert`
- **General**: `full-stack-dev-expert`, `agency-automation-expert`

**If refactoring involves n8n workflows**: Delegate to n8n agents first.

---

## 📊 EXECUTION OVERVIEW

This orchestrator executes in **7 coordinated phases** with **28+ specialized Task agents**:

- **Phase 0**: Context Gathering & Safety (Interactive + Validation)
- **Phase 1**: Discovery & Analysis (6 parallel Task agents)
- **Phase 1.5**: Refactoring Opportunity Synthesis (1 Task agent)
- **Phase 2**: Risk Analysis (8 parallel Task agents)
- **Phase 3**: Strategy Generation (1 Task agent)
- **Phase 3.5**: User Approval (Interactive)
- **Phase 5**: Execution (Dynamic Task agents per batch)
- **Phase 6**: Validation (7 parallel Task agents)
- **Phase 7**: Commit & Documentation

---

## PHASE 0: CONTEXT GATHERING & SAFETY SETUP

### STEP 0.1: Verify Prerequisites & Create Safety Checkpoint

Before starting ANY analysis, verify safety and create checkpoint:

```bash
# 1. Check git status - MUST be clean or user-approved
git status

# 2. Verify we're in a valid project
ls package.json || ls requirements.txt || ls go.mod || ls Cargo.toml

# 3. Create safety checkpoint
git add -A
git commit -m "CHECKPOINT: Pre-refactor state ($(date))" || echo "Clean state, no checkpoint needed"
git branch synrg-refactor-checkpoint-$(date +%Y%m%d-%H%M%S)
```

**If git is dirty**: Use AskUserQuestion tool to ask:
- "Your git working directory has uncommitted changes. How should we proceed?"
- Options:
  - "Commit changes first (recommended)"
  - "Stash changes and proceed"
  - "Cancel - I'll clean up manually"

**MANDATORY**: Stop execution if user chooses "Cancel" or if no valid project detected.

---

### STEP 0.2: Interactive Context Gathering (MANDATORY)

Use the **AskUserQuestion tool** to gather essential context before any analysis:

```javascript
// REQUIRED QUESTION 1: Scope Definition
{
  question: "Which parts of the codebase should be restructured?",
  header: "Scope",
  multiSelect: false,
  options: [
    {
      label: "Entire project (comprehensive overhaul)",
      description: "Restructure all source files - full codebase reorganization"
    },
    {
      label: "Specific directory (e.g., src/components, lib/)",
      description: "Focus on one directory tree only"
    },
    {
      label: "Files matching pattern (e.g., *.tsx, api/)",
      description: "Restructure only files matching specific glob patterns"
    },
    {
      label: "Let analysis decide (recommended)",
      description: "Run discovery first, then I'll review and choose scope"
    }
  ]
}

// REQUIRED QUESTION 2: Constraints & Exclusions
{
  question: "Are there any files or folders that should NOT be moved?",
  header: "Exclusions",
  multiSelect: false,
  options: [
    {
      label: "Standard exclusions only",
      description: "node_modules, dist, build, .git (common exclusions)"
    },
    {
      label: "Also exclude config files",
      description: "+ config files, .env, public assets, root-level configs"
    },
    {
      label: "Also exclude test files",
      description: "+ test files (reorganize separately later)"
    },
    {
      label: "Custom exclusions",
      description: "I'll specify custom patterns in next message"
    }
  ]
}

// REQUIRED QUESTION 3: Risk Tolerance
{
  question: "How should we handle high-risk file moves (critical paths, many dependents)?",
  header: "Risk Tolerance",
  multiSelect: false,
  options: [
    {
      label: "Skip high-risk moves (safest)",
      description: "Only move low/medium risk files automatically"
    },
    {
      label: "Present for manual approval",
      description: "Show me high-risk moves, I'll approve each one"
    },
    {
      label: "Proceed with extra validation",
      description: "Move high-risk files but with comprehensive testing"
    },
    {
      label: "Full auto-pilot (trust analysis)",
      description: "Move all files based on analysis confidence"
    }
  ]
}

// REQUIRED QUESTION 4: Code Quality Improvement Level (INTEGRATED REFACTORING)
{
  question: "How much code quality improvement during restructuring?",
  header: "Quality Level",
  multiSelect: false,
  options: [
    {
      label: "Minimal: Just file moves",
      description: "Rename obvious issues only, no structural changes"
    },
    {
      label: "Conservative: Extract constants, simple methods",
      description: "Low-risk refactorings (constants, short method extractions)"
    },
    {
      label: "Balanced: Include class splits, interfaces",
      description: "Moderate refactorings (extract classes, guard clauses, DIP)"
    },
    {
      label: "Comprehensive: Full SOLID + patterns",
      description: "All refactorings (SOLID fixes, design patterns, major splits)"
    },
    {
      label: "Suggest: Show opportunities, I approve",
      description: "Analysis only - I'll approve each refactoring individually"
    }
  ]
}

// REQUIRED QUESTION 5: Validation Requirements
{
  question: "Which validation checks should run after restructuring?",
  header: "Validation",
  multiSelect: true,  // Can select multiple
  options: [
    {
      label: "Type checking",
      description: "TypeScript/Python type validation (tsc, mypy)"
    },
    {
      label: "Build validation",
      description: "Ensure project builds successfully"
    },
    {
      label: "Test suite",
      description: "Run all tests (unit + integration + e2e)"
    },
    {
      label: "Code quality metrics",
      description: "Complexity, coupling, cohesion measurements"
    },
    {
      label: "Manual smoke test",
      description: "I'll manually verify key functionality"
    }
  ]
}
```

**After gathering context, synthesize into execution parameters:**

```javascript
const executionConfig = {
  scope: userAnswers.scope,
  exclusions: userAnswers.exclusions,
  riskTolerance: userAnswers.riskTolerance,
  qualityLevel: userAnswers.qualityImprovementLevel,
  validations: userAnswers.validations,
  objective: "$ARGUMENTS",

  // Derived settings
  shouldRunDiscoveryFirst: userAnswers.scope === "Let analysis decide",
  allowHighRiskMoves: userAnswers.riskTolerance !== "Skip high-risk moves",
  requiresRefactoringApproval: userAnswers.qualityLevel === "Suggest",
  comprehensiveValidation: userAnswers.validations.length >= 3
};
```

**Display Configuration Summary**:
```
📋 SYNRG-REFACTOR Configuration
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Objective: {$ARGUMENTS}
Scope: {executionConfig.scope}
Exclusions: {executionConfig.exclusions}
Risk Tolerance: {executionConfig.riskTolerance}
Quality Level: {executionConfig.qualityLevel}
Validations: {executionConfig.validations.join(', ')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ready to proceed with Phase 1: Discovery & Analysis
```

---

### 🆕 MCP Tool Delegation Protocol for Refactoring (v4.2)

**When refactoring involves MCP-managed systems** (n8n workflows, GitHub repos, etc.), spawn MCP delegation agents alongside discovery agents.

**Detection Logic**:
```javascript
function detectMCPRefactoringNeeds(objective, scope) {
  const mcpPatterns = {
    'n8n-mcp': {
      indicators: ['workflow', 'n8n', 'automation', 'node'],
      tools: ['mcp__n8n-mcp__n8n_get_workflow', 'mcp__n8n-mcp__validate_workflow']
    },
    'github-mcp': {
      indicators: ['repository', 'github', 'branch', 'PR'],
      tools: ['mcp__n8n-workflows__get_file_contents', 'mcp__n8n-workflows__list_commits']
    }
  };

  const detected = [];
  for (const [name, config] of Object.entries(mcpPatterns)) {
    if (config.indicators.some(i => objective.toLowerCase().includes(i))) {
      detected.push({ name, tools: config.tools });
    }
  }
  return detected;
}
```

**MCP-Aware Discovery Agent**:
```javascript
// If MCP systems detected, add MCP delegation agent to Phase 1 batch
const mcpNeeds = detectMCPRefactoringNeeds(objective, scope);
if (mcpNeeds.length > 0) {
  // Spawn MCP delegation agent alongside 6 discovery agents (7 total)
  const mcpAgent = {
    id: 'mcp-context-delegate',
    role: 'MCP System Context Gathering',
    task: 'Fetch and distill MCP system state for refactoring context',
    tools: mcpNeeds.flatMap(m => m.tools),
    delegationProtocol: {
      returnFormat: {
        summary: 'Brief state summary',
        vitalData: 'Current configurations, active workflows',
        warnings: 'Conflicts, deprecated configs',
        references: 'IDs for affected systems'
      },
      excludeFromReturn: ['Full JSON payloads', 'Complete workflow definitions']
    }
  };
  discoveryAgents.push(mcpAgent);
}
```

**Context Efficiency in Refactoring**:
- MCP agents run parallel to file discovery agents
- Return distilled context (70-90% reduction)
- Director integrates MCP state into refactoring strategy
- No raw MCP payloads in main orchestrator context

---

## PHASE 1: DISCOVERY & ANALYSIS

**Objective**: Build complete understanding of codebase structure, dependencies, data flow, **AND identify refactoring opportunities**

**CRITICAL**: This phase spawns **6 parallel Task agents** simultaneously. You MUST invoke all 6 Tasks in a **single message** for maximum parallelization.

### BATCH 1A: File System & Code Quality Analysis (6 Parallel Task Agents)

**Execute ALL 6 Task invocations in parallel (single message with 6 Task tool calls):**

```javascript
// AGENT 1A: FileScanner
Task({
  subagent_type: "general-purpose",
  description: "Scan and categorize all files",
  prompt: `You are Agent 1A-FileScanner for SYNRG-REFACTOR v3.0.

**CONTEXT**:
- User Objective: ${executionConfig.objective}
- Scope: ${executionConfig.scope}
- Exclusions: ${executionConfig.exclusions}

**TASK**: Scan and categorize all files in scope

**DELIVERABLE**: Structured file tree with metadata (JSON format)

**ACTIONS**:
1. Use Glob tool to find all files matching scope patterns
2. For each file, extract:
   - Path (absolute)
   - Type (component, util, type, config, test, api, service, hook, style)
   - Size (lines of code)
   - Last modified timestamp
   - Estimated import count (use heuristics)
3. Categorize files:
   - needs_analysis: Large files (>500 lines), suspicious naming
   - standard: Normal files
   - critical: Entry points, main config files
4. Flag issues:
   - Suspiciously large files (>500 lines)
   - Inconsistent naming (PascalCase vs camelCase mismatches)
   - Orphaned files (no imports)

**OUTPUT FORMAT** (JSON):
{
  "summary": {
    "totalFiles": number,
    "byType": { "component": count, "util": count, ... },
    "byCategory": { "needs_analysis": count, "standard": count, "critical": count },
    "avgSize": number,
    "largeFiles": count
  },
  "files": [
    {
      "path": "src/components/UserProfile.tsx",
      "type": "component",
      "size": 245,
      "lastModified": "2024-10-15T10:30:00Z",
      "estimatedImports": 8,
      "category": "standard",
      "flags": []
    },
    ...
  ]
}

**VALIDATION CRITERIA**:
- ✅ File count > 0 (at least some files found)
- ✅ All paths exist and are accessible
- ✅ All files properly categorized
- ✅ JSON is valid and parseable

**EVIDENCE REQUIRED**:
- Complete JSON file tree
- Summary statistics
- List of flagged files (if any)

**ROBUSTNESS REQUIREMENTS** (SYNRG v3.0):
- If Glob tool fails: Perform 5-Why root cause analysis
- If file access errors: Assess impact (which files blocked, why)
- If zero files found: Escalate immediately (likely scope issue)
- Report any errors with comprehensive error analysis

**TIME BUDGET**: Take as long as needed for thorough analysis
**CONTEXT BUDGET**: ~30K tokens maximum

Execute this task with production-grade quality.`
})

// AGENT 1B: DependencyMapper
Task({
  subagent_type: "general-purpose",
  description: "Build dependency graph with coupling",
  prompt: `You are Agent 1B-DependencyMapper for SYNRG-REFACTOR v3.0.

**CONTEXT**:
- User Objective: ${executionConfig.objective}
- Scope: ${executionConfig.scope}

**TASK**: Parse all imports/exports and build dependency graph WITH coupling metrics

**DELIVERABLE**: Dependency graph with import chains and coupling analysis (JSON format)

**ACTIONS**:
1. Use Grep tool to find all import statements:
   - import/from statements (JavaScript/TypeScript)
   - require statements (CommonJS)
   - import statements (Python)
   - use statements (Rust)
   - Appropriate patterns for detected language
2. For each file, map:
   - Which files it imports (dependencies)
   - Which files import it (dependents)
   - Import depth (how many hops from entry point)
3. Calculate coupling metrics:
   - Fan-In: How many files import this file
   - Fan-Out: How many files this file imports
   - Afferent Coupling (Ca): Number of external classes that depend on this
   - Efferent Coupling (Ce): Number of external classes this depends on
   - Instability (I): Ce / (Ca + Ce) where 0 = stable, 1 = unstable
4. Identify issues:
   - Circular dependencies (A → B → C → A)
   - Orphaned files (no imports or dependents)
   - Highly coupled files (Fan-In > 20 or Fan-Out > 15)
   - "Shotgun Surgery" smell (one change requires many file edits)

**OUTPUT FORMAT** (JSON):
{
  "summary": {
    "totalDependencies": number,
    "circularDeps": number,
    "orphanedFiles": number,
    "highCouplingFiles": number,
    "avgFanIn": number,
    "avgFanOut": number,
    "avgInstability": number
  },
  "dependencies": {
    "src/utils/api.ts": {
      "imports": ["axios", "./types", "./config"],
      "importedBy": ["src/pages/Dashboard.tsx", "src/lib/user-service.ts"],
      "fanIn": 12,
      "fanOut": 3,
      "afferentCoupling": 12,
      "efferentCoupling": 3,
      "instability": 0.2,
      "circular": false,
      "shotgunSurgery": false,
      "importDepth": 3
    },
    ...
  },
  "circularDependencies": [
    {
      "cycle": ["src/utils/api.ts", "src/lib/user.ts", "src/utils/api.ts"],
      "severity": "high"
    }
  ],
  "orphanedFiles": ["src/legacy/old-util.ts"]
}

**VALIDATION CRITERIA**:
- ✅ All imports resolved (or marked as unresolved)
- ✅ No missing files in dependency graph
- ✅ Circular dependencies correctly identified
- ✅ Coupling metrics calculated for all files

**EVIDENCE REQUIRED**:
- Complete dependency graph (JSON)
- Circular dependency list with severity
- High-coupling file list
- Coupling metrics summary

**ROBUSTNESS REQUIREMENTS** (SYNRG v3.0):
- If import parsing fails: Analyze which language/pattern caused issue
- If circular deps found: Assess breaking strategies
- If orphaned files: Determine if safe to delete or archive
- Comprehensive error analysis on any failures

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~40K tokens maximum

Execute with production-grade precision.`
})

// AGENT 1C: CodeFlowTracer
Task({
  subagent_type: "general-purpose",
  description: "Trace critical execution paths",
  prompt: `You are Agent 1C-CodeFlowTracer for SYNRG-REFACTOR v3.0.

**CONTEXT**:
- User Objective: ${executionConfig.objective}
- Scope: ${executionConfig.scope}

**TASK**: Trace data flow and user interaction paths to identify critical execution paths

**DELIVERABLE**: Critical execution paths and data flow diagram (JSON format)

**ACTIONS**:
1. Identify entry points:
   - Main application files (main.tsx, App.tsx, index.tsx)
   - API route handlers (pages/api/, app/api/, routes/)
   - Server entry points (server.ts, app.py)
   - CLI entry points
2. Trace execution flows:
   - User interactions → Components → Services → Data layer
   - API requests → Controllers → Services → Database
   - Data flow: Props, State, Context, API calls, DB queries
3. Map critical paths:
   - Authentication flows (login, logout, session)
   - Payment processing (if applicable)
   - Core business logic flows
   - Data CRUD operations
4. Rate criticality:
   - Critical: Auth, payments, core APIs (failure = system down)
   - High: Major features (failure = bad UX)
   - Medium: Secondary features
   - Low: Nice-to-have, rarely used

**OUTPUT FORMAT** (JSON):
{
  "summary": {
    "entryPoints": number,
    "criticalPaths": number,
    "highPaths": number,
    "totalFlows": number
  },
  "entryPoints": [
    {
      "path": "src/pages/Login.tsx",
      "type": "ui-entry",
      "criticality": "critical"
    }
  ],
  "flows": [
    {
      "name": "user-authentication",
      "entry": "src/pages/Login.tsx",
      "path": [
        "src/components/LoginForm.tsx",
        "src/lib/auth-service.ts",
        "src/api/auth.ts",
        "database"
      ],
      "criticality": "critical",
      "reason": "Auth gateway - all protected routes depend",
      "touchPoints": 8,
      "dataFlow": "credentials → validation → JWT → session storage"
    },
    ...
  ]
}

**VALIDATION CRITERIA**:
- ✅ All entry points identified
- ✅ Critical paths correctly rated
- ✅ Data flow accurately traced
- ✅ No missing critical business logic

**EVIDENCE REQUIRED**:
- Flow diagram (JSON structure)
- Criticality ratings with justification
- Complete path traces

**ROBUSTNESS REQUIREMENTS** (SYNRG v3.0):
- If entry points unclear: Use heuristics and document assumptions
- If flows too complex: Simplify representation without losing accuracy
- If critical paths uncertain: Escalate for user confirmation
- Comprehensive error analysis on failures

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~35K tokens maximum

Execute with production-grade thoroughness.`
})

// AGENT 1D: PatternDetector
Task({
  subagent_type: "general-purpose",
  description: "Detect framework patterns and anti-patterns",
  prompt: `You are Agent 1D-PatternDetector for SYNRG-REFACTOR v3.0.

**CONTEXT**:
- User Objective: ${executionConfig.objective}
- Scope: ${executionConfig.scope}

**TASK**: Identify framework patterns and architectural anti-patterns

**DELIVERABLE**: Pattern analysis report with recommendations (JSON format)

**ACTIONS**:
1. Detect framework and conventions:
   - Next.js (App Router vs Pages Router)
   - React (version, patterns used)
   - Express, Fastify, NestJS
   - FastAPI, Django, Flask
   - Other frameworks (detect automatically)
2. Identify framework conventions:
   - Where API routes should be
   - Component organization patterns
   - Data fetching patterns
   - State management patterns
3. Detect anti-patterns:
   - God objects (classes doing too much)
   - Scattered utilities (random util files)
   - Mixed concerns (business logic in UI)
   - Inconsistent naming (camelCase vs snake_case, PascalCase misuse)
   - Wrong locations (components in lib/, utils in components/)
4. Suggest ideal patterns:
   - Framework-specific best practices
   - Industry-standard folder structures
   - Recommended organization by domain

**OUTPUT FORMAT** (JSON):
{
  "framework": {
    "name": "Next.js",
    "version": "14.x",
    "variant": "App Router",
    "confidence": "high"
  },
  "conventions": {
    "detected": [
      "API routes in app/api/",
      "Server components by default",
      "Named exports for components"
    ],
    "recommended": [
      "Use route groups for organization",
      "Colocate route-specific components",
      "Use parallel routes for complex UIs"
    ]
  },
  "antiPatterns": [
    {
      "type": "scattered_utils",
      "severity": "medium",
      "files": ["src/utils/misc.ts", "lib/helpers.ts", "components/utils.ts"],
      "issue": "Utility functions scattered across 3 locations",
      "recommendation": "Consolidate into domain-specific utils (e.g., utils/string/, utils/date/)",
      "priority": "high"
    },
    {
      "type": "mixed_concerns",
      "severity": "high",
      "files": ["src/components/Dashboard.tsx"],
      "issue": "Business logic (calculations, API calls) in UI component",
      "recommendation": "Extract to custom hooks or service layer",
      "priority": "critical"
    }
  ],
  "idealStructure": {
    "description": "Next.js 14 App Router with domain-driven design",
    "example": "/app, /features, /lib, /components/ui, /utils"
  }
}

**VALIDATION CRITERIA**:
- ✅ Framework correctly detected
- ✅ Anti-patterns accurately identified
- ✅ Recommendations actionable
- ✅ Severity ratings justified

**EVIDENCE REQUIRED**:
- Framework detection proof
- Anti-pattern examples
- Ideal structure recommendations

**ROBUSTNESS REQUIREMENTS** (SYNRG v3.0):
- If framework unclear: Document assumptions
- If anti-patterns ambiguous: Explain reasoning
- If recommendations conflict: Prioritize by impact
- Comprehensive error analysis on failures

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~30K tokens maximum

Execute with senior developer-level insight.`
})

// AGENT 1E: CodeSmellDetector
Task({
  subagent_type: "general-purpose",
  description: "Detect code smells for refactoring",
  prompt: `You are Agent 1E-CodeSmellDetector for SYNRG-REFACTOR v3.0.

**CONTEXT**:
- User Objective: ${executionConfig.objective}
- Scope: ${executionConfig.scope}
- Quality Level: ${executionConfig.qualityLevel}

**TASK**: Detect code smells indicating refactoring opportunities

**DELIVERABLE**: Code smell report with refactoring recommendations (JSON format)

**ACTIONS**:
Scan for common code smells across three levels:

**METHOD-LEVEL SMELLS**:
- Long Method: Functions >50 lines → Extract Method
- Long Parameter List: >4 parameters → Parameter Object
- Complex Conditionals: Nested if/else >3 levels → Guard Clauses
- Duplicated Code: Similar blocks → Extract Method/Class
- Feature Envy: Method uses more of another class → Move Method
- Data Clumps: Same variables together → Extract Class

**CLASS-LEVEL SMELLS**:
- Large Class: >300 lines or >10 methods → Extract Class
- God Class: Knows/does too much → Split Responsibilities
- Lazy Class: Does too little → Inline or delete
- Data Class: Only fields, no behavior → Move Methods here
- Refused Bequest: Inherits unused methods → Composition

**DESIGN SMELLS**:
- Divergent Change: Changed for many reasons → Split (SRP)
- Shotgun Surgery: One change needs many edits → Move Method
- Parallel Inheritance: Adding subclass needs another → Collapse
- Speculative Generality: Unused abstractions → Remove (YAGNI)
- Message Chains: a.getB().getC() → Hide Delegate
- Middle Man: Only delegates → Remove or Inline
- Inappropriate Intimacy: Classes too coupled → Move or Extract

**OUTPUT FORMAT** (JSON):
{
  "summary": {
    "totalSmells": number,
    "bySeverity": { "critical": count, "high": count, "medium": count, "low": count },
    "byType": { "method": count, "class": count, "design": count }
  },
  "smells": [
    {
      "file": "src/services/UserService.ts",
      "smell": "Large Class",
      "severity": "high",
      "location": { "line": 1, "endLine": 458 },
      "metrics": {
        "lines": 458,
        "methods": 23,
        "complexity": 156
      },
      "refactoring": {
        "type": "Extract Class",
        "suggestion": "Split into UserAuthService, UserProfileService, UserPreferencesService",
        "confidence": "high",
        "effort": "medium",
        "benefits": [
          "Improved Single Responsibility",
          "Better testability",
          "Easier AI navigation",
          "Reduced complexity per class"
        ],
        "solidPrinciple": "Single Responsibility (SRP)"
      }
    },
    ...
  ]
}

**VALIDATION CRITERIA**:
- ✅ All smells categorized with severity
- ✅ Actionable refactorings for each smell
- ✅ Effort/benefit analysis included
- ✅ SOLID principles mapped where applicable

**EVIDENCE REQUIRED**:
- Complete smell inventory
- Refactoring roadmap
- Prioritization by severity and effort

**ROBUSTNESS REQUIREMENTS** (SYNRG v3.0):
- If file too large to analyze: Analyze by sections
- If smells ambiguous: Document reasoning
- If refactoring unclear: Provide multiple options
- Comprehensive error analysis on failures

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~35K tokens maximum

Execute with senior refactoring expertise.`
})

// AGENT 1F: ComplexityAnalyzer
Task({
  subagent_type: "general-purpose",
  description: "Analyze code complexity metrics",
  prompt: `You are Agent 1F-ComplexityAnalyzer for SYNRG-REFACTOR v3.0.

**CONTEXT**:
- User Objective: ${executionConfig.objective}
- Scope: ${executionConfig.scope}

**TASK**: Analyze code complexity and maintainability metrics

**DELIVERABLE**: Complexity report with improvement opportunities (JSON format)

**ACTIONS**:
Calculate complexity metrics for all functions/methods:

**COMPLEXITY METRICS**:
1. Cyclomatic Complexity: Independent execution paths
   - Target: <10 (low)
   - Warning: 10-20 (medium)
   - Critical: >20 (high)

2. Cognitive Complexity: Mental effort to understand
   - Target: <15
   - Warning: 15-30
   - Critical: >30

3. Maintainability Index: 0-100 score
   - Good: >60
   - Warning: 40-60
   - Poor: <40

4. Nesting Depth: Maximum nesting level
   - Good: <4
   - Warning: 4-6
   - Poor: >6

5. Lines of Code: Physical, logical, comment lines

6. LCOM (Lack of Cohesion of Methods):
   - Target: <0.5 (high cohesion)
   - Warning: 0.5-0.7
   - Poor: >0.7 (low cohesion)

**OUTPUT FORMAT** (JSON):
{
  "summary": {
    "totalFunctions": number,
    "highComplexity": number,
    "mediumComplexity": number,
    "lowComplexity": number,
    "avgCyclomaticComplexity": number,
    "avgCognitiveComplexity": number,
    "avgMaintainability": number,
    "criticalFunctions": number
  },
  "complexity": [
    {
      "file": "src/lib/payment-processor.ts",
      "function": "processPayment",
      "location": { "line": 45, "endLine": 192 },
      "metrics": {
        "cyclomaticComplexity": 23,
        "cognitiveComplexity": 31,
        "maintainabilityIndex": 42,
        "nestingDepth": 6,
        "linesOfCode": 147,
        "logicalLines": 128,
        "commentLines": 12
      },
      "rating": "critical",
      "refactoring": {
        "priority": "high",
        "suggestions": [
          "Extract nested logic to helper methods (reduce nesting)",
          "Replace switch/case with Strategy pattern (reduce complexity)",
          "Apply guard clauses for early returns (improve readability)",
          "Split into smaller functions (<50 lines each)"
        ],
        "estimatedComplexityAfter": 8,
        "effortEstimate": "high",
        "benefits": [
          "74% complexity reduction (23 → 8)",
          "Improved maintainability (42 → 75)",
          "Better testability"
        ]
      }
    },
    ...
  ]
}

**VALIDATION CRITERIA**:
- ✅ Complexity calculated for all functions
- ✅ Metrics accurate and meaningful
- ✅ Refactoring priorities justified
- ✅ Improvement estimates realistic

**EVIDENCE REQUIRED**:
- Complexity heatmap (high to low)
- Refactoring priority list
- Before/after estimates

**ROBUSTNESS REQUIREMENTS** (SYNRG v3.0):
- If complexity calculation fails: Use approximations, document method
- If metrics inconsistent: Validate against multiple methods
- If function too complex to analyze: Break into sections
- Comprehensive error analysis on failures

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~30K tokens maximum

Execute with quantitative precision.`
})
```

**CRITICAL EXECUTION NOTE**:
You MUST invoke all 6 Task agents **in a single message** using parallel Task tool calls. Do NOT invoke them sequentially. Example:

```
I'm now spawning 6 parallel discovery agents:
[Invoke all 6 Task calls here in one message]
```

**After All 6 Agents Complete**:
1. Collect all 6 outputs
2. Validate each output against its success criteria
3. If any agent failed: Perform mandatory error analysis (5-Why, impact assessment, cascade risk)
4. Synthesize into Phase 1 Discovery Report
5. Store results for Phase 1.5 (Refactoring Orchestrator)

---

## PHASE 1.5: REFACTORING OPPORTUNITY SYNTHESIS

**Objective**: Synthesize all code quality findings into integrated refactoring roadmap

**Execute 1 Task agent** to orchestrate refactoring strategy:

```javascript
Task({
  subagent_type: "general-purpose",
  description: "Synthesize refactoring roadmap",
  prompt: `You are Agent 1.5-RefactoringOrchestrator for SYNRG-REFACTOR v3.0.

**CONTEXT**:
- User Objective: ${executionConfig.objective}
- Quality Level: ${executionConfig.qualityLevel}

**INPUT** (from Phase 1 agents):
- Code Smell Report (Agent 1E)
- Complexity Analysis (Agent 1F)
- Dependency Coupling (Agent 1B)
- Anti-Patterns (Agent 1D)

**TASK**: Prioritize refactoring opportunities integrated with file restructuring

**DELIVERABLE**: Prioritized refactoring roadmap by phase (JSON format)

**ACTIONS**:

1. **IDENTIFY REFACTORING PATTERNS**:

   **Extraction Refactorings**:
   - Extract Method: Break long methods (>50 lines)
   - Extract Class: Split large classes (>300 lines)
   - Extract Interface: Define abstractions for DIP
   - Extract Variable: Clarify complex expressions
   - Extract Constant: Replace magic numbers

   **Simplification Refactorings**:
   - Guard Clauses: Replace nested conditionals
   - Consolidate Conditional: Simplify complex conditions
   - Replace Conditional with Polymorphism: Strategy pattern
   - Decompose Conditional: Extract condition logic

   **Moving Refactorings**:
   - Move Method: Relocate to appropriate class
   - Move Field: Relocate closer to usage
   - Inline Method/Class: Remove unnecessary abstraction

2. **APPLY SOLID PRINCIPLES**:

   **Single Responsibility (SRP)**:
   - Identify classes doing multiple things
   - Suggest splits along responsibility boundaries
   - Example: UserService → UserAuthService + UserProfileService

   **Open/Closed (OCP)**:
   - Find switch/case or if/else on types
   - Suggest Strategy or Template Method
   - Example: PaymentProcessor → IPaymentStrategy

   **Liskov Substitution (LSP)**:
   - Check inheritance hierarchies
   - Suggest composition over inheritance where violated

   **Interface Segregation (ISP)**:
   - Find large interfaces (>10 methods)
   - Split into focused interfaces

   **Dependency Inversion (DIP)**:
   - Find concrete dependencies
   - Suggest interface extraction + DI

3. **IDENTIFY DESIGN PATTERN OPPORTUNITIES**:

   **Creational**: Factory, Builder, Singleton (sparingly)
   **Structural**: Adapter, Decorator, Facade
   **Behavioral**: Strategy, Observer, Command, Template Method, State

4. **PRIORITIZE REFACTORINGS**:

   Priority = (Impact × 2 + Urgency) / (Effort + Risk)

   **Urgency factors**:
   - Blocks restructuring: +10
   - High complexity (>15): +5
   - Violates SOLID: +3
   - Duplicated code: +2
   - Code smell count: +1 per smell

**OUTPUT FORMAT** (JSON):
{
  "summary": {
    "totalRefactorings": number,
    "byPhase": { "preMove": count, "duringMove": count, "afterMove": count },
    "byType": { "extract": count, "simplify": count, "pattern": count },
    "estimatedEffort": "medium/high/low",
    "complexityReduction": "percentage estimate"
  },
  "refactoringRoadmap": {
    "preMove": [
      {
        "file": "src/services/UserService.ts",
        "action": "Extract Class (3-way split)",
        "reason": "Violates SRP, blocks domain structure",
        "split": [
          "features/auth/services/auth-service.ts",
          "features/user-profile/services/profile-service.ts",
          "features/preferences/services/preferences-service.ts"
        ],
        "priority": "critical",
        "effort": "medium",
        "risk": "low",
        "solidPrinciple": "Single Responsibility",
        "benefits": [
          "Clear domain boundaries",
          "Reduced complexity (156 → avg 52)",
          "Independent testing",
          "Better AI navigation"
        ],
        "blocksRestructure": true
      }
    ],
    "duringMove": [
      {
        "file": "src/utils/helpers.ts",
        "action": "Split by domain + Extract Constants",
        "reason": "Low cohesion (LCOM 0.87), magic numbers",
        "newFiles": [
          "utils/string/formatters.ts",
          "utils/date/calculators.ts",
          "utils/math/operations.ts",
          "utils/constants.ts"
        ],
        "priority": "high",
        "effort": "low",
        "risk": "low",
        "opportunistic": true
      }
    ],
    "afterMove": [
      {
        "file": "src/components/Dashboard.tsx",
        "action": "Extract Custom Hooks",
        "reason": "Complex useEffect (cognitive complexity: 18)",
        "newHooks": [
          "hooks/useDashboardData.ts",
          "hooks/useDashboardFilters.ts"
        ],
        "priority": "medium",
        "effort": "medium",
        "risk": "low"
      }
    ],
    "patterns": [
      {
        "location": "src/lib/payment-processor.ts",
        "pattern": "Strategy Pattern",
        "currentIssue": "Switch statement on payment type (OCP violation)",
        "implementation": {
          "steps": [
            "Create IPaymentStrategy interface",
            "Implement CreditCardStrategy, PayPalStrategy, CryptoStrategy",
            "Use PaymentStrategyFactory for instantiation"
          ]
        },
        "priority": "high",
        "effort": "high",
        "solidPrinciple": "Open/Closed",
        "benefits": [
          "Easy to add new payment methods",
          "65% complexity reduction",
          "Better separation of concerns"
        ]
      }
    ]
  }
}

**VALIDATION CRITERIA**:
- ✅ Roadmap prioritized and validated
- ✅ All refactorings mapped to SOLID principles
- ✅ Effort/benefit analysis realistic
- ✅ Dependencies between refactorings identified

**EVIDENCE REQUIRED**:
- Complete refactoring plan
- ROI analysis (effort vs. benefit)
- Integration strategy with file moves

**ROBUSTNESS REQUIREMENTS** (SYNRG v3.0):
- If conflicting refactorings: Prioritize by impact
- If effort estimates uncertain: Provide ranges
- If risk high: Flag for user approval
- Comprehensive error analysis on failures

**TIME BUDGET**: Take as long as needed for thorough strategy
**CONTEXT BUDGET**: ~50K tokens maximum

Execute with strategic precision.`
})
```

**After Agent 1.5 Completes**:
1. Validate refactoring roadmap
2. Store for Phase 3 (Architecture Strategy)
3. Prepare for Phase 2 (Risk Analysis)

---

## PHASE 2: RISK ANALYSIS

**Objective**: Identify ALL integrity risks AND technical debt

**Execute 8 parallel Task agents** simultaneously for comprehensive risk assessment:

```javascript
// AGENT 2A: AutoGenDetector
Task({
  subagent_type: "general-purpose",
  description: "Identify auto-generated files",
  prompt: `You are Agent 2A-AutoGenDetector for SYNRG-REFACTOR v3.0.

**TASK**: Identify auto-generated files and document regeneration commands

**DELIVERABLE**: Auto-gen file list with regeneration commands (JSON format)

**ACTIONS**:
1. Use Grep tool to scan for markers:
   - "@generated" (common marker)
   - "DO NOT EDIT" (warning)
   - "This file is auto-generated" (explicit)
   - "Code generated by" (tool-specific)
2. Check filename patterns:
   - *.generated.ts/js/py
   - *.g.ts (GraphQL codegen)
   - database.ts (Supabase pattern)
   - schema.ts (common pattern)
   - Files in /generated/, /__generated__/
3. Find generation scripts:
   - package.json scripts (generate:*, gen:*)
   - Makefile targets
   - .sh scripts
   - codegen.yml, graphql.config.js
4. Document regeneration commands

**OUTPUT FORMAT** (JSON):
{
  "summary": {
    "totalAutoGenerated": number,
    "withRegenCommands": number,
    "missingCommands": number
  },
  "autoGenerated": [
    {
      "path": "src/types/database.ts",
      "marker": "@generated by Supabase CLI",
      "generationTool": "Supabase",
      "regenerateCmd": "supabase gen types typescript > src/types/database.ts",
      "moveStrategy": "regenerate_after_move",
      "risk": "high (manual edit = type cascades)"
    },
    ...
  ],
  "missingRegenCommands": [
    "src/graphql/schema.generated.ts"
  ]
}

**VALIDATION CRITERIA**:
- ✅ All generation scripts documented
- ✅ Regeneration commands tested (if possible)
- ✅ Move strategies defined

**EVIDENCE REQUIRED**:
- Auto-gen file list
- Regeneration commands
- Testing proof (if commands run)

**ROBUSTNESS REQUIREMENTS** (SYNRG v3.0):
- If regen command unclear: Document best guess + escalate
- If marker ambiguous: Use multiple detection methods
- Comprehensive error analysis on failures

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~25K tokens maximum`
})

// AGENT 2B: CriticalPathAnalyzer
Task({
  subagent_type: "general-purpose",
  description: "Flag files in critical paths",
  prompt: `You are Agent 2B-CriticalPathAnalyzer for SYNRG-REFACTOR v3.0.

**INPUT**: Critical execution paths from Agent 1C (CodeFlowTracer)

**TASK**: Flag files in critical execution paths with move strategies

**DELIVERABLE**: Criticality ratings for all files (JSON format)

**ACTIONS**:
1. Cross-reference with CodeFlowTracer output
2. Rate each file:
   - Low: Leaf components, utility functions (safe to move anytime)
   - Medium: Services, hooks (move with validation)
   - High: Core APIs, shared services (move with comprehensive testing)
   - Critical: Entry points, auth gateway (move last with full validation + user approval)
3. Consider factors:
   - Auth-related: Always critical
   - Payment-related: Always critical
   - Core APIs: High to critical
   - Entry points: Critical
4. Define move strategies per criticality level

**OUTPUT FORMAT** (JSON):
{
  "criticality": {
    "src/lib/auth-service.ts": {
      "rating": "critical",
      "reason": "Auth gateway - all protected routes depend on this",
      "dependents": 47,
      "moveStrategy": "move_last_with_full_validation",
      "approvalRequired": true,
      "testingRequired": ["unit", "integration", "e2e", "manual"]
    },
    ...
  },
  "byRating": {
    "critical": 3,
    "high": 12,
    "medium": 45,
    "low": 120
  }
}

**VALIDATION CRITERIA**:
- ✅ All critical paths identified
- ✅ Ratings justified
- ✅ Move strategies defined

**EVIDENCE REQUIRED**:
- Criticality matrix
- Move strategies per file

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~30K tokens maximum`
})

// AGENT 2C: CircularDependencyChecker
Task({
  subagent_type: "general-purpose",
  description: "Find circular dependencies",
  prompt: `You are Agent 2C-CircularDependencyChecker for SYNRG-REFACTOR v3.0.

**INPUT**: Dependency graph from Agent 1B (DependencyMapper)

**TASK**: Find and document circular dependency chains with break strategies

**DELIVERABLE**: Cycles with break strategies (JSON format)

**ACTIONS**:
1. Analyze dependency graph for cycles
2. For each cycle:
   - Document the cycle path (A → B → C → A)
   - Assess severity (length of cycle, criticality of files)
   - Identify weakest link (easiest import to break)
3. Suggest break strategies:
   - Extract shared types to separate file
   - Use dependency injection
   - Refactor to remove circular reference
   - Introduce event-driven architecture

**OUTPUT FORMAT** (JSON):
{
  "summary": {
    "totalCycles": number,
    "criticalCycles": number,
    "avgCycleLength": number
  },
  "circularDeps": [
    {
      "cycle": ["src/utils/api.ts", "src/lib/user.ts", "src/types/api.ts", "src/utils/api.ts"],
      "severity": "medium",
      "cycleLength": 3,
      "breakStrategy": {
        "action": "Extract shared types",
        "newFile": "src/types/shared-api-types.ts",
        "steps": [
          "Create src/types/shared-api-types.ts",
          "Move User type from lib/user.ts to shared-api-types.ts",
          "Update imports in api.ts and user.ts"
        ]
      },
      "blocksRestructure": true,
      "priority": "high"
    }
  ]
}

**VALIDATION CRITERIA**:
- ✅ All cycles detected and documented
- ✅ Break strategies actionable
- ✅ Priorities justified

**EVIDENCE REQUIRED**:
- Cycle list with paths
- Break strategies

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~25K tokens maximum`
})

// AGENT 2D: TypeSafetyValidator
Task({
  subagent_type: "general-purpose",
  description: "Analyze type dependencies",
  prompt: `You are Agent 2D-TypeSafetyValidator for SYNRG-REFACTOR v3.0.

**TASK**: Analyze type dependencies and cascade risks

**DELIVERABLE**: Type dependency map with cascade ratings (JSON format)

**ACTIONS**:
1. Identify type definition files:
   - *.types.ts, types.ts
   - interface definitions
   - type aliases
2. Map type consumers (who imports these types)
3. Calculate cascade risk:
   - Low: <5 consumers
   - Medium: 5-10 consumers
   - High: >10 consumers
4. Identify shared types across domains (problematic)
5. Suggest mitigation strategies:
   - Create barrel exports (index.ts)
   - Extract to shared/types
   - Use type re-exports

**OUTPUT FORMAT** (JSON):
{
  "typeDeps": {
    "src/types/user.ts": {
      "consumers": 34,
      "cascadeRisk": "high",
      "consumingDomains": ["auth", "profile", "admin", "api"],
      "moveStrategy": "create_barrel_export_first",
      "mitigation": {
        "action": "Add src/types/index.ts re-export",
        "steps": [
          "Create src/types/index.ts",
          "Re-export all types",
          "Update imports to use barrel export"
        ]
      }
    }
  }
}

**VALIDATION CRITERIA**:
- ✅ All type dependencies mapped
- ✅ Cascade risks assessed
- ✅ Mitigation strategies provided

**EVIDENCE REQUIRED**:
- Type dependency graph
- Cascade risk ratings

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~30K tokens maximum`
})

// AGENT 2E: ExternalIntegrationScanner
Task({
  subagent_type: "general-purpose",
  description: "Scan external integrations",
  prompt: `You are Agent 2E-ExternalIntegrationScanner for SYNRG-REFACTOR v3.0.

**TASK**: Identify external dependencies and integration points

**DELIVERABLE**: External dependency report (JSON format)

**ACTIONS**:
1. Find files importing from node_modules:
   - Use Grep for "from \"" or "require(\"" (no ./ or ../)
2. Identify integration types:
   - API clients (axios, fetch wrappers)
   - Database connections (prisma, mongoose, supabase)
   - SDKs (Stripe, Auth0, AWS)
   - UI libraries (MUI, Ant Design)
3. Check environment variable dependencies:
   - Use Grep for process.env.*, import.meta.env.*
4. Find config file references:
   - vite.config.ts, next.config.js, etc.

**OUTPUT FORMAT** (JSON):
{
  "externalDeps": {
    "src/lib/supabase-client.ts": {
      "externalImports": ["@supabase/supabase-js"],
      "envVars": ["SUPABASE_URL", "SUPABASE_ANON_KEY"],
      "configReferences": ["vite.config.ts"],
      "moveStrategy": "update_config_after_move",
      "risk": "medium"
    }
  }
}

**VALIDATION CRITERIA**:
- ✅ All external deps documented
- ✅ Config references identified
- ✅ Move strategies defined

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~25K tokens maximum`
})

// AGENT 2F: TestCoverageMapper
Task({
  subagent_type: "general-purpose",
  description: "Map test files to source",
  prompt: `You are Agent 2F-TestCoverageMapper for SYNRG-REFACTOR v3.0.

**TASK**: Map test files to source files

**DELIVERABLE**: Test-to-source mapping with coverage (JSON format)

**ACTIONS**:
1. Find all test files:
   - *.test.ts/js/tsx/jsx/py
   - *.spec.ts/js/tsx/jsx/py
   - __tests__/* directories
2. Map to source files (same name pattern)
3. Identify orphaned tests (no source file)
4. Identify untested files (no test file)
5. Assess test quality (basic heuristics)

**OUTPUT FORMAT** (JSON):
{
  "testMapping": {
    "src/lib/user-service.test.ts": {
      "sourceFile": "src/lib/user-service.ts",
      "moveStrategy": "move_together",
      "coverage": "high",
      "testCount": 23
    }
  },
  "orphanedTests": [],
  "untestedFiles": ["src/utils/old-helper.ts"]
}

**VALIDATION CRITERIA**:
- ✅ All test files mapped
- ✅ Coverage assessed
- ✅ Move strategies defined

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~25K tokens maximum`
})

// AGENT 2G: TechnicalDebtAnalyzer
Task({
  subagent_type: "general-purpose",
  description: "Quantify technical debt",
  prompt: `You are Agent 2G-TechnicalDebtAnalyzer for SYNRG-REFACTOR v3.0.

**TASK**: Quantify technical debt and prioritize paydown

**DELIVERABLE**: Technical debt inventory with paydown strategy (JSON format)

**ACTIONS**:

**Identify technical debt categories**:

**CODE DEBT**:
- TODO/FIXME/HACK comments (use Grep)
- Deprecated API usage
- Commented-out code blocks
- Dead code (unused exports)
- Console.log/debug statements

**DESIGN DEBT**:
- SOLID principle violations (from Agent 1E)
- Missing abstractions (duplicated logic)
- Over-engineering (unnecessary abstractions)
- Hard-coded values (magic numbers/strings)

**TEST DEBT**:
- Missing tests (from Agent 2F)
- Skipped/disabled tests (test.skip, @Ignore)
- Flaky tests indicators
- Low assertion quality

**DOCUMENTATION DEBT**:
- Missing JSDoc/docstrings
- Outdated comments (referencing old code)
- Missing README files
- Undocumented APIs

**Calculate Technical Debt Ratio**:
TDR = (Remediation Cost / Development Cost) × 100
- Target: <5%
- Warning: 5-10%
- Critical: >10%

**OUTPUT FORMAT** (JSON):
{
  "summary": {
    "totalItems": 247,
    "estimatedDebtHours": 127,
    "technicalDebtRatio": 8.3,
    "categories": {
      "code": 142,
      "design": 68,
      "test": 23,
      "documentation": 14
    }
  },
  "critical": [
    {
      "item": "TODOs in auth-service.ts",
      "type": "code-debt",
      "count": 8,
      "severity": "high",
      "reason": "Critical auth logic with unresolved issues",
      "action": "Resolve before moving auth files",
      "effort": "medium"
    }
  ],
  "opportunistic": [
    {
      "item": "Missing tests in UserService",
      "type": "test-debt",
      "coverage": 23,
      "action": "Add tests when extracting classes",
      "effort": "high"
    }
  ]
}

**VALIDATION CRITERIA**:
- ✅ All debt cataloged
- ✅ Paydown plan prioritized
- ✅ Effort estimates realistic

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~30K tokens maximum`
})

// AGENT 2H: CohesionAnalyzer
Task({
  subagent_type: "general-purpose",
  description: "Measure module cohesion",
  prompt: `You are Agent 2H-CohesionAnalyzer for SYNRG-REFACTOR v3.0.

**TASK**: Measure module cohesion and suggest improvements

**DELIVERABLE**: Cohesion report with refactoring suggestions (JSON format)

**ACTIONS**:

**Calculate cohesion metrics**:

**LCOM (Lack of Cohesion of Methods)**:
- Low LCOM (0-0.5) = high cohesion (good)
- Medium LCOM (0.5-0.7) = moderate cohesion
- High LCOM (>0.7) = low cohesion (split class)

**Cohesion Types** (worst to best):
- Coincidental: Random grouping
- Logical: Similar operations
- Temporal: Done at same time
- Procedural: Operations in sequence
- Communicational: Operate on same data
- Sequential: Output → input chaining
- Functional: Single, well-defined task ✅ (best)

**Identify low-cohesion modules**:
- Classes where methods don't share fields
- Utility files with unrelated functions
- Modules mixing multiple concerns

**OUTPUT FORMAT** (JSON):
{
  "cohesion": {
    "src/utils/helpers.ts": {
      "cohesionType": "coincidental",
      "lcom": 0.87,
      "issues": [
        "Contains string, date, math, DOM utils",
        "No shared functionality",
        "15 functions, no common data"
      ],
      "refactoring": {
        "action": "Split into focused modules",
        "newModules": [
          "utils/string/formatters.ts",
          "utils/date/calculators.ts",
          "utils/math/operations.ts",
          "utils/dom/manipulators.ts"
        ],
        "cohesionAfter": "functional",
        "effort": "low",
        "priority": "high"
      }
    }
  }
}

**VALIDATION CRITERIA**:
- ✅ Cohesion measured for all modules
- ✅ Split recommendations justified
- ✅ Effort estimates realistic

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~30K tokens maximum`
})
```

**CRITICAL**: Invoke all 8 Task agents in parallel (single message).

**After All 8 Agents Complete**:
1. Collect all 8 outputs
2. Validate each output
3. If any failures: Perform mandatory error analysis
4. Synthesize into Phase 2 Risk Report
5. Proceed to Phase 3 (Strategy Generation)

---

## PHASE 3: STRATEGY GENERATION

**Objective**: Design optimal file structure WITH integrated refactoring

**Execute 1 Task agent** (ArchitectureStrategist):

```javascript
Task({
  subagent_type: "general-purpose",
  description: "Design architecture strategy",
  prompt: `You are Agent 3-ArchitectureStrategist for SYNRG-REFACTOR v3.0.

**CONTEXT**:
- User Objective: ${executionConfig.objective}
- Quality Level: ${executionConfig.qualityLevel}
- Risk Tolerance: ${executionConfig.riskTolerance}

**INPUT** (All previous phase outputs):
- Phase 1: Discovery (6 agent outputs)
- Phase 1.5: Refactoring Roadmap
- Phase 2: Risk Analysis (8 agent outputs)

**TASK**: Design ideal structure + integrated refactoring plan

**DELIVERABLE**: Complete restructuring + refactoring plan (JSON format)

**STRATEGY DESIGN PRINCIPLES**:
1. Domain-Driven Structure (group by business domain)
2. Colocation (related files together)
3. Clear Entry Points (barrel exports)
4. AI Context Optimization (easy navigation)
5. Separation of Concerns (no mixed responsibilities)
6. SOLID Compliance (all 5 principles)
7. High Cohesion, Low Coupling (measured and validated)

**EXAMPLE ENHANCED STRUCTURE**:
```
/src
  /features              # Domain-specific features
    /auth
      /services
        - auth-service.ts         (REFACTORED: split from UserService)
        - IAuthService.ts         (NEW: interface for DIP)
      /strategies                 (NEW: Strategy pattern)
        - IAuthStrategy.ts
        - PasswordStrategy.ts
        - OAuthStrategy.ts
      /components
        - LoginForm.tsx
      /hooks
        - useAuth.ts
      /types
        - auth.types.ts
      - index.ts                  (barrel export)
      - README.md

    /user-profile
      /services
        - profile-service.ts      (REFACTORED: extracted from UserService)
        - IProfileService.ts      (NEW: DIP)
      /components
      /hooks                      (NEW: extracted from components)
        - useProfile.ts
      - index.ts
      - README.md

  /lib                    # Shared libraries
    /api-client
      - api-client.ts             (REFACTORED: interface extracted)
      - IApiClient.ts             (NEW: DIP)
    /database
      - supabase-client.ts

  /components/ui          # Reusable UI components
    /button
    /input

  /utils                  # Pure functions (REFACTORED: split by domain)
    /string
      - formatters.ts
      - validators.ts
    /date
      - calculators.ts
    /constants              (NEW: extracted magic numbers)
      - api-constants.ts
      - ui-constants.ts

  /types                  # Shared types
    - index.ts            (barrel export)
```

**MOVE SEQUENCING WITH INTEGRATED REFACTORING**:

Design move batches that integrate refactoring:

**PHASE A: Pre-Move Refactorings** (Do First - Sequential)
- Batch A1: Break Circular Dependencies
  * Extract shared types
  * Validation: No cycles remain
- Batch A2: Extract Large Classes
  * UserService → 3 services
  * PaymentProcessor → Strategy pattern
  * Validation: Each class <300 lines, SRP compliant
- Batch A3: Extract Interfaces (DIP)
  * IAuthService, IApiClient, etc.
  * Validation: High-level depends on abstractions

**PHASE B: Low-Risk Moves + Opportunistic Refactoring** (8 parallel)
- Batch B1: Move UI Components
  * Move + Extract button variants to constants
  * Move + Extract validation to hooks
  * Validation: Type-check passes
- Batch B2: Split & Move Utilities
  * Split helpers.ts by domain
  * Extract magic numbers to constants
  * Rename vague names
  * Validation: Type-check passes

**PHASE C: Medium-Risk Moves + Method Extractions** (4 parallel)
- Batch C1: Move Services
  * Move + Extract guard clauses
  * Move + Apply Strategy pattern
  * Create barrel exports
  * Validation: Type-check + Build pass

**PHASE D: High-Risk Moves + Design Patterns** (Sequential)
- Batch D1: Move Core Services
  * Move + Apply Adapter pattern
  * Create interfaces
  * Update N dependents
  * Validation: Type-check + Build + Full tests

**PHASE E: Critical Moves** (Sequential + User Approval)
- Batch E1: Entry Points
  * Update imports
  * Extract route config
  * Validation: Full suite + Manual verification

**OUTPUT FORMAT** (JSON):
{
  "idealStructure": {
    "description": "Domain-driven with SOLID compliance",
    "tree": { ... },
    "principles": ["Domain-Driven", "Colocation", "SOLID", "High Cohesion"]
  },
  "movePlan": {
    "phaseA": {
      "name": "Pre-Move Refactorings",
      "batches": [ ... ],
      "parallel": false,
      "approvalRequired": false
    },
    "phaseB": {
      "name": "Low-Risk Moves",
      "batches": [ ... ],
      "parallel": true,
      "maxParallelAgents": 8
    },
    ...
  },
  "refactoringIntegration": {
    "totalRefactorings": number,
    "byPhase": { ... },
    "complexityReductionEstimate": "percentage"
  },
  "riskAssessment": {
    "totalFiles": number,
    "byRisk": { "low": count, "medium": count, "high": count, "critical": count },
    "highRiskFiles": [ ... ]
  }
}

**VALIDATION CRITERIA**:
- ✅ Complete plan with all phases
- ✅ Refactorings properly integrated
- ✅ Dependencies respected
- ✅ Risk mitigation strategies included

**EVIDENCE REQUIRED**:
- Complete move plan
- Refactoring roadmap
- Validation strategy per batch

**ROBUSTNESS REQUIREMENTS** (SYNRG v3.0):
- If plan too complex: Simplify without losing quality
- If refactorings conflict with moves: Resolve dependencies
- If risk assessment uncertain: Escalate for user input
- Comprehensive error analysis on failures

**TIME BUDGET**: Take as long as needed for comprehensive strategy
**CONTEXT BUDGET**: ~60K tokens maximum

Execute with architectural excellence.`
})
```

**After Agent 3 Completes**:
1. Validate architecture strategy
2. Prepare for Phase 3.5 (User Approval)

---

## PHASE 3.5: USER APPROVAL

**Present Integrated Plan to User**:

```markdown
# 📋 SYNRG-REFACTOR Integrated Plan

## Overview
- Files to move: {count}
- Files to refactor: {count}
- Classes to split: {count}
- Interfaces to extract: {count}
- Design patterns to apply: {count}
- Estimated complexity reduction: {percentage}%
- Estimated coupling reduction: {percentage}%

## Based on Your Quality Level: {executionConfig.qualityLevel}

### {If "Comprehensive" or "Balanced":}

#### Critical Refactorings (Will Execute)

1. **Extract Class: UserService → 3 Services**
   - Current: 458 lines, 23 methods, complexity 156
   - After: 3 services, avg 144 lines, avg 8 methods, complexity 38
   - Benefit: -75% complexity, SRP compliance, better testability
   - Effort: Medium (2-3 hours), Risk: Low

2. **Strategy Pattern: PaymentProcessor**
   - Current: Switch statement (OCP violation)
   - After: IPaymentStrategy + strategies
   - Benefit: Easy extension, -65% complexity
   - Effort: High (4-5 hours), Risk: Medium

### {If "Conservative" or "Minimal":}

#### Safe Refactorings (Will Execute)

1. **Extract Constants: {count} magic numbers**
   - Hard-coded values → named constants
   - Effort: Low (30 min), Risk: None

2. **Extract Methods: {count} long functions**
   - Functions >50 lines → smaller methods
   - Effort: Low, Risk: Low

### {If "Suggest":}

#### Suggested Refactorings (Your Approval Required)

[List with individual approval options]

## Move Plan Summary

### Phase A: Pre-Move Refactorings (Sequential)
- Duration: Estimated {hours} hours
- Risk: Low to Medium
- Files affected: {count}

### Phase B: Low-Risk Moves (8 Parallel Agents)
- Duration: Estimated {hours} hours
- Risk: Low
- Files to move: {count}

### Phase C: Medium-Risk Moves (4 Parallel Agents)
- Duration: Estimated {hours} hours
- Risk: Medium
- Files to move: {count}

### Phase D: High-Risk Moves (Sequential)
- Duration: Estimated {hours} hours
- Risk: High
- Files to move: {count}
- **Your approval required before execution**

### Phase E: Critical Moves (Sequential + Approval)
- Duration: Estimated {hours} hours
- Risk: Critical
- Files to move: {count}
- **Your approval required for each move**

## Validation Plan

After each batch:
✅ Type-check: {if enabled}
✅ Build: {if enabled}
✅ Tests: {if enabled}
✅ Quality metrics: {if enabled}

## Rollback Strategy

- Git checkpoint created: synrg-refactor-checkpoint-{timestamp}
- Rollback script: .synrg-rollback.sh
- Each batch can be individually reverted

## Estimated Total Time

- Total: {hours} hours
- Refactorings: {hours} hours
- Moves: {hours} hours
- Validation: {hours} hours

---

Ready to proceed?
```

**Use AskUserQuestion** to get approval:

```javascript
{
  question: "Proceed with this integrated restructuring + refactoring plan?",
  header: "Approval",
  multiSelect: false,
  options: [
    {
      label: "Approve entire plan",
      description: "Execute all phases as described"
    },
    {
      label: "Approve up to Phase C only",
      description: "Skip high-risk and critical moves for now"
    },
    {
      label: "Approve refactorings, defer moves",
      description: "Do refactorings first, review before moving files"
    },
    {
      label: "Let me approve each phase individually",
      description: "Stop after each phase for my approval"
    },
    {
      label: "Modify plan",
      description: "I want to change some aspects (will specify)"
    }
  ]
}
```

**Based on user response**:
- "Approve entire plan" → Proceed to Phase 5 (Execution)
- "Approve up to Phase C" → Execute Phases A, B, C only
- "Approve refactorings, defer moves" → Execute refactorings, then pause
- "Let me approve individually" → Pause after each phase
- "Modify plan" → Enter interactive modification mode

---

## PHASE 5: EXECUTION

**Objective**: Execute move plan with integrated refactoring

**CRITICAL**: This phase dynamically spawns Task agents based on the approved plan. Execution follows the batch structure from Phase 3.

### Execution Protocol

For each batch in the approved plan:

1. **Create Git Checkpoint**
2. **Execute Pre-Move Refactorings** (if applicable)
3. **Execute File Moves** (parallel or sequential based on batch config)
4. **Execute Post-Move Refactorings** (if applicable)
5. **Run Validation** (based on user config)
6. **If validation fails**: Rollback batch, perform error analysis, escalate

### Example Batch Execution

**BATCH B1: Low-Risk UI Component Moves (8 Parallel Agents)**

```bash
# 1. Checkpoint
git add -A
git commit -m "CHECKPOINT: Before Batch B1 (UI components)" || echo "Clean"
git tag synrg-batch-b1-pre
```

```javascript
// 2. Spawn 8 parallel Task agents for file moves
Task({
  subagent_type: "general-purpose",
  description: "Move Button component",
  prompt: `You are Batch-B1-Agent-1 for SYNRG-REFACTOR v3.0.

**TASK**: Move Button component with opportunistic refactoring

**FILES TO MOVE**:
- src/components/Button.tsx → src/components/ui/button/Button.tsx
- src/components/Button.module.css → src/components/ui/button/Button.module.css

**OPPORTUNISTIC REFACTORINGS**:
1. Extract button variants (primary, secondary, danger) to constants
2. Extract button sizes (sm, md, lg) to constants
3. Move constants to: src/utils/constants/ui-constants.ts

**ACTIONS**:
1. Read source files
2. Create target directories (if needed)
3. Execute refactorings (extract constants)
4. Move files to new locations
5. Update imports in Button.tsx
6. Update all files that import Button (use Grep to find)
7. Validate: No broken imports

**DELIVERABLE**: JSON report
{
  "filesMove": [...],
  "refactoringsApplied": [...],
  "importsUpdated": [...],
  "success": boolean,
  "evidence": "..."
}

**VALIDATION CRITERIA**:
- ✅ Files moved successfully
- ✅ All imports updated
- ✅ No broken references
- ✅ Constants extracted to correct location

**ROBUSTNESS REQUIREMENTS** (SYNRG v3.0):
- If file move fails: Perform 5-Why root cause analysis
- If import update fails: Assess cascade risk
- Comprehensive error analysis on any failure

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~20K tokens maximum`
})

// ... Invoke 7 more parallel Task agents for other UI components
```

```bash
# 3. After all 8 agents complete: Validate
npm run type-check || echo "Type errors detected"

# 4. If validation fails: Rollback
if [ $? -ne 0 ]; then
  git reset --hard synrg-batch-b1-pre
  echo "Batch B1 failed validation - rolled back"
  # Escalate to user with error analysis
fi

# 5. If validation succeeds: Commit batch
git add -A
git commit -m "refactor(batch-b1): Move UI components with refactoring

- Moved 8 UI components to components/ui/
- Extracted button variants and sizes to constants
- Updated 23 imports

✅ Type-check: Passed
✅ Complexity: Improved

Generated by: SYNRG-REFACTOR v3.0"
```

### Batch Types

**Sequential Batches** (High-Risk, Critical):
- Execute one Task agent at a time
- Validate after each move
- Pause for user approval if configured

**Parallel Batches** (Low-Risk, Medium-Risk):
- Execute multiple Task agents simultaneously
- Collect all results
- Validate once after all agents complete

### Error Handling

**If Any Agent Fails**:

1. **MANDATORY Error Analysis** (SYNRG v3.0):
   - 5-Why root cause analysis
   - Current impact assessment
   - Future impact prediction
   - Cascade risk analysis
   - Comprehensive error report

2. **Rollback Decision**:
   - If high cascade risk (>70%): Immediate rollback
   - If medium risk: Ask user (continue or rollback)
   - If low risk: Retry with alternative approach

3. **Escalation**:
   - Present error analysis to user
   - Suggest alternative approaches
   - Get user decision on how to proceed

---

## PHASE 6: VALIDATION

**Objective**: Comprehensively validate restructuring + refactoring results

**Execute 7 parallel Task agents** for comprehensive validation:

```javascript
// AGENT 6A: ImportValidator
Task({
  subagent_type: "general-purpose",
  description: "Validate all imports",
  prompt: `You are Agent 6A-ImportValidator for SYNRG-REFACTOR v3.0.

**TASK**: Validate all imports are correct and resolvable

**ACTIONS**:
1. Use Grep to find all import statements
2. Verify each import resolves to existing file
3. Check for broken imports (file not found)
4. Check for circular imports (after moves)
5. Verify barrel exports work correctly

**OUTPUT FORMAT** (JSON):
{
  "totalImports": number,
  "resolved": number,
  "broken": number,
  "brokenImports": [
    {
      "file": "...",
      "line": number,
      "import": "...",
      "issue": "..."
    }
  ],
  "success": boolean
}

**VALIDATION CRITERIA**:
- ✅ All imports resolved
- ✅ No broken imports
- ✅ No new circular dependencies

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~25K tokens maximum`
})

// AGENT 6B: TypeCheckValidator
Task({
  subagent_type: "general-purpose",
  description: "Run type checking",
  prompt: `You are Agent 6B-TypeCheckValidator for SYNRG-REFACTOR v3.0.

**TASK**: Run type checking and validate no type errors

**ACTIONS**:
1. Detect project type system:
   - TypeScript: Run tsc --noEmit
   - Python: Run mypy
   - Other: Appropriate type checker
2. Capture output
3. Categorize errors (if any):
   - Pre-existing (were there before)
   - New (introduced by refactoring)
   - Critical (block deployment)

**OUTPUT FORMAT** (JSON):
{
  "typeChecker": "tsc",
  "totalErrors": number,
  "newErrors": number,
  "preExistingErrors": number,
  "errors": [...],
  "success": boolean
}

**VALIDATION CRITERIA**:
- ✅ Zero new type errors
- ✅ Pre-existing errors unchanged or improved

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~25K tokens maximum`
})

// AGENT 6C: BuildValidator
Task({
  subagent_type: "general-purpose",
  description: "Run build process",
  prompt: `You are Agent 6C-BuildValidator for SYNRG-REFACTOR v3.0.

**TASK**: Validate project builds successfully

**ACTIONS**:
1. Detect build command:
   - package.json: npm run build / yarn build
   - Makefile: make build
   - Other: Appropriate build command
2. Run build process
3. Capture output and errors
4. Check for build artifacts

**OUTPUT FORMAT** (JSON):
{
  "buildCommand": "npm run build",
  "exitCode": number,
  "duration": "seconds",
  "output": "...",
  "success": boolean
}

**VALIDATION CRITERIA**:
- ✅ Build succeeds (exit code 0)
- ✅ No critical warnings
- ✅ Build artifacts created

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~25K tokens maximum`
})

// AGENT 6D: TestValidator
Task({
  subagent_type: "general-purpose",
  description: "Run test suite",
  prompt: `You are Agent 6D-TestValidator for SYNRG-REFACTOR v3.0.

**TASK**: Run test suite and validate all tests pass

**ACTIONS**:
1. Detect test command:
   - package.json: npm test / yarn test
   - pytest, cargo test, etc.
2. Run test suite
3. Capture results
4. Categorize failures (if any):
   - Pre-existing failures
   - New failures (introduced by refactoring)

**OUTPUT FORMAT** (JSON):
{
  "testCommand": "npm test",
  "totalTests": number,
  "passed": number,
  "failed": number,
  "skipped": number,
  "newFailures": number,
  "failures": [...],
  "success": boolean
}

**VALIDATION CRITERIA**:
- ✅ Zero new test failures
- ✅ Pre-existing failures unchanged

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~30K tokens maximum`
})

// AGENT 6E: GitValidator
Task({
  subagent_type: "general-purpose",
  description: "Validate git state",
  prompt: `You are Agent 6E-GitValidator for SYNRG-REFACTOR v3.0.

**TASK**: Validate git state is clean and trackable

**ACTIONS**:
1. Run git status
2. Check for untracked files
3. Check for uncommitted changes
4. Verify all moves were tracked by git (git mv vs manual move)

**OUTPUT FORMAT** (JSON):
{
  "status": "clean" | "dirty",
  "untrackedFiles": number,
  "modifiedFiles": number,
  "gitMoveTracked": boolean,
  "success": boolean
}

**VALIDATION CRITERIA**:
- ✅ Git status clean OR all changes committed
- ✅ Git move history preserved

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~20K tokens maximum`
})

// AGENT 6F: CodeQualityValidator
Task({
  subagent_type: "general-purpose",
  description: "Validate code quality improvements",
  prompt: `You are Agent 6F-CodeQualityValidator for SYNRG-REFACTOR v3.0.

**TASK**: Validate code quality improvements (before/after metrics)

**ACTIONS**:
1. Re-run complexity analysis (like Agent 1F)
2. Re-calculate coupling/cohesion (like Agents 1B, 2H)
3. Verify SOLID compliance improved
4. Check remaining code smells
5. Validate pattern implementations

**OUTPUT FORMAT** (JSON):
{
  "before": {
    "avgComplexity": number,
    "highComplexityFuncs": number,
    "avgCoupling": number,
    "codeSmells": number,
    "solidViolations": number
  },
  "after": {
    "avgComplexity": number,
    "highComplexityFuncs": number,
    "avgCoupling": number,
    "codeSmells": number,
    "solidViolations": number
  },
  "improvements": {
    "complexityReduction": "percentage",
    "couplingReduction": "percentage",
    "smellsEliminated": number,
    "solidGain": "percentage"
  },
  "success": boolean
}

**VALIDATION CRITERIA**:
- ✅ Complexity reduced (or maintained)
- ✅ Coupling reduced (or maintained)
- ✅ Code smells decreased
- ✅ SOLID compliance improved

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~30K tokens maximum`
})

// AGENT 6G: RefactoringValidator
Task({
  subagent_type: "general-purpose",
  description: "Validate refactorings applied",
  prompt: `You are Agent 6G-RefactoringValidator for SYNRG-REFACTOR v3.0.

**TASK**: Validate refactorings were applied correctly

**ACTIONS**:
1. Verify extracted classes exist with correct methods
2. Verify interfaces implemented correctly
3. Verify design patterns applied as specified
4. Check no behavioral changes (tests still pass)
5. Verify file splits resulted in smaller files

**OUTPUT FORMAT** (JSON):
{
  "refactoringValidation": {
    "completed": [
      {
        "refactoring": "Extract Class: UserService → 3",
        "status": "success",
        "newFiles": [...],
        "testsPass": boolean,
        "complexityBefore": number,
        "complexityAfter": number,
        "reduction": "percentage"
      }
    ],
    "incomplete": [],
    "failed": []
  },
  "success": boolean
}

**VALIDATION CRITERIA**:
- ✅ All planned refactorings completed
- ✅ Tests pass after refactorings
- ✅ Complexity improvements achieved

**TIME BUDGET**: Take as long as needed
**CONTEXT BUDGET**: ~25K tokens maximum`
})
```

**CRITICAL**: Invoke all 7 Task agents in parallel (single message).

**After All 7 Agents Complete**:
1. Collect all 7 validation reports
2. Synthesize into comprehensive validation report
3. If ANY validator fails:
   - Perform mandatory error analysis (SYNRG v3.0)
   - Assess cascade risk
   - Present options to user (rollback, fix, or proceed with issues)
4. If all validators pass:
   - Proceed to Phase 7 (Commit & Documentation)

---

## PHASE 7: COMMIT & DOCUMENTATION

**Objective**: Create comprehensive commit and documentation

### Step 1: Generate Comprehensive Commit Message

```bash
git add -A
git commit -m "$(cat <<'EOF'
refactor: SYNRG intelligent restructuring + code quality elevation

Restructured project for AI optimization with systematic quality improvements.

## File Structure Changes
- Files moved: {count}
- Folders created: {count}
- Import updates: {count}
- Barrel exports added: {count}

## Code Quality Improvements
- Complexity reduced: {percentage}% (avg {before} → {after})
- Coupling reduced: {percentage}%
- Code smells eliminated: {count} ({percentage}%)
- SOLID compliance: +{percentage}%
- High-complexity functions: {before} → {after}

## Refactorings Applied
- Classes extracted: {count}
- Interfaces created: {count}
- Design patterns: {list}
- Methods extracted: {count}
- Constants extracted: {count}

## SOLID Principles
✅ Single Responsibility: Split large classes
✅ Open/Closed: Applied Strategy pattern
✅ Liskov Substitution: Fixed inheritance hierarchies
✅ Interface Segregation: Created focused interfaces
✅ Dependency Inversion: Extracted interfaces

## Validation Results
✅ Type-check: Passed ({count} files)
✅ Build: Passed
✅ Tests: Passed ({passed}/{total})
✅ Quality: Significantly improved

## Structure Overview
{Brief description of new structure}

## Rollback
If needed:
- Script: bash .synrg-rollback.sh
- Manual: git reset --hard synrg-refactor-checkpoint-{timestamp}

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Generated by: SYNRG-REFACTOR v3.0
Complexity: -{complexityReduction}%
SOLID: +{solidImprovement}%
Coupling: -{couplingReduction}%
EOF
)"
```

### Step 2: Generate Rollback Script

```bash
cat > .synrg-rollback.sh <<'EOF'
#!/bin/bash
# SYNRG-REFACTOR Rollback Script
# Generated: {timestamp}

echo "⚠️  SYNRG-REFACTOR Rollback"
echo "This will revert all changes from the refactoring."
read -p "Are you sure? (yes/no): " confirm

if [ "$confirm" = "yes" ]; then
  echo "Rolling back to checkpoint: synrg-refactor-checkpoint-{timestamp}"
  git reset --hard synrg-refactor-checkpoint-{timestamp}
  echo "✅ Rollback complete"
else
  echo "Rollback cancelled"
fi
EOF

chmod +x .synrg-rollback.sh
```

### Step 3: Generate Documentation

**Create REFACTORING_SUMMARY.md**:

```markdown
# SYNRG-REFACTOR Summary

**Generated**: {timestamp}
**Version**: v3.0
**Objective**: {user objective}

## Overview

This codebase has been systematically restructured and refactored using SYNRG-REFACTOR v3.0, an AI-powered orchestrator that combines intelligent file organization with code quality elevation.

## Changes Made

### Structure Improvements

**Before**:
- {description of old structure}
- Files scattered across {count} locations
- No clear domain boundaries

**After**:
- Domain-driven structure with {count} feature domains
- Clear separation of concerns
- Improved AI navigation and context efficiency

### Code Quality Improvements

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Avg Complexity | {before} | {after} | -{percentage}% |
| High-Complexity Functions | {before} | {after} | -{percentage}% |
| Avg Coupling | {before} | {after} | -{percentage}% |
| Code Smells | {before} | {after} | -{percentage}% |
| SOLID Violations | {before} | {after} | -{percentage}% |

### Refactorings Applied

#### Classes Extracted
1. **UserService → 3 Services**
   - AuthService: {lines} lines, complexity {value}
   - ProfileService: {lines} lines, complexity {value}
   - PreferencesService: {lines} lines, complexity {value}
   - Benefit: -75% complexity, SRP compliance

#### Design Patterns Implemented
1. **Strategy Pattern: PaymentProcessor**
   - Replaced switch statement with IPaymentStrategy
   - Benefit: Easy extension, OCP compliance

#### Methods Extracted
- Total: {count} methods
- Avg method size: {before} → {after} lines
- Benefit: Improved readability

#### Constants Extracted
- Total: {count} constants
- Eliminated magic numbers: {count}
- Benefit: Improved maintainability

### SOLID Principles

✅ **Single Responsibility (SRP)**
- Split {count} large classes into focused services
- Each class now has one clear responsibility

✅ **Open/Closed (OCP)**
- Applied Strategy pattern for extensibility
- No more switch statements on types

✅ **Liskov Substitution (LSP)**
- Fixed inheritance hierarchies
- Favor composition over inheritance

✅ **Interface Segregation (ISP)**
- Created focused interfaces
- No more fat interfaces

✅ **Dependency Inversion (DIP)**
- High-level modules depend on abstractions
- {count} interfaces extracted

## New Structure

```
{Tree view of new structure}
```

## Validation

All validation checks passed:

- ✅ **Type-check**: 0 errors
- ✅ **Build**: Success
- ✅ **Tests**: {passed}/{total} passing
- ✅ **Quality Metrics**: Improved across all dimensions

## How to Navigate

### By Feature Domain
- **Auth**: `src/features/auth/`
- **User Profile**: `src/features/user-profile/`
- ...

### By Type
- **Components**: `src/components/ui/`
- **Utilities**: `src/utils/`
- **Types**: `src/types/`

### Barrel Exports
Each feature domain has an `index.ts` barrel export for clean imports:
```typescript
import { AuthService, useAuth } from '@/features/auth';
```

## Rollback

If you need to revert these changes:

```bash
# Quick rollback
bash .synrg-rollback.sh

# Manual rollback
git reset --hard synrg-refactor-checkpoint-{timestamp}
```

## Next Steps

**Recommended**:
1. Review high-priority TODOs in {files}
2. Add tests for newly extracted classes
3. Document public APIs in {services}
4. Consider further domain refinement in {areas}

**Optional**:
- Apply remaining refactoring opportunities (see REFACTORING_OPPORTUNITIES.md)
- Improve test coverage to >80%
- Add API documentation

---

🤖 Generated by SYNRG-REFACTOR v3.0
```

### Step 4: Present Final Report to User

```markdown
# ✅ SYNRG-REFACTOR COMPLETE

## Summary

Successfully restructured and refactored your codebase with production-grade quality.

### Achievements

📂 **Structure**
- Files moved: {count}
- Folders created: {count}
- Barrel exports: {count}

📈 **Quality**
- Complexity: -{percentage}%
- Coupling: -{percentage}%
- Code smells: -{percentage}%
- SOLID compliance: +{percentage}%

⚙️ **Refactorings**
- Classes extracted: {count}
- Interfaces created: {count}
- Design patterns: {count}
- Methods extracted: {count}

✅ **Validation**
- Type-check: Passed
- Build: Passed
- Tests: {passed}/{total} passing
- Quality: Significantly improved

### Time Investment

- Total: {hours} hours
- Discovery: {hours} hours
- Refactoring: {hours} hours
- Execution: {hours} hours
- Validation: {hours} hours

### Files Generated

- **.synrg-rollback.sh**: Rollback script
- **REFACTORING_SUMMARY.md**: Complete documentation
- **REFACTORING_OPPORTUNITIES.md**: Future improvement suggestions

### Git Checkpoint

Created checkpoint branch: `synrg-refactor-checkpoint-{timestamp}`

### Rollback

If needed: `bash .synrg-rollback.sh`

---

🎉 Your codebase is now:
- Intelligently organized for AI agents
- Compliant with SOLID principles
- Significantly lower complexity
- Production-ready with comprehensive validation

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

---

## 🔧 REFACTORING TECHNIQUES REFERENCE

**Quick reference for patterns used during refactoring:**

### Extract Method
```typescript
// Before: Long function (60 lines)
function processOrder(order) {
  // validation (10 lines)
  // calculation (20 lines)
  // discount (15 lines)
  // save (15 lines)
}

// After: Clear, testable methods
function processOrder(order) {
  validateOrder(order);
  const total = calculateTotal(order);
  const discount = calculateDiscount(total, order.customer);
  await saveOrder(order, total - discount);
}
```

### Extract Class (SRP)
```typescript
// Before: God class (458 lines)
class UserService {
  login() {}
  logout() {}
  getProfile() {}
  updateProfile() {}
  getPreferences() {}
}

// After: Focused classes
class AuthService { login() {} logout() {} }
class ProfileService { getProfile() {} updateProfile() {} }
class PreferencesService { getPreferences() {} }
```

### Strategy Pattern (OCP)
```typescript
// Before: Switch statement (OCP violation)
class PaymentProcessor {
  process(payment) {
    switch(payment.type) {
      case 'card': /* logic */
      case 'paypal': /* logic */
    }
  }
}

// After: Strategy pattern
interface IPaymentStrategy { process(payment) }
class CreditCardStrategy implements IPaymentStrategy {}
class PayPalStrategy implements IPaymentStrategy {}
class PaymentProcessor {
  constructor(private strategies: Map<string, IPaymentStrategy>) {}
  process(payment) {
    return this.strategies.get(payment.type).process(payment);
  }
}
```

### Guard Clauses
```typescript
// Before: Nested conditionals (5 levels)
function calculate(user) {
  if (user) {
    if (user.active) {
      if (user.premium) {
        if (user.purchases > 10) {
          return 0.20;
        } else { return 0.10; }
      } else { return 0.05; }
    }
  }
  return 0;
}

// After: Flat, readable
function calculate(user) {
  if (!user || !user.active) return 0;
  if (!user.premium) return 0.05;
  return user.purchases > 10 ? 0.20 : 0.10;
}
```

---

## 📋 SUCCESS CRITERIA

### Structural
- ✅ All files in logical locations
- ✅ Clear domain boundaries
- ✅ Consistent naming conventions
- ✅ Barrel exports created where appropriate
- ✅ READMEs generated for each feature domain

### Quality (Enhanced)
- ✅ Complexity reduced by target % (or maintained)
- ✅ SOLID compliance improved significantly
- ✅ Code smells eliminated or reduced
- ✅ Coupling reduced (lower afferent/efferent)
- ✅ Cohesion increased (lower LCOM)
- ✅ Design patterns applied correctly

### Validation
- ✅ Type-check passing (0 new errors)
- ✅ Build succeeding (exit code 0)
- ✅ All tests passing (0 new failures)
- ✅ Git clean or properly committed
- ✅ **Quality metrics improved or maintained**

### Documentation
- ✅ Comprehensive commit with changelog
- ✅ Rollback script generated and tested
- ✅ **Refactoring catalog (REFACTORING_SUMMARY.md)**
- ✅ **Before/after metrics documented**

---

## 📊 VERSION & EVOLUTION

**Version**: v3.0.0 (Robustness-First with True Orchestration)
**Created**: 2025-10-29
**Evolution Log**: `${CLAUDE_COMMANDS}/synrg-refactor.evolution.log`

### What's New in v3.0

**🚀 True Agent Orchestration**:
- ✅ All conceptual agents → actual Task tool invocations
- ✅ Parallel execution implemented (not just described)
- ✅ Director/Orchestrator pattern fully functional
- ✅ Dynamic agent spawning based on plan

**🎯 SYNRG v3.0 Robustness-First Integration**:
- ✅ Mandatory error analysis on all failures (5-Why, impact, cascade risk)
- ✅ Comprehensive quality gates (4-layer validation framework)
- ✅ Production-ready from start (no quick fixes)
- ✅ Take as long as needed for perfection
- ✅ No workarounds - implement properly

**📈 Enhanced Capabilities**:
- File restructuring (domain-driven)
- Code smell detection (20+ types)
- Complexity analysis (6 metrics)
- SOLID validation (all 5 principles)
- Design patterns (12+ patterns)
- Technical debt quantification
- Coupling/cohesion metrics
- **Integrated refactoring during moves**

**🔄 Execution Modes**:
- **Minimal**: File moves + rename issues
- **Conservative**: + Extract constants, simple methods
- **Balanced**: + Class splits, interfaces, guard clauses
- **Comprehensive**: + SOLID fixes, design patterns
- **Suggest**: Show opportunities, user approves each

### v2.0 → v3.0 Transformation

| Aspect | v2.0 | v3.0 |
|--------|------|------|
| **Agent Execution** | Conceptual (YAML descriptions) | Actual (Task tool invocations) |
| **Parallelization** | Described but not implemented | True parallel Task calls |
| **Orchestration** | Manual interpretation | Automated director/orchestrator |
| **Error Handling** | Basic rollback | Comprehensive RCA + impact analysis |
| **Quality Gates** | Checklist | 4-layer validation framework |
| **Philosophy** | Efficiency-focused | Robustness-first (SYNRG v3.0) |

---

## 🛡️ ROBUSTNESS GUARANTEES (SYNRG v3.0)

Every execution of SYNRG-REFACTOR v3.0 guarantees:

1. ✅ **Work perfectly** - No edge case failures
2. ✅ **Be fully tested** - Comprehensive validation
3. ✅ **Handle all errors** - Graceful degradation
4. ✅ **Be well documented** - Complete documentation
5. ✅ **Be secure** - No vulnerabilities introduced
6. ✅ **Perform optimally** - No regressions
7. ✅ **Be maintainable** - Clean, modular code
8. ✅ **Be production-ready** - Deploy with confidence

---

**Remember**: SYNRG-REFACTOR v3.0 is not just a file mover - it's a comprehensive code transformation system that elevates your codebase to senior developer standards while maintaining production-grade quality and robustness throughout the entire process.

Execute with confidence. Your codebase is in good hands.
