---
description: Execute SYNRG Spec-Driven Development - Progressive refinement from constitution to implementation with mandatory phase gating
argument-hint: [init|specify|clarify|plan|tasks|implement|status|continue] [objective or feature name]
---

# SYNRG Spec-Driven Development Command
## Progressive Refinement Pipeline with Mandatory Phase Gating

You are executing the SYNRG Spec-Driven Development (SDD) Protocol - a methodology where executable specifications directly generate working implementations through a controlled 6-phase progressive refinement pipeline.

**Core Philosophy**: "Never implement without specification. Every implementation flows from specs through controlled refinement phases that cannot be skipped."

**Adapted From**: GitHub's spec-kit methodology, translated to SYNRG principles.

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
│  SPEC-SPECIFIC: Spec document reads MUST be delegated to sub-agents         │
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

## 🔒 UNIVERSAL SYNRG PROTOCOLS (USP v1.0 - Compact)

**All gates apply. Full specs: `~/.claude/skills/universal-synrg-protocols.md`**

### PRE-IMPLEMENTATION GATES
```
GATE 1: ANTI-MEMORY    - READ files, don't trust memory
GATE 2: GIT_STRATEGY   - Use --branch flag for auto-branch creation
GATE 3: CERTAINTY      - Spec-driven = high certainty, but verify implementations
GATE 4: SECURITY       - Security review in each phase
GATE 5: USER_VERIFY    - Phase gating provides natural checkpoints
```

### POST-IMPLEMENTATION REVIEWS
```
REVIEW 1: OBJECTIVE    - Spec fully implemented? All tests pass?
REVIEW 2: SECURITY     - Security audit of implementation
REVIEW 3: DOCS (P5)    - Spec IS the documentation, ensure consistency
REVIEW 4: COMMIT       - Use /synrg-commit for atomic commits
REVIEW 5: QUALITY      - All phases passed → COMPLETE
```

---

## 🔴 CRITICAL: Phase Gating Protocol (MANDATORY)

**The 7 phases MUST execute in order. No phase can be skipped.**

```
┌─────────────────────────────────────────────────────────────────────┐
│  PHASE PROGRESSION (MANDATORY ORDER - NO EXCEPTIONS)                │
│                                                                     │
│  1. CONSTITUTION  →  Define immutable principles (9 Articles)       │
│         ↓ (requires: nothing)                                       │
│  2. SPECIFY       →  Generate detailed specification                │
│         ↓ (requires: constitution.md complete)                      │
│  3. CLARIFY       →  Resolve all ambiguities via Q&A                │
│         ↓ (requires: spec.md complete)                              │
│  4. PLAN          →  Generate implementation plan                   │
│         ↓ (requires: clarifications.md complete, 0 pending)         │
│  5. TASKS         →  Break plan into atomic tasks + test specs      │
│         ↓ (requires: plan.md complete)                              │
│  6. TESTS (RED)   →  Write tests, confirm they FAIL                 │
│         ↓ (requires: tasks.md ready, Article III enforcement)       │
│  7. IMPLEMENT     →  Make tests pass (GREEN), then refactor         │
│         ↓ (requires: tests.md with RED confirmation)                │
│  ✓ COMPLETE       →  All tests GREEN, feature implemented           │
└─────────────────────────────────────────────────────────────────────┘
```

**Test-First Flow (Article III)**:
```
TASKS → TESTS (write) → RED (confirm fail) → IMPLEMENT → GREEN (confirm pass) → REFACTOR
```

**Test Execution Order (Article IX)**:
```
1. Contract Tests    → Define API boundaries
2. Integration Tests → Verify system interactions
3. E2E Tests         → Validate user flows
4. Unit Tests        → Verify individual functions
```

**Phase Gate Validation**: Before entering ANY phase, validate that:
1. Previous phase artifact exists
2. Previous phase status is "complete" or "ready"
3. No pending items from previous phase
4. For IMPLEMENT phase: tests.md must show RED (failing tests confirmed)

---

## 🧠 CLAUDE TOOL SELECTION PROTOCOL (Reference: /synrg)

**For each phase, select the optimal Claude tool type:**

| Phase | Recommended Tool Type | Rationale |
|-------|----------------------|-----------|
| CONSTITUTION | DIRECT | One-time setup |
| SPECIFY | SUB-AGENT | Large spec generation |
| CLARIFY | DIRECT | Interactive Q&A |
| PLAN | SUB-AGENT | Parallel analysis |
| TASKS | SUB-AGENT | Task decomposition |
| TESTS | SUB-AGENT | Test generation |
| IMPLEMENT | SUB-AGENT + SLASH COMMAND | May chain /synrg-refactor |

**Spec-Driven Tool Creation:**
- Recurring spec patterns → Create SKILL for spec methodology
- Automated validation → Create HOOK for spec compliance
- Domain-specific specs → Create SUB-AGENT for that domain

**Full Protocol**: See `/synrg` command for complete Tool Type Decision Matrix

---

## Regeneration Triggers (Cascade Protocol)

When an upstream artifact changes, downstream artifacts may become stale. This protocol defines automatic regeneration behavior.

### Trigger Matrix

| Changed Artifact | Triggers Regeneration Of |
|------------------|--------------------------|
| `constitutional-articles.md` | ALL artifacts (full cascade) |
| `spec.md` (scope change) | `clarifications.md` → `plan.md` → `tasks.md` → `tests.md` |
| `spec.md` (detail only) | Validate only, no cascade |
| `clarifications.md` | `plan.md` → `tasks.md` → `tests.md` |
| `plan.md` (architecture) | `tasks.md` → `tests.md` |
| `plan.md` (task order only) | `tasks.md` only |
| `tasks.md` | `tests.md` (for affected tasks only) |
| `research.md` | Advisory only - flag for review |
| `data-model.md` | `contracts/*.yaml` → `tests.md` (contract tests only) |

### Hash-Based Change Detection

Each artifact stores a hash of its upstream dependencies:

```yaml
# In plan.md frontmatter
---
upstream_hashes:
  spec: "sha256-abc123..."
  clarifications: "sha256-def456..."
status: "valid"  # or "stale" if hashes mismatch
---
```

**Staleness Check Algorithm**:
```javascript
function checkStaleness(artifact) {
  const currentHashes = artifact.upstream_hashes;
  for (const [upstream, storedHash] of Object.entries(currentHashes)) {
    const actualHash = computeHash(readArtifact(upstream));
    if (actualHash !== storedHash) {
      return { stale: true, reason: `${upstream} has changed` };
    }
  }
  return { stale: false };
}
```

### Cascade Modes

| Mode | Behavior | Use When |
|------|----------|----------|
| `full` | Regenerate all downstream artifacts | Constitutional changes, major scope shifts |
| `incremental` | Only regenerate stale artifacts | Normal development flow |
| `validate` | Check staleness, report but don't regenerate | Pre-commit validation |
| `force` | Regenerate regardless of hash | Manual override, corruption recovery |

### Subcommand: `regenerate`

```bash
/synrg-spec regenerate [mode] [feature-name]

# Examples:
/synrg-spec regenerate incremental user-auth   # Only stale artifacts
/synrg-spec regenerate full user-auth          # Everything from spec down
/synrg-spec regenerate validate user-auth      # Check only, no changes
```

**Implementation**:
```javascript
// When regenerate is invoked
if (subcommand === "regenerate") {
  const mode = args[0] || "incremental";
  const feature = args[1];

  const staleness = checkAllArtifacts(feature);

  if (mode === "validate") {
    return reportStaleness(staleness);
  }

  if (mode === "full") {
    // Regenerate cascade: spec → clarify → plan → tasks → tests
    await runPhase("specify", feature);
    await runPhase("clarify", feature);
    await runPhase("plan", feature);
    await runPhase("tasks", feature);
    await runPhase("tests", feature);
  }

  if (mode === "incremental") {
    for (const staleArtifact of staleness.staleList) {
      await regenerateArtifact(staleArtifact, feature);
    }
  }
}
```

### Auto-Staleness Warnings

When any phase runs, it first checks upstream hashes:

```
⚠️ STALE ARTIFACT DETECTED
   clarifications.md has changed since plan.md was generated

   Options:
   1. /synrg-spec regenerate incremental {feature} - Update plan.md
   2. /synrg-spec continue - Proceed anyway (not recommended)
   3. /synrg-spec status - View full staleness report
```

---

## 🔴 MANDATORY: Sub-Agent Delegation Protocol (v4.3)

**BEFORE any phase execution, CHECK for real Claude Code agents:**

```
┌─────────────────────────────────────────────────────────────────────┐
│  SUB-AGENT DELEGATION CHECK (MANDATORY)                             │
│                                                                     │
│  1. IDENTIFY: Is this task delegatable to a focused agent?          │
│  2. MATCH: Check ~/.claude/agents/ for qualified agents             │
│  3. CREATE: If no match exists, create the agent first              │
│  4. DELEGATE: Use Task tool with specific agent type                │
└─────────────────────────────────────────────────────────────────────┘
```

### Real Delegation (Not Pseudocode)

```javascript
// Use Task tool for actual delegation
Task({
  subagent_type: "general-purpose",
  prompt: "[Phase-specific task with full context]",
  model: "haiku"  // haiku for focused tasks, sonnet for complex
})
```

---

## Command Syntax

```bash
/synrg-spec [subcommand] [objective or feature name]

# Subcommands:
  init        Initialize new spec (creates structure + constitutional articles)
  specify     Generate detailed specification from objective
  clarify     Run clarification Q&A cycle
  plan        Generate implementation plan from spec + clarifications
  analyze     Cross-validate all artifacts for consistency (optional but recommended)
  tasks       Break plan into atomic tasks WITH test specifications
  tests       Generate and validate tests (RED phase - tests must FAIL)
  implement   Execute tasks via SYNRG Director (GREEN phase - make tests pass)
  status      Show current phase and progress for active spec
  continue    Auto-detect current phase and proceed to next
  checklist   Generate quality validation checklist for current phase
  regenerate  Refresh stale artifacts (modes: incremental|full|validate|force)

# Flags:
  --brownfield    Enable brownfield mode (existing codebase analysis)
  --branch        Auto-generate feature branch name
```

### Usage Examples

```bash
# Start a new feature spec
/synrg-spec init user-authentication

# Generate specification for the feature
/synrg-spec specify user-authentication

# Run clarification cycle
/synrg-spec clarify user-authentication

# Generate implementation plan
/synrg-spec plan user-authentication

# Break into tasks
/synrg-spec tasks user-authentication

# Execute implementation
/synrg-spec implement user-authentication

# Check current status
/synrg-spec status user-authentication

# Auto-continue from current phase
/synrg-spec continue user-authentication

# Brownfield mode: enhance existing feature
/synrg-spec init --brownfield improve-checkout-performance

# Create feature branch automatically
/synrg-spec init --branch payment-gateway-v2
```

---

## Brownfield Mode (Existing Codebase Enhancement)

When working with existing codebases, use `--brownfield` flag to activate analysis-first workflow.

### Brownfield vs Greenfield

| Aspect | Greenfield | Brownfield |
|--------|------------|------------|
| Starting point | Empty project | Existing code |
| Constitution | Created fresh | Inferred from codebase |
| Specification | Define from scratch | Gap analysis against existing |
| Constraints | Architecture decisions | Preserve compatibility |
| Testing | All new tests | Extend existing test suite |
| Risk | Lower (no legacy) | Higher (regression risk) |

### Brownfield Workflow

```
1. ANALYZE → Scan existing codebase for patterns, conventions, tests
2. AUDIT   → Identify what exists, what's missing, what conflicts
3. INIT    → Create spec constrained by existing architecture
4. SPECIFY → Define enhancement scope with compatibility checks
5. [Standard flow continues...]
```

### Brownfield Init Execution

```javascript
async function executeBrownfieldInit(specDir, objective) {
  // 1. Analyze existing codebase
  const codebaseAnalysis = await Task({
    subagent_type: "Explore",
    prompt: `Analyze this codebase to understand:
1. Project structure and conventions
2. Existing patterns (architecture, naming, testing)
3. Technology stack and dependencies
4. Test coverage and testing patterns
5. API contracts and integrations
6. Configuration and environment patterns

Focus on areas relevant to: ${objective}

Return structured analysis with:
- existingPatterns: []
- conventions: {}
- dependencies: []
- testingApproach: {}
- integrationPoints: []`,
    model: "sonnet"
  });

  // 2. Infer constitutional constraints
  const inferredConstitution = await Task({
    subagent_type: "general-purpose",
    prompt: `Based on this codebase analysis, infer constitutional articles that MUST be preserved:

CODEBASE ANALYSIS:
${JSON.stringify(codebaseAnalysis, null, 2)}

Generate constitutional articles that:
1. Preserve existing architectural patterns
2. Maintain backward compatibility
3. Follow established conventions
4. Extend (don't replace) existing test patterns
5. Respect existing API contracts

Mark each article with: [INFERRED] or [REQUIRED]`,
    model: "sonnet"
  });

  // 3. Gap analysis
  const gapAnalysis = await Task({
    subagent_type: "general-purpose",
    prompt: `Perform gap analysis for objective: ${objective}

EXISTING CODEBASE:
${JSON.stringify(codebaseAnalysis, null, 2)}

Identify:
1. What already exists that can be reused
2. What needs to be modified (with compatibility notes)
3. What needs to be created new
4. Potential conflicts with existing code
5. Regression risks

Output as structured gap analysis.`,
    model: "sonnet"
  });

  // 4. Write brownfield-aware artifacts
  await writeFile(`${specDir}/codebase-analysis.md`, formatAnalysis(codebaseAnalysis));
  await writeFile(`${specDir}/gap-analysis.md`, formatGapAnalysis(gapAnalysis));
  await writeFile(`${specDir}/constitution.md`, inferredConstitution);

  return {
    success: true,
    mode: 'brownfield',
    artifacts: ['codebase-analysis.md', 'gap-analysis.md', 'constitution.md']
  };
}
```

### Additional Brownfield Artifacts

```
specs/NNN-feature-name/
├── codebase-analysis.md   # Existing code patterns (brownfield only)
├── gap-analysis.md        # What exists vs what's needed (brownfield only)
├── constitution.md        # Includes [INFERRED] articles
└── ...
```

### codebase-analysis.md Template

```markdown
---
feature: "{featureName}"
document: "codebase-analysis"
mode: "brownfield"
created: "{timestamp}"
scan_scope: "{directories scanned}"
---

# Codebase Analysis: {featureName}

## Project Structure

```
[Existing directory structure relevant to feature]
```

## Existing Patterns

### Architectural Patterns
| Pattern | Location | Impact on Feature |
|---------|----------|-------------------|
| [Pattern] | [Where used] | [How it affects our work] |

### Naming Conventions
| Element | Convention | Example |
|---------|------------|---------|
| Files | [pattern] | `user.service.ts` |
| Functions | [pattern] | `getUserById()` |
| Variables | [pattern] | `userCount` |

### Testing Patterns
- Test framework: [Jest/Mocha/etc]
- Test location: [__tests__/spec/etc]
- Naming: [*.test.ts/*.spec.ts]
- Coverage tool: [tool]

---

## Dependencies

### Direct Dependencies (package.json)
| Package | Version | Purpose |
|---------|---------|---------|
| [pkg] | [ver] | [why used] |

### Relevant to Feature
| Dependency | How It Affects Us |
|------------|-------------------|
| [dep] | [impact] |

---

## Integration Points

| Integration | Type | Contract Location |
|-------------|------|-------------------|
| [API/Service] | [REST/GraphQL/etc] | [path to contract] |

---

## Configuration

| Config File | Purpose | Relevant Settings |
|-------------|---------|-------------------|
| [file] | [purpose] | [settings we care about] |
```

### gap-analysis.md Template

```markdown
---
feature: "{featureName}"
document: "gap-analysis"
mode: "brownfield"
created: "{timestamp}"
reuse_percentage: {X}%
new_code_percentage: {Y}%
---

# Gap Analysis: {featureName}

## Summary

| Category | Count | Effort |
|----------|-------|--------|
| Reusable | X | LOW |
| Modify | Y | MEDIUM |
| Create New | Z | HIGH |
| Total | N | [aggregate] |

---

## Reusable Components

These exist and can be used as-is:

| Component | Location | Confidence |
|-----------|----------|------------|
| [name] | [path] | HIGH/MEDIUM |

---

## Components to Modify

These exist but need changes:

| Component | Change Required | Compatibility Risk |
|-----------|-----------------|-------------------|
| [name] | [what changes] | LOW/MEDIUM/HIGH |

### Modification Details

#### [Component Name]
- **Current behavior**: [what it does now]
- **Required behavior**: [what we need]
- **Change scope**: [files affected]
- **Backward compatibility**: [breaking/non-breaking]
- **Migration needed**: [yes/no]

---

## New Components Needed

These don't exist and must be created:

| Component | Type | Dependencies |
|-----------|------|--------------|
| [name] | [file/class/function] | [what it depends on] |

---

## Conflict Risks

| Existing Code | Potential Conflict | Resolution |
|---------------|-------------------|------------|
| [code/pattern] | [conflict description] | [how to resolve] |

---

## Regression Risks

| Area | Risk Level | Mitigation |
|------|------------|------------|
| [area] | HIGH/MEDIUM/LOW | [how to prevent] |
```

---

## Branch Auto-Generation (--branch Flag)

When using `--branch` flag, a git branch is automatically created following conventional naming patterns.

### Branch Naming Patterns

| Pattern | Example | Use Case |
|---------|---------|----------|
| `feature/{spec-number}-{slug}` | `feature/001-user-auth` | New features |
| `fix/{spec-number}-{slug}` | `fix/002-login-bug` | Bug fixes |
| `refactor/{spec-number}-{slug}` | `refactor/003-db-layer` | Code improvements |
| `enhance/{spec-number}-{slug}` | `enhance/004-perf-boost` | Enhancements |

### Branch Generation Logic

```javascript
function generateBranchName(featureName, specNumber, objective) {
  // 1. Detect branch type from objective keywords
  const type = detectBranchType(objective);

  // 2. Create slug from feature name
  const slug = featureName
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')
    .substring(0, 30);

  // 3. Construct branch name
  return `${type}/${specNumber}-${slug}`;
}

function detectBranchType(objective) {
  const lower = objective.toLowerCase();

  if (lower.includes('fix') || lower.includes('bug') || lower.includes('issue')) {
    return 'fix';
  }
  if (lower.includes('refactor') || lower.includes('clean') || lower.includes('reorganize')) {
    return 'refactor';
  }
  if (lower.includes('improve') || lower.includes('enhance') || lower.includes('optimize')) {
    return 'enhance';
  }
  return 'feature';  // Default
}
```

### Branch Creation in Init

```javascript
async function executeInitPhaseWithBranch(featureName, objective, options) {
  // Standard init first
  const initResult = await executeInitPhase(featureName, objective);

  if (options.branch) {
    const branchName = generateBranchName(
      featureName,
      initResult.specDir.match(/(\d{3})/)[1],
      objective
    );

    // Check if branch exists
    const branchExists = await Bash({
      command: `git rev-parse --verify ${branchName} 2>/dev/null`,
      description: "Check if branch exists"
    }).then(() => true).catch(() => false);

    if (branchExists) {
      // Checkout existing branch
      await Bash({
        command: `git checkout ${branchName}`,
        description: `Switch to existing branch ${branchName}`
      });
    } else {
      // Create and checkout new branch
      await Bash({
        command: `git checkout -b ${branchName}`,
        description: `Create feature branch ${branchName}`
      });
    }

    // Record branch in phase state
    const phaseState = JSON.parse(await readFile(`${initResult.specDir}/.phase-state.json`));
    phaseState.branch = branchName;
    phaseState.branchCreated = new Date().toISOString();
    await writeFile(
      `${initResult.specDir}/.phase-state.json`,
      JSON.stringify(phaseState, null, 2)
    );

    return {
      ...initResult,
      branch: branchName
    };
  }

  return initResult;
}
```

### Phase State with Branch

```json
{
  "featureName": "user-authentication",
  "specDir": "specs/001-user-authentication",
  "branch": "feature/001-user-auth",
  "branchCreated": "2025-01-15T10:30:00Z",
  "currentPhase": "specify",
  "phases": {
    "init": { "status": "complete", "completedAt": "2025-01-15T10:30:00Z" }
  }
}
```

### Branch Completion on Implement

When implementation completes, the status output includes merge instructions:

```
✅ IMPLEMENTATION COMPLETE

Branch: feature/001-user-auth
Commits: 12

Ready to merge:
  git checkout main
  git merge --no-ff feature/001-user-auth
  git push origin main
  git branch -d feature/001-user-auth

Or create PR:
  gh pr create --base main --head feature/001-user-auth
```

---

## Directory Structure

**All spec state persists in the `specs/` directory at project root:**

```
specs/
├── 001-user-authentication/
│   ├── constitution.md        # Phase 1: Immutable principles
│   ├── spec.md                # Phase 2: Detailed specification
│   ├── clarifications.md      # Phase 3: Q&A resolutions
│   ├── plan.md                # Phase 4: Implementation plan
│   ├── tasks.md               # Phase 5: Task breakdown
│   ├── tests.md               # Phase 5b: Test specifications
│   ├── implementation.log     # Phase 6: Execution log
│   ├── .phase-state.json      # Phase tracking metadata
│   │
│   ├── # SUPPORTING DOCUMENTS (generated during PLAN phase)
│   ├── research.md            # Technical research & prior art
│   ├── data-model.md          # Entity relationships & schemas
│   ├── quickstart.md          # Developer onboarding guide
│   └── contracts/             # API contract specifications
│       ├── api.yaml           # OpenAPI 3.0 spec
│       ├── events.yaml        # AsyncAPI spec (if event-driven)
│       └── README.md          # Contract usage guide
├── 002-payment-integration/
│   └── ...
└── .spec-index.json           # Index of all specs
```

**Naming Convention**: `NNN-feature-name/` where NNN is auto-incremented.

---

## SYNRG Constitutional Articles (9 Core Principles)

**These principles govern ALL spec-driven development in SYNRG. They are IMMUTABLE.**

### Article I: Library-First Principle
> Every feature MUST begin as a standalone library with clear boundaries, minimal dependencies, and a defined interface. No direct implementation in application code until library is complete and tested. This forces modular, reusable design from the start.

**Enforcement**:
- Features start in `libs/` or `packages/` directory
- Must be independently testable
- Must have clear public API before integration
- Application code imports from library, never the reverse

### Article II: CLI Interface Mandate
> All libraries MUST expose functionality via command-line interface for testing and validation. Accept text input (stdin/args/files), produce text output (stdout). Support JSON for structured data exchange. This enforces observability and testability.

**Enforcement**:
- Every library has a CLI entry point
- CLI can be used to validate behavior without application context
- Enables scripted testing and automation

### Article III: Test-First Imperative (NON-NEGOTIABLE)
> No implementation code before tests. Tests MUST be written AND approved by user. Tests MUST be confirmed to FAIL (Red phase) before any implementation begins. This completely inverts traditional AI code generation.

**Enforcement**:
- TASKS phase generates test specifications, not implementation tasks
- Implementation phase runs tests FIRST to confirm they fail
- Only after RED confirmation does implementation proceed
- GREEN confirmation required before task is marked complete
- **Test Execution Order**: Contract tests → Integration tests → E2E tests → Unit tests

### Article IV: Specification Sovereignty
> Specifications define the contract. Implementation serves the spec, not the other way around. When conflict arises between spec and implementation, the spec wins. Specifications are the source of truth.

**Enforcement**:
- All implementation traces back to specification
- Deviations require spec amendment (not silent changes)
- Code review validates spec compliance

### Article V: Clarification Before Action
> No planning without clarification. All ambiguities MUST be resolved through explicit Q&A before any implementation planning begins. Assumptions are FORBIDDEN. Every `[NEEDS CLARIFICATION]` marker must be resolved.

**Enforcement**:
- CLARIFY phase is mandatory (cannot skip)
- Plan phase blocked until pending_count = 0
- LLM cannot "assume" - must ask user

### Article VI: Progressive Refinement
> Each phase refines the output of the previous phase. Constitution guides specification. Specification guides clarification. Clarification guides planning. Planning guides tasks. Tasks guide implementation. No phase can operate without its predecessor.

**Enforcement**:
- Phase gating validates predecessor completion
- Hash chains verify artifact integrity
- Each artifact references its predecessor

### Article VII: Simplicity Principle
> Maximum 3 projects/components for initial implementation. Additional complexity requires documented justification. No future-proofing - build for today's requirements. Start simple, add complexity only when proven necessary.

**Enforcement**:
- PLAN phase limited to 3 initial phases
- Expansion requires explicit user approval
- "YAGNI" (You Aren't Gonna Need It) applied rigorously

### Article VIII: Anti-Abstraction Principle
> Use framework features directly rather than wrapping. Trust the framework. Single model representation - no parallel data structures. Avoid unnecessary abstraction layers that add complexity without clear value.

**Enforcement**:
- No wrapper classes unless explicitly justified
- Direct framework API usage preferred
- Abstraction layers require cost-benefit analysis in plan

### Article IX: Integration-First Testing
> Prefer real databases over mocks. Use actual service instances over stubs. Contract tests are MANDATORY before implementation begins. Test in realistic environments, not artificial ones.

**Enforcement**:
- Contract tests defined before implementation
- Integration tests use real services where possible
- Mocks only for external third-party APIs with rate limits
- E2E tests run in staging-like environment

---

## Machine-Parseable State (Article VI Enforcement)

> All state MUST be stored in structured Markdown with YAML frontmatter. Human-readable AND machine-parseable. No hidden state in agent memory.

---

## Phase State Detection

**Auto-detect current phase for any spec:**

```javascript
const PHASES = ['init', 'specify', 'clarify', 'plan', 'analyze', 'tasks', 'tests', 'implement', 'complete'];

const PHASE_ARTIFACTS = {
  'init': 'constitution.md',
  'specify': 'spec.md',
  'clarify': 'clarifications.md',
  'plan': 'plan.md',
  'analyze': 'analysis.md',       // Optional but recommended
  'tasks': 'tasks.md',
  'tests': 'tests.md',            // RED phase confirmation
  'implement': 'implementation.log'
};

const PHASE_REQUIREMENTS = {
  'init': [],
  'specify': ['constitution.md'],
  'clarify': ['spec.md'],
  'plan': ['clarifications.md'],
  'analyze': ['plan.md'],         // Optional - can be skipped
  'tasks': ['plan.md'],           // analyze is optional
  'tests': ['tasks.md'],          // Article III: Tests before implementation
  'implement': ['tests.md']       // Requires RED confirmation
};

// Special requirement: tests.md must show RED_CONFIRMED status before implement
const PHASE_SPECIAL_REQUIREMENTS = {
  'implement': {
    artifact: 'tests.md',
    requiredStatus: 'RED_CONFIRMED',
    errorMessage: 'Tests must be written and confirmed FAILING (RED) before implementation'
  }
};

function getCurrentPhase(specDir) {
  // Check phases in reverse order to find most advanced complete phase
  for (let i = PHASES.length - 1; i >= 0; i--) {
    const phase = PHASES[i];
    if (phase === 'complete') continue;

    const artifact = PHASE_ARTIFACTS[phase];
    const artifactPath = `${specDir}/${artifact}`;

    if (fileExists(artifactPath)) {
      const content = readFile(artifactPath);
      const frontmatter = parseYAMLFrontmatter(content);

      if (frontmatter.status === 'complete' || frontmatter.status === 'ready') {
        // This phase is complete, check if next phase needs work
        const nextPhase = PHASES[i + 1];
        if (nextPhase && nextPhase !== 'complete') {
          return nextPhase; // Next phase is current
        }
        return 'complete'; // All done
      } else {
        return phase; // This phase is in progress
      }
    }
  }
  return 'init'; // No artifacts found, start from beginning
}

function canEnterPhase(phase, specDir) {
  const requirements = PHASE_REQUIREMENTS[phase];

  for (const required of requirements) {
    const artifactPath = `${specDir}/${required}`;

    if (!fileExists(artifactPath)) {
      return { allowed: false, reason: `Missing required artifact: ${required}` };
    }

    const content = readFile(artifactPath);
    const frontmatter = parseYAMLFrontmatter(content);

    if (frontmatter.status !== 'complete' && frontmatter.status !== 'ready') {
      return { allowed: false, reason: `Previous phase not complete: ${required}` };
    }

    // Special check for clarifications - must have 0 pending
    if (required === 'clarifications.md' && frontmatter.pending_count > 0) {
      return { allowed: false, reason: `${frontmatter.pending_count} clarification questions still pending` };
    }
  }

  return { allowed: true };
}
```

---

## PHASE 1: INIT — Constitutional Foundation

**Purpose**: Initialize spec directory and define constitutional articles for the feature.

**Entry Condition**: None (starting phase)
**Output Artifact**: `specs/NNN-feature-name/constitution.md`
**Exit Condition**: Constitution file exists with status: complete

### Execution Protocol

```javascript
async function executeInitPhase(featureName, objective) {
  // 1. Create spec directory with auto-incremented NNN prefix
  const specIndex = loadOrCreateSpecIndex();
  const nextNumber = String(specIndex.nextNumber).padStart(3, '0');
  const specDir = `specs/${nextNumber}-${slugify(featureName)}`;

  await createDirectory(specDir);

  // 2. Generate constitution using template + user input
  const constitution = await generateConstitution({
    featureName: featureName,
    objective: objective,
    timestamp: new Date().toISOString()
  });

  // 3. Write constitution.md
  await writeFile(`${specDir}/constitution.md`, constitution);

  // 4. Initialize phase state
  await writeFile(`${specDir}/.phase-state.json`, JSON.stringify({
    featureName: featureName,
    specDir: specDir,
    currentPhase: 'specify',  // Ready for next phase
    phases: {
      init: { status: 'complete', completedAt: new Date().toISOString() }
    }
  }, null, 2));

  // 5. Update spec index
  specIndex.specs.push({
    number: nextNumber,
    name: featureName,
    directory: specDir,
    created: new Date().toISOString(),
    status: 'in_progress'
  });
  specIndex.nextNumber++;
  await writeFile('specs/.spec-index.json', JSON.stringify(specIndex, null, 2));

  return {
    success: true,
    phase: 'init',
    specDir: specDir,
    nextPhase: 'specify'
  };
}
```

### Constitution Template

```markdown
---
feature: "{featureName}"
objective: "{objective}"
created: "{timestamp}"
phase: "constitution"
status: "complete"
---

# Constitutional Articles: {featureName}

## Objective
{objective}

---

## Article 1: Specification Sovereignty

**For this feature, specifications govern:**
- [Define what the spec controls for this feature]
- [Define boundaries of the specification]

**Implementation MUST NOT:**
- [Define what implementation cannot override]

---

## Article 2: Clarification Before Action

**Before planning, the following MUST be clarified:**
- [ ] [Area of ambiguity 1]
- [ ] [Area of ambiguity 2]
- [ ] [Area of ambiguity 3]

**Assumptions that are FORBIDDEN:**
- [Assumption 1 - must be verified]
- [Assumption 2 - must be verified]

---

## Article 3: Progressive Refinement

**Refinement pathway for this feature:**
1. Constitution defines: [what principles govern]
2. Specification defines: [what will be built]
3. Clarification resolves: [what ambiguities exist]
4. Plan defines: [how it will be built]
5. Tasks define: [atomic work units]
6. Implementation produces: [deliverables]

---

## Article 4: Machine-Parseable State

**State artifacts for this feature:**
- `constitution.md` - This file (immutable after completion)
- `spec.md` - Detailed specification
- `clarifications.md` - Q&A resolutions
- `plan.md` - Implementation plan
- `tasks.md` - Task breakdown
- `implementation.log` - Execution record

**Format requirements:**
- YAML frontmatter for metadata
- Markdown for content
- Structured sections with headers

---

## Article 5: Phase Gate Integrity

**Phase gates for this feature:**
- [ ] Constitution complete before specification
- [ ] Specification complete before clarification
- [ ] All clarifications resolved before planning
- [ ] Plan complete before task breakdown
- [ ] Tasks ready before implementation

**Skipping phases is a VIOLATION.**

---

## Feature-Specific Constraints

### Technical Constraints
- [Constraint 1]
- [Constraint 2]

### Business Constraints
- [Constraint 1]
- [Constraint 2]

### Compliance Requirements
- [Requirement 1]
- [Requirement 2]

---

## Success Criteria

This feature is complete when:
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

---

**Constitution Hash**: {sha256-hash}
**Immutable After**: {timestamp}
```

### User Interaction for Init

When executing `init`, use AskUserQuestion to gather:

1. **Feature Name**: "What is the name of this feature?"
2. **Objective**: "What is the high-level objective? (1-2 sentences)"
3. **Key Constraints**: "What technical or business constraints exist?"
4. **Success Criteria**: "How will we know when this feature is complete?"

---

## PHASE 2: SPECIFY — Detailed Specification

**Purpose**: Generate detailed specification from objective and constitutional constraints.

**Entry Condition**: `constitution.md` exists with status: complete
**Output Artifact**: `specs/NNN-feature-name/spec.md`
**Exit Condition**: Spec file exists with status: complete

### Execution Protocol

```javascript
async function executeSpecifyPhase(specDir) {
  // 1. Validate phase gate
  const canEnter = canEnterPhase('specify', specDir);
  if (!canEnter.allowed) {
    throw new Error(`Cannot enter specify phase: ${canEnter.reason}`);
  }

  // 2. Load constitution
  const constitution = await readFile(`${specDir}/constitution.md`);
  const constitutionData = parseYAMLFrontmatter(constitution);

  // 3. Generate specification using sub-agent
  const specificationPrompt = `
You are a specification generation agent. Generate a detailed specification based on:

CONSTITUTION:
${constitution}

REQUIREMENTS:
1. Follow all constitutional articles
2. Be specific and unambiguous
3. Include functional and non-functional requirements
4. Define interfaces and data structures
5. List all assumptions (to be clarified in next phase)

OUTPUT FORMAT:
Use the specification template with YAML frontmatter.
Status should be "complete" when done.
`;

  const specification = await Task({
    subagent_type: "general-purpose",
    prompt: specificationPrompt,
    model: "sonnet"
  });

  // 4. Write spec.md
  await writeFile(`${specDir}/spec.md`, specification);

  // 5. Update phase state
  await updatePhaseState(specDir, 'specify', 'complete');

  return {
    success: true,
    phase: 'specify',
    nextPhase: 'clarify'
  };
}
```

### Specification Template

```markdown
---
feature: "{featureName}"
phase: "specification"
status: "complete"
constitution_hash: "{sha256-of-constitution}"
created: "{timestamp}"
requirements_count: {count}
assumptions_count: {count}
---

# Specification: {featureName}

## 1. Overview

### 1.1 Purpose
[What this feature does and why it exists]

### 1.2 Scope
[What is included and explicitly excluded]

### 1.3 Background
[Context and motivation]

---

## 2. User Scenarios (Priority-Ordered)

**User stories MUST be ranked by criticality. Each story should be independently testable and deployable.**

### P1: Critical User Journeys (Must Have)

#### US1: [Primary User Journey]
**As a** [actor]
**I want** [action]
**So that** [value]

**Acceptance Criteria (Given-When-Then)**:
```gherkin
Given [initial context/precondition]
When [action performed]
Then [expected outcome]
And [additional outcome if applicable]
```

**Independent Testability**: YES - Can be developed, tested, and deployed standalone

---

#### US2: [Secondary Critical Journey]
**As a** [actor]
**I want** [action]
**So that** [value]

**Acceptance Criteria (Given-When-Then)**:
```gherkin
Given [initial context/precondition]
When [action performed]
Then [expected outcome]
```

---

### P2: Important User Journeys (Should Have)

#### US3: [Important but not critical journey]
**As a** [actor]
**I want** [action]
**So that** [value]

**Acceptance Criteria (Given-When-Then)**:
```gherkin
Given [initial context/precondition]
When [action performed]
Then [expected outcome]
```

---

### P3+: Enhancement User Journeys (Nice to Have)

#### US4: [Enhancement journey]
**As a** [actor]
**I want** [action]
**So that** [value]

**Acceptance Criteria**: [NEEDS CLARIFICATION]

---

## 3. Functional Requirements

### 3.1 Core Functionality

| ID | Requirement | Priority | User Story | Source |
|----|-------------|----------|------------|--------|
| FR-001 | [Requirement description] | MUST | US1 | Constitution |
| FR-002 | [Requirement description] | MUST | US1, US2 | User need |
| FR-003 | [Requirement description] | SHOULD | US3 | Enhancement |

### 3.2 User Interactions
[How users interact with this feature]

### 3.3 System Interactions
[How this feature interacts with other systems]

---

## 4. Non-Functional Requirements

### 4.1 Performance
| ID | Requirement | Target | Measurement |
|----|-------------|--------|-------------|
| NFR-001 | Response time | < 200ms | P95 latency |
| NFR-002 | Throughput | 1000 req/s | Load test |

### 4.2 Security
- [Security requirement 1]
- [Security requirement 2]

### 4.3 Reliability
- [Reliability requirement]

### 4.4 Scalability
- [Scalability requirement]

---

## 5. Architecture

### 5.1 High-Level Design
[Architecture overview - can include ASCII diagrams]

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │────▶│   Service   │────▶│  Database   │
└─────────────┘     └─────────────┘     └─────────────┘
```

### 5.2 Components
[Component descriptions]

### 5.3 Data Flow
[How data moves through the system]

---

## 6. Interfaces

### 6.1 API Endpoints
| Method | Endpoint | Description | Request | Response |
|--------|----------|-------------|---------|----------|
| POST | /api/v1/resource | Create resource | {...} | {...} |

### 6.2 Data Structures
```typescript
interface Resource {
  id: string;
  name: string;
  // ...
}
```

### 6.3 External Integrations
[Third-party services, APIs]

---

## 7. Data Model

### 7.1 Entities
[Entity descriptions and relationships]

### 7.2 Schema
[Database schema or data structures]

---

## 8. Constraints

### 8.1 Technical Constraints
[From constitution + additional]

### 8.2 Business Constraints
[From constitution + additional]

### 8.3 Regulatory/Compliance
[Any compliance requirements]

---

## 9. Assumptions (TO BE CLARIFIED)

**These assumptions MUST be verified in the clarification phase.**
**Items marked `[NEEDS CLARIFICATION]` are MANDATORY to resolve before planning.**

| ID | Assumption | Priority | Risk if Wrong | Clarification Needed |
|----|------------|----------|---------------|---------------------|
| A-001 | [Assumption] | SCOPE | [Risk] | [Question to ask] |
| A-002 | [Assumption] | SECURITY | [Risk] | [Question to ask] |
| A-003 | [Assumption] | UX | [Risk] | [Question to ask] |
| A-004 | [Assumption] | TECHNICAL | [Risk] | [Question to ask] |

**Priority Order for Resolution**:
1. **SCOPE** - Highest priority (defines what we build)
2. **SECURITY** - High priority (compliance and safety)
3. **UX** - Medium priority (user experience decisions)
4. **TECHNICAL** - Lower priority (implementation details)

---

## 10. Dependencies

### 10.1 External Dependencies

| Dependency | Version | Purpose | Required |
|------------|---------|---------|----------|
| [Library/Service] | [Version] | [Why needed] | YES/NO |

### 10.2 Internal Dependencies

| Module | Purpose | Status |
|--------|---------|--------|
| [Module name] | [What it provides] | [Existing/New] |

### 10.3 Infrastructure Dependencies

| Resource | Requirement | Notes |
|----------|-------------|-------|
| [Database/Cache/etc] | [Specs needed] | [NEEDS CLARIFICATION] |

---

## 11. Acceptance Criteria

**Feature is complete when ALL criteria are met:**

- [ ] AC-001: [Criterion] (US1)
- [ ] AC-002: [Criterion] (US1)
- [ ] AC-003: [Criterion] (US2)

---

## 12. Open Questions

[Questions that emerged during specification that need answers]

| ID | Question | Priority | Category |
|----|----------|----------|----------|
| OQ-001 | [Question 1] | [SCOPE/SECURITY/UX/TECHNICAL] | [NEEDS CLARIFICATION] |
| OQ-002 | [Question 2] | [SCOPE/SECURITY/UX/TECHNICAL] | [NEEDS CLARIFICATION] |

---

**Specification Hash**: {sha256-hash}
**Ready for Clarification**: YES
```

---

## PHASE 3: CLARIFY — Ambiguity Resolution

**Purpose**: Resolve all ambiguities through structured Q&A before any planning begins.

**Entry Condition**: `spec.md` exists with status: complete
**Output Artifact**: `specs/NNN-feature-name/clarifications.md`
**Exit Condition**: All questions answered, pending_count: 0

### Execution Protocol

**CRITICAL PATTERN: Maximum 3 Clarification Rounds with Priority-Based Reduction**

Each round focuses on progressively fewer, higher-priority questions:
- **Round 1**: All questions, grouped by priority (SCOPE → SECURITY → UX → TECHNICAL)
- **Round 2**: Only SCOPE and SECURITY questions remaining + any blocking questions
- **Round 3**: Only SCOPE questions + absolute blockers (must proceed with defaults otherwise)

```javascript
// Priority weights for question ordering
const PRIORITY_ORDER = {
  'SCOPE': 1,      // Highest - defines what we build
  'SECURITY': 2,   // High - compliance and safety
  'UX': 3,         // Medium - user experience decisions
  'TECHNICAL': 4   // Lower - implementation details (can default)
};

const MAX_CLARIFICATION_ROUNDS = 3;

async function executeClarifyPhase(specDir) {
  // 1. Validate phase gate
  const canEnter = canEnterPhase('clarify', specDir);
  if (!canEnter.allowed) {
    throw new Error(`Cannot enter clarify phase: ${canEnter.reason}`);
  }

  // 2. Load spec
  const spec = await readFile(`${specDir}/spec.md`);

  // 3. Check if clarifications.md exists (continue existing Q&A)
  let clarifications;
  const clarificationsPath = `${specDir}/clarifications.md`;

  if (fileExists(clarificationsPath)) {
    clarifications = await readFile(clarificationsPath);
    const frontmatter = parseYAMLFrontmatter(clarifications);

    if (frontmatter.pending_count === 0) {
      return { success: true, phase: 'clarify', status: 'already_complete' };
    }
    // Continue with pending questions from current round
  } else {
    // 4. Generate clarification questions from spec (sorted by priority)
    clarifications = await generateClarificationQuestions(spec);
    await writeFile(clarificationsPath, clarifications);
  }

  // 5. Execute iterative clarification rounds
  let currentRound = getFrontmatter(clarifications).current_round || 1;

  while (currentRound <= MAX_CLARIFICATION_ROUNDS) {
    const pendingQuestions = extractPendingQuestions(clarifications);

    if (pendingQuestions.length === 0) {
      break; // All questions answered
    }

    // Sort questions by priority for this round
    const sortedQuestions = pendingQuestions.sort((a, b) =>
      PRIORITY_ORDER[a.priority] - PRIORITY_ORDER[b.priority]
    );

    // Filter questions based on round (progressive reduction)
    const roundQuestions = filterQuestionsForRound(sortedQuestions, currentRound);

    if (roundQuestions.length === 0) {
      // No more questions for this round, apply defaults and complete
      await applyDefaultsForRemainingQuestions(clarificationsPath, pendingQuestions);
      break;
    }

    // Present round header
    console.log(`\n--- Clarification Round ${currentRound}/${MAX_CLARIFICATION_ROUNDS} ---`);
    console.log(`Questions remaining: ${roundQuestions.length}`);
    if (currentRound < MAX_CLARIFICATION_ROUNDS) {
      console.log(`(Lower priority questions will use defaults if not addressed by round ${MAX_CLARIFICATION_ROUNDS})`);
    }

    // Ask questions in priority order
    for (const question of roundQuestions) {
      const answer = await AskUserQuestion({
        questions: [{
          question: `[${question.priority}] ${question.text}`,
          header: question.category,
          options: question.suggestedOptions || [
            { label: "Yes", description: "Confirm this assumption" },
            { label: "No", description: "Reject this assumption" },
            { label: "Clarify", description: "Need more context" },
            { label: "Use Default", description: `Accept default: ${question.defaultValue || 'None specified'}` }
          ],
          multiSelect: false
        }]
      });

      // Update clarifications.md with answer
      await updateClarification(clarificationsPath, question.id, answer);
    }

    // Increment round
    currentRound++;
    await updateRoundCount(clarificationsPath, currentRound);

    // Reload clarifications for next iteration
    clarifications = await readFile(clarificationsPath);
  }

  // 6. Final verification - apply defaults to any remaining questions
  const finalClarifications = await readFile(clarificationsPath);
  const finalFrontmatter = parseYAMLFrontmatter(finalClarifications);

  if (finalFrontmatter.pending_count > 0) {
    console.log(`\n⚠️ ${finalFrontmatter.pending_count} questions unanswered after ${MAX_CLARIFICATION_ROUNDS} rounds.`);
    console.log('Applying documented defaults for remaining questions.');
    await applyDefaultsForRemainingQuestions(clarificationsPath,
      extractPendingQuestions(finalClarifications));
  }

  await updatePhaseState(specDir, 'clarify', 'complete');
  return { success: true, phase: 'clarify', nextPhase: 'plan' };
}

// Filter questions based on round number (progressive focus)
function filterQuestionsForRound(questions, round) {
  switch (round) {
    case 1:
      // Round 1: All questions
      return questions;
    case 2:
      // Round 2: Only SCOPE and SECURITY priorities
      return questions.filter(q =>
        q.priority === 'SCOPE' || q.priority === 'SECURITY' || q.isBlocker
      );
    case 3:
      // Round 3: Only SCOPE and absolute blockers
      return questions.filter(q =>
        q.priority === 'SCOPE' || q.isBlocker
      );
    default:
      return [];
  }
}

// Apply defaults for questions that weren't answered within 3 rounds
async function applyDefaultsForRemainingQuestions(clarificationsPath, questions) {
  for (const question of questions) {
    const defaultAnswer = question.defaultValue ||
      `[DEFAULT APPLIED] No explicit answer provided. Using documented default or conservative interpretation.`;

    await updateClarification(clarificationsPath, question.id, {
      answer: defaultAnswer,
      source: 'DEFAULT',
      round: 'EXCEEDED_MAX_ROUNDS'
    });
  }
}
```

### Clarifications Template

```markdown
---
feature: "{featureName}"
phase: "clarification"
status: "in_progress"  # or "complete" when pending_count = 0
spec_hash: "{sha256-of-spec}"
created: "{timestamp}"
current_round: 1          # 1, 2, or 3 (max 3 rounds)
max_rounds: 3             # Maximum rounds before defaults applied
total_questions: {count}
answered_count: {count}
pending_count: {count}
defaults_applied: 0       # Count of questions resolved via defaults
---

# Clarifications: {featureName}

## Summary

| Metric | Value |
|--------|-------|
| Current Round | {current_round}/3 |
| Total Questions | {total} |
| Answered | {answered} |
| Pending | {pending} |
| Defaults Applied | {defaults_applied} |
| Clarification Complete | {YES/NO} |

## Priority Resolution Order

Questions are asked in priority order:
1. **SCOPE** (Round 1-3) - What we're building
2. **SECURITY** (Round 1-2) - Compliance and safety
3. **UX** (Round 1 only unless blocking) - User experience
4. **TECHNICAL** (Round 1 only unless blocking) - Implementation details

> **Note**: Questions not addressed by Round 3 will use documented defaults.

---

## Questions from Assumptions

### Q-A001: [Question from Assumption A-001]
**Source**: Assumption A-001 in spec.md
**Priority**: SCOPE | SECURITY | UX | TECHNICAL
**Category**: Technical
**Status**: PENDING | ANSWERED | DEFAULT
**Round**: 1 | 2 | 3 | EXCEEDED_MAX_ROUNDS

**Question**:
[Full question text]

**Context**:
[Why this matters]

**Default Value**:
[What we'll assume if not answered by Round 3]

**Answer**:
[User's response - empty if pending]

**Answer Source**:
USER | DEFAULT

**Impact on Plan**:
[How this answer affects the implementation plan]

---

### Q-A002: [Question from Assumption A-002]
**Source**: Assumption A-002 in spec.md
**Priority**: SCOPE | SECURITY | UX | TECHNICAL
**Category**: Business
**Status**: PENDING | ANSWERED | DEFAULT
**Round**: 1 | 2 | 3 | EXCEEDED_MAX_ROUNDS

**Question**:
[Full question text]

**Default Value**:
[What we'll assume if not answered by Round 3]

**Answer**:
[User's response]

**Answer Source**:
USER | DEFAULT

**Impact on Plan**:
[How this answer affects the implementation plan]

---

## Questions from Open Items

### Q-O001: [Question from Open Question 1]
**Source**: Open Questions in spec.md
**Priority**: SCOPE | SECURITY | UX | TECHNICAL
**Category**: Architecture
**Status**: PENDING | ANSWERED | DEFAULT
**Round**: 1 | 2 | 3 | EXCEEDED_MAX_ROUNDS

**Question**:
[Full question text]

**Default Value**:
[What we'll assume if not answered by Round 3]

**Answer**:
[User's response]

**Answer Source**:
USER | DEFAULT

**Impact on Plan**:
[How this answer affects the implementation plan]

---

## Auto-Generated Questions

### Q-G001: [Auto-detected ambiguity]
**Source**: Specification Analysis
**Priority**: SCOPE | SECURITY | UX | TECHNICAL
**Category**: Interface
**Status**: PENDING | ANSWERED | DEFAULT
**Round**: 1 | 2 | 3 | EXCEEDED_MAX_ROUNDS
**Is Blocker**: YES | NO

**Question**:
[Full question text]

**Default Value**:
[What we'll assume if not answered by Round 3]

**Answer**:
[User's response]

**Answer Source**:
USER | DEFAULT

**Impact on Plan**:
[How this answer affects the implementation plan]

---

## Clarification Summary

**Resolution Statistics:**
| Round | Questions Asked | Answered | Defaulted |
|-------|-----------------|----------|-----------|
| 1     | {count}         | {count}  | 0         |
| 2     | {count}         | {count}  | 0         |
| 3     | {count}         | {count}  | {count}   |

**Key Decisions Made:**
1. [Decision 1 from Q-A001] (Source: USER)
2. [Decision 2 from Q-O001] (Source: USER)
3. [Decision 3 from Q-G001] (Source: DEFAULT)

**Constraints Added:**
1. [New constraint from clarifications]

**Scope Changes:**
1. [Any scope adjustments based on clarifications]

**Defaults Applied:**
1. [Question ID]: [Default value used] - [Rationale]

---

**Clarifications Hash**: {sha256-hash}
**Ready for Planning**: {YES/NO - based on pending_count = 0}
**All Questions Resolved**: {YES - including defaults}
```

### Question Generation Logic

```javascript
// Priority classification for clarification questions
const PRIORITY_KEYWORDS = {
  SCOPE: ['feature', 'scope', 'include', 'exclude', 'boundary', 'requirement', 'must', 'need', 'goal', 'objective'],
  SECURITY: ['auth', 'permission', 'access', 'encrypt', 'secure', 'credential', 'token', 'compliance', 'gdpr', 'pii'],
  UX: ['user', 'interface', 'flow', 'experience', 'design', 'layout', 'display', 'format', 'style', 'responsive'],
  TECHNICAL: ['implement', 'architecture', 'database', 'api', 'performance', 'cache', 'storage', 'integration', 'library']
};

function assignPriority(questionText) {
  const lowerText = questionText.toLowerCase();

  // Check each priority level (in order of importance)
  for (const [priority, keywords] of Object.entries(PRIORITY_KEYWORDS)) {
    if (keywords.some(keyword => lowerText.includes(keyword))) {
      return priority;
    }
  }

  return 'TECHNICAL'; // Default to lowest priority
}

function isBlockingQuestion(questionText, source) {
  // Questions that MUST be answered before proceeding
  const blockingPatterns = [
    /security|compliance|legal|gdpr|pii/i,
    /critical|blocking|required|mandatory/i,
    /core functionality|primary use case/i
  ];

  return blockingPatterns.some(pattern => pattern.test(questionText));
}

async function generateClarificationQuestions(spec) {
  // Extract assumptions from spec (with their priority from the assumptions table)
  const assumptions = extractSection(spec, 'Assumptions');

  // Extract open questions from spec (with their priority from the open questions table)
  const openQuestions = extractSection(spec, 'Open Questions');

  // Auto-detect ambiguities using sub-agent
  const autoQuestions = await Task({
    subagent_type: "general-purpose",
    prompt: `Analyze this specification and identify any ambiguities or unclear areas that need clarification before implementation planning.

SPECIFICATION:
${spec}

For each ambiguity found, provide in JSON format:
{
  "id": "Q-G001",
  "question": "The clarification question",
  "context": "Why this matters",
  "priority": "SCOPE | SECURITY | UX | TECHNICAL",
  "isBlocker": true/false,
  "defaultValue": "What to assume if not answered",
  "suggestedOptions": ["Option 1", "Option 2", "Option 3"]
}

PRIORITY CLASSIFICATION:
- SCOPE: Defines what we build (features, boundaries, requirements)
- SECURITY: Compliance, authentication, authorization, data protection
- UX: User experience, interface design, interaction patterns
- TECHNICAL: Implementation details, architecture, performance

BLOCKER CRITERIA:
- Mark as blocker if answer fundamentally changes architecture
- Mark as blocker if security/compliance implications
- Mark as blocker if affects core user journey

Focus on:
- Undefined edge cases
- Missing error handling requirements
- Unclear data validation rules
- Ambiguous user flow decisions
- Integration points without clear contracts`,
    model: "haiku"
  });

  // Process and assign priorities to all questions
  const processedQuestions = processQuestionsWithPriority({
    fromAssumptions: assumptions.map(a => ({
      ...a,
      priority: a.priority || assignPriority(a.question),
      isBlocker: isBlockingQuestion(a.question, 'assumption')
    })),
    fromOpenQuestions: openQuestions.map(q => ({
      ...q,
      priority: q.priority || assignPriority(q.question),
      isBlocker: isBlockingQuestion(q.question, 'open_question')
    })),
    autoGenerated: autoQuestions
  });

  // Sort by priority (SCOPE first, then SECURITY, UX, TECHNICAL)
  processedQuestions.sort((a, b) =>
    PRIORITY_ORDER[a.priority] - PRIORITY_ORDER[b.priority]
  );

  return formatClarificationsDocument(processedQuestions);
}
```

---

## PHASE 4: PLAN — Implementation Planning

**Purpose**: Generate a phased implementation plan from spec + clarifications.

**Entry Condition**: `clarifications.md` exists with status: complete, pending_count: 0
**Output Artifact**: `specs/NNN-feature-name/plan.md`
**Exit Condition**: Plan file exists with status: complete

### Execution Protocol

```javascript
async function executePlanPhase(specDir) {
  // 1. Validate phase gate (STRICT - clarifications must have 0 pending)
  const canEnter = canEnterPhase('plan', specDir);
  if (!canEnter.allowed) {
    throw new Error(`Cannot enter plan phase: ${canEnter.reason}`);
  }

  // 2. Load all previous phase artifacts
  const constitution = await readFile(`${specDir}/constitution.md`);
  const spec = await readFile(`${specDir}/spec.md`);
  const clarifications = await readFile(`${specDir}/clarifications.md`);

  // 3. Generate implementation plan using sub-agent
  const plan = await Task({
    subagent_type: "general-purpose",
    prompt: `You are an implementation planning agent. Generate a phased implementation plan.

CONSTITUTION (Governing Principles):
${constitution}

SPECIFICATION (What to Build):
${spec}

CLARIFICATIONS (Resolved Ambiguities):
${clarifications}

Generate a comprehensive implementation plan that:
1. Breaks work into logical phases
2. Each phase has clear objectives and deliverables
3. Identifies dependencies between phases
4. Includes validation criteria for each phase
5. Assesses risks and provides mitigations
6. Follows progressive refinement (each phase builds on previous)

Use the plan template format with YAML frontmatter.
Set status to "complete" when done.`,
    model: "sonnet"
  });

  // 4. Write plan.md
  await writeFile(`${specDir}/plan.md`, plan);

  // 5. Generate supporting documents in parallel
  await Promise.all([
    generateResearchDoc(specDir, spec, clarifications),
    generateDataModelDoc(specDir, spec, clarifications),
    generateQuickstartDoc(specDir, spec, plan),
    generateContractsDir(specDir, spec, clarifications)
  ]);

  // 6. Update phase state
  await updatePhaseState(specDir, 'plan', 'complete');

  return {
    success: true,
    phase: 'plan',
    nextPhase: 'tasks',
    supportingDocs: ['research.md', 'data-model.md', 'quickstart.md', 'contracts/']
  };
}
```

### Plan Template

```markdown
---
feature: "{featureName}"
phase: "planning"
status: "complete"
clarifications_hash: "{sha256-of-clarifications}"
created: "{timestamp}"
total_phases: {count}
estimated_effort: "{effort estimate}"
risk_level: "LOW|MEDIUM|HIGH"
---

# Implementation Plan: {featureName}

## Executive Summary

**Objective**: [From constitution]
**Approach**: [High-level implementation approach]
**Estimated Effort**: [Total effort estimate]
**Risk Level**: [Overall risk assessment]

---

## Phase Overview

```
Phase 1: Foundation     ──▶ [deliverable]
    │
    ▼
Phase 2: Core Logic     ──▶ [deliverable]
    │
    ▼
Phase 3: Integration    ──▶ [deliverable]
    │
    ▼
Phase 4: Validation     ──▶ [deliverable]
```

---

## Phase 1: {Phase Name}

### Objective
[What this phase accomplishes]

### Prerequisites
- [Prerequisite 1]
- [Prerequisite 2]

### Deliverables
1. [Deliverable 1]
2. [Deliverable 2]

### Tasks (High-Level)
1. [ ] [Task description]
2. [ ] [Task description]
3. [ ] [Task description]

### Dependencies
- **Depends On**: [Nothing | Phase X]
- **Blocks**: [Phase 2, Phase 3]

### Validation Criteria
- [ ] [How to verify phase is complete]
- [ ] [What tests must pass]

### Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk] | LOW/MED/HIGH | LOW/MED/HIGH | [Mitigation] |

### Effort Estimate
- Estimated: [X hours/days]
- Confidence: [HIGH/MEDIUM/LOW]

---

## Phase 2: {Phase Name}

[Same structure as Phase 1]

---

## Phase 3: {Phase Name}

[Same structure as Phase 1]

---

## Phase 4: {Phase Name}

[Same structure as Phase 1]

---

## Dependency Graph

```
[ASCII diagram showing phase dependencies]

Phase 1 ─────┬─────▶ Phase 2
             │
             └─────▶ Phase 3 ─────▶ Phase 4
```

---

## Risk Assessment (Aggregate)

### High Risks
| Risk | Phase | Probability | Impact | Mitigation |
|------|-------|-------------|--------|------------|
| [Risk] | 2 | HIGH | HIGH | [Mitigation] |

### Medium Risks
| Risk | Phase | Probability | Impact | Mitigation |
|------|-------|-------------|--------|------------|
| [Risk] | 1 | MEDIUM | MEDIUM | [Mitigation] |

---

## Resource Requirements

### Technical Resources
- [Resource 1]
- [Resource 2]

### External Dependencies
- [Dependency 1]
- [Dependency 2]

---

## Rollback Strategy

**If implementation fails:**
1. [Rollback step 1]
2. [Rollback step 2]

**Point of no return**: [Describe when rollback becomes expensive]

---

## Success Criteria

**Plan is successfully executed when:**
- [ ] All phases complete
- [ ] All deliverables produced
- [ ] All validation criteria met
- [ ] No high-risk items unmitigated

---

**Plan Hash**: {sha256-hash}
**Ready for Task Breakdown**: YES
```

---

## Supporting Documents (Generated with Plan)

During plan generation, four supporting documents are automatically created to provide context and accelerate development.

### Supporting Document Generators

```javascript
// Generate research.md - Prior art and technical research
async function generateResearchDoc(specDir, spec, clarifications) {
  const research = await Task({
    subagent_type: "general-purpose",
    prompt: `You are a technical research agent. Compile relevant research for this feature.

SPECIFICATION:
${spec}

CLARIFICATIONS:
${clarifications}

Generate research.md covering:
1. **Prior Art**: Similar implementations in open source
2. **Design Patterns**: Applicable architectural patterns
3. **Technology Options**: Framework/library alternatives evaluated
4. **Best Practices**: Industry standards for this domain
5. **Anti-Patterns**: What to avoid based on prior failures
6. **References**: Links to documentation, articles, examples

Use YAML frontmatter with: feature, created, sources_count, confidence_level`,
    model: "haiku"
  });
  await writeFile(`${specDir}/research.md`, research);
}

// Generate data-model.md - Entity relationships and schemas
async function generateDataModelDoc(specDir, spec, clarifications) {
  const dataModel = await Task({
    subagent_type: "general-purpose",
    prompt: `You are a data modeling agent. Define the data model for this feature.

SPECIFICATION:
${spec}

CLARIFICATIONS:
${clarifications}

Generate data-model.md covering:
1. **Entities**: All data entities with attributes and types
2. **Relationships**: Entity relationships (1:1, 1:N, N:M)
3. **State Machines**: Entity state transitions (if applicable)
4. **Validation Rules**: Data constraints and invariants
5. **Indexes**: Performance-critical query patterns
6. **Migration Path**: Schema evolution strategy

Include ASCII diagrams for entity relationships.
Use YAML frontmatter with: feature, entities_count, relationships_count`,
    model: "haiku"
  });
  await writeFile(`${specDir}/data-model.md`, dataModel);
}

// Generate quickstart.md - Developer onboarding guide
async function generateQuickstartDoc(specDir, spec, plan) {
  const quickstart = await Task({
    subagent_type: "general-purpose",
    prompt: `You are a documentation agent. Create a quickstart guide for developers.

SPECIFICATION:
${spec}

IMPLEMENTATION PLAN:
${plan}

Generate quickstart.md covering:
1. **Prerequisites**: What developers need before starting
2. **Setup Steps**: Step-by-step environment setup
3. **Key Concepts**: Core abstractions developers must understand
4. **Common Tasks**: How to perform typical operations
5. **Testing**: How to run and write tests
6. **Debugging**: Common issues and solutions
7. **Architecture Overview**: High-level component diagram

Use YAML frontmatter with: feature, estimated_setup_time, difficulty_level`,
    model: "haiku"
  });
  await writeFile(`${specDir}/quickstart.md`, quickstart);
}

// Generate contracts/ directory - API specifications
async function generateContractsDir(specDir, spec, clarifications) {
  // Create contracts directory
  await mkdir(`${specDir}/contracts`);

  // Generate OpenAPI spec
  const openapi = await Task({
    subagent_type: "general-purpose",
    prompt: `You are an API contract agent. Generate OpenAPI 3.0 specification.

SPECIFICATION:
${spec}

CLARIFICATIONS:
${clarifications}

Generate a complete OpenAPI 3.0 YAML specification including:
1. All endpoints with methods, paths, parameters
2. Request/response schemas with examples
3. Authentication requirements
4. Error responses (4xx, 5xx)
5. Pagination patterns (if applicable)
6. Rate limiting headers (if applicable)

Output pure YAML (no markdown code fences).`,
    model: "haiku"
  });
  await writeFile(`${specDir}/contracts/api.yaml`, openapi);

  // Check if event-driven and generate AsyncAPI if needed
  if (spec.includes('event') || spec.includes('websocket') || spec.includes('message')) {
    const asyncapi = await Task({
      subagent_type: "general-purpose",
      prompt: `Generate AsyncAPI 2.0 specification for event-driven components.

SPECIFICATION:
${spec}

Include all channels, message schemas, and pub/sub patterns.
Output pure YAML (no markdown code fences).`,
      model: "haiku"
    });
    await writeFile(`${specDir}/contracts/events.yaml`, asyncapi);
  }

  // Generate contracts README
  const readme = `# API Contracts

This directory contains machine-readable API specifications.

## Files

- **api.yaml** - OpenAPI 3.0 REST API specification
- **events.yaml** - AsyncAPI 2.0 event specification (if applicable)

## Usage

### Validate contracts
\`\`\`bash
npx @openapitools/openapi-generator-cli validate -i api.yaml
\`\`\`

### Generate client SDK
\`\`\`bash
npx @openapitools/openapi-generator-cli generate -i api.yaml -g typescript-fetch -o ./sdk
\`\`\`

### Generate mock server
\`\`\`bash
npx prism mock api.yaml
\`\`\`

## Contract-First Development

These contracts define the API before implementation. All implementations
MUST conform to these specifications. Contract tests validate compliance.
`;
  await writeFile(`${specDir}/contracts/README.md`, readme);
}
```

### research.md Template

```markdown
---
feature: "{featureName}"
document: "research"
created: "{timestamp}"
sources_count: {count}
confidence_level: "HIGH|MEDIUM|LOW"
---

# Technical Research: {featureName}

## Prior Art

### Open Source Implementations
| Project | Approach | Pros | Cons |
|---------|----------|------|------|
| [Project 1] | [How they solved it] | [Benefits] | [Drawbacks] |

### Commercial Solutions
[Analysis of how commercial products handle this]

---

## Design Patterns

### Recommended Patterns
1. **[Pattern Name]**: [Why it applies, how to use it]
2. **[Pattern Name]**: [Why it applies, how to use it]

### Pattern Selection Rationale
[Why these patterns were chosen over alternatives]

---

## Technology Evaluation

| Technology | Evaluated | Decision | Rationale |
|------------|-----------|----------|-----------|
| [Tech 1] | ✅ | SELECTED | [Why] |
| [Tech 2] | ✅ | REJECTED | [Why not] |

---

## Best Practices

1. **[Practice]**: [Description and application]
2. **[Practice]**: [Description and application]

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It's Harmful | What To Do Instead |
|--------------|------------------|-------------------|
| [Anti-pattern] | [Consequences] | [Better approach] |

---

## References

1. [Title](URL) - [Brief description]
2. [Title](URL) - [Brief description]
```

### data-model.md Template

```markdown
---
feature: "{featureName}"
document: "data-model"
created: "{timestamp}"
entities_count: {count}
relationships_count: {count}
---

# Data Model: {featureName}

## Entity Relationship Diagram

```
┌─────────────┐       ┌─────────────┐
│   Entity A  │──────<│   Entity B  │
├─────────────┤  1:N  ├─────────────┤
│ id: uuid    │       │ id: uuid    │
│ name: str   │       │ a_id: uuid  │
│ created: ts │       │ value: int  │
└─────────────┘       └─────────────┘
```

---

## Entities

### Entity A

| Attribute | Type | Constraints | Description |
|-----------|------|-------------|-------------|
| id | UUID | PK, NOT NULL | Primary identifier |
| name | VARCHAR(255) | NOT NULL, UNIQUE | Display name |
| created_at | TIMESTAMP | NOT NULL, DEFAULT NOW | Creation timestamp |
| updated_at | TIMESTAMP | ON UPDATE | Last modification |

**Indexes**:
- `idx_entity_a_name` (name) - For lookup by name
- `idx_entity_a_created` (created_at DESC) - For chronological queries

---

## Relationships

| From | To | Type | Description |
|------|----|------|-------------|
| Entity A | Entity B | 1:N | A owns many Bs |

---

## State Machines

### Entity A Lifecycle

```
┌─────────┐    create    ┌────────┐    activate   ┌────────┐
│  DRAFT  │─────────────▶│ PENDING│──────────────▶│ ACTIVE │
└─────────┘              └────────┘               └────────┘
                              │                        │
                              │ reject                 │ archive
                              ▼                        ▼
                         ┌────────┐              ┌──────────┐
                         │REJECTED│              │ ARCHIVED │
                         └────────┘              └──────────┘
```

---

## Validation Rules

| Entity | Rule | Enforcement |
|--------|------|-------------|
| Entity A | name must be unique | DB constraint + application |
| Entity B | value must be positive | Application validation |

---

## Migration Strategy

**v1 → v2 Changes**:
1. Add `status` column to Entity A
2. Migrate existing records to `ACTIVE` status
3. Add NOT NULL constraint after migration
```

### quickstart.md Template

```markdown
---
feature: "{featureName}"
document: "quickstart"
created: "{timestamp}"
estimated_setup_time: "{X minutes}"
difficulty_level: "BEGINNER|INTERMEDIATE|ADVANCED"
---

# Quickstart: {featureName}

## Prerequisites

- [ ] Node.js 18+ installed
- [ ] Project repository cloned
- [ ] Environment variables configured
- [ ] Database running (if applicable)

---

## Setup Steps

### 1. Install Dependencies

\`\`\`bash
npm install
\`\`\`

### 2. Configure Environment

\`\`\`bash
cp .env.example .env
# Edit .env with your values
\`\`\`

### 3. Initialize Feature

\`\`\`bash
npm run setup:{feature}
\`\`\`

---

## Key Concepts

### Concept 1: {Name}

[Explanation of core abstraction developers need to understand]

### Concept 2: {Name}

[Explanation of core abstraction developers need to understand]

---

## Common Tasks

### Task: {Common Operation}

\`\`\`typescript
// Example code
import { Feature } from './feature';

const result = await Feature.doSomething();
\`\`\`

---

## Testing

### Run Tests

\`\`\`bash
npm run test:{feature}
\`\`\`

### Write a Test

\`\`\`typescript
describe('{Feature}', () => {
  it('should do something', async () => {
    // Test code
  });
});
\`\`\`

---

## Debugging

### Common Issue 1: {Problem}

**Symptoms**: [What you see]
**Cause**: [Why it happens]
**Solution**: [How to fix]

---

## Architecture Overview

```
┌─────────────────────────────────────────┐
│                  API Layer              │
├─────────────────────────────────────────┤
│              Service Layer              │
├─────────────────────────────────────────┤
│            Repository Layer             │
├─────────────────────────────────────────┤
│               Database                  │
└─────────────────────────────────────────┘
```
```

---

## PHASE 5: TASKS — Task Breakdown

**Purpose**: Break implementation plan into atomic, assignable tasks.

**Entry Condition**: `plan.md` exists with status: complete
**Output Artifact**: `specs/NNN-feature-name/tasks.md`
**Exit Condition**: Tasks file exists with status: ready

### Execution Protocol

```javascript
async function executeTasksPhase(specDir) {
  // 1. Validate phase gate
  const canEnter = canEnterPhase('tasks', specDir);
  if (!canEnter.allowed) {
    throw new Error(`Cannot enter tasks phase: ${canEnter.reason}`);
  }

  // 2. Load plan
  const plan = await readFile(`${specDir}/plan.md`);

  // 3. Generate task breakdown using sub-agent
  const tasks = await Task({
    subagent_type: "general-purpose",
    prompt: `You are a task breakdown agent. Convert this implementation plan into atomic, executable tasks.

IMPLEMENTATION PLAN:
${plan}

Generate a task list where each task:
1. Has a unique ID (TASK-001, TASK-002, etc.)
2. Is atomic (can be completed in one work session)
3. Has clear acceptance criteria
4. Lists dependencies on other tasks
5. Is assignable (could be given to a developer or sub-agent)
6. Includes effort estimate
7. Has a [P] parallel marker if it can run independently

**PARALLEL TASK IDENTIFICATION [P]**:
Mark tasks with [P] in the title if ALL of these are true:
- No dependencies on other incomplete tasks
- No shared state mutations with concurrent tasks
- No file write conflicts with other tasks
- No database migration that must run first
- Can be tested independently

Example: "### TASK-001: Create user schema [P]" (parallel-safe)
Example: "### TASK-003: Implement registration" (depends on TASK-001, no [P])

**PARALLELIZATION CRITERIA**:
✅ Database schema tasks for different tables → [P]
✅ Independent API endpoints → [P]
✅ Separate UI components → [P]
✅ Utility function implementations → [P]
❌ Migration tasks → Sequential (no [P])
❌ Tasks depending on other tasks → Sequential (no [P])
❌ Shared resource modifications → Sequential (no [P])

**TEST SPECIFICATION REQUIREMENT** (Article III):
Each task MUST include a test specification in Given-When-Then format:
\`\`\`gherkin
Given [precondition]
When [action]
Then [expected outcome]
\`\`\`

Group tasks by phase from the plan.
Use the tasks template format with YAML frontmatter.
Include a "Parallel Execution Groups" section showing which [P] tasks can run together.
Set status to "ready" when complete.`,
    model: "haiku"
  });

  // 4. Write tasks.md
  await writeFile(`${specDir}/tasks.md`, tasks);

  // 5. Update phase state
  await updatePhaseState(specDir, 'tasks', 'complete');

  return {
    success: true,
    phase: 'tasks',
    nextPhase: 'implement'
  };
}
```

### Tasks Template

```markdown
---
feature: "{featureName}"
phase: "tasks"
status: "ready"
plan_hash: "{sha256-of-plan}"
created: "{timestamp}"
total_tasks: {count}
parallel_tasks: {count}        # Tasks marked with [P]
sequential_tasks: {count}      # Tasks without [P]
by_status:
  pending: {count}
  in_progress: 0
  completed: 0
  blocked: 0
by_priority:
  critical: {count}
  high: {count}
  medium: {count}
  low: {count}
parallel_groups:               # Groups of [P] tasks that can run together
  - group: 1
    tasks: ["TASK-001", "TASK-002"]
  - group: 2
    tasks: ["TASK-004"]
---

# Task List: {featureName}

## Summary

| Metric | Value |
|--------|-------|
| Total Tasks | {total} |
| Pending | {pending} |
| In Progress | {in_progress} |
| Completed | {completed} |
| Blocked | {blocked} |
| Ready for Implementation | YES |

---

## Phase 1 Tasks

### TASK-001: {Task Title} [P]

| Field | Value |
|-------|-------|
| **ID** | TASK-001 |
| **Phase** | 1 |
| **Priority** | CRITICAL / HIGH / MEDIUM / LOW |
| **Status** | pending |
| **Estimate** | {X hours} |
| **Parallel** | `[P]` - Can run independently |
| **Assignable** | YES |

**Description**:
[Detailed description of what needs to be done]

**Acceptance Criteria**:
- [ ] [Criterion 1]
- [ ] [Criterion 2]

**Dependencies**:
- Depends on: [None | TASK-XXX]
- Blocks: [TASK-XXX, TASK-YYY]

**Test Specification** (Article III Compliance):
```gherkin
Given [precondition]
When [action]
Then [expected outcome]
```

**Technical Notes**:
[Any implementation hints or constraints]

---

### TASK-002: {Task Title} [P]

| Field | Value |
|-------|-------|
| **ID** | TASK-002 |
| **Phase** | 1 |
| **Priority** | HIGH |
| **Status** | pending |
| **Estimate** | {X hours} |
| **Parallel** | `[P]` - Can run independently |
| **Assignable** | YES |

[Same structure as TASK-001]

---

### TASK-003: {Task Title}

| Field | Value |
|-------|-------|
| **ID** | TASK-003 |
| **Phase** | 1 |
| **Priority** | MEDIUM |
| **Status** | pending |
| **Estimate** | {X hours} |
| **Parallel** | NO - Depends on TASK-001, TASK-002 |
| **Assignable** | YES |

[Same structure - note: NO [P] marker because it has dependencies]

---

## Phase 2 Tasks

### TASK-004: {Task Title} [P]

[Same structure with [P] marker if parallel-safe]

---

## Parallel Task Notation

**`[P]` Marker Meaning**: Task can be executed in parallel with other `[P]` tasks in the same phase.

**Parallelization Criteria**:
- ✅ No shared state mutations
- ✅ No file write conflicts
- ✅ No database migration dependencies
- ✅ No API contract dependencies on other tasks
- ✅ Can be tested independently

**Tasks WITHOUT `[P]`**: Must wait for dependencies to complete before starting.

---

## Task Dependency Graph

```
[P] TASK-001 ─────┬─────▶ TASK-003
                  │
[P] TASK-002 ─────┴─────▶ [P] TASK-004 ─────▶ TASK-005
```

**Legend**:
- `[P]` = Parallel-safe (can run with other [P] tasks)
- `──▶` = Dependency (must complete before next)

---

## Critical Path

**Tasks on critical path (no slack):**
1. TASK-001 → TASK-003 → TASK-005

**Parallel Execution Groups**:

| Group | Tasks | Can Run With |
|-------|-------|--------------|
| P1 | TASK-001 [P], TASK-002 [P] | Each other |
| P2 | TASK-004 [P] | After P1 completes |
| SEQ | TASK-003, TASK-005 | Sequential only |

---

## Execution Order (Recommended)

**Batch 1 (Parallel)** - All `[P]` tasks with no dependencies:
- [P] TASK-001
- [P] TASK-002

**Batch 2 (After Batch 1)** - Tasks depending on Batch 1:
- TASK-003
- [P] TASK-004

**Batch 3 (Sequential)** - Final tasks:
- TASK-005

---

**Tasks Hash**: {sha256-hash}
**Ready for Tests**: YES
```

---

## PHASE 5.5: ANALYZE — Cross-Artifact Validation (Optional but Recommended)

**Purpose**: Validate consistency and coverage across all artifacts before tests.

**Entry Condition**: `tasks.md` exists with status: ready
**Output Artifact**: `specs/NNN-feature-name/analysis.md` (optional)
**Exit Condition**: Validation passes OR issues documented for resolution

### Execution Protocol

```javascript
async function executeAnalyzePhase(specDir) {
  // Load all artifacts
  const artifacts = {
    constitution: await readFile(`${specDir}/constitution.md`),
    spec: await readFile(`${specDir}/spec.md`),
    clarifications: await readFile(`${specDir}/clarifications.md`),
    plan: await readFile(`${specDir}/plan.md`),
    tasks: await readFile(`${specDir}/tasks.md`)
  };

  const analysis = {
    specToConstitution: validateSpecAgainstConstitution(artifacts),
    planToSpec: validatePlanAgainstSpec(artifacts),
    tasksToPlan: validateTasksAgainstPlan(artifacts),
    orphanedRequirements: findOrphanedRequirements(artifacts),
    missingCoverage: findMissingCoverage(artifacts),
    inconsistencies: findInconsistencies(artifacts),
    articleCompliance: validateArticleCompliance(artifacts)
  };

  // Check for issues
  const issues = [
    ...analysis.orphanedRequirements,
    ...analysis.missingCoverage,
    ...analysis.inconsistencies,
    ...analysis.articleCompliance.violations
  ];

  if (issues.length > 0) {
    await writeFile(`${specDir}/analysis.md`, formatAnalysisReport(analysis));
    return {
      success: false,
      issues: issues,
      recommendation: 'Resolve issues before proceeding to TESTS phase'
    };
  }

  return { success: true, phase: 'analyze', status: 'passed' };
}

function validateArticleCompliance(artifacts) {
  const violations = [];

  // Article I: Library-First
  if (!artifacts.plan.includes('libs/') && !artifacts.plan.includes('packages/')) {
    violations.push({
      article: 'I',
      issue: 'Plan does not specify library-first structure',
      severity: 'HIGH'
    });
  }

  // Article III: Test-First
  const testTasks = extractTasks(artifacts.tasks).filter(t =>
    t.description.toLowerCase().includes('test'));
  if (testTasks.length === 0) {
    violations.push({
      article: 'III',
      issue: 'No test tasks defined - Test-First Imperative violated',
      severity: 'CRITICAL'
    });
  }

  // Article VII: Simplicity
  const phases = extractPhases(artifacts.plan);
  if (phases.length > 3) {
    violations.push({
      article: 'VII',
      issue: `Plan has ${phases.length} phases, exceeds Simplicity Principle (max 3)`,
      severity: 'MEDIUM',
      requiresJustification: true
    });
  }

  return { violations };
}
```

### Analysis Report Template

```markdown
---
feature: "{featureName}"
phase: "analysis"
status: "complete"
issues_found: {count}
critical_issues: {count}
---

# Cross-Artifact Analysis: {featureName}

## Consistency Validation

### Specification ↔ Constitution
- [x] All constitutional articles referenced
- [x] No spec conflicts with constitution
- [ ] Issue: [Description of any inconsistency]

### Plan ↔ Specification
- [x] All requirements have plan coverage
- [x] No orphaned requirements
- [ ] Issue: [Description of any inconsistency]

### Tasks ↔ Plan
- [x] All plan phases have tasks
- [x] Task dependencies match plan dependencies
- [ ] Issue: [Description of any inconsistency]

## Article Compliance

| Article | Status | Notes |
|---------|--------|-------|
| I. Library-First | ✅/❌ | [Details] |
| II. CLI Interface | ✅/❌ | [Details] |
| III. Test-First | ✅/❌ | [Details] |
| IV. Spec Sovereignty | ✅/❌ | [Details] |
| V. Clarification | ✅/❌ | [Details] |
| VI. Progressive | ✅/❌ | [Details] |
| VII. Simplicity | ✅/❌ | [Details] |
| VIII. Anti-Abstraction | ✅/❌ | [Details] |
| IX. Integration-First | ✅/❌ | [Details] |

## Issues Requiring Resolution

### CRITICAL
[List any critical issues blocking progress]

### HIGH
[List high-priority issues]

### MEDIUM
[List medium-priority issues]

## Recommendations

[Specific actions to resolve issues before proceeding]
```

---

## PHASE 6: TESTS — Test-First Implementation (Article III Enforcement)

**Purpose**: Write tests BEFORE implementation. Confirm tests FAIL (RED phase).

**Entry Condition**: `tasks.md` exists with status: ready
**Output Artifact**: `specs/NNN-feature-name/tests.md`
**Exit Condition**: All tests written AND confirmed FAILING (RED status)

### Execution Protocol

```javascript
async function executeTestsPhase(specDir) {
  // 1. Validate phase gate
  const canEnter = canEnterPhase('tests', specDir);
  if (!canEnter.allowed) {
    throw new Error(`Cannot enter tests phase: ${canEnter.reason}`);
  }

  // 2. Load task specifications
  const tasks = await readFile(`${specDir}/tasks.md`);
  const taskList = extractTasks(tasks);

  // 3. Generate test specifications in required order (Article IX)
  const testOrder = ['contract', 'integration', 'e2e', 'unit'];

  const testSpecs = {
    contract: await generateContractTests(taskList, specDir),
    integration: await generateIntegrationTests(taskList, specDir),
    e2e: await generateE2ETests(taskList, specDir),
    unit: await generateUnitTests(taskList, specDir)
  };

  // 4. Write test files
  for (const testType of testOrder) {
    await writeTestFiles(specDir, testType, testSpecs[testType]);
  }

  // 5. Run tests - MUST FAIL (RED phase)
  const testResults = await runTestsInOrder(specDir, testOrder);

  // 6. Validate RED status
  const redConfirmation = validateRedPhase(testResults);

  if (!redConfirmation.allTestsFailing) {
    // PROBLEM: Some tests are passing - they shouldn't yet!
    return {
      success: false,
      phase: 'tests',
      issue: 'Tests should FAIL before implementation exists',
      passingTests: redConfirmation.passingTests,
      action: 'Remove implementations or fix test expectations'
    };
  }

  // 7. Write tests.md with RED confirmation
  await writeFile(`${specDir}/tests.md`, formatTestsDocument({
    testSpecs: testSpecs,
    redConfirmation: redConfirmation,
    status: 'RED_CONFIRMED'
  }));

  // 8. User approval for RED phase
  const userApproval = await AskUserQuestion({
    questions: [{
      question: `All ${redConfirmation.totalTests} tests are FAILING (RED). Approve to proceed to implementation?`,
      header: "RED Phase",
      options: [
        { label: "Approve", description: "Proceed to IMPLEMENT phase" },
        { label: "Review", description: "Show me the failing tests" },
        { label: "Modify", description: "I want to change some tests" }
      ],
      multiSelect: false
    }]
  });

  if (userApproval !== 'Approve') {
    return {
      success: false,
      phase: 'tests',
      status: 'awaiting_user_review',
      testSpecs: testSpecs
    };
  }

  return {
    success: true,
    phase: 'tests',
    status: 'RED_CONFIRMED',
    nextPhase: 'implement'
  };
}

function validateRedPhase(testResults) {
  const passingTests = testResults.filter(t => t.status === 'passed');
  const failingTests = testResults.filter(t => t.status === 'failed');

  return {
    allTestsFailing: passingTests.length === 0,
    totalTests: testResults.length,
    passingTests: passingTests.map(t => t.name),
    failingTests: failingTests.map(t => t.name),
    redStatus: passingTests.length === 0 ? 'CONFIRMED' : 'INVALID'
  };
}
```

### Tests Document Template

```markdown
---
feature: "{featureName}"
phase: "tests"
status: "RED_CONFIRMED"
tasks_hash: "{sha256-of-tasks}"
created: "{timestamp}"
red_confirmed_at: "{timestamp}"
total_tests: {count}
by_type:
  contract: {count}
  integration: {count}
  e2e: {count}
  unit: {count}
---

# Test Specifications: {featureName}

## RED Phase Confirmation

| Metric | Value |
|--------|-------|
| Total Tests | {count} |
| Passing | 0 (Required for RED) |
| Failing | {count} |
| RED Status | ✅ CONFIRMED |
| User Approved | {timestamp} |

---

## Test Execution Order (Article IX)

```
1. Contract Tests    → Define API boundaries first
2. Integration Tests → Verify system interactions
3. E2E Tests         → Validate user flows
4. Unit Tests        → Verify individual functions
```

---

## 1. Contract Tests

### CT-001: {Contract Test Name}

**Purpose**: [What API contract this validates]
**Endpoint/Interface**: [API endpoint or interface being tested]

```typescript
// Test file: tests/contracts/{feature}.contract.test.ts
describe('{Contract}', () => {
  it('should {expectation}', () => {
    // Arrange
    // Act
    // Assert
  });
});
```

**RED Status**: ❌ FAILING (Expected - no implementation yet)
**Expected Error**: [Expected error message]

---

## 2. Integration Tests

### IT-001: {Integration Test Name}

**Purpose**: [What system interaction this validates]
**Systems Involved**: [List of systems/services]

```typescript
// Test file: tests/integration/{feature}.integration.test.ts
describe('{Integration}', () => {
  it('should {expectation}', () => {
    // Arrange (real database/services)
    // Act
    // Assert
  });
});
```

**RED Status**: ❌ FAILING
**Expected Error**: [Expected error message]

---

## 3. E2E Tests

### E2E-001: {E2E Test Name}

**Purpose**: [What user flow this validates]
**User Story**: [Reference to user story]

```typescript
// Test file: tests/e2e/{feature}.e2e.test.ts
describe('{User Flow}', () => {
  it('should allow user to {action}', () => {
    // Simulate complete user journey
  });
});
```

**RED Status**: ❌ FAILING
**Expected Error**: [Expected error message]

---

## 4. Unit Tests

### UT-001: {Unit Test Name}

**Purpose**: [What function/module this validates]
**Function**: [Function being tested]

```typescript
// Test file: tests/unit/{module}.unit.test.ts
describe('{Function}', () => {
  it('should {expectation}', () => {
    expect(functionUnderTest(input)).toBe(expected);
  });
});
```

**RED Status**: ❌ FAILING
**Expected Error**: [Expected error message]

---

## Implementation Acceptance Criteria

**GREEN Phase will be achieved when:**
- [ ] All contract tests pass
- [ ] All integration tests pass
- [ ] All E2E tests pass
- [ ] All unit tests pass
- [ ] No test modifications during implementation (test spec is frozen)

---

**Tests Hash**: {sha256-hash}
**Ready for Implementation**: YES (RED CONFIRMED)
```

---

## PHASE 7: IMPLEMENT — Execution (GREEN Phase)

**Purpose**: Make all tests pass (GREEN). Execute via SYNRG Director delegation.

**Entry Condition**: `tests.md` exists with status: RED_CONFIRMED
**Output Artifact**: `specs/NNN-feature-name/implementation.log`
**Exit Condition**: All tests GREEN, all tasks marked complete

### Execution Protocol

```javascript
async function executeImplementPhase(specDir) {
  // 1. Validate phase gate
  const canEnter = canEnterPhase('implement', specDir);
  if (!canEnter.allowed) {
    throw new Error(`Cannot enter implement phase: ${canEnter.reason}`);
  }

  // 2. Load all artifacts for context
  const constitution = await readFile(`${specDir}/constitution.md`);
  const spec = await readFile(`${specDir}/spec.md`);
  const clarifications = await readFile(`${specDir}/clarifications.md`);
  const plan = await readFile(`${specDir}/plan.md`);
  const tasks = await readFile(`${specDir}/tasks.md`);

  // 3. Extract task list
  const taskList = extractTasks(tasks);
  const pendingTasks = taskList.filter(t => t.status === 'pending');

  // 4. Initialize implementation log
  const logPath = `${specDir}/implementation.log`;
  await initializeImplementationLog(logPath, {
    featureName: getFeatureName(specDir),
    totalTasks: taskList.length,
    startedAt: new Date().toISOString()
  });

  // 5. Execute tasks in dependency order via SYNRG Director
  for (const batch of groupTasksByDependency(pendingTasks)) {
    // Execute batch in parallel
    const results = await Promise.all(batch.map(async task => {
      // Log task start
      await appendToLog(logPath, {
        event: 'task_started',
        taskId: task.id,
        timestamp: new Date().toISOString()
      });

      // Execute via SYNRG
      const result = await executeTaskViaSYNRG(task, {
        constitution,
        spec,
        clarifications,
        plan
      });

      // Log task completion
      await appendToLog(logPath, {
        event: result.success ? 'task_completed' : 'task_failed',
        taskId: task.id,
        timestamp: new Date().toISOString(),
        result: result
      });

      // Update task status in tasks.md
      await updateTaskStatus(specDir, task.id,
        result.success ? 'completed' : 'failed');

      return result;
    }));

    // Check for failures
    const failures = results.filter(r => !r.success);
    if (failures.length > 0) {
      await appendToLog(logPath, {
        event: 'batch_failure',
        failures: failures,
        timestamp: new Date().toISOString()
      });
      // Handle failure - could pause or continue based on config
    }
  }

  // 6. Finalize
  const finalTasks = await readFile(`${specDir}/tasks.md`);
  const finalTaskList = extractTasks(finalTasks);
  const completedCount = finalTaskList.filter(t => t.status === 'completed').length;

  const success = completedCount === finalTaskList.length;

  await appendToLog(logPath, {
    event: 'implementation_complete',
    success: success,
    completedTasks: completedCount,
    totalTasks: finalTaskList.length,
    completedAt: new Date().toISOString()
  });

  if (success) {
    await updatePhaseState(specDir, 'implement', 'complete');
  }

  return {
    success: success,
    phase: 'implement',
    completedTasks: completedCount,
    totalTasks: finalTaskList.length,
    nextPhase: success ? 'complete' : null
  };
}

async function executeTaskViaSYNRG(task, context) {
  // Delegate to SYNRG Director for actual implementation
  return await Task({
    subagent_type: "general-purpose",
    prompt: `Execute this implementation task following SYNRG robustness-first principles.

TASK:
${JSON.stringify(task, null, 2)}

CONTEXT:
- Constitution: ${context.constitution.substring(0, 500)}...
- Spec Summary: ${extractSummary(context.spec)}
- Key Clarifications: ${extractKeyClarifications(context.clarifications)}
- Plan Phase: ${extractRelevantPhase(context.plan, task.phase)}

REQUIREMENTS:
1. Follow constitutional articles
2. Implement according to specification
3. Respect clarification decisions
4. Follow the plan
5. Meet all acceptance criteria
6. Report success/failure with evidence

Execute the task and report results.`,
    model: "sonnet"
  });
}
```

### Implementation Log Format

```markdown
---
feature: "{featureName}"
phase: "implementation"
status: "in_progress"
tasks_hash: "{sha256-of-tasks}"
started_at: "{timestamp}"
completed_at: null
total_tasks: {count}
completed_tasks: 0
failed_tasks: 0
---

# Implementation Log: {featureName}

## Execution Summary

| Metric | Value |
|--------|-------|
| Started | {timestamp} |
| Completed | {timestamp or "In Progress"} |
| Total Tasks | {count} |
| Completed | {count} |
| Failed | {count} |
| Success Rate | {percentage} |

---

## Execution Timeline

### {timestamp} - Implementation Started
- Total tasks: {count}
- Batches planned: {count}

### {timestamp} - TASK-001 Started
- Task: {title}
- Phase: 1

### {timestamp} - TASK-001 Completed
- Status: SUCCESS
- Duration: {duration}
- Evidence: [link or description]

### {timestamp} - TASK-002 Started
- Task: {title}

### {timestamp} - TASK-002 Failed
- Status: FAILED
- Error: {error message}
- Root Cause: {analysis}
- Retry: {YES/NO}

---

## Final Status

**Implementation**: {COMPLETE / PARTIAL / FAILED}

**Completed Tasks**:
- [x] TASK-001: {title}
- [x] TASK-003: {title}

**Failed Tasks**:
- [ ] TASK-002: {title} - {reason}

**Acceptance Criteria**:
- [x] All phase 1 deliverables produced
- [ ] All phase 2 deliverables produced
- [ ] All tests passing

---

**Implementation Hash**: {sha256-hash}
```

---

## STATUS Subcommand

**Purpose**: Display current phase and progress for a spec.

```javascript
async function executeStatusSubcommand(featureName) {
  const specDir = findSpecDir(featureName);

  if (!specDir) {
    return { error: `Spec not found: ${featureName}` };
  }

  const currentPhase = getCurrentPhase(specDir);
  const phaseState = await readFile(`${specDir}/.phase-state.json`);

  // Check each phase artifact
  const phaseStatus = {};
  for (const phase of PHASES) {
    const artifact = PHASE_ARTIFACTS[phase];
    if (artifact && fileExists(`${specDir}/${artifact}`)) {
      const content = await readFile(`${specDir}/${artifact}`);
      const frontmatter = parseYAMLFrontmatter(content);
      phaseStatus[phase] = {
        exists: true,
        status: frontmatter.status,
        completedAt: frontmatter.completed_at
      };
    } else {
      phaseStatus[phase] = { exists: false };
    }
  }

  return {
    featureName: featureName,
    specDir: specDir,
    currentPhase: currentPhase,
    phaseStatus: phaseStatus,
    nextAction: getNextAction(currentPhase, phaseStatus)
  };
}
```

### Status Output Format

```
SYNRG-SPEC Status: {featureName}
================================

Directory: specs/001-{featureName}/
Current Phase: CLARIFY

Phase Progress:
  [x] INIT        - complete (2025-12-11 10:00)
  [x] SPECIFY     - complete (2025-12-11 10:15)
  [~] CLARIFY     - in_progress (3/5 questions answered)
  [ ] PLAN        - pending
  [ ] TASKS       - pending
  [ ] IMPLEMENT   - pending

Next Action: Run `/synrg-spec clarify {featureName}` to continue Q&A

Files:
  - constitution.md  [COMPLETE]
  - spec.md          [COMPLETE]
  - clarifications.md [IN PROGRESS - 2 pending]
  - plan.md          [NOT STARTED]
  - tasks.md         [NOT STARTED]
```

---

## CONTINUE Subcommand

**Purpose**: Auto-detect current phase and proceed through remaining phases.

```javascript
async function executeContinueSubcommand(featureName) {
  const specDir = findSpecDir(featureName);

  if (!specDir) {
    return { error: `Spec not found: ${featureName}` };
  }

  let currentPhase = getCurrentPhase(specDir);

  while (currentPhase !== 'complete') {
    console.log(`\n=== Executing Phase: ${currentPhase.toUpperCase()} ===\n`);

    // Execute current phase
    const result = await executePhase(currentPhase, specDir);

    if (!result.success) {
      console.log(`Phase ${currentPhase} did not complete: ${result.reason}`);

      // If clarify phase and has pending questions, prompt user
      if (currentPhase === 'clarify' && result.reason?.includes('pending')) {
        const continueAsk = await AskUserQuestion({
          questions: [{
            question: "Clarification phase has pending questions. Continue answering?",
            header: "Continue?",
            options: [
              { label: "Yes", description: "Continue answering questions" },
              { label: "No", description: "Stop here and resume later" }
            ],
            multiSelect: false
          }]
        });

        if (continueAsk === 'No') {
          return {
            status: 'paused',
            phase: currentPhase,
            resumeWith: `/synrg-spec continue ${featureName}`
          };
        }
        // Continue with clarify phase
        continue;
      }

      return {
        status: 'failed',
        phase: currentPhase,
        reason: result.reason
      };
    }

    // Move to next phase
    currentPhase = result.nextPhase || getCurrentPhase(specDir);

    // Ask user before proceeding to next phase (optional - can be configured)
    if (currentPhase !== 'complete') {
      console.log(`\nPhase ${result.phase} complete. Next: ${currentPhase}`);
    }
  }

  return {
    status: 'complete',
    message: `All phases complete for ${featureName}. Implementation finished.`
  };
}

async function executePhase(phase, specDir) {
  switch (phase) {
    case 'init':
      // Init is handled separately (needs featureName + objective)
      return { success: true, nextPhase: 'specify' };
    case 'specify':
      return await executeSpecifyPhase(specDir);
    case 'clarify':
      return await executeClarifyPhase(specDir);
    case 'plan':
      return await executePlanPhase(specDir);
    case 'tasks':
      return await executeTasksPhase(specDir);
    case 'implement':
      return await executeImplementPhase(specDir);
    default:
      return { success: false, reason: `Unknown phase: ${phase}` };
  }
}
```

---

## Error Handling & Recovery

### Phase Failure Protocol

```javascript
async function handlePhaseFailure(phase, error, specDir) {
  // 1. Log failure
  await appendToPhaseLog(specDir, {
    phase: phase,
    event: 'failure',
    error: error.message,
    timestamp: new Date().toISOString()
  });

  // 2. Determine recovery strategy
  const recovery = determineRecoveryStrategy(phase, error);

  switch (recovery.strategy) {
    case 'retry':
      // Retry the phase
      return { action: 'retry', phase: phase };

    case 'rollback':
      // Rollback to previous phase
      await rollbackToPhase(specDir, recovery.targetPhase);
      return { action: 'rollback', targetPhase: recovery.targetPhase };

    case 'manual':
      // Requires manual intervention
      return {
        action: 'manual',
        phase: phase,
        instructions: recovery.instructions
      };

    case 'abort':
      // Fatal error - cannot continue
      return { action: 'abort', reason: error.message };
  }
}
```

### Rollback Protocol

```javascript
async function rollbackToPhase(specDir, targetPhase) {
  const phaseIndex = PHASES.indexOf(targetPhase);

  // Remove artifacts for phases after targetPhase
  for (let i = phaseIndex + 1; i < PHASES.length; i++) {
    const phase = PHASES[i];
    const artifact = PHASE_ARTIFACTS[phase];

    if (artifact && fileExists(`${specDir}/${artifact}`)) {
      // Backup before removing
      await moveFile(
        `${specDir}/${artifact}`,
        `${specDir}/rollback/${artifact}.${Date.now()}`
      );
    }
  }

  // Update phase state
  await updatePhaseState(specDir, targetPhase, 'pending');

  return { success: true, currentPhase: targetPhase };
}
```

---

## Integration with SYNRG Ecosystem

### Using with /synrg

When the `implement` phase delegates to SYNRG Director:

```javascript
// The implement phase can invoke the full /synrg command
const synrgResult = await SlashCommand({
  command: `/synrg Execute tasks for ${featureName} following the spec-driven plan`
});
```

### Using with /synrg-refactor

If implementation requires refactoring:

```javascript
// Can delegate to synrg-refactor for structural changes
const refactorResult = await SlashCommand({
  command: `/synrg-refactor Restructure codebase for ${featureName} implementation`
});
```

### Anti-Memory Protocol Integration

**This command embeds Anti-Memory Protocol by design:**
- All state in Markdown files (not agent memory)
- Hash chains verify artifact integrity
- Clarification phase forces explicit verification
- No assumptions allowed without documentation

---

## Command Entry Point

**When `/synrg-spec` is invoked, parse arguments and dispatch:**

```javascript
async function synrgSpecMain(args) {
  // Parse flags first
  const { flags, positional } = parseFlags(args);
  const [subcommand, ...rest] = positional;
  const featureOrObjective = rest.join(' ');

  // Options object from flags
  const options = {
    brownfield: flags.includes('--brownfield'),
    branch: flags.includes('--branch')
  };

  switch (subcommand) {
    case 'init':
      // Need feature name and objective
      if (!featureOrObjective) {
        // Interactive mode - ask for details
        const details = await gatherInitDetails();
        if (options.brownfield) {
          return await executeBrownfieldInit(details.specDir, details.objective);
        }
        return await executeInitPhaseWithBranch(details.name, details.objective, options);
      }
      if (options.brownfield) {
        const specDir = await createSpecDir(featureOrObjective);
        return await executeBrownfieldInit(specDir, featureOrObjective);
      }
      return await executeInitPhaseWithBranch(featureOrObjective, featureOrObjective, options);

    case 'specify':
      return await executeSpecifyPhase(findSpecDir(featureOrObjective));

    case 'clarify':
      return await executeClarifyPhase(findSpecDir(featureOrObjective));

    case 'plan':
      return await executePlanPhase(findSpecDir(featureOrObjective));

    case 'tasks':
      return await executeTasksPhase(findSpecDir(featureOrObjective));

    case 'tests':
      return await executeTestsPhase(findSpecDir(featureOrObjective));

    case 'implement':
      return await executeImplementPhase(findSpecDir(featureOrObjective));

    case 'status':
      return await executeStatusSubcommand(featureOrObjective);

    case 'continue':
      return await executeContinueSubcommand(featureOrObjective);

    case 'checklist':
      return await executeChecklistSubcommand(featureOrObjective);

    case 'analyze':
      return await executeAnalyzeSubcommand(featureOrObjective);

    case 'regenerate':
      return await executeRegenerateSubcommand(featureOrObjective, flags);

    default:
      // If no subcommand, assume it's an objective for init
      if (subcommand) {
        const fullObjective = [subcommand, ...rest].join(' ');
        const name = slugify(fullObjective.substring(0, 50));
        if (options.brownfield) {
          const specDir = await createSpecDir(name);
          return await executeBrownfieldInit(specDir, fullObjective);
        }
        return await executeInitPhaseWithBranch(name, fullObjective, options);
      }

      return showHelp();
  }
}

// Parse flags from arguments
function parseFlags(args) {
  const flags = [];
  const positional = [];

  for (const arg of args) {
    if (arg.startsWith('--')) {
      flags.push(arg);
    } else {
      positional.push(arg);
    }
  }

  return { flags, positional };
}

// Regenerate subcommand implementation
async function executeRegenerateSubcommand(featureName, flags) {
  const specDir = findSpecDir(featureName);
  if (!specDir) {
    return { success: false, error: `Spec not found: ${featureName}` };
  }

  // Parse regeneration mode from flags
  let mode = 'incremental'; // default
  if (flags.includes('full') || flags.some(f => f.includes('full'))) {
    mode = 'full';
  } else if (flags.includes('validate') || flags.some(f => f.includes('validate'))) {
    mode = 'validate';
  } else if (flags.includes('force') || flags.some(f => f.includes('force'))) {
    mode = 'force';
  }

  console.log(`\n🔄 Regeneration Mode: ${mode.toUpperCase()}`);
  console.log(`   Feature: ${featureName}\n`);

  // Check staleness for all artifacts
  const staleness = await checkAllArtifacts(specDir);

  if (mode === 'validate') {
    // Just report, don't regenerate
    console.log('Staleness Report:');
    for (const [artifact, status] of Object.entries(staleness)) {
      const icon = status.stale ? '⚠️ STALE' : '✅ VALID';
      console.log(`  ${icon}: ${artifact}`);
      if (status.stale) {
        console.log(`       Reason: ${status.reason}`);
      }
    }
    return { success: true, mode: 'validate', staleness };
  }

  if (mode === 'full') {
    // Regenerate all from spec down
    console.log('Full regeneration cascade:');
    await runPhase('specify', specDir);
    await runPhase('clarify', specDir);
    await runPhase('plan', specDir);
    await runPhase('tasks', specDir);
    await runPhase('tests', specDir);
    console.log('✅ Full regeneration complete');
    return { success: true, mode: 'full' };
  }

  if (mode === 'incremental' || mode === 'force') {
    // Only regenerate stale artifacts (or all if force)
    const toRegenerate = mode === 'force'
      ? Object.keys(staleness)
      : Object.entries(staleness).filter(([_, s]) => s.stale).map(([k]) => k);

    if (toRegenerate.length === 0) {
      console.log('✅ All artifacts up-to-date. No regeneration needed.');
      return { success: true, mode, regenerated: [] };
    }

    console.log(`Regenerating ${toRegenerate.length} artifact(s)...`);
    for (const artifact of toRegenerate) {
      await regenerateArtifact(artifact, specDir);
      console.log(`  ✅ ${artifact}`);
    }

    return { success: true, mode, regenerated: toRegenerate };
  }
}

function showHelp() {
  return `
SYNRG Spec-Driven Development

Usage: /synrg-spec [subcommand] [feature-name or objective] [flags]

Subcommands:
  init [name]        Initialize new spec with constitutional articles
  specify [name]     Generate detailed specification
  clarify [name]     Run clarification Q&A cycle
  plan [name]        Generate implementation plan
  analyze [name]     Cross-validate all artifacts for consistency
  tasks [name]       Break plan into atomic tasks
  tests [name]       Generate tests (RED phase - must fail)
  implement [name]   Execute tasks via SYNRG Director (GREEN phase)
  status [name]      Show current phase and progress
  continue [name]    Auto-continue from current phase
  checklist [name]   Generate quality validation checklist
  regenerate [name]  Refresh stale artifacts (use with modes below)

Flags:
  --brownfield       Enable brownfield mode (analyze existing codebase first)
  --branch           Auto-generate feature branch name

Regenerate Modes:
  incremental        Only regenerate stale artifacts (default)
  full               Regenerate all downstream from spec
  validate           Check staleness without regenerating
  force              Regenerate all regardless of staleness

Examples:
  /synrg-spec init user-authentication
  /synrg-spec init --brownfield improve-checkout-performance
  /synrg-spec init --branch payment-gateway-v2
  /synrg-spec continue user-authentication
  /synrg-spec status user-authentication
  /synrg-spec regenerate user-authentication incremental
  /synrg-spec regenerate user-authentication validate
  /synrg-spec Add dark mode toggle to settings

Phase Order (MANDATORY - 7 Phases):
  1. init → 2. specify → 3. clarify → 4. plan → 5. tasks → 6. tests (RED) → 7. implement (GREEN)

Test-First Flow (Article III):
  TASKS → TESTS (write) → RED (confirm fail) → IMPLEMENT → GREEN (confirm pass)

Phases cannot be skipped. Each phase validates that the previous phase is complete.
`;
}
```

---

## Cross-Artifact Checklist Generation

**Purpose**: Generate comprehensive validation checklists by analyzing all spec artifacts for quality assurance.

### Checklist Subcommand Implementation

```javascript
async function executeChecklistSubcommand(featureName) {
  const specDir = findSpecDir(featureName);
  if (!specDir) {
    return { success: false, error: `Spec not found: ${featureName}` };
  }

  // Determine current phase and generate appropriate checklist
  const state = await getPhaseState(specDir);
  const checklist = await generateCrossArtifactChecklist(specDir, state.currentPhase);

  // Write checklist to file
  const checklistPath = `${specDir}/checklist-${state.currentPhase}.md`;
  await writeFile(checklistPath, formatChecklistDocument(checklist));

  console.log(`\n✅ Checklist generated: ${checklistPath}`);
  console.log(`\n${checklist.summary}`);

  return { success: true, checklist, path: checklistPath };
}

// Cross-artifact checklist generator
async function generateCrossArtifactChecklist(specDir, phase) {
  // Load all available artifacts
  const artifacts = await loadAllArtifacts(specDir);

  // Generate phase-specific checklist
  const checklist = {
    phase: phase,
    generated: new Date().toISOString(),
    sections: [],
    totalItems: 0,
    criticalItems: 0,
    summary: ''
  };

  // 1. Constitutional Compliance Check
  if (artifacts.constitution) {
    checklist.sections.push(await checkConstitutionalCompliance(artifacts));
  }

  // 2. Specification Completeness Check
  if (artifacts.spec) {
    checklist.sections.push(await checkSpecCompleteness(artifacts.spec));
  }

  // 3. Clarification Resolution Check
  if (artifacts.clarifications) {
    checklist.sections.push(await checkClarificationResolution(artifacts.clarifications));
  }

  // 4. Plan-to-Spec Traceability Check
  if (artifacts.plan && artifacts.spec) {
    checklist.sections.push(await checkPlanTraceability(artifacts.plan, artifacts.spec));
  }

  // 5. Task-to-Plan Traceability Check
  if (artifacts.tasks && artifacts.plan) {
    checklist.sections.push(await checkTaskTraceability(artifacts.tasks, artifacts.plan));
  }

  // 6. Test Coverage Check (if tests exist)
  if (artifacts.tests) {
    checklist.sections.push(await checkTestCoverage(artifacts.tests, artifacts.spec));
  }

  // Calculate totals
  for (const section of checklist.sections) {
    checklist.totalItems += section.items.length;
    checklist.criticalItems += section.items.filter(i => i.critical).length;
  }

  checklist.summary = generateChecklistSummary(checklist);

  return checklist;
}

// Constitutional compliance validation
async function checkConstitutionalCompliance(artifacts) {
  const { constitution, spec, plan, tasks } = artifacts;

  const items = [];

  // Extract constitutional articles
  const articles = extractConstitutionalArticles(constitution);

  for (const article of articles) {
    // Check spec compliance
    if (spec) {
      items.push({
        id: `CONST-SPEC-${article.id}`,
        description: `Spec complies with Article ${article.id}: ${article.title}`,
        critical: true,
        status: 'PENDING', // To be checked
        artifact: 'spec.md',
        requirement: article.text
      });
    }

    // Check plan compliance
    if (plan) {
      items.push({
        id: `CONST-PLAN-${article.id}`,
        description: `Plan respects Article ${article.id}: ${article.title}`,
        critical: true,
        status: 'PENDING',
        artifact: 'plan.md',
        requirement: article.text
      });
    }
  }

  return {
    name: 'Constitutional Compliance',
    description: 'Verify all artifacts comply with immutable constitutional articles',
    items
  };
}

// Specification completeness check
async function checkSpecCompleteness(spec) {
  const requiredSections = [
    { id: 'user-scenarios', name: 'User Scenarios', critical: true },
    { id: 'functional-requirements', name: 'Functional Requirements', critical: true },
    { id: 'non-functional-requirements', name: 'Non-Functional Requirements', critical: false },
    { id: 'architecture', name: 'Architecture Overview', critical: false },
    { id: 'interfaces', name: 'External Interfaces', critical: false },
    { id: 'data-model', name: 'Data Model', critical: false },
    { id: 'constraints', name: 'Constraints', critical: true },
    { id: 'assumptions', name: 'Assumptions', critical: true },
    { id: 'dependencies', name: 'Dependencies', critical: true },
    { id: 'open-questions', name: 'Open Questions', critical: true }
  ];

  const items = [];

  for (const section of requiredSections) {
    const exists = spec.includes(`## ${section.name}`) ||
                   spec.includes(`### ${section.name}`);

    items.push({
      id: `SPEC-${section.id.toUpperCase()}`,
      description: `Spec contains ${section.name} section`,
      critical: section.critical,
      status: exists ? 'PASS' : 'FAIL',
      artifact: 'spec.md'
    });
  }

  // Check for [NEEDS CLARIFICATION] markers
  const needsClarification = (spec.match(/\[NEEDS CLARIFICATION\]/g) || []).length;
  items.push({
    id: 'SPEC-NO-PENDING',
    description: 'No unresolved [NEEDS CLARIFICATION] markers',
    critical: true,
    status: needsClarification === 0 ? 'PASS' : 'FAIL',
    count: needsClarification,
    artifact: 'spec.md'
  });

  // Check for user story IDs
  const userStories = (spec.match(/US\d+/g) || []);
  items.push({
    id: 'SPEC-USER-STORIES',
    description: 'User stories have traceable IDs (US1, US2, etc.)',
    critical: true,
    status: userStories.length > 0 ? 'PASS' : 'FAIL',
    count: userStories.length,
    artifact: 'spec.md'
  });

  return {
    name: 'Specification Completeness',
    description: 'Verify spec contains all required sections and no pending markers',
    items
  };
}

// Clarification resolution check
async function checkClarificationResolution(clarifications) {
  const frontmatter = parseYAMLFrontmatter(clarifications);

  const items = [
    {
      id: 'CLAR-COMPLETE',
      description: 'All clarification rounds completed',
      critical: true,
      status: frontmatter.status === 'complete' ? 'PASS' : 'FAIL',
      artifact: 'clarifications.md'
    },
    {
      id: 'CLAR-PENDING',
      description: 'No pending questions remain',
      critical: true,
      status: (frontmatter.pending_count || 0) === 0 ? 'PASS' : 'FAIL',
      count: frontmatter.pending_count || 0,
      artifact: 'clarifications.md'
    },
    {
      id: 'CLAR-DEFAULTS',
      description: 'Defaults applied count documented',
      critical: false,
      status: frontmatter.defaults_applied !== undefined ? 'PASS' : 'WARN',
      count: frontmatter.defaults_applied || 0,
      artifact: 'clarifications.md'
    }
  ];

  return {
    name: 'Clarification Resolution',
    description: 'Verify all clarification questions have been answered or defaulted',
    items
  };
}

// Plan-to-spec traceability check
async function checkPlanTraceability(plan, spec) {
  // Extract user story IDs from spec
  const specUserStories = [...new Set(spec.match(/US\d+/g) || [])];

  // Extract user story references from plan
  const planUserStories = [...new Set(plan.match(/US\d+/g) || [])];

  // Extract functional requirement IDs from spec
  const specFRs = [...new Set(spec.match(/FR-\d+/g) || [])];

  // Extract FR references from plan
  const planFRs = [...new Set(plan.match(/FR-\d+/g) || [])];

  const items = [];

  // Check each spec user story is referenced in plan
  for (const us of specUserStories) {
    items.push({
      id: `TRACE-${us}`,
      description: `User Story ${us} is addressed in plan`,
      critical: true,
      status: planUserStories.includes(us) ? 'PASS' : 'FAIL',
      artifact: 'plan.md'
    });
  }

  // Check each FR is referenced in plan
  for (const fr of specFRs) {
    items.push({
      id: `TRACE-${fr}`,
      description: `Requirement ${fr} is addressed in plan`,
      critical: true,
      status: planFRs.includes(fr) ? 'PASS' : 'FAIL',
      artifact: 'plan.md'
    });
  }

  // Check plan has phases
  const hasPhases = plan.includes('## Phase') || plan.includes('### Phase');
  items.push({
    id: 'PLAN-PHASES',
    description: 'Plan contains phased implementation',
    critical: true,
    status: hasPhases ? 'PASS' : 'FAIL',
    artifact: 'plan.md'
  });

  return {
    name: 'Plan-to-Spec Traceability',
    description: 'Verify all spec requirements are addressed in the plan',
    items
  };
}

// Task-to-plan traceability check
async function checkTaskTraceability(tasks, plan) {
  // Extract plan phase IDs
  const planPhases = [...new Set(plan.match(/Phase \d+|PHASE-\d+/gi) || [])];

  // Check tasks reference plan phases
  const taskPhases = [...new Set(tasks.match(/Phase \d+|PHASE-\d+/gi) || [])];

  const items = [
    {
      id: 'TASK-PHASES',
      description: 'Tasks map to plan phases',
      critical: true,
      status: taskPhases.length > 0 ? 'PASS' : 'FAIL',
      artifact: 'tasks.md'
    }
  ];

  // Check for test specifications in tasks
  const hasTestSpecs = tasks.includes('Test Specification') ||
                        tasks.includes('test:') ||
                        tasks.includes('Given') && tasks.includes('When') && tasks.includes('Then');
  items.push({
    id: 'TASK-TESTS',
    description: 'Tasks include test specifications',
    critical: true,
    status: hasTestSpecs ? 'PASS' : 'FAIL',
    artifact: 'tasks.md'
  });

  // Check for atomic task IDs
  const taskIDs = (tasks.match(/TASK-\d+|T-\d+/g) || []);
  items.push({
    id: 'TASK-IDS',
    description: 'Tasks have traceable IDs',
    critical: true,
    status: taskIDs.length > 0 ? 'PASS' : 'FAIL',
    count: taskIDs.length,
    artifact: 'tasks.md'
  });

  return {
    name: 'Task-to-Plan Traceability',
    description: 'Verify all tasks map to plan phases and include test specs',
    items
  };
}

// Test coverage check
async function checkTestCoverage(tests, spec) {
  // Extract user stories from spec
  const specUserStories = [...new Set(spec.match(/US\d+/g) || [])];

  // Extract acceptance criteria from spec (Given-When-Then)
  const givenWhenThens = (spec.match(/Given[\s\S]*?When[\s\S]*?Then/gi) || []).length;

  // Extract test cases from tests file
  const testCases = (tests.match(/test\(|it\(|describe\(/g) || []).length;

  const items = [
    {
      id: 'TEST-COVERAGE',
      description: 'Test cases exist for acceptance criteria',
      critical: true,
      status: testCases >= givenWhenThens ? 'PASS' : 'WARN',
      expected: givenWhenThens,
      actual: testCases,
      artifact: 'tests/'
    }
  ];

  // Check each user story has tests
  for (const us of specUserStories) {
    const hasTest = tests.includes(us);
    items.push({
      id: `TEST-${us}`,
      description: `Tests exist for ${us}`,
      critical: true,
      status: hasTest ? 'PASS' : 'FAIL',
      artifact: 'tests/'
    });
  }

  return {
    name: 'Test Coverage',
    description: 'Verify tests cover all user stories and acceptance criteria',
    items
  };
}

// Generate summary
function generateChecklistSummary(checklist) {
  const passCount = checklist.sections.reduce((sum, s) =>
    sum + s.items.filter(i => i.status === 'PASS').length, 0);
  const failCount = checklist.sections.reduce((sum, s) =>
    sum + s.items.filter(i => i.status === 'FAIL').length, 0);
  const warnCount = checklist.sections.reduce((sum, s) =>
    sum + s.items.filter(i => i.status === 'WARN').length, 0);

  const criticalFails = checklist.sections.reduce((sum, s) =>
    sum + s.items.filter(i => i.status === 'FAIL' && i.critical).length, 0);

  return `
Checklist Summary for Phase: ${checklist.phase}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ PASS: ${passCount}
❌ FAIL: ${failCount} (${criticalFails} critical)
⚠️  WARN: ${warnCount}

Total: ${checklist.totalItems} items
Critical: ${checklist.criticalItems} items

${criticalFails > 0 ? '🚫 BLOCKED: Critical items failing. Must resolve before proceeding.' : '✅ READY: All critical items passing.'}
`;
}

// Format checklist as markdown document
function formatChecklistDocument(checklist) {
  let doc = `---
phase: "${checklist.phase}"
generated: "${checklist.generated}"
total_items: ${checklist.totalItems}
critical_items: ${checklist.criticalItems}
---

# Quality Validation Checklist

**Phase**: ${checklist.phase}
**Generated**: ${checklist.generated}

---

`;

  for (const section of checklist.sections) {
    doc += `## ${section.name}\n\n`;
    doc += `${section.description}\n\n`;

    for (const item of section.items) {
      const icon = item.status === 'PASS' ? '✅' :
                   item.status === 'FAIL' ? '❌' :
                   item.status === 'WARN' ? '⚠️' : '⏳';
      const critical = item.critical ? ' **[CRITICAL]**' : '';

      doc += `- [${item.status === 'PASS' ? 'x' : ' '}] ${icon} ${item.description}${critical}\n`;
      if (item.count !== undefined) {
        doc += `  - Count: ${item.count}\n`;
      }
      if (item.artifact) {
        doc += `  - Artifact: \`${item.artifact}\`\n`;
      }
    }
    doc += '\n---\n\n';
  }

  doc += `## Summary\n\n${checklist.summary}\n`;

  return doc;
}
```

### Analyze Subcommand Implementation

```javascript
async function executeAnalyzeSubcommand(featureName) {
  const specDir = findSpecDir(featureName);
  if (!specDir) {
    return { success: false, error: `Spec not found: ${featureName}` };
  }

  console.log(`\n🔍 Analyzing artifacts in ${specDir}...\n`);

  // Load all artifacts
  const artifacts = await loadAllArtifacts(specDir);

  // Run cross-validation
  const analysis = {
    consistency: [],
    coverage: [],
    traceability: [],
    quality: []
  };

  // 1. Consistency checks
  if (artifacts.spec && artifacts.clarifications) {
    // Check clarification answers are reflected in spec
    const clarAnswers = extractAnsweredQuestions(artifacts.clarifications);
    for (const answer of clarAnswers) {
      if (answer.source === 'USER') {
        // Verify impact is reflected in spec
        analysis.consistency.push({
          check: `Clarification ${answer.id} reflected in spec`,
          status: 'REVIEW', // Manual review needed
          details: answer.impact
        });
      }
    }
  }

  // 2. Coverage checks
  if (artifacts.spec) {
    const userStories = extractUserStories(artifacts.spec);
    for (const story of userStories) {
      const coverage = {
        planCovered: artifacts.plan?.includes(story.id),
        tasksCovered: artifacts.tasks?.includes(story.id),
        testsCovered: artifacts.tests?.includes(story.id)
      };
      analysis.coverage.push({
        storyId: story.id,
        ...coverage,
        complete: Object.values(coverage).every(v => v)
      });
    }
  }

  // 3. Traceability checks
  const traceMatrix = buildTraceabilityMatrix(artifacts);
  analysis.traceability = traceMatrix;

  // 4. Quality score
  const qualityScore = calculateQualityScore(analysis);

  // Generate report
  const reportPath = `${specDir}/analysis-report.md`;
  await writeFile(reportPath, formatAnalysisReport(analysis, qualityScore));

  console.log(`\n📊 Analysis complete. Quality Score: ${qualityScore}%`);
  console.log(`📄 Report: ${reportPath}\n`);

  return {
    success: true,
    qualityScore,
    analysis,
    reportPath
  };
}

function buildTraceabilityMatrix(artifacts) {
  const matrix = [];

  // Extract all traceable items
  const specs = extractTraceableItems(artifacts.spec, 'FR-', 'US');
  const plans = extractTraceableItems(artifacts.plan, 'PHASE-', 'TASK-');
  const tasks = extractTraceableItems(artifacts.tasks, 'TASK-', 'TEST-');

  for (const spec of specs) {
    matrix.push({
      specItem: spec,
      inPlan: plans.some(p => p.references?.includes(spec.id)),
      inTasks: tasks.some(t => t.references?.includes(spec.id)),
      complete: false // Calculated
    });
  }

  return matrix;
}

function calculateQualityScore(analysis) {
  let score = 100;

  // Deduct for incomplete coverage
  const incompleteCoverage = analysis.coverage.filter(c => !c.complete).length;
  score -= incompleteCoverage * 5;

  // Deduct for missing traceability
  const missingTrace = analysis.traceability.filter(t => !t.inPlan || !t.inTasks).length;
  score -= missingTrace * 3;

  return Math.max(0, Math.min(100, score));
}

function formatAnalysisReport(analysis, qualityScore) {
  return `---
type: "analysis-report"
generated: "${new Date().toISOString()}"
quality_score: ${qualityScore}
---

# Cross-Artifact Analysis Report

**Quality Score**: ${qualityScore}%

---

## Coverage Analysis

| User Story | In Plan | In Tasks | In Tests | Complete |
|------------|---------|----------|----------|----------|
${analysis.coverage.map(c =>
  `| ${c.storyId} | ${c.planCovered ? '✅' : '❌'} | ${c.tasksCovered ? '✅' : '❌'} | ${c.testsCovered ? '✅' : '❌'} | ${c.complete ? '✅' : '❌'} |`
).join('\n')}

---

## Traceability Matrix

| Spec Item | In Plan | In Tasks |
|-----------|---------|----------|
${analysis.traceability.map(t =>
  `| ${t.specItem.id} | ${t.inPlan ? '✅' : '❌'} | ${t.inTasks ? '✅' : '❌'} |`
).join('\n')}

---

## Consistency Checks

${analysis.consistency.map(c =>
  `- **${c.check}**: ${c.status}\n  ${c.details || ''}`
).join('\n')}

---

## Recommendations

${qualityScore < 80 ? '⚠️ Quality score below threshold. Address the following:' : '✅ Quality acceptable.'}

${analysis.coverage.filter(c => !c.complete).map(c =>
  `- Complete coverage for ${c.storyId}`
).join('\n')}

${analysis.traceability.filter(t => !t.inPlan || !t.inTasks).map(t =>
  `- Add traceability for ${t.specItem.id}`
).join('\n')}
`;
}
```

---

## Self-Evolution Integration

**After each execution, contribute to SYNRG evolution:**

```javascript
async function recordSpecEvolution(specDir, executionResult) {
  // Log to evolution system
  const evolutionEntry = {
    command: 'synrg-spec',
    specDir: specDir,
    result: executionResult,
    timestamp: new Date().toISOString(),
    phasesCompleted: executionResult.phases?.filter(p => p.status === 'complete').length,
    errors: executionResult.errors || [],
    patterns: extractPatterns(executionResult)
  };

  // Append to evolution log
  await appendToEvolutionLog(evolutionEntry);

  // If patterns detected, suggest evolution
  if (evolutionEntry.patterns.length > 0) {
    console.log(`\nDetected ${evolutionEntry.patterns.length} patterns for potential evolution.`);
    console.log(`Run /synrg-evolve to integrate improvements.`);
  }
}
```

---

## Validation Checklist

Before considering any phase complete:

- [ ] **Phase gate validated** - All requirements met
- [ ] **Artifact exists** - Output file created
- [ ] **YAML frontmatter valid** - Status set correctly
- [ ] **Hash recorded** - Integrity chain maintained
- [ ] **No pending items** - All questions/tasks addressed
- [ ] **Constitutional compliance** - Follows all articles

---

## Success Criteria

**The `/synrg-spec` command succeeds when:**

1. User can initialize a new spec with `init`
2. Each phase enforces gate validation (cannot skip)
3. `continue` auto-progresses through all phases
4. `status` shows accurate phase progress
5. All state persists in Markdown (no hidden memory state)
6. Implementation phase delegates to SYNRG Director
7. Full spec-kit functionality preserved (progressive refinement)
8. Integrates with SYNRG principles (robustness-first, anti-memory)

---

## 📊 VERSION HISTORY & EVOLUTION TRACKING

**Version**: 1.1.0 (100% Spec-Kit Translation Fidelity)
**Last Updated**: 2025-12-14
**Evolution Status**: Complete - Full spec-kit methodology translation

---

### v1.1.0 - COMPLETE SPEC-KIT INTEGRATION (2025-12-14)

**MILESTONE: 100% Translation Fidelity to spec-kit methodology**

**Final Additions (from v1.0.0 → v1.1.0)**:

1. **🆕 Enhanced Command Entry Point**
   - Full flag parsing (`--brownfield`, `--branch`)
   - `tests` subcommand explicitly added to dispatcher
   - `regenerate` subcommand with full mode support (incremental/full/validate/force)
   - Proper integration of `executeInitPhaseWithBranch` for branch flag handling

2. **🆕 Regenerate Subcommand Implementation**
   - Four modes: incremental (default), full, validate, force
   - Staleness reporting with visual indicators
   - Cascade regeneration support
   - Detailed logging of regeneration progress

3. **🆕 Updated Help Documentation**
   - Complete subcommand list including tests and regenerate
   - Flag documentation (--brownfield, --branch)
   - Regenerate mode descriptions
   - Updated phase order showing 7 phases with Test-First flow
   - More comprehensive examples

4. **📋 Version History Section**
   - Evolution tracking like main /synrg command
   - Feature completion matrix
   - Implementation statistics

---

### v1.0.0 - INITIAL SPEC-KIT TRANSLATION (2025-12-11 → 2025-12-13)

**Core Implementation (~95% Translation)**:

| Priority | Feature | Status | Lines Added |
|----------|---------|--------|-------------|
| P1 | Supporting Documents | ✅ Complete | ~450 |
| P2 | [P] Parallel Task Markers | ✅ Complete | ~180 |
| P3 | Regeneration Triggers | ✅ Complete | ~115 |
| P4 | Brownfield Mode | ✅ Complete | ~260 |
| P5 | Branch Auto-Generation | ✅ Complete | ~140 |

**Key Features**:

1. **7-Phase Pipeline**: init → specify → clarify → plan → tasks → tests → implement
2. **Phase Gating Protocol**: Mandatory order with prerequisite validation
3. **9 Constitutional Articles**: Immutable principles governing development
4. **Test-First Imperative (Article III)**: RED/GREEN phase confirmation
5. **Integration-First Testing (Article IX)**: Contract → Integration → E2E → Unit test order
6. **Machine-Parseable State**: YAML frontmatter with hash-based integrity chains
7. **Clarification Priority System**: SCOPE → SECURITY → UX → TECHNICAL with 3-round max
8. **Cross-Artifact Validation**: Checklist and analyze subcommands
9. **Error Recovery**: Rollback protocol with artifact backup
10. **SYNRG Integration**: Anti-Memory Protocol embedded, Director delegation

---

### Implementation Statistics

| Metric | Value |
|--------|-------|
| Total Lines | ~4,500+ |
| Phases | 7 (+ analyze optional) |
| Subcommands | 12 |
| Constitutional Articles | 9 |
| Supporting Documents | 4 (research, data-model, quickstart, contracts/) |
| Template Types | 11 (constitution, spec, clarifications, plan, tasks, tests, implementation.log, etc.) |

---

### Spec-Kit Feature Coverage Matrix

| Spec-Kit Feature | Implementation Status | Notes |
|-----------------|----------------------|-------|
| Progressive Refinement Pipeline | ✅ 100% | 7-phase mandatory order |
| Specification Templates | ✅ 100% | User scenarios, requirements, architecture |
| Clarification Q&A | ✅ 100% | Priority-based, 3-round max with defaults |
| Implementation Planning | ✅ 100% | Phased approach with dependencies |
| Task Breakdown | ✅ 100% | Atomic tasks with test specifications |
| Test-First Development | ✅ 100% | RED/GREEN phase confirmation |
| Cross-Artifact Traceability | ✅ 100% | Checklist and analyze validation |
| Machine-Parseable State | ✅ 100% | YAML frontmatter throughout |
| Hash-Based Integrity | ✅ 100% | Upstream dependency tracking |
| Regeneration Triggers | ✅ 100% | 4 modes with cascade matrix |
| Parallel Task Markers | ✅ 100% | [P] notation with dependency graphs |
| Supporting Documents | ✅ 100% | research, data-model, quickstart, contracts/ |
| Brownfield Mode | ✅ 100% | Codebase analysis, gap analysis, inferred constitution |
| Branch Management | ✅ 100% | Auto-generation, tracking, merge instructions |
| Error Recovery | ✅ 100% | Rollback protocol, artifact backup |
| SYNRG Integration | ✅ 100% | Anti-Memory, Director delegation, evolution |

---

### Alignment with SYNRG Principles

| SYNRG Principle | Alignment |
|-----------------|-----------|
| Robustness-First | ✅ No phase skipping, mandatory validation |
| Anti-Memory Protocol | ✅ All state in Markdown files, no hidden memory |
| Value-First Analysis | ✅ Constitutional constraints, clarification before action |
| Comprehensive Quality Gates | ✅ Test-first, cross-artifact validation |
| Sub-Agent Delegation | ✅ SYNRG Director integration for implementation |

---

### Future Evolution Considerations

**Potential v1.2.0 Enhancements** (not blocking 100% status):
- Interactive TUI for phase navigation
- Real-time artifact diff visualization
- Integration with project management tools (JIRA, Linear)
- Automated PR generation from implementation phase
- Metrics dashboard for spec health

---

**Based On**: GitHub spec-kit methodology
**Aligned With**: SYNRG v4.0 robustness-first principles
**Translation Fidelity**: 100%
