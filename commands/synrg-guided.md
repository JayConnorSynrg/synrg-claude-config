---
description: Execute SYNRG Guided Orchestrator - Interactive planning with autonomous execution and adaptive parallelization
argument-hint: [objective or task description]
---

# SYNRG Guided Orchestrator Command
## Interactive Planning + Autonomous Execution + Intelligent Adaptive Parallelization

You are executing the SYNRG Guided Orchestrator - combining interactive planning, VALUE-FIRST analysis, and intelligent adaptive parallelization for maximum efficiency without sacrificing quality.

**Core Philosophy**: "Plan interactively, execute autonomously, parallelize intelligently, validate comprehensively."

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
| `mcp__n8n-mcp__*` | `n8n-mcp-delegate` | `~/.claude/agents/n8n-mcp-delegate.md` |
| `mcp__n8n-workflows__*` | `github-mcp-delegate` | `~/.claude/agents/github-mcp-delegate.md` |

**Delegation Examples:**
```javascript
// n8n workflow operations
Task({ subagent_type: "n8n-mcp-delegate", prompt: "Get workflow {id}", model: "haiku" })

// GitHub repository operations
Task({ subagent_type: "github-mcp-delegate", prompt: "Search repos for {query}", model: "haiku" })
```

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

**Full Protocol**: See `~/.claude/skills/mandatory-context-delegation.md`

---

## 🔒 UNIVERSAL PRE-IMPLEMENTATION REVIEW (MANDATORY - USP v1.0)

**HARD STOP**: Complete ALL gates before ANY code modification.

### GATE 1: Anti-Memory Checkpoint (P1 + P6)
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⚠️ ANTI-MEMORY CHECKPOINT - DO NOT TRUST MEMORY                            │
│                                                                              │
│  □ READ actual files being modified (not from memory)                        │
│  □ VERIFY file locations with Glob                                           │
│  □ CHECK current state: read specific lines to change                        │
│  □ CONFIRM dependencies from package.json/requirements.txt                   │
│                                                                              │
│  NEVER assume, guess, or speculate without reading files first               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### GATE 2: GIT_STRATEGY_DECISION
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  □ git status / git branch --show-current                                    │
│  □ files <= 2 AND simple → DIRECT COMMIT                                     │
│  □ files 3-10 OR medium → FEATURE BRANCH                                     │
│  □ files > 10 OR complex → WORKTREE + rollback plan                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

### GATE 3: CERTAINTY_GATED_ATOMIC_CHANGE (P4)
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  "When uncertain, scope INWARD - never compensate with larger changes"       │
│                                                                              │
│  Certainty = (Evidence + Understanding + Isolation) / 3                      │
│  Level 1 (line): >=70% | Level 2 (func): >=80% | Level 3 (related): >=85%    │
│  Level 4 (multi-file): >=90% | Level 5 (arch): >=95% + USER                  │
│                                                                              │
│  IF certainty < threshold: STOP → DISSECT → GATHER → RE-EVALUATE             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### GATE 4: ENTERPRISE_SECURITY_GATE
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  □ SECRETS: No hardcoded API keys, tokens, passwords                         │
│  □ OWASP: No SQL injection, XSS, command injection vectors                   │
│  □ PRIVILEGE: No sudo/admin without approval                                 │
│  □ DEPS: No known vulnerable dependencies                                    │
│  PASS → Proceed | FAIL → Block and fix                                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

### GATE 5: User Verification (P2)
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Before major changes: Present summary → Get approval                        │
│  Trigger: >3 files OR critical paths OR uncertainty                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Full Protocol**: See `~/.claude/skills/universal-synrg-protocols.md`

---

## 🧠 CLAUDE TOOL SELECTION PROTOCOL (Reference: /synrg)

**BEFORE executing ANY task, select the optimal Claude tool type:**

| Tool Type | When to Use | Action |
|-----------|-------------|--------|
| **SUB-AGENTS** | Isolated context, parallel execution, >500 token responses | Task tool with agent type |
| **SLASH COMMANDS** | Multi-phase orchestration, command chaining | SlashCommand tool |
| **HOOKS** | Event-triggered automation (pre-commit, etc.) | Create in .claude/hooks/ |
| **SKILLS** | Reusable methodology across agents | Create in .claude/skills/ |
| **DIRECT TOOLS** | Simple one-shot operations (last resort) | Built-in tools |

**Tool Creation Gate**: If optimal tool doesn't exist AND task is recurring → CREATE the tool first.

**Ecosystem Proliferation**: After improvements → PROPAGATE to ALL /synrg-* commands.

**Full Protocol**: See `/synrg` command for complete Tool Type Decision Matrix, Task Analysis Protocol, and examples.

---

## 🔴 MANDATORY: Sub-Agent Delegation Protocol (v4.3)

**BEFORE any phase execution, CHECK for real Claude Code agents:**

```
┌─────────────────────────────────────────────────────────────┐
│  SUB-AGENT DELEGATION CHECK (MANDATORY)                     │
│                                                             │
│  1. IDENTIFY: Is this task delegatable to a focused agent?  │
│  2. MATCH: Check ~/.claude/agents/ for qualified agents     │
│  3. CREATE: If no match exists, create the agent first      │
│  4. DELEGATE: Use Task tool with specific agent type        │
└─────────────────────────────────────────────────────────────┘
```

### Real Delegation (Not Pseudocode)

```javascript
// Use Task tool for actual delegation
Task({
  subagent_type: "general-purpose",
  prompt: "[Task with full context and pattern library reference]",
  model: "haiku"  // haiku for focused tasks, sonnet for complex
})
```

### Available Agents

Check `~/.claude/agents/` for available agents. Key n8n agents:
- `n8n-node-validator`, `n8n-connection-fixer`, `n8n-version-researcher`
- `n8n-expression-debugger`, `n8n-pattern-retriever`, `n8n-workflow-expert`

**If no qualified agent exists**: Create it first, then delegate.

---

## 🎯 EXECUTION FLOW OVERVIEW

```
PHASE 0: Sub-Agent Delegation Check (NEW - v4.3)
         ↓
PHASE 1: Interactive Context Gathering
         ↓
PHASE 2: VALUE-FIRST Pre-Change Analysis
         ↓
PHASE 3: Interactive Planning with Parallelization Strategy
         ↓
PHASE 4: Parallelization Diagram Generation (MANDATORY)
         ↓
PHASE 5: Autonomous Adaptive Execution
         ↓
PHASE 6: Autonomous Error Recovery Loop (if needed)
         ↓
PHASE 7: Comprehensive Validation & Reporting
```

---

## PHASE 1: INTERACTIVE CONTEXT GATHERING

**Objective**: Understand user intent, constraints, and preferences before analysis.

Use the AskUserQuestion tool to gather:

### Required Questions:

1. **Scope & Constraints**:
   - "What are the must-have vs nice-to-have requirements?"
   - "Are there any parts of the codebase we should avoid modifying?"
   - "What's the acceptable timeline for this work?"

2. **Quality & Testing Preferences**:
   - "Should we validate with Playwright screenshots after each change?"
   - "What level of test coverage is required (unit/integration/e2e)?"
   - "Are there specific user flows that must remain functional?"

3. **Risk Tolerance**:
   - "How risk-averse should we be? (Maximum caution vs Balanced vs Move fast)"
   - "Should we auto-proceed on low-risk changes or escalate all decisions?"

4. **Technical Preferences**:
   - "Any specific patterns, libraries, or approaches you prefer?"
   - "Should we prioritize speed, reliability, or maintainability?"

**After gathering context, synthesize into execution parameters:**

```yaml
execution_context:
  objective: [User's primary goal]
  must_have_requirements: [Critical features]
  nice_to_have: [Optional enhancements]
  constraints: [Technical, timeline, budget]
  risk_tolerance: [HIGH_CAUTION | BALANCED | MOVE_FAST]
  auto_proceed_threshold: [0-100, higher = more autonomous]
  validation_requirements:
    screenshot_evidence: [YES/NO]
    test_coverage_target: [percentage]
    critical_flows: [list]
  technical_preferences:
    patterns: [preferred patterns]
    libraries: [preferred libraries]
    priority: [speed/reliability/maintainability]
```

---

## PHASE 2: VALUE-FIRST PRE-CHANGE ANALYSIS (MANDATORY)

**Trigger**: ALWAYS before planning ANY changes
**Purpose**: Understand what exists, quantify value, predict impact

### 2.1: Director/Orchestrator Architecture Reconnaissance

**MANDATORY**: Deploy Director pattern with 5 parallel sub-agents for comprehensive reconnaissance.

```javascript
async function orchestrateArchitectureMapping(objective, executionContext) {
  // Initialize Architecture Reconnaissance Director
  const director = initializeDirector('Architecture Reconnaissance Director');

  // Plan reconnaissance based on objective
  const reconPlan = await director.planReconnaissance({
    objective: objective,
    userContext: executionContext,
    requiredAnalysis: [
      'codebase_structure',
      'dependencies',
      'quality_metrics',
      'production_context',
      'affected_systems'
    ]
  });

  // Spawn 5 specialized sub-agents in parallel
  const reconAgents = [
    {
      id: 'codebase-analyzer',
      role: 'Codebase Structure Analysis',
      task: 'Map directory structure, patterns, conventions, complexity',
      tools: ['Glob', 'Grep', 'Read'],
      contextScope: 'Files and directories only',
      deliverable: {
        structure: 'Directory layout',
        patterns: 'Architectural patterns',
        conventions: 'Naming and style',
        complexity: 'Cyclomatic complexity metrics'
      }
    },
    {
      id: 'dependency-mapper',
      role: 'Dependency Graph Analysis',
      task: 'Map internal, external, shared dependencies',
      tools: ['Glob', 'Grep', 'Read'],
      contextScope: 'Import statements, package files',
      deliverable: {
        internal: 'Internal module dependencies',
        external: 'External package dependencies',
        shared: 'Shared resources and utilities',
        graph: 'Dependency graph structure'
      }
    },
    {
      id: 'quality-assessor',
      role: 'Code Quality Metrics',
      task: 'Assess testing, documentation, quality, performance, security',
      tools: ['Bash', 'Read', 'Grep'],
      contextScope: 'Test files, docs, configs, git history',
      deliverable: {
        testing: 'Test coverage and quality',
        documentation: 'Documentation completeness',
        codeQuality: 'Maintainability scores',
        performance: 'Performance benchmarks',
        security: 'Security audit status'
      }
    },
    {
      id: 'production-analyzer',
      role: 'Production Context Analysis',
      task: 'Analyze stability, usage, business impact',
      tools: ['Bash', 'Read', 'Grep'],
      contextScope: 'Logs, monitoring, git history, docs',
      deliverable: {
        stability: 'Uptime, incidents, error rates',
        usage: 'User metrics, critical paths',
        business: 'Revenue impact, compliance, SLA'
      }
    },
    {
      id: 'impact-identifier',
      role: 'Affected Systems Identification',
      task: 'Identify primary targets, secondary impacts, dependency chains',
      tools: ['Grep', 'Read', 'Glob'],
      contextScope: 'Related files and dependencies',
      deliverable: {
        primaryTargets: 'Direct targets',
        secondaryImpacts: 'Indirect systems affected',
        dependencyChain: 'Full dependency chain'
      }
    }
  ];

  // 🆕 MCP TOOL DELEGATION (v4.2)
  // If objective involves MCP tools, spawn specialized MCP delegation agents
  const mcpRequirements = detectMCPToolRequirements(objective);
  if (mcpRequirements.length > 0) {
    console.log(`🔌 MCP Delegation: Detected ${mcpRequirements.length} MCP tool requirements`);
    const mcpAgents = createMCPDelegationAgents(mcpRequirements);
    reconAgents.push(...mcpAgents);
  }

  // Execute sub-agents in parallel (60-70% context reduction)
  // MCP agents return distilled findings only (additional 70-90% reduction on MCP payloads)
  console.log(`🎯 Director: Spawning ${reconAgents.length} sub-agents for parallel reconnaissance...`);

  const agentResults = await Promise.all(
    reconAgents.map(agent => executeReconAgent(agent, reconPlan))
  );

  // Director consolidates findings
  const consolidated = await director.consolidateFindings({
    agentReports: agentResults,
    objective: objective,
    synthesisStrategy: 'comprehensive_merge'
  });

  // Validate completeness
  const validation = await director.validateCompleteness({
    findings: consolidated,
    requiredData: reconPlan.requiredAnalysis,
    confidenceThreshold: 0.85
  });

  // Gap filling if needed
  if (!validation.complete) {
    const additionalAgents = await director.createAdditionalAgents(validation.gaps);
    const additionalResults = await Promise.all(
      additionalAgents.map(agent => executeReconAgent(agent, reconPlan))
    );
    consolidated.merge(additionalResults);
  }

  return consolidated;
}
```

### 2.2: Value Quantification (0-100 Scores)

```javascript
function quantifyStructureValue(reconnaissance) {
  return {
    productionStability: calculate({
      uptime: reconnaissance.productionContext.stability.uptime,
      incidents: reconnaissance.productionContext.stability.incidents,
      errorRate: reconnaissance.productionContext.stability.errorRate,
      weight: 0.30  // 30% of total value
    }),

    businessLogicValue: calculate({
      criticalPath: reconnaissance.affectedSystems.isInCriticalUserFlow,
      revenueImpact: reconnaissance.affectedSystems.affectsRevenueFlow,
      compliance: reconnaissance.affectedSystems.hasComplianceRequirements,
      userImpact: reconnaissance.productionContext.usage.userPercentage,
      weight: 0.25  // 25% of total value
    }),

    integrationValue: calculate({
      inboundDependencies: reconnaissance.dependencies.consumers.length,
      outboundDependencies: reconnaissance.dependencies.dependencies.length,
      externalAPIs: reconnaissance.dependencies.externalIntegrations.length,
      couplingLevel: reconnaissance.dependencies.couplingScore,
      weight: 0.20  // 20% of total value
    }),

    codeQuality: calculate({
      testCoverage: reconnaissance.qualityMetrics.testing.coverage,
      documentation: reconnaissance.qualityMetrics.documentation.completeness,
      maintainability: reconnaissance.qualityMetrics.codeQuality.maintainability,
      complexity: reconnaissance.qualityMetrics.codeQuality.complexity,
      weight: 0.15  // 15% of total value
    }),

    teamKnowledgeValue: calculate({
      documentation: reconnaissance.qualityMetrics.documentation.completeness,
      ageInMonths: reconnaissance.codebase.ageInMonths,
      contributorCount: reconnaissance.codebase.uniqueContributors,
      busFactor: reconnaissance.codebase.busFactor,
      weight: 0.10  // 10% of total value
    }),

    totalValue: /* weighted sum of above */,
    category: /* HIGH (≥70) | MEDIUM (40-69) | LOW (<40) */
  };
}
```

**Value Score Interpretation**:
- **90-100**: Exceptional - preserve at almost all costs
- **70-89**: High - preserve unless compelling reason
- **40-69**: Medium - evaluate trade-offs carefully
- **20-39**: Low - restructuring may be beneficial
- **0-19**: Very Low - strong candidate for replacement

### 2.3: Change Impact Prediction

```javascript
async function predictChangeImpact(proposedChanges, valueScore) {
  return {
    technicalImpact: {
      filesAffected: estimateFileChanges(),
      linesChanged: estimateLineChanges(),
      testsRequiringUpdate: estimateTestChanges(),
      regressionRisk: calculateRegressionProbability()
    },

    productionImpact: {
      downtimeRequired: estimateDowntime(),
      rollbackComplexity: assessRollbackDifficulty(),
      userExperienceChange: predictUXImpact(),
      performanceDelta: predictPerformanceChange()
    },

    integrationImpact: {
      breakingChanges: identifyBreakingChanges(),
      dependentSystemsAffected: mapAffectedDependents(),
      apiContractChanges: detectAPIChanges(),
      dataSchemaChanges: detectSchemaChanges()
    },

    valueAtRisk: {
      stabilityRisk: (valueScore.productionStability / 100) * (regressionRisk / 100) * 100,
      integrationRisk: (valueScore.integrationValue / 100) * breakingChanges.length * 20,
      knowledgeRisk: (valueScore.teamKnowledgeValue / 100) * (deletedLines / totalLines) * 100,
      totalRiskScore: /* weighted sum */
    },

    expectedBenefits: {
      qualityImprovement: estimateQualityGain(),
      performanceGain: estimatePerformanceGain(),
      maintainabilityGain: estimateMaintainabilityGain(),
      featureEnablement: assessNewCapabilities(),
      totalBenefitScore: /* weighted sum */
    },

    netValueChange: expectedBenefits.total - valueAtRisk.total
  };
}
```

### 2.4: Protected Structure Detection

```javascript
const PROTECTED_STRUCTURES = {
  database: {
    priority: 'MAXIMUM',
    patterns: [/migrations?\//i, /schema\.(ts|js|sql)/i, /prisma\/schema/i],
    risks: ['Data loss', 'Production downtime', 'Cascade failures'],
    autoEscalate: true
  },
  apiContracts: {
    priority: 'HIGH',
    patterns: [/api.*routes?/i, /controllers?\//i, /.*\.api\.(ts|js)/i],
    risks: ['Breaking changes', 'Integration failures', 'SLA violations'],
    autoEscalate: true
  },
  authentication: {
    priority: 'MAXIMUM',
    patterns: [/auth/i, /jwt|session|oauth/i],
    risks: ['Security vulnerabilities', 'System lockout', 'Data exposure'],
    autoEscalate: true
  },
  productionConfig: {
    priority: 'HIGH',
    patterns: [/\.env\.production/i, /config.*production/i, /secrets|credentials/i],
    risks: ['Production outage', 'Secret exposure', 'Deployment failures'],
    autoEscalate: true
  }
};
```

### 🆕 2.4.5: MCP Tool Delegation Protocol (v4.2)

**When**: Objective involves MCP tools (n8n, GitHub, etc.)
**Why**: MCP tool calls return large payloads that consume context. Delegation to sub-agents optimizes context usage.

**MCP Tool Detection**:
```javascript
function detectMCPToolRequirements(objective) {
  const mcpPatterns = {
    'n8n-mcp': {
      keywords: ['n8n', 'workflow', 'node', 'template', 'execution', 'automation'],
      tools: [
        'mcp__n8n-mcp__search_nodes', 'mcp__n8n-mcp__get_node',
        'mcp__n8n-mcp__search_templates', 'mcp__n8n-mcp__get_template',
        'mcp__n8n-mcp__n8n_get_workflow', 'mcp__n8n-mcp__validate_workflow'
      ]
    },
    'n8n-workflows': {
      keywords: ['github', 'repository', 'pull request', 'issue', 'commit'],
      tools: [
        'mcp__n8n-workflows__search_repositories', 'mcp__n8n-workflows__get_file_contents',
        'mcp__n8n-workflows__list_pull_requests', 'mcp__n8n-workflows__get_pull_request'
      ]
    }
  };

  const required = [];
  for (const [name, config] of Object.entries(mcpPatterns)) {
    if (config.keywords.some(kw => objective.toLowerCase().includes(kw))) {
      required.push({ mcpName: name, tools: config.tools });
    }
  }
  return required;
}
```

**MCP Delegation Agent Factory**:
```javascript
function createMCPDelegationAgents(mcpRequirements) {
  return mcpRequirements.map(req => ({
    id: `${req.mcpName}-delegate`,
    role: `${req.mcpName} MCP Tool Analysis`,
    task: 'Execute MCP tool calls and distill vital information only',
    tools: [...req.tools, 'Read'],
    contextScope: 'MCP tool responses only',
    delegationProtocol: {
      returnFormat: {
        summary: '2-3 sentence summary',
        vitalData: 'Key extracted data points',
        recommendations: 'Specific suggestions',
        warnings: 'Issues or anti-patterns',
        references: 'IDs/paths for follow-up'
      },
      excludeFromReturn: [
        'Full JSON payloads', 'Raw API responses',
        'Complete node definitions', 'Execution logs'
      ]
    },
    deliverable: {
      summary: 'Brief findings summary',
      vitalData: 'Extracted key information',
      recommendations: 'Best practices to follow',
      warnings: 'Validation issues detected',
      references: 'IDs for on-demand retrieval'
    }
  }));
}
```

**MCP Delegation Execution**:
```javascript
async function executeMCPDelegationAgent(agent, plan) {
  console.log(`🔌 MCP Delegation: ${agent.role}`);

  // Execute in isolated context
  const rawFindings = await agent.execute(createIsolatedContext({
    tools: agent.tools,
    scope: agent.contextScope,
    objective: plan.objective
  }));

  // DISTILLATION: Return only vital info (70-90% context reduction)
  return {
    agentId: agent.id,
    findings: distillMCPFindings(rawFindings, agent.delegationProtocol),
    contextSaved: rawFindings.rawSize - distilledFindings.size
  };
}
```

**Context Efficiency**:
- **Raw MCP Response**: ~10,000-50,000 tokens (full JSON payloads)
- **Distilled Findings**: ~500-2,000 tokens (vital information only)
- **Context Reduction**: 70-96% per MCP tool call
- **Director Receives**: Actionable summaries, not raw data

### 2.5: Intelligent Decision Framework

```javascript
function decidePreserveVsRestructure(valueScore, impactPrediction, protectedDetection, executionContext) {
  const decision = {
    recommendation: null,
    confidence: null,
    reasoning: [],
    escalateToUser: false,
    alternativeApproaches: []
  };

  // Rule 1: Protected Structures → ALWAYS PRESERVE & ESCALATE
  if (protectedDetection.hasProtectedStructures) {
    decision.recommendation = 'PRESERVE_WITH_SAFEGUARDS';
    decision.escalateToUser = true;
    return decision;
  }

  // Rule 2: High Value + High Risk → PRESERVE & ENHANCE
  if (valueScore.totalValue >= 70 && impactPrediction.valueAtRisk.totalRiskScore >= 50) {
    decision.recommendation = 'PRESERVE_AND_ENHANCE';
    decision.escalateToUser = (executionContext.risk_tolerance === 'HIGH_CAUTION');
    return decision;
  }

  // Rule 3: Low Value + High Benefit → RESTRUCTURE (auto-proceed if context allows)
  if (valueScore.totalValue < 40 && impactPrediction.expectedBenefits.totalBenefitScore >= 60) {
    decision.recommendation = 'COMPREHENSIVE_RESTRUCTURE';
    decision.escalateToUser = (executionContext.auto_proceed_threshold < 70);
    return decision;
  }

  // Rule 4: Medium Value → ADAPTIVE (escalate based on context)
  if (valueScore.totalValue >= 40 && valueScore.totalValue < 70) {
    decision.recommendation = 'ADAPTIVE_ENHANCEMENT';
    decision.escalateToUser = (executionContext.auto_proceed_threshold < 50);
    return decision;
  }

  // Rule 5: Negative Net Value → DO NOT PROCEED
  if (impactPrediction.netValueChange < 0) {
    decision.recommendation = 'DO_NOT_PROCEED';
    decision.escalateToUser = true;
    return decision;
  }

  // Default: Proceed with validation
  decision.recommendation = 'PROCEED_WITH_VALIDATION';
  decision.escalateToUser = false;
  return decision;
}
```

**Output from Phase 2**:

```markdown
## VALUE-FIRST ANALYSIS COMPLETE

**Existing Structure Value**: [score]/100 ([HIGH/MEDIUM/LOW])

**Value Breakdown**:
- Production Stability: [score]/100
- Business Logic Value: [score]/100
- Integration Value: [score]/100
- Code Quality: [score]/100
- Team Knowledge: [score]/100

**Change Impact Prediction**:
- Risk Score: [score]/100
- Benefit Score: [score]/100
- Net Value Change: [+/-][value]

**Protected Structures**: [YES/NO] - [List if detected]

**RECOMMENDATION**: [PRESERVE_WITH_SAFEGUARDS | PRESERVE_AND_ENHANCE | ADAPTIVE_ENHANCEMENT | COMPREHENSIVE_RESTRUCTURE | DO_NOT_PROCEED]

**Auto-Proceed**: [YES/NO based on user's auto_proceed_threshold]
```

---

## PHASE 3: INTERACTIVE PLANNING WITH PARALLELIZATION STRATEGY

**Objective**: Create detailed execution plan with intelligent parallelization strategy.

### 3.1: Task Decomposition & Dependency Analysis

```javascript
async function decomposeTasksWithDependencies(objective, valueAnalysis, executionContext) {
  // Break objective into atomic tasks
  const atomicTasks = await decomposeIntoAtomicTasks(objective);

  // Analyze dependencies between tasks
  const dependencyGraph = await buildDependencyGraph(atomicTasks);

  // Classify tasks by parallelizability
  const taskClassification = atomicTasks.map(task => ({
    task: task,
    type: classifyTask(task, valueAnalysis),
    parallelSafe: isParallelSafe(task, dependencyGraph, valueAnalysis),
    criticalPath: isOnCriticalPath(task, dependencyGraph),
    riskLevel: assessTaskRisk(task, valueAnalysis),
    estimatedDuration: estimateTaskDuration(task),
    requiredValidation: determineValidationRequirements(task, executionContext)
  }));

  return {
    tasks: taskClassification,
    dependencyGraph: dependencyGraph,
    criticalPathTasks: taskClassification.filter(t => t.criticalPath),
    parallelizableTasks: taskClassification.filter(t => t.parallelSafe),
    sequentialTasks: taskClassification.filter(t => !t.parallelSafe)
  };
}

function classifyTask(task, valueAnalysis) {
  // Classify based on VALUE-FIRST analysis
  if (task.affectsProtectedStructures) return 'PROTECTED_STRUCTURE_MODIFICATION';
  if (task.affectsHighValueComponents && valueAnalysis.totalValue >= 70) return 'HIGH_VALUE_ENHANCEMENT';
  if (task.requiresArchitecturalChange) return 'ARCHITECTURAL_CHANGE';
  if (task.hasBreakingChanges) return 'BREAKING_CHANGE';
  return 'STANDARD_IMPLEMENTATION';
}

function isParallelSafe(task, dependencyGraph, valueAnalysis) {
  // Parallel safety criteria
  const hasNoDependencies = dependencyGraph.incomingEdges(task.id).length === 0;
  const lowRisk = task.riskLevel < 40;
  const noSharedStateModification = !task.modifiesSharedState;
  const notProtectedStructure = !task.affectsProtectedStructures;

  return hasNoDependencies && (lowRisk || noSharedStateModification) && notProtectedStructure;
}
```

### 3.2: Intelligent Parallelization Strategy

```javascript
function createParallelizationStrategy(taskAnalysis, executionContext) {
  const strategy = {
    executionMode: determineExecutionMode(taskAnalysis, executionContext),
    batches: [],
    sequentialPhases: [],
    checkpoints: []
  };

  // Intelligent adaptive approach
  if (executionContext.execution_strategy === 'INTELLIGENT_ADAPTIVE') {
    // Separate safe-parallel from sequential-required tasks
    const safeTasks = taskAnalysis.tasks.filter(t => t.parallelSafe && t.riskLevel < 30);
    const criticalTasks = taskAnalysis.tasks.filter(t => t.criticalPath || t.riskLevel >= 50);
    const mediumTasks = taskAnalysis.tasks.filter(t => !t.parallelSafe && t.riskLevel < 50);

    // Batch 1: Safe parallel tasks (low risk, independent)
    if (safeTasks.length > 0) {
      strategy.batches.push({
        id: 'batch-1-safe-parallel',
        type: 'PARALLEL',
        tasks: safeTasks,
        maxConcurrency: Math.min(safeTasks.length, 10),
        validationCheckpoint: true,
        description: 'Low-risk independent tasks - safe for parallel execution'
      });
    }

    // Phase 1: Critical path tasks (sequential with validation)
    if (criticalTasks.length > 0) {
      strategy.sequentialPhases.push({
        id: 'phase-1-critical',
        type: 'SEQUENTIAL',
        tasks: criticalTasks,
        validationFrequency: 'AFTER_EACH_TASK',
        description: 'Critical path tasks - sequential execution with per-task validation'
      });
    }

    // Batch 2: Medium tasks (small parallel batches)
    if (mediumTasks.length > 0) {
      const batchSize = 3; // Small batches for medium-risk tasks
      for (let i = 0; i < mediumTasks.length; i += batchSize) {
        strategy.batches.push({
          id: `batch-2-medium-${Math.floor(i/batchSize) + 1}`,
          type: 'PARALLEL',
          tasks: mediumTasks.slice(i, i + batchSize),
          maxConcurrency: batchSize,
          validationCheckpoint: true,
          description: 'Medium-risk tasks - small parallel batches with checkpoints'
        });
      }
    }

    // Add checkpoints after each batch/phase
    strategy.checkpoints = [
      ...strategy.batches.map(b => ({ after: b.id, type: 'BATCH_VALIDATION' })),
      ...strategy.sequentialPhases.map(p => ({ after: p.id, type: 'PHASE_VALIDATION' }))
    ];
  }

  return strategy;
}
```

### 3.3: Present Plan to User for Approval

**Before proceeding, show user the complete plan with parallelization strategy:**

```markdown
## 📋 EXECUTION PLAN READY FOR APPROVAL

**Objective**: [User's objective]

**VALUE-FIRST Analysis Summary**:
- Current Structure Value: [score]/100 ([category])
- Recommendation: [decision.recommendation]
- Auto-Proceed: [YES/NO]

---

### EXECUTION STRATEGY: Intelligent Adaptive Parallelization

**Total Tasks**: [count]
- Safe Parallel: [count] tasks
- Sequential Critical: [count] tasks
- Medium Parallel Batches: [count] tasks

**Estimated Duration**: [estimate]
**Risk Level**: [LOW/MEDIUM/HIGH]

---

### EXECUTION FLOW:

[This will be followed by the MANDATORY parallelization diagram in Phase 4]

**BATCH 1 - Safe Parallel** (Independent low-risk tasks):
├─ Task 1: [Description] - Risk: LOW - Est: [duration]
├─ Task 2: [Description] - Risk: LOW - Est: [duration]
└─ Task 3: [Description] - Risk: LOW - Est: [duration]
   ↓
📊 Checkpoint: Validate batch results before proceeding

**PHASE 1 - Critical Sequential** (High-value/high-risk tasks):
├─ Task 4: [Description] - Risk: HIGH - Est: [duration]
   ├─ Validation: [Comprehensive 5-layer]
   ↓
├─ Task 5: [Description] - Risk: HIGH - Est: [duration]
   ├─ Validation: [Comprehensive 5-layer]
   ↓
└─ Task 6: [Description] - Risk: HIGH - Est: [duration]
   ├─ Validation: [Comprehensive 5-layer]
   ↓
📊 Checkpoint: Validate phase results

**BATCH 2 - Medium Parallel** (Small batches, medium risk):
├─ Task 7: [Description] - Risk: MEDIUM - Est: [duration]
├─ Task 8: [Description] - Risk: MEDIUM - Est: [duration]
└─ Task 9: [Description] - Risk: MEDIUM - Est: [duration]
   ↓
📊 Checkpoint: Final validation

---

### QUALITY GATES (Enforced at each checkpoint):

**Layer 0 - Anti-Memory Protocol Checkpoint** (v4.1 NEW):
- ✅ Known failure patterns detected in task scope
- ✅ Reference documentation consulted (not memory reconstruction)
- ✅ Configuration syntax validated against reference
- ✅ No expression prefix contamination (e.g., "=data" vs "data")
- ✅ Anti-Memory Protocol injected into sub-agent prompts (if applicable)

**🔴 ANTI-MEMORY CHECKPOINT PROTOCOL**:
```javascript
async function antiMemoryCheckpoint(task, executionContext) {
  const knownPatterns = detectKnownFailurePatterns(task);

  if (knownPatterns.length === 0) {
    return { status: 'PASS', reason: 'No known failure patterns in task scope' };
  }

  // Verify reference was consulted
  const referenceChecks = await Promise.all(
    knownPatterns.map(async pattern => {
      const reference = getReference(pattern);
      const taskConfig = extractConfigFromTask(task, pattern);

      return {
        pattern,
        referenceConsulted: reference.wasAccessed,
        configMatchesReference: await validateAgainstReference(taskConfig, reference),
        syntaxContamination: detectSyntaxContamination(taskConfig)
      };
    })
  );

  const failures = referenceChecks.filter(check =>
    !check.referenceConsulted ||
    !check.configMatchesReference ||
    check.syntaxContamination
  );

  if (failures.length > 0) {
    return {
      status: 'FAIL',
      reason: 'Anti-Memory Protocol violation',
      failures: failures,
      action: 'STOP: Re-read reference documentation before proceeding'
    };
  }

  return { status: 'PASS', reason: 'All references consulted, configurations valid' };
}
```

**If Anti-Memory Checkpoint FAILS**:
1. ⛔ STOP execution immediately
2. 📖 READ the reference documentation for failing patterns
3. 📋 COPY exact syntax from reference (do not reconstruct)
4. ✅ VALIDATE configuration matches reference
5. 🔄 RE-RUN checkpoint before proceeding

---

**Layer 1 - Technical Validation**:
- ✅ All tests passing (Unit + Integration + E2E)
- ✅ Zero type errors
- ✅ Build succeeds
- ✅ No console errors

**Layer 2 - Integration Validation**:
- ✅ Components connect properly
- ✅ Data flows correctly
- ✅ APIs communicate as expected
- ✅ No regressions detected

**Layer 2.5 - Ecosystem Validation**:
- ✅ Inbound dependencies functional
- ✅ Outbound dependencies reachable
- ✅ Critical paths intact
- ✅ Integration points operational

**Layer 3 - User Reality Check**:
- ✅ Actual user can complete task
- ✅ UX is intuitive
- ✅ Works in production-like conditions
[✅ Screenshot evidence required] (if executionContext.validation_requirements.screenshot_evidence)

**Layer 4 - Future-Proofing**:
- ✅ Security audit passed
- ✅ Performance benchmarked
- ✅ Documentation complete
- ✅ Error handling comprehensive

---

**❓ APPROVAL REQUIRED**

Do you approve this execution plan?
- **YES** → Proceed to Phase 4 (Parallelization Diagram)
- **MODIFY** → Adjust [specify what to change]
- **NO** → Re-plan with different approach
```

---

## PHASE 4: PARALLELIZATION DIAGRAM GENERATION (MANDATORY)

**CRITICAL**: Before executing ANY parallel batches, generate visual diagram showing:
1. Batch structure
2. Sub-agent assignments
3. Data dependencies
4. Validation checkpoints
5. Critical path flow

### 4.1: Generate ASCII Parallelization Diagram

```javascript
function generateParallelizationDiagram(parallelizationStrategy, taskAnalysis) {
  const diagram = [];

  diagram.push("╔════════════════════════════════════════════════════════════════╗");
  diagram.push("║         SYNRG-GUIDED PARALLELIZATION EXECUTION MAP            ║");
  diagram.push("╚════════════════════════════════════════════════════════════════╝");
  diagram.push("");

  // For each batch/phase in strategy
  parallelizationStrategy.batches.forEach((batch, batchIndex) => {
    diagram.push(`┌─ BATCH ${batchIndex + 1}: ${batch.description}`);
    diagram.push(`│  Type: ${batch.type} | Max Concurrency: ${batch.maxConcurrency}`);
    diagram.push(`│  Risk Level: ${calculateBatchRisk(batch.tasks)}`);
    diagram.push("│");

    // Show parallel tasks
    if (batch.type === 'PARALLEL') {
      diagram.push("│  ┌─────────────┬─────────────┬─────────────┬─────────────┐");

      // Group tasks by parallel execution slots
      const slots = Math.ceil(batch.tasks.length / batch.maxConcurrency);
      for (let slot = 0; slot < slots; slot++) {
        const tasksInSlot = batch.tasks.slice(
          slot * batch.maxConcurrency,
          (slot + 1) * batch.maxConcurrency
        );

        const taskLines = tasksInSlot.map(t => `│  │ Agent-${t.id}`);
        taskLines.forEach(line => diagram.push(line));

        const descLines = tasksInSlot.map(t => `│  │ ${truncate(t.task.description, 10)}`);
        descLines.forEach(line => diagram.push(line));

        const riskLines = tasksInSlot.map(t => `│  │ Risk: ${t.riskLevel}`);
        riskLines.forEach(line => diagram.push(line));

        diagram.push("│  │─────────────┼─────────────┼─────────────┼─────────────│");
      }

      diagram.push("│  └─────────────┴─────────────┴─────────────┴─────────────┘");
    }

    // Show data dependencies
    const dependencies = identifyBatchDependencies(batch.tasks);
    if (dependencies.length > 0) {
      diagram.push("│");
      diagram.push("│  Data Dependencies:");
      dependencies.forEach(dep => {
        diagram.push(`│    • Agent-${dep.from} → Agent-${dep.to}: ${dep.dataType}`);
      });
    }

    // Show validation checkpoint
    if (batch.validationCheckpoint) {
      diagram.push("│");
      diagram.push("│  ↓");
      diagram.push("│  📊 VALIDATION CHECKPOINT");
      diagram.push("│     ✓ All agents completed successfully");
      diagram.push("│     ✓ Quality gates passed");
      diagram.push("│     ✓ No regressions detected");
      diagram.push("│     ✓ Evidence collected");
    }

    diagram.push("└──────────────────────────────────────────────────────────");
    diagram.push("");
  });

  // Add sequential phases
  parallelizationStrategy.sequentialPhases.forEach((phase, phaseIndex) => {
    diagram.push(`┌─ PHASE ${phaseIndex + 1}: ${phase.description}`);
    diagram.push(`│  Type: ${phase.type} | Validation: ${phase.validationFrequency}`);
    diagram.push("│");

    phase.tasks.forEach((task, taskIndex) => {
      diagram.push(`│  ├─ Step ${taskIndex + 1}: Agent-${task.id}`);
      diagram.push(`│  │  Task: ${task.task.description}`);
      diagram.push(`│  │  Risk: ${task.riskLevel} | Duration: ${task.estimatedDuration}`);

      if (phase.validationFrequency === 'AFTER_EACH_TASK') {
        diagram.push("│  │  ↓");
        diagram.push("│  │  📊 Validate (5-layer comprehensive)");
      }

      diagram.push("│  │");
    });

    diagram.push("└──────────────────────────────────────────────────────────");
    diagram.push("");
  });

  // Add critical path visualization
  const criticalPath = identifyCriticalPath(taskAnalysis.dependencyGraph);
  diagram.push("╔════════════════════════════════════════════════════════════════╗");
  diagram.push("║                    CRITICAL PATH ANALYSIS                      ║");
  diagram.push("╚════════════════════════════════════════════════════════════════╝");
  diagram.push("");
  diagram.push("  [START]");
  criticalPath.forEach((task, index) => {
    diagram.push("     ↓");
    diagram.push(`  [Task-${task.id}] ${truncate(task.description, 40)}`);
    diagram.push(`   Duration: ${task.estimatedDuration} | Risk: ${task.riskLevel}`);
  });
  diagram.push("     ↓");
  diagram.push("  [END] - Total Critical Path: ${calculateCriticalPathDuration(criticalPath)}");
  diagram.push("");

  // Add sub-agent interaction matrix
  diagram.push("╔════════════════════════════════════════════════════════════════╗");
  diagram.push("║              SUB-AGENT INTERACTION MATRIX                      ║");
  diagram.push("╚════════════════════════════════════════════════════════════════╝");
  diagram.push("");

  const allAgents = [
    ...parallelizationStrategy.batches.flatMap(b => b.tasks),
    ...parallelizationStrategy.sequentialPhases.flatMap(p => p.tasks)
  ];

  const interactions = identifyAgentInteractions(allAgents, taskAnalysis.dependencyGraph);

  diagram.push("  Agent Interactions:");
  diagram.push("  ┌──────────┬──────────┬──────────────┬─────────────────────┐");
  diagram.push("  │ From     │ To       │ Data Type    │ Timing              │");
  diagram.push("  ├──────────┼──────────┼──────────────┼─────────────────────┤");

  interactions.forEach(interaction => {
    diagram.push(`  │ Agent-${interaction.from} │ Agent-${interaction.to} │ ${interaction.dataType} │ ${interaction.timing} │`);
  });

  diagram.push("  └──────────┴──────────┴──────────────┴─────────────────────┘");
  diagram.push("");

  // Add legend
  diagram.push("═══════════════════════════════════════════════════════════════");
  diagram.push("LEGEND:");
  diagram.push("  📊 = Validation Checkpoint");
  diagram.push("  ↓  = Sequential Flow");
  diagram.push("  │  = Parallel Execution");
  diagram.push("  Risk Levels: LOW (<30) | MEDIUM (30-60) | HIGH (≥60)");
  diagram.push("═══════════════════════════════════════════════════════════════");

  return diagram.join('\n');
}
```

### 4.2: Present Diagram to User

```markdown
## 📊 PARALLELIZATION EXECUTION DIAGRAM

**MANDATORY REVIEW**: Please review the following execution diagram showing:
- Batch structure and parallel execution slots
- Sub-agent assignments and responsibilities
- Data dependencies between agents
- Validation checkpoints and timing
- Critical path through the execution

---

[ASCII DIAGRAM GENERATED ABOVE]

---

**Execution Insights**:
- **Total Parallelization**: [X]% of tasks can run in parallel
- **Critical Path Duration**: [Y] minutes
- **Total Wall-Clock Time**: [Z] minutes (vs [W] minutes sequential)
- **Time Savings**: [Z-W] minutes ([percentage]% faster)
- **Risk Distribution**: [N] low-risk, [M] medium-risk, [P] high-risk tasks

**Key Dependencies**:
1. [Agent-X] must complete before [Agent-Y] can start (reason: [data dependency])
2. [Agent-A] and [Agent-B] share [resource], coordinated via [mechanism]
3. [Critical Path] tasks cannot be parallelized due to [reason]

---

**❓ DIAGRAM APPROVAL**

Does this execution strategy look correct?
- **YES** → Proceed to Phase 5 (Autonomous Execution)
- **OPTIMIZE** → Suggest improvements to parallelization
- **REPLAN** → Revise task decomposition
```

---

## PHASE 5: AUTONOMOUS ADAPTIVE EXECUTION

**Objective**: Execute approved plan autonomously, escalating ONLY for value-first decisions or critical errors.

### 5.1: Autonomous Execution Loop

```javascript
async function executeAdaptiveParallelization(parallelizationStrategy, executionContext, valueAnalysis) {
  const executionState = {
    currentPhase: null,
    completedTasks: [],
    failedTasks: [],
    inProgressTasks: [],
    checkpointResults: [],
    escalations: []
  };

  // Execute batches
  for (const batch of parallelizationStrategy.batches) {
    executionState.currentPhase = batch.id;

    console.log(`🚀 Executing ${batch.id}: ${batch.description}`);
    console.log(`   Type: ${batch.type} | Concurrency: ${batch.maxConcurrency}`);

    if (batch.type === 'PARALLEL') {
      // Execute tasks in parallel
      const batchResults = await Promise.allSettled(
        batch.tasks.map(task => executeTaskAutonomously(task, executionContext, valueAnalysis))
      );

      // Process results
      batchResults.forEach((result, index) => {
        const task = batch.tasks[index];

        if (result.status === 'fulfilled') {
          executionState.completedTasks.push({
            taskId: task.id,
            result: result.value,
            timestamp: Date.now()
          });
        } else {
          executionState.failedTasks.push({
            taskId: task.id,
            error: result.reason,
            timestamp: Date.now()
          });
        }
      });

      // Checkpoint validation
      if (batch.validationCheckpoint) {
        const checkpointResult = await performCheckpointValidation(
          batch,
          executionState,
          executionContext
        );

        executionState.checkpointResults.push(checkpointResult);

        if (!checkpointResult.passed) {
          // Checkpoint failed - decide whether to escalate or auto-recover
          const shouldEscalate = decideEscalation(checkpointResult, executionContext);

          if (shouldEscalate) {
            await escalateToUser({
              type: 'CHECKPOINT_FAILURE',
              batch: batch.id,
              failures: checkpointResult.failures,
              recommendation: checkpointResult.recommendation
            });

            // Wait for user decision
            const userDecision = await getUserDecision();

            if (userDecision === 'ABORT') {
              return executionState;
            } else if (userDecision === 'RETRY') {
              // Retry failed tasks
              continue;
            }
          } else {
            // Auto-recover using Phase 6 error recovery loop
            await autonomousErrorRecovery(checkpointResult.failures, executionContext);
          }
        }
      }
    }
  }

  // Execute sequential phases
  for (const phase of parallelizationStrategy.sequentialPhases) {
    executionState.currentPhase = phase.id;

    console.log(`🎯 Executing ${phase.id}: ${phase.description}`);
    console.log(`   Type: ${phase.type} | Validation: ${phase.validationFrequency}`);

    for (const task of phase.tasks) {
      const taskResult = await executeTaskAutonomously(task, executionContext, valueAnalysis);

      if (taskResult.success) {
        executionState.completedTasks.push({
          taskId: task.id,
          result: taskResult,
          timestamp: Date.now()
        });

        // Per-task validation if required
        if (phase.validationFrequency === 'AFTER_EACH_TASK') {
          const validation = await perform5LayerValidation(taskResult, executionContext);

          if (!validation.passed) {
            // Task validation failed - trigger error recovery
            const recovered = await autonomousErrorRecovery([{
              taskId: task.id,
              error: validation.error,
              result: taskResult
            }], executionContext);

            if (!recovered) {
              // Escalate if auto-recovery failed
              await escalateToUser({
                type: 'TASK_VALIDATION_FAILURE',
                task: task.id,
                error: validation.error,
                recommendation: 'Manual intervention required'
              });

              return executionState;
            }
          }
        }
      } else {
        executionState.failedTasks.push({
          taskId: task.id,
          error: taskResult.error,
          timestamp: Date.now()
        });

        // Trigger autonomous error recovery
        const recovered = await autonomousErrorRecovery([{
          taskId: task.id,
          error: taskResult.error
        }], executionContext);

        if (!recovered) {
          await escalateToUser({
            type: 'TASK_EXECUTION_FAILURE',
            task: task.id,
            error: taskResult.error
          });

          return executionState;
        }
      }
    }
  }

  return executionState;
}
```

### 5.2: Autonomous Task Execution

```javascript
async function executeTaskAutonomously(task, executionContext, valueAnalysis) {
  const taskState = {
    attempts: 0,
    maxAttempts: 3,
    success: false,
    result: null,
    error: null,
    evidence: []
  };

  while (taskState.attempts < taskState.maxAttempts && !taskState.success) {
    taskState.attempts++;

    try {
      console.log(`  ├─ Agent-${task.id}: ${task.task.description} (Attempt ${taskState.attempts})`);

      // 0. PRE-CHECK: Auto-generated file detection
      if (task.task.involvesFileEdit) {
        const fileCheck = await checkIfAutoGenerated(task.task.targetFile);
        if (fileCheck.isGenerated && fileCheck.hasGenerationScript) {
          console.log(`  │  ⚠️  Auto-generated file detected, using generation script`);
          await runGenerationScript(fileCheck.script);
          taskState.success = true;
          taskState.result = { method: 'regenerated', script: fileCheck.script };
          continue;
        }
      }

      // 1. CAPTURE BASELINE
      const baseline = await captureCurrentState(task);

      // 2. PLAN ROBUST SOLUTION (not quick fix)
      const robustPlan = await planRobustSolution(task, valueAnalysis);

      // 3. IMPLEMENT WITH COMPREHENSIVE QUALITY
      const implementation = await implementRobustChange({
        codeChange: robustPlan.implementation,
        tests: robustPlan.tests,
        errorHandling: robustPlan.errorHandling,
        documentation: robustPlan.docs,
        securityCheck: robustPlan.security,
        performanceTest: robustPlan.performance
      });

      // 4. VALIDATE COMPREHENSIVELY (5 layers)
      const validation = await perform5LayerValidation(implementation, executionContext);

      // 5. COLLECT EVIDENCE
      if (executionContext.validation_requirements.screenshot_evidence) {
        const screenshot = await captureScreenshot(implementation);
        taskState.evidence.push({ type: 'screenshot', data: screenshot });
      }

      taskState.evidence.push({ type: 'test_results', data: validation.testResults });
      taskState.evidence.push({ type: 'benchmark', data: validation.performanceBenchmark });

      // 6. DECISION POINT
      if (validation.passed && validation.ecosystemHealth === 'HEALTHY') {
        taskState.success = true;
        taskState.result = {
          implementation: implementation,
          validation: validation,
          evidence: taskState.evidence
        };

        console.log(`  │  ✅ Agent-${task.id} completed successfully`);

      } else if (validation.ecosystemHealth === 'BROKEN') {
        // Ecosystem failure - revert and report
        await revertToBaseline(baseline);

        throw new Error(`Ecosystem validation failed: ${validation.ecosystemError}`);

      } else if (validation.regression) {
        // Regression detected - revert and try alternative
        await revertToBaseline(baseline);

        console.log(`  │  ⚠️  Regression detected, trying alternative approach`);

        // This will trigger next attempt in the loop

      } else {
        throw new Error(`Validation failed: ${validation.error}`);
      }

    } catch (error) {
      taskState.error = error;
      console.log(`  │  ❌ Agent-${task.id} failed: ${error.message}`);

      // Error will be handled by autonomous recovery in next phase
    }
  }

  return taskState;
}
```

### 5.3: Checkpoint Validation

```javascript
async function performCheckpointValidation(batch, executionState, executionContext) {
  console.log(`\n📊 CHECKPOINT: Validating ${batch.id}`);

  const checkpointResult = {
    batchId: batch.id,
    passed: true,
    failures: [],
    warnings: [],
    evidence: [],
    recommendation: null
  };

  // Gather all completed tasks from this batch
  const batchTasks = executionState.completedTasks.filter(t =>
    batch.tasks.some(bt => bt.id === t.taskId)
  );

  // Validate each completed task
  for (const completedTask of batchTasks) {
    const taskValidation = await perform5LayerValidation(
      completedTask.result,
      executionContext
    );

    if (!taskValidation.passed) {
      checkpointResult.passed = false;
      checkpointResult.failures.push({
        taskId: completedTask.taskId,
        error: taskValidation.error,
        layer: taskValidation.failedLayer
      });
    }

    // Collect evidence
    checkpointResult.evidence.push({
      taskId: completedTask.taskId,
      validation: taskValidation,
      evidence: completedTask.result.evidence
    });
  }

  // Cross-task validation (integration between batch tasks)
  const integration Validation = await validateBatchIntegration(batchTasks);

  if (!integrationValidation.passed) {
    checkpointResult.passed = false;
    checkpointResult.failures.push({
      type: 'INTEGRATION_FAILURE',
      error: integrationValidation.error
    });
  }

  // Determine recommendation
  if (!checkpointResult.passed) {
    if (checkpointResult.failures.every(f => f.layer === 'TECHNICAL')) {
      checkpointResult.recommendation = 'AUTO_RECOVER';
    } else if (checkpointResult.failures.some(f => f.type === 'ECOSYSTEM_FAILURE')) {
      checkpointResult.recommendation = 'ESCALATE_IMMEDIATE';
    } else {
      checkpointResult.recommendation = 'TRY_ALTERNATIVE';
    }
  }

  console.log(`  Result: ${checkpointResult.passed ? '✅ PASSED' : '❌ FAILED'}`);
  if (!checkpointResult.passed) {
    console.log(`  Failures: ${checkpointResult.failures.length}`);
    console.log(`  Recommendation: ${checkpointResult.recommendation}`);
  }

  return checkpointResult;
}
```

### 5.4: Escalation Decision Logic

```javascript
function decideEscalation(checkpointResult, executionContext) {
  // ALWAYS escalate for these conditions
  if (checkpointResult.recommendation === 'ESCALATE_IMMEDIATE') return true;
  if (checkpointResult.failures.some(f => f.type === 'ECOSYSTEM_FAILURE')) return true;
  if (checkpointResult.failures.some(f => f.type === 'PROTECTED_STRUCTURE')) return true;

  // Auto-proceed based on context
  if (executionContext.risk_tolerance === 'MOVE_FAST') {
    // Only escalate critical failures
    return checkpointResult.failures.some(f => f.severity === 'CRITICAL');
  }

  if (executionContext.risk_tolerance === 'HIGH_CAUTION') {
    // Escalate all failures
    return checkpointResult.failures.length > 0;
  }

  // BALANCED approach (default)
  if (executionContext.auto_proceed_threshold >= 70) {
    // High autonomy - only escalate high-severity failures
    return checkpointResult.failures.some(f => f.severity === 'HIGH' || f.severity === 'CRITICAL');
  } else if (executionContext.auto_proceed_threshold >= 40) {
    // Medium autonomy - escalate medium+ severity
    return checkpointResult.failures.some(f => f.severity !== 'LOW');
  } else {
    // Low autonomy - escalate everything
    return checkpointResult.failures.length > 0;
  }
}
```

---

## PHASE 6: AUTONOMOUS ERROR RECOVERY LOOP

**Objective**: When errors are detected, autonomously test → analyze → validate → fix without user intervention.

### 6.1: Autonomous Error Recovery Protocol

```javascript
async function autonomousErrorRecovery(failures, executionContext) {
  console.log(`\n🔧 AUTONOMOUS ERROR RECOVERY: ${failures.length} failure(s) detected`);

  const recoveryState = {
    originalFailures: failures,
    recoveredFailures: [],
    persistentFailures: [],
    attempts: []
  };

  for (const failure of failures) {
    console.log(`\n  ┌─ Recovering: Task-${failure.taskId}`);
    console.log(`  │  Error: ${failure.error.message}`);

    // Execute autonomous recovery loop
    const recovered = await executeRecoveryLoop(failure, executionContext);

    if (recovered.success) {
      recoveryState.recoveredFailures.push({
        taskId: failure.taskId,
        originalError: failure.error,
        solution: recovered.solution,
        attempts: recovered.attempts
      });

      console.log(`  └─ ✅ Recovery successful after ${recovered.attempts} attempt(s)`);
    } else {
      recoveryState.persistentFailures.push({
        taskId: failure.taskId,
        error: failure.error,
        recoveryAttempts: recovered.attempts,
        lastError: recovered.lastError
      });

      console.log(`  └─ ❌ Recovery failed after ${recovered.attempts} attempt(s)`);
    }

    recoveryState.attempts.push(recovered);
  }

  // Return success if ALL failures recovered
  const allRecovered = recoveryState.persistentFailures.length === 0;

  if (allRecovered) {
    console.log(`\n✅ AUTONOMOUS RECOVERY: All failures resolved`);
  } else {
    console.log(`\n⚠️  AUTONOMOUS RECOVERY: ${recoveryState.persistentFailures.length} failure(s) persist`);
  }

  return allRecovered;
}
```

### 6.2: Recovery Loop (Test → Analyze → Validate → Fix)

```javascript
async function executeRecoveryLoop(failure, executionContext) {
  const recoveryState = {
    success: false,
    attempts: 0,
    maxAttempts: 3,
    solution: null,
    lastError: null,
    analysisHistory: []
  };

  while (recoveryState.attempts < recoveryState.maxAttempts && !recoveryState.success) {
    recoveryState.attempts++;

    console.log(`  │  Attempt ${recoveryState.attempts}/${recoveryState.maxAttempts}`);

    try {
      // STEP 1: TEST - Reproduce the error
      console.log(`  │  ├─ 1. TESTING: Reproducing error...`);
      const errorReproduction = await reproduceError(failure);

      if (!errorReproduction.reproduced) {
        // Error no longer occurs - consider it resolved
        console.log(`  │  │  ✅ Error no longer reproducible`);
        recoveryState.success = true;
        recoveryState.solution = { type: 'SELF_RESOLVED' };
        break;
      }

      console.log(`  │  │  ✅ Error reproduced: ${errorReproduction.error.message}`);

      // Capture screenshot evidence if UI-related
      let screenshot = null;
      if (executionContext.validation_requirements.screenshot_evidence && errorReproduction.isUIError) {
        screenshot = await captureErrorScreenshot(errorReproduction);
        console.log(`  │  │  📸 Screenshot captured`);
      }

      // STEP 2: ANALYZE - Comprehensive error analysis
      console.log(`  │  ├─ 2. ANALYZING: Performing comprehensive error analysis...`);
      const analysis = await performComprehensiveErrorAnalysis({
        error: errorReproduction.error,
        screenshot: screenshot,
        context: failure,
        attempt: recoveryState.attempts,
        previousAnalyses: recoveryState.analysisHistory
      });

      recoveryState.analysisHistory.push(analysis);

      console.log(`  │  │  ✅ Analysis complete:`);
      console.log(`  │  │     Root Cause: ${analysis.rootCause.layer5}`);
      console.log(`  │  │     Pattern Match: ${analysis.patternMatch || 'None'}`);
      console.log(`  │  │     Severity: ${analysis.currentImpact.severity}`);
      console.log(`  │  │     Cascade Risk: ${analysis.cascadeRisk.probability}%`);

      // Check if this matches a known pattern
      if (analysis.patternMatch) {
        console.log(`  │  │  🎯 Known pattern detected: ${analysis.patternMatch}`);

        // Apply known solution
        const knownSolution = await applyKnownPatternSolution(analysis.patternMatch);

        // Validate the known solution
        console.log(`  │  ├─ 3. VALIDATING: Testing known solution...`);
        const validation = await validateSolution(knownSolution, executionContext);

        if (validation.passed) {
          console.log(`  │  │  ✅ Known solution validated successfully`);
          recoveryState.success = true;
          recoveryState.solution = {
            type: 'KNOWN_PATTERN',
            pattern: analysis.patternMatch,
            solution: knownSolution
          };
          break;
        } else {
          console.log(`  │  │  ❌ Known solution validation failed`);
          // Continue to Step 4 to develop custom fix
        }
      }

      // STEP 3: VALIDATE - Current state validation
      console.log(`  │  ├─ 3. VALIDATING: Checking current system state...`);
      const currentStateValidation = await validateCurrentState(failure.taskId);

      if (currentStateValidation.canProceed) {
        console.log(`  │  │  ✅ System state allows fix attempt`);
      } else {
        console.log(`  │  │  ⚠️  System state issue: ${currentStateValidation.issue}`);

        // Attempt to fix system state first
        await fixSystemState(currentStateValidation.issue);
      }

      // STEP 4: FIX - Develop and apply fix plan
      console.log(`  │  ├─ 4. FIXING: Developing fix plan...`);
      const fixPlan = await developFixPlan({
        analysis: analysis,
        currentState: currentStateValidation,
        valueAnalysis: failure.valueAnalysis,
        executionContext: executionContext,
        previousAttempts: recoveryState.attempts - 1
      });

      console.log(`  │  │  Fix Strategy: ${fixPlan.strategy}`);
      console.log(`  │  │  Estimated Risk: ${fixPlan.risk}`);
      console.log(`  │  │  Estimated Duration: ${fixPlan.estimatedDuration}`);

      // Capture baseline before applying fix
      const baseline = await captureCurrentState();

      // Apply fix
      console.log(`  │  │  Applying fix...`);
      const fixResult = await applyFix(fixPlan);

      // Validate fix (comprehensive 5-layer)
      console.log(`  │  │  Validating fix...`);
      const fixValidation = await perform5LayerValidation(fixResult, executionContext);

      if (fixValidation.passed && fixValidation.ecosystemHealth === 'HEALTHY') {
        console.log(`  │  │  ✅ Fix validated successfully`);
        recoveryState.success = true;
        recoveryState.solution = {
          type: 'CUSTOM_FIX',
          fixPlan: fixPlan,
          result: fixResult,
          validation: fixValidation
        };
        break;

      } else if (fixValidation.ecosystemHealth === 'BROKEN') {
        console.log(`  │  │  ❌ Fix broke ecosystem - reverting`);
        await revertToBaseline(baseline);

        // Try alternative approach on next iteration

      } else if (fixValidation.regression) {
        console.log(`  │  │  ❌ Fix caused regression - reverting`);
        await revertToBaseline(baseline);

        // Try alternative approach on next iteration

      } else {
        console.log(`  │  │  ❌ Fix validation failed: ${fixValidation.error}`);
        await revertToBaseline(baseline);
      }

    } catch (error) {
      console.log(`  │  │  ❌ Recovery attempt failed: ${error.message}`);
      recoveryState.lastError = error;

      // Continue to next attempt
    }
  }

  return recoveryState;
}
```

### 6.3: Comprehensive Error Analysis (Integrated into Recovery)

```javascript
async function performComprehensiveErrorAnalysis(errorContext) {
  console.log(`  │  │  Performing 5-Why analysis...`);

  return {
    // 5-Why Root Cause Analysis
    rootCause: await identify5WhyRootCause(errorContext.error),

    // Pattern matching
    patternMatch: await matchKnownPattern(errorContext.error),

    // Current impact assessment
    currentImpact: await assessCurrentImpact(errorContext.error),

    // Future impact prediction
    futureImpact: await predictFutureImpact(errorContext.error, errorContext.rootCause),

    // Cascade failure analysis
    cascadeRisk: await analyzeCascadePotential(errorContext.error),

    // Preventive actions
    preventiveActions: await identifyPreventiveActions(errorContext.error, errorContext.rootCause),

    // Screenshot analysis (if available)
    screenshotAnalysis: errorContext.screenshot ?
      await analyzeErrorScreenshot(errorContext.screenshot) : null,

    // Learning from previous attempts
    learningFromPrevious: errorContext.previousAnalyses.length > 0 ?
      await synthesizeLearnings(errorContext.previousAnalyses) : null
  };
}
```

### 6.4: Fix Plan Development

```javascript
async function developFixPlan(fixContext) {
  const { analysis, currentState, valueAnalysis, executionContext, previousAttempts } = fixContext;

  // Determine fix strategy based on analysis
  let strategy;

  if (analysis.patternMatch && previousAttempts === 0) {
    strategy = 'APPLY_KNOWN_PATTERN';
  } else if (analysis.rootCause.requiresArchitecturalChange) {
    strategy = 'ARCHITECTURAL_FIX';
  } else if (analysis.currentImpact.severity === 'CRITICAL') {
    strategy = 'IMMEDIATE_MITIGATION';
  } else if (previousAttempts > 0) {
    strategy = 'ALTERNATIVE_APPROACH';
  } else {
    strategy = 'STANDARD_FIX';
  }

  // Generate fix plan
  const fixPlan = {
    strategy: strategy,
    approach: null,
    steps: [],
    risk: 'LOW',
    estimatedDuration: '5-10 minutes',
    rollbackProcedure: null,
    validation: [],
    preventiveMeasures: []
  };

  // Strategy-specific planning
  switch (strategy) {
    case 'APPLY_KNOWN_PATTERN':
      fixPlan.approach = `Apply documented solution for ${analysis.patternMatch}`;
      fixPlan.steps = await getPatternSolutionSteps(analysis.patternMatch);
      fixPlan.risk = 'LOW';
      break;

    case 'ARCHITECTURAL_FIX':
      fixPlan.approach = 'Architectural change required - escalate if auto_proceed_threshold < 80';
      if (executionContext.auto_proceed_threshold < 80) {
        throw new Error('ESCALATE_REQUIRED: Architectural change needs user approval');
      }
      fixPlan.steps = await planArchitecturalFix(analysis, valueAnalysis);
      fixPlan.risk = 'HIGH';
      fixPlan.estimatedDuration = '30-60 minutes';
      break;

    case 'IMMEDIATE_MITIGATION':
      fixPlan.approach = 'Critical issue - apply immediate mitigation';
      fixPlan.steps = await planImmediateMitigation(analysis);
      fixPlan.risk = 'MEDIUM';
      break;

    case 'ALTERNATIVE_APPROACH':
      fixPlan.approach = `Alternative approach (previous attempt ${previousAttempts} failed)`;
      fixPlan.steps = await planAlternativeFix(analysis, previousAttempts);
      fixPlan.risk = 'MEDIUM';
      break;

    default:
      fixPlan.approach = 'Standard robust fix';
      fixPlan.steps = await planStandardFix(analysis);
      fixPlan.risk = 'LOW';
  }

  // Add comprehensive quality gates to fix plan
  fixPlan.validation = [
    'Technical validation (all tests pass)',
    'Integration validation (no regressions)',
    'Ecosystem validation (all dependencies healthy)',
    'User validation (user flows work)',
    'Future-proofing validation (preventive measures in place)'
  ];

  // Add preventive measures based on error analysis
  fixPlan.preventiveMeasures = analysis.preventiveActions;

  // Define rollback procedure
  fixPlan.rollbackProcedure = await defineRollbackProcedure(fixPlan);

  return fixPlan;
}
```

---

## PHASE 7: COMPREHENSIVE VALIDATION & REPORTING

**Objective**: Validate all results comprehensively and provide detailed execution report.

### 7.1: 5-Layer Validation Framework

```javascript
async function perform5LayerValidation(result, executionContext) {
  const validation = {
    passed: true,
    failedLayer: null,
    layers: {},
    ecosystemHealth: 'HEALTHY',
    evidence: []
  };

  // Layer 1: Technical Validation
  console.log(`  │  Validating Layer 1: Technical...`);
  validation.layers.technical = await validateTechnical(result);
  if (!validation.layers.technical.passed) {
    validation.passed = false;
    validation.failedLayer = 'TECHNICAL';
    return validation;
  }

  // Layer 2: Integration Validation
  console.log(`  │  Validating Layer 2: Integration...`);
  validation.layers.integration = await validateIntegration(result);
  if (!validation.layers.integration.passed) {
    validation.passed = false;
    validation.failedLayer = 'INTEGRATION';
    return validation;
  }

  // Layer 2.5: Ecosystem Validation
  console.log(`  │  Validating Layer 2.5: Ecosystem...`);
  validation.layers.ecosystem = await validateEcosystem(result);
  validation.ecosystemHealth = validation.layers.ecosystem.health;
  if (validation.ecosystemHealth === 'BROKEN') {
    validation.passed = false;
    validation.failedLayer = 'ECOSYSTEM';
    return validation;
  }

  // Layer 3: User Reality Check
  console.log(`  │  Validating Layer 3: User Reality...`);
  validation.layers.user = await validateUserReality(result, executionContext);
  if (!validation.layers.user.passed) {
    validation.passed = false;
    validation.failedLayer = 'USER';
    return validation;
  }

  // Layer 4: Future-Proofing
  console.log(`  │  Validating Layer 4: Future-Proofing...`);
  validation.layers.futureProofing = await validateFutureProofing(result);
  if (!validation.layers.futureProofing.passed) {
    validation.passed = false;
    validation.failedLayer = 'FUTURE_PROOFING';
    return validation;
  }

  // Collect evidence
  validation.evidence = [
    validation.layers.technical.evidence,
    validation.layers.integration.evidence,
    validation.layers.ecosystem.evidence,
    validation.layers.user.evidence,
    validation.layers.futureProofing.evidence
  ];

  return validation;
}
```

### 7.2: Generate Execution Report

```markdown
## 📊 SYNRG-GUIDED EXECUTION REPORT

**Objective**: [User's original objective]
**Execution Started**: [timestamp]
**Execution Completed**: [timestamp]
**Total Duration**: [wall-clock time]

---

### VALUE-FIRST ANALYSIS SUMMARY

**Structure Value Assessment**:
- Total Value Score: [score]/100 ([HIGH/MEDIUM/LOW])
- Production Stability: [score]/100
- Business Logic Value: [score]/100
- Integration Value: [score]/100
- Code Quality: [score]/100
- Team Knowledge: [score]/100

**Change Impact Prediction**:
- Risk Score: [score]/100
- Benefit Score: [score]/100
- Net Value Change: [+/-][value]

**Decision**: [PRESERVE_WITH_SAFEGUARDS | PRESERVE_AND_ENHANCE | ADAPTIVE_ENHANCEMENT | COMPREHENSIVE_RESTRUCTURE]

**Protected Structures**: [List if any detected]

---

### EXECUTION SUMMARY

**Total Tasks**: [count]
- ✅ Completed Successfully: [count]
- ❌ Failed: [count]
- 🔧 Auto-Recovered: [count]

**Parallelization Efficiency**:
- Parallel Tasks: [count] ([percentage]% of total)
- Sequential Tasks: [count] ([percentage]% of total)
- Time Saved vs Sequential: [minutes] ([percentage]% faster)

**Batches Executed**: [count]
- Batch 1 (Safe Parallel): [X] tasks, [duration], [status]
- Phase 1 (Critical Sequential): [X] tasks, [duration], [status]
- Batch 2 (Medium Parallel): [X] tasks, [duration], [status]

**Validation Checkpoints**:
- Total Checkpoints: [count]
- Passed: [count]
- Failed (Auto-Recovered): [count]
- Failed (Escalated): [count]

---

### AUTONOMOUS ERROR RECOVERY

**Errors Encountered**: [count]
**Auto-Recovery Success Rate**: [percentage]%

**Recovery Details**:
1. Task-[ID]: [Error description]
   - Pattern Match: [Pattern name or "None"]
   - Recovery Attempts: [count]
   - Recovery Method: [KNOWN_PATTERN | CUSTOM_FIX | SELF_RESOLVED]
   - Status: [✅ Recovered | ❌ Escalated]

2. [Additional recoveries...]

**Known Patterns Applied**:
- Pattern-001-AutoGeneratedFiles: [count] times
- Pattern-002-ExportMismatch: [count] times
- [Additional patterns...]

---

### QUALITY VALIDATION RESULTS

**5-Layer Validation**:
- ✅ Layer 1 (Technical): [PASSED/FAILED]
  - All tests passing: [YES/NO]
  - Zero type errors: [YES/NO]
  - Build succeeds: [YES/NO]

- ✅ Layer 2 (Integration): [PASSED/FAILED]
  - Components connect: [YES/NO]
  - Data flows correctly: [YES/NO]
  - APIs functional: [YES/NO]

- ✅ Layer 2.5 (Ecosystem): [PASSED/FAILED]
  - Ecosystem Health: [HEALTHY/DEGRADED/BROKEN]
  - Inbound dependencies: [count] validated
  - Outbound dependencies: [count] validated
  - Critical paths: [count] validated

- ✅ Layer 3 (User Reality): [PASSED/FAILED]
  - User flows tested: [count]
  - UX intuitive: [YES/NO]
  - Production-ready: [YES/NO]

- ✅ Layer 4 (Future-Proofing): [PASSED/FAILED]
  - Security audit: [PASSED/FAILED]
  - Performance benchmark: [PASSED/FAILED]
  - Documentation: [COMPLETE/INCOMPLETE]

**Evidence Collected**:
- Screenshots: [count]
- Test Results: [count]
- Performance Benchmarks: [count]
- Security Scans: [count]

---

### ESCALATIONS TO USER

**Total Escalations**: [count]

[If escalations occurred:]
1. [Escalation Type]: [Description]
   - Reason: [Why escalated]
   - User Decision: [What user decided]
   - Outcome: [Result after decision]

[If no escalations:]
✅ No escalations required - fully autonomous execution

---

### COMPREHENSIVE DELIVERABLES

**Code Changes**:
- Files Modified: [count]
- Lines Added: [count]
- Lines Removed: [count]
- Tests Added: [count]

**Documentation**:
- Code Comments: [COMPLETE/INCOMPLETE]
- API Documentation: [COMPLETE/INCOMPLETE]
- Architecture Diagrams: [UPDATED/NOT_NEEDED]

**Quality Metrics**:
- Test Coverage: [percentage]%
- Performance Impact: [+/-][percentage]%
- Security Vulnerabilities: [count] ([0] = excellent)
- Code Complexity: [LOW/MEDIUM/HIGH]

**Preventive Actions Implemented**:
1. [Preventive measure 1]
2. [Preventive measure 2]
3. [Additional measures...]

---

### EXECUTION INSIGHTS

**What Worked Well**:
- [Insight 1]
- [Insight 2]

**Challenges Encountered**:
- [Challenge 1]: [How resolved]
- [Challenge 2]: [How resolved]

**Pattern Recognition**:
- New Patterns Discovered: [count]
- Existing Patterns Validated: [count]

**Recommendations for Future**:
- [Recommendation 1]
- [Recommendation 2]

---

### FINAL STATUS

**Overall Success**: [✅ COMPLETE | ⚠️ PARTIAL | ❌ FAILED]

**Production Ready**: [YES/NO]

**Next Steps**: [If any remaining work]

---

**Execution completed successfully! All quality gates passed. ✅**
```

---

## 🧬 SELF-EVOLUTION & PATTERN LEARNING

**After every execution, the command learns and improves.**

### Pattern Library Management

```javascript
async function updatePatternLibrary(executionReport) {
  // Extract new patterns from errors encountered
  const newPatterns = executionReport.errors
    .filter(e => e.recoveryMethod === 'CUSTOM_FIX' && e.recoveryAttempts > 1)
    .map(e => ({
      trigger: e.error.type,
      detection: e.analysis.rootCause,
      solution: e.recoveryPlan,
      occurrences: 1,
      successRate: e.recovered ? 100 : 0
    }));

  // Update existing patterns with new occurrences
  for (const pattern of knownPatterns) {
    const matchedErrors = executionReport.errors.filter(e =>
      e.patternMatch === pattern.name
    );

    if (matchedErrors.length > 0) {
      pattern.occurrences += matchedErrors.length;
      pattern.successRate = calculateSuccessRate(pattern, matchedErrors);
    }
  }

  // Add new patterns if they occur multiple times
  newPatterns.forEach(newPattern => {
    if (!knownPatterns.some(p => p.trigger === newPattern.trigger)) {
      knownPatterns.push({
        name: `Pattern-${knownPatterns.length + 1}-${generatePatternName(newPattern)}`,
        ...newPattern,
        added: Date.now()
      });
    }
  });

  // Save updated pattern library
  await savePatternLibrary(knownPatterns);
}
```

---

## 🔒 UNIVERSAL POST-IMPLEMENTATION REVIEW (MANDATORY - USP v1.0)

**HARD STOP**: Complete ALL reviews before marking task complete.

### REVIEW 1: Objective Verification
```
□ Original objective achieved? □ Most efficient approach? □ No unnecessary complexity?
Status: [ACHIEVED/PARTIAL/NEEDS_WORK]
```

### REVIEW 2: Post-Change Security
```
□ Secrets scan passed □ No injection vectors □ Dependencies secure
Status: [APPROVED/NEEDS_REMEDIATION]
```

### REVIEW 3: Documentation Check (P5)
```
□ API docs updated (if API changed) □ README updated (if config changed)
□ Architecture docs updated (if structure changed)
Status: [COMPLETE/PENDING]
```

### REVIEW 4: SYNRG-COMMIT Chain
```
Option A: /synrg-commit (RECOMMENDED) - Full atomic decomposition
Option B: Manual with <type>(<scope>): <summary> + WHY/HOW/IMPACT

Commit must be understandable by: Junior (WHAT) + Senior (WHY) + Stakeholders (IMPACT)
Status: [COMPLETED/PENDING]
```

### REVIEW 5: Final Quality Gate
```
□ Objective: YES □ Security: YES □ Docs: YES □ Commit: YES □ No regressions: YES
TASK: [COMPLETE/BLOCKED]
```

**Full Protocol**: See `~/.claude/skills/universal-synrg-protocols.md`

---

## 📚 COMMAND INVOCATION

**Usage**:
```bash
/synrg-guided [objective or task description]
```

**Examples**:
```bash
/synrg-guided refactor authentication system to use OAuth2
/synrg-guided add real-time notifications feature
/synrg-guided optimize database queries for performance
/synrg-guided fix all TypeScript errors in the codebase
```

---

## ⚙️ CONFIGURATION PARAMETERS

Users can customize execution through their responses to Phase 1 questions:

```yaml
default_config:
  risk_tolerance: BALANCED  # HIGH_CAUTION | BALANCED | MOVE_FAST
  auto_proceed_threshold: 60  # 0-100, higher = more autonomous
  screenshot_evidence: true  # Require screenshots for validation
  test_coverage_target: 80  # Percentage
  parallelization_strategy: INTELLIGENT_ADAPTIVE  # Always adaptive
  validation_strictness: COMPREHENSIVE  # Always 5-layer
  error_recovery_attempts: 3  # Auto-recovery attempts before escalation
```

---

**Ready to execute SYNRG Guided Orchestration with interactive planning, autonomous execution, and intelligent adaptive parallelization! 🚀**
