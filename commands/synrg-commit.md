---
synrg_version: "1.0.0"
command: "synrg-commit"
created: "2025-11-02"
updated: "2026-01-09"
min_claude_version: "opus-4"
requires:
  protocols: [git-commit]
  agents: []
  skills: [commit-message-craft, git-strategy-decision]
breaking_changes: []
description: Intelligent Atomic Commit Orchestrator with Director/Sub-Agent Pattern
argument-hint: [scope or commit message hint]
---

# SYNRG-COMMIT Command
## Intelligent Atomic Commit Orchestrator with Director/Sub-Agent Pattern

**Philosophy**: SYNRG v3.0 Robustness-First

---

## Command Purpose

Analyze uncommitted changes using parallel sub-agents, decompose them into logical atomic commits, generate senior-level conventional commit messages, and execute git operations automatically with comprehensive validation and safety mechanisms.

**Core Capabilities**:
- 🔍 **Deep Change Analysis**: 6 parallel sub-agents analyze git diff, context, intent, quality, impact, and history
- ⚛️ **Atomic Decomposition**: Intelligent grouping of changes into independently testable, logical commits
- 📝 **Senior-Level Messages**: Conventional commit format with comprehensive body and footer
- 🤖 **Fully Automatic**: Executes git operations autonomously with safety checks
- 🛡️ **Production-Grade**: Comprehensive error handling, rollback, and validation

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
│  COMMIT-SPECIFIC: Git analysis MUST be delegated (6 parallel sub-agents)    │
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
GATE 2: GIT_STRATEGY   - Assess scope → select branch/worktree strategy
GATE 3: CERTAINTY      - Calculate certainty, reduce scope if < threshold
GATE 4: SECURITY       - Secrets/OWASP/Privilege/Deps check
GATE 5: USER_VERIFY    - Get approval before major changes (>3 files)
```

### POST-IMPLEMENTATION REVIEWS
```
REVIEW 1: OBJECTIVE    - Achieved? Efficient? No unnecessary complexity?
REVIEW 2: SECURITY     - Re-scan for secrets, injection vectors, CVEs
REVIEW 3: DOCS (P5)    - Update API/README/architecture docs if affected
REVIEW 4: COMMIT       - This command IS the commit workflow
REVIEW 5: QUALITY      - All gates passed → COMPLETE
```

---

## 🧠 CLAUDE TOOL SELECTION PROTOCOL (Reference: /synrg)

**For commit operations, select the optimal Claude tool type:**

| Task | Recommended Tool Type | Rationale |
|------|----------------------|-----------|
| Change analysis | SUB-AGENTS (parallel) | 6 parallel analysis agents |
| Commit grouping | DIRECT | Synthesis in director context |
| Pre-commit validation | HOOK | Event-triggered automation |
| Complex refactor first | SLASH COMMAND | Chain /synrg-refactor |

**Commit-Specific Tool Creation:**
- New validation rule → Create/update pre-commit HOOK
- New analysis pattern → Create SUB-AGENT for that analysis type

**Full Protocol**: See `/synrg` command for complete Tool Type Decision Matrix.

---

## When to Use This Command

**Use `/synrg-commit` when:**
- ✅ You have multiple unrelated changes that should be separate commits
- ✅ You want senior-level commit messages automatically generated
- ✅ You need to ensure commits are atomic and logically organized
- ✅ You want comprehensive analysis before committing
- ✅ You have both staged and unstaged changes to organize

**Don't use `/synrg-commit` when:**
- ❌ You have a simple single-purpose change (use `git commit` directly)
- ❌ You want to manually craft very specific commit messages
- ❌ You're in the middle of a complex rebase or merge
- ❌ Your working directory is in a conflicted state

---

## Execution Overview

```
┌─────────────────────────────────────────────────────────────┐
│                  SYNRG-COMMIT Director                      │
│                                                             │
│  Phase 1: RECONNAISSANCE (Parallel Analysis)               │
│  ┌────────────┬────────────┬────────────┬────────────┐    │
│  │  Diff      │  Context   │   Intent   │  Quality   │    │
│  │ Analyzer   │   Mapper   │  Detector  │  Checker   │    │
│  └────────────┴────────────┴────────────┴────────────┘    │
│  ┌────────────┬────────────┐                               │
│  │   Impact   │   History  │                               │
│  │  Assessor  │  Analyzer  │                               │
│  └────────────┴────────────┘                               │
│            ↓                                                │
│  Phase 2: DECOMPOSITION (Director Synthesis)               │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  • Consolidate findings from all agents              │  │
│  │  • Group changes into atomic commits                 │  │
│  │  • Generate conventional commit messages             │  │
│  │  • Determine commit order (dependency graph)         │  │
│  └──────────────────────────────────────────────────────┘  │
│            ↓                                                │
│  Phase 3: VALIDATION & EXECUTION                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  • Optional: Run pre-commit validation               │  │
│  │  • Execute atomic commits sequentially               │  │
│  │  • Validate each commit success                      │  │
│  │  • Report comprehensive summary                      │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Reconnaissance Director

### Director Initialization

**Objective**: Spawn 6 specialized sub-agents in parallel to comprehensively analyze all changes with maximum context efficiency.

**Director Responsibilities**:
1. Detect current git state (unstaged, staged, untracked files)
2. Initialize 6 parallel sub-agents with isolated contexts
3. Coordinate parallel execution
4. Consolidate findings into comprehensive analysis
5. Validate completeness and fill gaps if needed

### Sub-Agent Specifications

#### Sub-Agent 1: Git Diff Analyzer

**Role**: Parse and structure git status and diff output

**Context Scope**: Git commands only (no file reads)

**Tools**: `Bash` (git commands)

**Execution**:
```bash
# Detect current git state
git status --porcelain
git diff --cached --stat
git diff --stat
git diff --cached
git diff
git ls-files --others --exclude-standard
```

**Deliverable**:
```javascript
{
  unstaged: [
    {
      file: 'src/auth/profile.ts',
      status: 'modified',
      additions: 45,
      deletions: 12,
      hunks: [
        { startLine: 23, endLine: 45, context: '...' },
        { startLine: 67, endLine: 89, context: '...' }
      ]
    }
  ],
  staged: [
    {
      file: 'src/api/routes.ts',
      status: 'modified',
      additions: 15,
      deletions: 3,
      hunks: [...]
    }
  ],
  untracked: ['src/utils/helper.ts'],
  renamed: [{ from: 'old.ts', to: 'new.ts' }],
  deleted: ['deprecated.ts'],
  totalFiles: 5,
  totalAdditions: 60,
  totalDeletions: 15
}
```

#### Sub-Agent 2: Context Mapper

**Role**: Map changed files to architectural context and dependencies

**Context Scope**: File structure, imports, module boundaries

**Tools**: `Glob`, `Grep`, `Read`

**Execution**:
```javascript
// For each changed file:
// 1. Read imports and exports
// 2. Find related files (importers, imported by)
// 3. Identify module/feature boundary
// 4. Map to architectural layers

async function mapContext(changedFiles) {
  const context = {
    changedModules: [],
    affectedFeatures: [],
    dependencyGraph: {},
    relatedFiles: []
  };

  for (const file of changedFiles) {
    // Read file to extract imports
    const imports = extractImports(await readFile(file));

    // Find files that import this file
    const importers = await findImporters(file);

    // Identify module/feature
    const module = identifyModule(file); // e.g., 'auth', 'api', 'ui'
    const feature = identifyFeature(file); // e.g., 'user-profile', 'login'

    context.changedModules.push(module);
    context.affectedFeatures.push(feature);
    context.dependencyGraph[file] = { imports, importers };
    context.relatedFiles.push(...imports, ...importers);
  }

  return context;
}
```

**Deliverable**:
```javascript
{
  changedModules: ['auth', 'api'],
  affectedFeatures: ['user-profile', 'profile-update-endpoint'],
  dependencyGraph: {
    'src/auth/profile.ts': {
      imports: ['src/types/user.ts', 'src/db/users.ts'],
      importedBy: ['src/api/routes.ts', 'src/tests/profile.test.ts']
    }
  },
  relatedFiles: [
    { file: 'src/types/user.ts', relationship: 'imports' },
    { file: 'src/api/routes.ts', relationship: 'importedBy' }
  ],
  architecturalLayers: ['data', 'business-logic', 'api']
}
```

#### Sub-Agent 3: Intent Detector

**Role**: Infer developer intent from changes

**Context Scope**: Diff content, comments, function/variable names, commit context

**Tools**: `Grep`, `Read`, `Bash`

**Execution**:
```javascript
async function detectIntent(diff, changedFiles) {
  const intent = {
    primaryIntent: null,
    intentDescription: '',
    changeRationale: '',
    breaking: false,
    changeTypes: []
  };

  // Analyze diff for clues
  const hasNewFiles = diff.untracked.length > 0;
  const hasNewTests = diff.unstaged.some(f => f.file.includes('.test.'));
  const hasNewFunctions = await detectNewFunctions(diff);
  const hasRefactoring = await detectRefactoring(diff);
  const hasBugFix = await detectBugFixPattern(diff);
  const hasDocsChanges = diff.unstaged.some(f => f.file.endsWith('.md'));

  // Classify primary intent
  if (hasNewFiles && hasNewFunctions) {
    intent.primaryIntent = 'feat';
    intent.intentDescription = await inferFeatureDescription(diff);
  } else if (hasBugFix) {
    intent.primaryIntent = 'fix';
    intent.intentDescription = await inferBugDescription(diff);
  } else if (hasRefactoring && !hasNewFunctions) {
    intent.primaryIntent = 'refactor';
    intent.intentDescription = await inferRefactoringReason(diff);
  } else if (hasDocsChanges && !hasCodeChanges) {
    intent.primaryIntent = 'docs';
  } else {
    intent.primaryIntent = 'chore';
  }

  // Check for breaking changes
  intent.breaking = await detectBreakingChanges(diff);

  // Extract rationale from comments or branch name
  intent.changeRationale = await extractRationale(diff, branchName);

  return intent;
}
```

**Deliverable**:
```javascript
{
  primaryIntent: 'feat',
  intentDescription: 'Add user profile update endpoint with validation',
  changeRationale: 'Implements user story US-123 for profile management',
  breaking: false,
  changeTypes: [
    { type: 'feat', percentage: 70 },
    { type: 'test', percentage: 20 },
    { type: 'docs', percentage: 10 }
  ],
  confidence: 0.92
}
```

#### Sub-Agent 4: Quality Checker

**Role**: Assess code quality metrics for changes

**Context Scope**: Test files, lint output, type check, security scans

**Tools**: `Bash`, `Read`, `Grep`

**Execution**:
```bash
# Run quality checks
npm run type-check 2>&1 | tee type-check.log
npm run lint 2>&1 | tee lint.log
npm run test -- --coverage 2>&1 | tee test.log

# Optional: Security scan
npm audit --production 2>&1 | tee audit.log
```

```javascript
async function checkQuality(changedFiles) {
  const quality = {
    typeErrors: 0,
    lintStatus: 'passing',
    lintWarnings: 0,
    testCoverage: { before: 0, after: 0, delta: 0 },
    testsPassing: true,
    securityIssues: [],
    qualityGatesPassed: true
  };

  // Parse type check output
  const typeCheckOutput = await runTypeCheck();
  quality.typeErrors = countTypeErrors(typeCheckOutput);

  // Parse lint output
  const lintOutput = await runLint();
  quality.lintStatus = parseLintStatus(lintOutput);
  quality.lintWarnings = countLintWarnings(lintOutput);

  // Check test coverage (if tests exist)
  const testOutput = await runTests();
  quality.testCoverage = parseTestCoverage(testOutput);
  quality.testsPassing = parseTestStatus(testOutput);

  // Security audit
  const auditOutput = await runAudit();
  quality.securityIssues = parseSecurityIssues(auditOutput);

  // Determine if quality gates pass
  quality.qualityGatesPassed = (
    quality.typeErrors === 0 &&
    quality.lintStatus !== 'errors' &&
    quality.testsPassing &&
    quality.securityIssues.filter(i => i.severity === 'high').length === 0
  );

  return quality;
}
```

**Deliverable**:
```javascript
{
  typeErrors: 0,
  lintStatus: 'passing',
  lintWarnings: 2,
  testCoverage: {
    before: 85.3,
    after: 87.1,
    delta: +1.8,
    affectedFiles: ['src/auth/profile.ts']
  },
  testsPassing: true,
  testsAdded: 3,
  securityIssues: [],
  qualityGatesPassed: true,
  recommendations: []
}
```

#### Sub-Agent 5: Impact Assessor

**Role**: Predict impact and risk of changes

**Context Scope**: API contracts, database schemas, configuration, integration points

**Tools**: `Grep`, `Read`

**Execution**:
```javascript
async function assessImpact(changedFiles, diff, context) {
  const impact = {
    breakingChanges: [],
    affectedAPIs: [],
    databaseChanges: false,
    configChanges: false,
    deploymentRisk: 'low',
    rollbackProcedure: '',
    affectedSystems: []
  };

  // Check for breaking changes
  for (const file of changedFiles) {
    // API contract changes
    if (file.includes('api/') || file.includes('routes/')) {
      const apiChanges = await analyzeAPIChanges(file, diff);
      if (apiChanges.breaking) {
        impact.breakingChanges.push(apiChanges);
      }
      impact.affectedAPIs.push(...apiChanges.endpoints);
    }

    // Database schema changes
    if (file.includes('schema') || file.includes('migration')) {
      impact.databaseChanges = true;
      impact.deploymentRisk = 'high';
    }

    // Configuration changes
    if (file.includes('config') || file.endsWith('.env')) {
      impact.configChanges = true;
    }
  }

  // Assess deployment risk
  impact.deploymentRisk = calculateDeploymentRisk({
    breakingChanges: impact.breakingChanges.length,
    databaseChanges: impact.databaseChanges,
    affectedAPIs: impact.affectedAPIs.length,
    testCoverage: context.quality.testCoverage
  });

  // Generate rollback procedure
  impact.rollbackProcedure = generateRollbackProcedure(impact);

  return impact;
}
```

**Deliverable**:
```javascript
{
  breakingChanges: [],
  affectedAPIs: [
    {
      endpoint: 'PUT /api/user/profile',
      method: 'PUT',
      changeType: 'new',
      breaking: false
    }
  ],
  databaseChanges: false,
  configChanges: false,
  deploymentRisk: 'low',
  rollbackProcedure: 'Revert commits: git revert <commit-hash>',
  affectedSystems: ['user-service', 'profile-cache'],
  estimatedDowntime: '0 minutes'
}
```

#### Sub-Agent 6: Commit History Analyzer

**Role**: Analyze recent commit patterns and conventions

**Context Scope**: Git log, commit messages, branch history

**Tools**: `Bash` (git commands)

**Execution**:
```bash
# Analyze recent commit history
git log --oneline -20
git log --format="%s" -20
git log --format="%b" -10
git branch --show-current
```

```javascript
async function analyzeCommitHistory() {
  const history = {
    usesConventionalCommits: false,
    messageFormat: '',
    commonTypes: [],
    commonScopes: [],
    averageSubjectLength: 0,
    averageBodyLength: 0,
    includesFooters: false,
    branchName: ''
  };

  // Get recent commits
  const recentCommits = await getRecentCommits(20);

  // Detect conventional commits pattern
  const conventionalPattern = /^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .+/;
  const conventionalCount = recentCommits.filter(c =>
    conventionalPattern.test(c.subject)
  ).length;
  history.usesConventionalCommits = conventionalCount / recentCommits.length > 0.7;

  // Extract common types and scopes
  if (history.usesConventionalCommits) {
    history.commonTypes = extractCommonTypes(recentCommits);
    history.commonScopes = extractCommonScopes(recentCommits);
    history.messageFormat = 'type(scope): subject';
  }

  // Calculate average lengths
  history.averageSubjectLength = calculateAverage(
    recentCommits.map(c => c.subject.length)
  );

  // Check if bodies and footers are common
  history.averageBodyLength = calculateAverage(
    recentCommits.map(c => c.body.length)
  );
  history.includesFooters = recentCommits.some(c => c.footer);

  // Get current branch
  history.branchName = await getCurrentBranch();

  return history;
}
```

**Deliverable**:
```javascript
{
  usesConventionalCommits: true,
  messageFormat: 'type(scope): subject',
  commonTypes: ['feat', 'fix', 'refactor', 'test'],
  commonScopes: ['auth', 'api', 'ui', 'db'],
  averageSubjectLength: 48,
  averageBodyLength: 120,
  includesFooters: false,
  branchName: 'feature/user-profile-update',
  recentCommitPatterns: [
    'feat(auth): add user profile endpoint',
    'test(auth): add profile update tests',
    'fix(api): correct validation logic'
  ]
}
```

### Reconnaissance Consolidation

**Director Task**: Merge all sub-agent findings into comprehensive analysis

```javascript
async function consolidateReconnaissance(agentReports) {
  const consolidated = {
    // From git-diff-analyzer
    changes: agentReports.find(r => r.agentId === 'git-diff-analyzer').findings,

    // From context-mapper
    context: agentReports.find(r => r.agentId === 'context-mapper').findings,

    // From intent-detector
    intent: agentReports.find(r => r.agentId === 'intent-detector').findings,

    // From quality-checker
    quality: agentReports.find(r => r.agentId === 'quality-checker').findings,

    // From impact-assessor
    impact: agentReports.find(r => r.agentId === 'impact-assessor').findings,

    // From commit-history-analyzer
    conventions: agentReports.find(r => r.agentId === 'commit-history-analyzer').findings,

    // Metadata
    reconnaissanceMetadata: {
      totalAgents: agentReports.length,
      averageConfidence: calculateAverageConfidence(agentReports),
      timestamp: Date.now(),
      completeness: validateCompleteness(agentReports)
    }
  };

  // Cross-validate findings
  consolidated.crossValidation = crossValidateFindings(agentReports);

  return consolidated;
}
```

---

## Phase 2: Commit Decomposition Director

### Objective

Synthesize reconnaissance findings and decompose changes into atomic, logical commits with senior-level commit messages.

### Atomic Commit Principles

**A commit is atomic if**:
1. ✅ It has a single, clear purpose
2. ✅ It can be reverted independently
3. ✅ It builds and passes tests (if tests exist)
4. ✅ It doesn't break the application
5. ✅ It's the smallest meaningful unit of change

### Decomposition Algorithm

```javascript
async function decomposeIntoAtomicCommits(reconnaissance) {
  const { changes, context, intent, quality, impact, conventions } = reconnaissance;

  // STEP 1: Group changes by logical boundaries
  const groups = [];

  // Strategy 1: Group by feature/module
  const featureGroups = groupByFeature(changes, context);
  groups.push(...featureGroups);

  // Strategy 2: Group by intent
  const intentGroups = groupByIntent(changes, intent);
  groups.push(...intentGroups);

  // Strategy 3: Separate test changes from implementation
  const testGroups = separateTests(changes);
  groups.push(...testGroups);

  // Strategy 4: Separate documentation from code
  const docGroups = separateDocs(changes);
  groups.push(...docGroups);

  // STEP 2: Merge overlapping groups
  const mergedGroups = mergeOverlappingGroups(groups);

  // STEP 3: Validate atomicity of each group
  const atomicGroups = mergedGroups.filter(group =>
    validateAtomicity(group, context)
  );

  // STEP 4: Determine commit order (dependency graph)
  const orderedGroups = topologicalSort(atomicGroups, context.dependencyGraph);

  // STEP 5: Generate commit message for each group
  const commits = orderedGroups.map((group, index) => ({
    id: `commit-${index + 1}`,
    files: group.files,
    message: generateCommitMessage(group, reconnaissance),
    dependencies: group.dependencies,
    estimatedImpact: group.impact,
    atomic: true
  }));

  return commits;
}
```

### Commit Message Generation

**Format**: Conventional Commits Specification

```javascript
function generateCommitMessage(group, reconnaissance) {
  const { intent, conventions, context, impact } = reconnaissance;

  // HEADER: type(scope): subject
  const type = inferCommitType(group, intent);
  const scope = inferScope(group.files, context, conventions);
  const subject = generateSubject(group, intent, 50); // max 50 chars

  // BODY: What, Why, How
  const body = generateBody({
    what: describeChanges(group.files, group.diff),
    why: explainRationale(intent, group),
    how: describeImplementation(group, context),
    impact: summarizeImpact(impact, group)
  });

  // FOOTER: Breaking changes, issues, references
  const footer = [];

  if (impact.breakingChanges.length > 0) {
    footer.push(`BREAKING CHANGE: ${describeBreakingChange(impact)}`);
  }

  // Extract issue references from branch or comments
  const issues = extractIssueReferences(conventions.branchName, group.comments);
  if (issues.length > 0) {
    footer.push(`Refs: ${issues.join(', ')}`);
  }

  // Add co-author attribution
  footer.push('🤖 Generated with SYNRG-COMMIT');
  footer.push('Co-Authored-By: Claude <noreply@anthropic.com>');

  // Assemble full message
  const header = `${type}(${scope}): ${subject}`;
  const fullBody = body.trim();
  const fullFooter = footer.join('\n');

  return {
    header,
    body: fullBody,
    footer: fullFooter,
    full: `${header}\n\n${fullBody}\n\n${fullFooter}`.trim()
  };
}
```

### Commit Type Inference

```javascript
function inferCommitType(group, intent) {
  const files = group.files;

  // Priority 1: Use detected intent
  if (intent.primaryIntent && intent.confidence > 0.8) {
    return intent.primaryIntent;
  }

  // Priority 2: Infer from file patterns
  if (files.every(f => f.includes('.test.') || f.includes('.spec.'))) {
    return 'test';
  }

  if (files.every(f => f.endsWith('.md') || f.includes('/docs/'))) {
    return 'docs';
  }

  if (files.some(f => f.includes('package.json') || f.includes('config'))) {
    return 'chore';
  }

  // Priority 3: Analyze diff content
  const hasNewFunctions = group.diff.additions > group.diff.deletions * 2;
  const hasRefactoring = group.diff.additions === group.diff.deletions;

  if (hasNewFunctions) {
    return 'feat';
  }

  if (hasRefactoring) {
    return 'refactor';
  }

  // Default
  return 'chore';
}
```

### Scope Inference

```javascript
function inferScope(files, context, conventions) {
  // Priority 1: Use common scopes from history
  if (conventions.commonScopes.length > 0) {
    const detectedScope = detectScopeFromPath(files[0], conventions.commonScopes);
    if (detectedScope) return detectedScope;
  }

  // Priority 2: Use module/feature from context
  if (context.changedModules.length === 1) {
    return context.changedModules[0];
  }

  if (context.affectedFeatures.length === 1) {
    return context.affectedFeatures[0];
  }

  // Priority 3: Extract from file path
  const pathSegments = files[0].split('/');
  if (pathSegments.length > 1) {
    return pathSegments[1]; // e.g., src/auth/profile.ts -> auth
  }

  // Default: no scope
  return '';
}
```

### Subject Generation

```javascript
function generateSubject(group, intent, maxLength = 50) {
  let subject = '';

  // Start with intent description if available
  if (intent.intentDescription) {
    subject = intent.intentDescription.toLowerCase();
  } else {
    // Generate from file changes
    const action = inferAction(group.diff);
    const target = inferTarget(group.files);
    subject = `${action} ${target}`;
  }

  // Truncate to max length
  if (subject.length > maxLength) {
    subject = subject.substring(0, maxLength - 3) + '...';
  }

  // Ensure starts with lowercase verb
  subject = subject.charAt(0).toLowerCase() + subject.slice(1);

  // Remove trailing period
  subject = subject.replace(/\.$/, '');

  return subject;
}
```

### Body Generation

```javascript
function generateBody({ what, why, how, impact }) {
  const sections = [];

  // WHAT: Describe the changes
  if (what) {
    sections.push(`**What**: ${what}`);
  }

  // WHY: Explain the rationale
  if (why) {
    sections.push(`**Why**: ${why}`);
  }

  // HOW: Describe implementation approach
  if (how) {
    sections.push(`**How**: ${how}`);
  }

  // IMPACT: Summarize impact
  if (impact && impact !== 'No significant impact') {
    sections.push(`**Impact**: ${impact}`);
  }

  return sections.join('\n\n');
}
```

---

## Phase 3: Validation & Execution Director

### Pre-Commit Validation (Optional)

```javascript
async function runPreCommitValidation(commits, quality) {
  const validation = {
    testsPass: quality.testsPassing,
    lintPass: quality.lintStatus !== 'errors',
    typeCheckPass: quality.typeErrors === 0,
    securityPass: quality.securityIssues.filter(i => i.severity === 'critical').length === 0,
    buildPass: true, // Optional: run build
    allGatesPassed: false
  };

  // Run build if configured
  if (shouldRunBuild()) {
    const buildResult = await runBuild();
    validation.buildPass = buildResult.success;
  }

  validation.allGatesPassed = Object.values(validation).every(v => v === true);

  if (!validation.allGatesPassed) {
    return {
      canProceed: false,
      validation,
      blockers: identifyBlockers(validation)
    };
  }

  return {
    canProceed: true,
    validation
  };
}
```

### Commit Execution

```javascript
async function executeAtomicCommits(commits, options = {}) {
  const results = {
    successful: [],
    failed: [],
    skipped: [],
    totalCommits: commits.length
  };

  // Create safety backup
  const backupBranch = await createBackupBranch();

  try {
    for (const commit of commits) {
      console.log(`\n📝 Executing Commit ${commit.id}/${commits.length}`);
      console.log(`   Type: ${commit.message.header}`);
      console.log(`   Files: ${commit.files.length} file(s)`);

      // Stage files for this commit
      await stageFiles(commit.files);

      // Create commit with generated message
      const commitResult = await executeGitCommit(commit.message.full);

      if (commitResult.success) {
        results.successful.push({
          commitId: commit.id,
          hash: commitResult.hash,
          message: commit.message.header,
          files: commit.files
        });
        console.log(`   ✅ Success: ${commitResult.hash.substring(0, 7)}`);
      } else {
        results.failed.push({
          commitId: commit.id,
          error: commitResult.error,
          files: commit.files
        });
        console.log(`   ❌ Failed: ${commitResult.error}`);

        // Rollback on failure (optional)
        if (options.rollbackOnFailure) {
          await rollbackToBackup(backupBranch);
          break;
        }
      }
    }

    // Success - can delete backup
    if (results.failed.length === 0) {
      await deleteBackupBranch(backupBranch);
    }

  } catch (error) {
    // Critical error - rollback
    console.error(`\n❌ Critical error during commit execution: ${error.message}`);
    await rollbackToBackup(backupBranch);
    throw error;
  }

  return results;
}
```

### Git Operations

```javascript
async function stageFiles(files) {
  for (const file of files) {
    await executeGit(['add', file]);
  }
}

async function executeGitCommit(message) {
  try {
    // Use heredoc for proper message formatting
    const result = await executeGit([
      'commit',
      '-m',
      message
    ]);

    // Extract commit hash
    const hash = extractCommitHash(result.stdout);

    return {
      success: true,
      hash,
      stdout: result.stdout
    };
  } catch (error) {
    return {
      success: false,
      error: error.message
    };
  }
}

async function createBackupBranch() {
  const branchName = `synrg-commit-backup-${Date.now()}`;
  await executeGit(['branch', branchName]);
  return branchName;
}

async function rollbackToBackup(backupBranch) {
  await executeGit(['reset', '--hard', backupBranch]);
  await executeGit(['branch', '-D', backupBranch]);
}

async function deleteBackupBranch(backupBranch) {
  await executeGit(['branch', '-D', backupBranch]);
}
```

---

## Execution Protocol

### Interactive Mode (Default)

```javascript
async function executeSynrgCommit(options = {}) {
  console.log('🚀 SYNRG-COMMIT: Intelligent Atomic Commit Orchestrator\n');

  // PHASE 1: Reconnaissance
  console.log('Phase 1: Reconnaissance (Parallel Sub-Agents)');
  const reconnaissance = await executeReconnaissance();
  console.log(`✅ Analysis complete (${reconnaissance.reconnaissanceMetadata.totalAgents} agents)\n`);

  // PHASE 2: Decomposition
  console.log('Phase 2: Commit Decomposition');
  const commits = await decomposeIntoAtomicCommits(reconnaissance);
  console.log(`✅ Decomposed into ${commits.length} atomic commits\n`);

  // Display proposed commits
  displayProposedCommits(commits);

  // Ask for user approval (interactive mode)
  if (!options.autoApprove) {
    const approved = await askForApproval();
    if (!approved) {
      console.log('\n❌ Commit execution cancelled by user');
      return { cancelled: true };
    }
  }

  // PHASE 3: Validation & Execution
  console.log('\nPhase 3: Validation & Execution');

  // Optional: Pre-commit validation
  if (options.runValidation) {
    console.log('Running pre-commit validation...');
    const validation = await runPreCommitValidation(commits, reconnaissance.quality);
    if (!validation.canProceed) {
      console.log('\n❌ Pre-commit validation failed');
      console.log('Blockers:', validation.blockers);
      return { failed: true, validation };
    }
    console.log('✅ Pre-commit validation passed\n');
  }

  // Execute commits
  const results = await executeAtomicCommits(commits, options);

  // Display summary
  displayExecutionSummary(results);

  return results;
}
```

### Display Functions

```javascript
function displayProposedCommits(commits) {
  console.log('\n' + '='.repeat(70));
  console.log('PROPOSED ATOMIC COMMITS');
  console.log('='.repeat(70) + '\n');

  commits.forEach((commit, index) => {
    console.log(`Commit ${index + 1}/${commits.length}`);
    console.log(`┌─ ${commit.message.header}`);
    console.log(`├─ Files (${commit.files.length}):`);
    commit.files.forEach(f => console.log(`│  - ${f}`));
    console.log(`└─ Impact: ${commit.estimatedImpact}`);
    console.log('');
  });

  console.log('='.repeat(70) + '\n');
}

function displayExecutionSummary(results) {
  console.log('\n' + '='.repeat(70));
  console.log('EXECUTION SUMMARY');
  console.log('='.repeat(70) + '\n');

  console.log(`Total Commits: ${results.totalCommits}`);
  console.log(`✅ Successful: ${results.successful.length}`);
  console.log(`❌ Failed: ${results.failed.length}`);
  console.log(`⏭️  Skipped: ${results.skipped.length}\n`);

  if (results.successful.length > 0) {
    console.log('Successful Commits:');
    results.successful.forEach(c => {
      console.log(`  ${c.hash.substring(0, 7)} - ${c.message}`);
    });
  }

  if (results.failed.length > 0) {
    console.log('\nFailed Commits:');
    results.failed.forEach(c => {
      console.log(`  ${c.commitId} - ${c.error}`);
    });
  }

  console.log('\n' + '='.repeat(70) + '\n');
}
```

---

## Error Handling & Rollback

### Error Classification

```javascript
async function handleCommitError(error, context) {
  // Classify error type
  const errorType = classifyError(error);

  switch (errorType) {
    case 'MERGE_CONFLICT':
      return {
        action: 'abort',
        message: 'Merge conflict detected. Resolve conflicts manually.',
        rollback: true
      };

    case 'PRE_COMMIT_HOOK_FAILED':
      return {
        action: 'fix',
        message: 'Pre-commit hook failed. Fix issues and retry.',
        rollback: false,
        suggestion: analyzePrecomiitHookFailure(error)
      };

    case 'GIT_PERMISSION_ERROR':
      return {
        action: 'escalate',
        message: 'Git permission error. Check repository permissions.',
        rollback: false
      };

    case 'EMPTY_COMMIT':
      return {
        action: 'skip',
        message: 'No changes to commit.',
        rollback: false
      };

    default:
      return {
        action: 'escalate',
        message: `Unknown error: ${error.message}`,
        rollback: true
      };
  }
}
```

### Rollback Procedures

```javascript
async function rollbackCommits(commits, backupBranch) {
  console.log('\n🔄 Rolling back commits...');

  try {
    // Reset to backup branch
    await executeGit(['reset', '--hard', backupBranch]);
    console.log('✅ Rollback successful');

    // Clean up backup branch
    await executeGit(['branch', '-D', backupBranch]);

    return { success: true };
  } catch (error) {
    console.error('❌ Rollback failed:', error.message);
    console.log(`\n⚠️  Manual recovery required:`);
    console.log(`   git reset --hard ${backupBranch}`);
    console.log(`   git branch -D ${backupBranch}`);

    return { success: false, error };
  }
}
```

---

## Configuration & Options

### Command Options

```javascript
const defaultOptions = {
  // Execution mode
  autoApprove: false,           // Skip approval prompt
  dryRun: false,                // Preview commits without executing

  // Validation
  runValidation: false,         // Run pre-commit validation
  requireTests: false,          // Require tests to pass
  requireLint: false,           // Require lint to pass
  requireTypeCheck: false,      // Require type check to pass

  // Commit message
  messageFormat: 'conventional', // 'conventional' | 'simple' | 'detailed'
  includeBody: true,            // Include commit body
  includeFooter: true,          // Include commit footer
  maxSubjectLength: 50,         // Max subject line length

  // Decomposition
  minCommitSize: 1,             // Minimum files per commit
  maxCommitSize: 10,            // Maximum files per commit
  separateTests: true,          // Separate test changes
  separateDocs: true,           // Separate documentation

  // Safety
  createBackup: true,           // Create backup branch
  rollbackOnFailure: true,      // Rollback on any failure
  allowEmptyCommits: false,     // Allow commits with no changes

  // Analysis depth
  analysisDepth: 'deep',        // 'quick' | 'medium' | 'deep'
  contextWindow: 'full'         // 'minimal' | 'medium' | 'full'
};
```

### Usage Examples

```bash
# Basic usage (interactive mode)
/synrg-commit

# Auto-approve mode (skip confirmation)
/synrg-commit --auto-approve

# Dry run (preview only)
/synrg-commit --dry-run

# With pre-commit validation
/synrg-commit --run-validation

# Custom message format
/synrg-commit --message-format=detailed --max-subject-length=72
```

---

## Best Practices & Guidelines

### When to Use Atomic Commits

✅ **DO use atomic commits when:**
- Each commit represents a complete, logical unit of work
- Commits can be reviewed independently
- Commits can be cherry-picked to other branches
- Each commit tells a clear story in the git history

❌ **DON'T create atomic commits that:**
- Break the build or tests
- Are so small they have no meaning
- Mix unrelated changes
- Create unnecessary noise in history

### Commit Message Best Practices

✅ **DO write commit messages that:**
- Use imperative mood ("add feature" not "added feature")
- Start with a lowercase letter after type/scope
- Keep subject line under 50 characters
- Include comprehensive body explaining what/why/how
- Reference related issues or tickets

❌ **DON'T write commit messages that:**
- Are vague ("fix bug", "update code")
- Include implementation details in subject
- Use past tense or present continuous
- Exceed character limits without reason

### Git Workflow Integration

**Works well with:**
- Feature branch workflow
- Git Flow
- GitHub Flow
- Trunk-based development

**Integrates with:**
- Pre-commit hooks (husky, lint-staged)
- CI/CD pipelines
- Code review tools
- Commit linting (commitlint)

---

## Troubleshooting

### Common Issues

**Issue**: "No changes to commit"
- **Cause**: All changes are already committed
- **Solution**: Check `git status` to verify changes exist

**Issue**: "Pre-commit hook failed"
- **Cause**: Quality gates not passing
- **Solution**: Fix lint/test/type errors before committing

**Issue**: "Merge conflict detected"
- **Cause**: Working directory has unresolved conflicts
- **Solution**: Resolve conflicts manually before using synrg-commit

**Issue**: "Git permission error"
- **Cause**: Insufficient permissions for repository
- **Solution**: Check repository access and SSH keys

**Issue**: "Commit decomposition created too many commits"
- **Cause**: Very granular changes detected
- **Solution**: Use `--max-commits` option or `--min-commit-size`

---

## Version History

### v1.0.0 (2025-11-02) - Initial Release

**Core Features**:
- ✅ Director/orchestrator pattern with 6 parallel sub-agents
- ✅ Intelligent change analysis (git diff, context, intent, quality, impact, history)
- ✅ Atomic commit decomposition algorithm
- ✅ Conventional commit message generation
- ✅ Fully automatic git execution
- ✅ Pre-commit validation (optional)
- ✅ Comprehensive error handling and rollback
- ✅ Interactive and auto-approve modes
- ✅ Dry-run capability

**Sub-Agents**:
1. git-diff-analyzer - Parse git status and diffs
2. context-mapper - Map architectural context
3. intent-detector - Infer developer intent
4. quality-checker - Assess code quality
5. impact-assessor - Predict change impact
6. commit-history-analyzer - Analyze commit patterns

**Philosophy**: SYNRG v3.0 Robustness-First
- Comprehensive analysis over speed
- Context efficiency through parallelization
- Production-grade error handling
- Senior-level commit quality

---

## Future Enhancements

**Planned Features**:
- 🔮 AI-powered commit message improvement suggestions
- 🔮 Interactive commit message editing
- 🔮 Support for squashing/amending recent commits
- 🔮 Integration with GitHub/GitLab for PR templates
- 🔮 Commit template customization per project
- 🔮 Support for conventional commit scopes auto-detection
- 🔮 Integration with JIRA/Linear for ticket references
- 🔮 Commit message translation for international teams

---

## Support & Documentation

**Command Help**: `/synrg-commit --help`

**Examples Directory**: `${CLAUDE_COMMANDS}/examples/synrg-commit/`

**Related Commands**:
- `/synrg` - Main SYNRG orchestrator
- `/synrg-evolve` - Self-evolution integration
- `/synrg-refactor` - Intelligent file restructuring
- `/synrg-swarm` - Sub-agent development

**Feedback**: Report issues or suggestions via SYNRG evolution protocol

---

**Remember**: This command embodies SYNRG v3.0 robustness-first philosophy. Every commit is analyzed comprehensively, decomposed intelligently, and executed with production-grade safety mechanisms. The goal is not just to commit changes, but to create a clear, reviewable, and maintainable git history that tells the story of your codebase evolution.

🤖 **Generated with SYNRG v3.0 - Robustness-First, Production-Grade Multi-Agent Coordination**
