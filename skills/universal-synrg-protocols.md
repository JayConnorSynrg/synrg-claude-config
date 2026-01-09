---
name: universal-synrg-protocols
description: Universal protocol blocks for injection into all SYNRG commands - achieves 100% compliance
version: 1.0.0
compliance_target: 100%
---

# UNIVERSAL SYNRG PROTOCOLS (USP v1.0)

## Compliance Achievement Matrix

| Principle | Protocol | Target |
|-----------|----------|--------|
| P1: Read First | Anti-Memory Checkpoint | 100% |
| P2: User Verification | PRE_IMPLEMENTATION_GATE | 100% |
| P3: Step Explanations | EXPLANATION_PROTOCOL | 100% |
| P4: Minimal Changes | CERTAINTY_GATED_ATOMIC_CHANGE | 100% |
| P5: Documentation | DOCUMENTATION_UPDATE_GATE | 100% |
| P6: No Speculation | Anti-Memory Checkpoint | 100% |
| Enterprise Security | ENTERPRISE_SECURITY_GATE | 100% |
| Branch/Worktree | GIT_STRATEGY_DECISION | 100% |
| Commit Workflow | SYNRG_COMMIT_CHAIN | 100% |

---

## BLOCK 1: PRE-IMPLEMENTATION REVIEW (Inject Before Any Changes)

```markdown
## ══════════════════════════════════════════════════════════════════════════════
## UNIVERSAL PRE-IMPLEMENTATION REVIEW (MANDATORY - USP v1.0)
## ══════════════════════════════════════════════════════════════════════════════

**HARD STOP**: Complete ALL gates before ANY code modification.

### GATE 1: Anti-Memory Checkpoint (P1 + P6)
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ⚠️ ANTI-MEMORY CHECKPOINT - DO NOT TRUST MEMORY                            │
│                                                                              │
│  BEFORE making changes, you MUST:                                            │
│                                                                              │
│  □ READ the actual files being modified (not from memory)                    │
│  □ VERIFY file locations exist: use Glob to confirm paths                    │
│  □ CHECK current state: read the specific lines to be changed                │
│  □ CONFIRM dependencies: read package.json/requirements.txt                  │
│                                                                              │
│  NEVER:                                                                      │
│  ✗ Assume file contents from previous sessions                               │
│  ✗ Guess file paths or function signatures                                   │
│  ✗ Speculate about code structure without reading                            │
│  ✗ Make changes based on "I remember it was..."                              │
│                                                                              │
│  Evidence Required:                                                          │
│  - File read timestamp: [timestamp]                                          │
│  - Lines read: [line range]                                                  │
│  - Content verified: YES/NO                                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### GATE 2: GIT_STRATEGY_DECISION (Branch/Worktree)
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  GIT STRATEGY DECISION GATE                                                  │
│                                                                              │
│  STEP 1: Assess Current State                                                │
│  □ Run: git status                                                           │
│  □ Run: git branch --show-current                                            │
│  □ Uncommitted changes present? [YES/NO]                                     │
│                                                                              │
│  STEP 2: Assess Change Scope                                                 │
│  □ Files to be modified: [count]                                             │
│  □ Estimated complexity: [LOW/MEDIUM/HIGH]                                   │
│  □ Touches critical paths? [YES/NO]                                          │
│                                                                              │
│  STEP 3: Select Strategy                                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │ IF files <= 2 AND complexity = LOW AND no critical paths:           │    │
│  │   → DIRECT COMMIT on current branch                                 │    │
│  │                                                                     │    │
│  │ IF files 3-10 OR complexity = MEDIUM:                               │    │
│  │   → CREATE FEATURE BRANCH                                           │    │
│  │   → Name: feature/<scope>-<description>                             │    │
│  │                                                                     │    │
│  │ IF files > 10 OR complexity = HIGH OR critical paths = YES:         │    │
│  │   → CREATE WORKTREE with feature branch                             │    │
│  │   → Full rollback plan required                                     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  STEP 4: Execute Strategy                                                    │
│  □ Git commands executed: [list]                                             │
│  □ On correct branch: [branch name]                                          │
│  □ Ready to proceed: YES/NO                                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### GATE 3: CERTAINTY_GATED_ATOMIC_CHANGE (P4 - Minimal Changes)
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  CERTAINTY-GATED ATOMIC CHANGE GATE                                          │
│                                                                              │
│  "When uncertain, scope INWARD and dissect - never compensate with larger   │
│  changes."                                                                   │
│                                                                              │
│  STEP 1: Calculate Certainty                                                 │
│                                                                              │
│  Evidence Score (have you READ the files?):                                  │
│    □ 100% = Read exact files being modified                                  │
│    □ 75%  = Read related files, inferring target                             │
│    □ 50%  = Searched but not read target                                     │
│    □ 25%  = Working from memory/assumptions                                  │
│    Current: [__%]                                                            │
│                                                                              │
│  Understanding Score (do you understand the code?):                          │
│    □ 100% = Full call chain and side effects understood                      │
│    □ 75%  = Immediate context understood                                     │
│    □ 50%  = Purpose understood, not implementation                           │
│    □ 25%  = Unclear on purpose or implementation                             │
│    Current: [__%]                                                            │
│                                                                              │
│  Isolation Score (how contained is the change?):                             │
│    □ 100% = Change affects only target, no dependencies                      │
│    □ 75%  = Affects <3 files, known dependencies                             │
│    □ 50%  = Multiple files, some unknown deps                                │
│    □ 25%  = Cascading/unknown effects                                        │
│    Current: [__%]                                                            │
│                                                                              │
│  TOTAL CERTAINTY: (Evidence + Understanding + Isolation) / 3 = [__%]         │
│                                                                              │
│  STEP 2: Determine Change Level                                              │
│                                                                              │
│  │ Level │ Scope                    │ Min Certainty │                        │
│  │   1   │ Single expression/line   │ >= 70%        │                        │
│  │   2   │ Single function/block    │ >= 80%        │                        │
│  │   3   │ Multiple related changes │ >= 85%        │                        │
│  │   4   │ Multi-file (2-5)         │ >= 90%        │                        │
│  │   5   │ Architectural (>5 files) │ >= 95% + USER │                        │
│                                                                              │
│  Proposed change level: [1-5]                                                │
│  Certainty meets threshold: [YES/NO]                                         │
│                                                                              │
│  STEP 3: If Certainty < Threshold                                            │
│                                                                              │
│  IF certainty below threshold:                                               │
│    □ STOP - Do not proceed with change                                       │
│    □ DISSECT - What specific information is missing?                         │
│    □ GATHER - Read the specific files needed                                 │
│    □ RE-EVALUATE - Recalculate certainty after gathering                     │
│    □ REDUCE SCOPE - Lower to smaller atomic unit if still uncertain          │
│                                                                              │
│  NEVER:                                                                      │
│  ✗ Proceed with uncertain large changes                                      │
│  ✗ Compensate uncertainty with larger refactors                              │
│  ✗ Skip reading files because "it should be fine"                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### GATE 4: ENTERPRISE_SECURITY_GATE
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ENTERPRISE SECURITY GATE                                                    │
│                                                                              │
│  Before approving ANY code change:                                           │
│                                                                              │
│  1. SECRETS DETECTION [CRITICAL]                                             │
│     □ No hardcoded API keys, tokens, passwords                               │
│     □ No private keys or certificates in code                                │
│     □ No connection strings with credentials                                 │
│     Status: [PASS/FAIL]                                                      │
│                                                                              │
│  2. OWASP TOP 10 SCAN [HIGH]                                                 │
│     □ No SQL injection vectors                                               │
│     □ No XSS vectors (innerHTML, document.write)                             │
│     □ No command injection (eval, exec, system)                              │
│     □ No path traversal vulnerabilities                                      │
│     Status: [PASS/FAIL]                                                      │
│                                                                              │
│  3. PRIVILEGE ESCALATION CHECK [HIGH]                                        │
│     □ No sudo/admin without explicit approval                                │
│     □ No permission changes to critical files                                │
│     □ No service account credential exposure                                 │
│     Status: [PASS/NEEDS_APPROVAL]                                            │
│                                                                              │
│  4. DEPENDENCY SECURITY [MEDIUM]                                             │
│     □ No known vulnerable dependencies added                                 │
│     □ Lock files updated properly                                            │
│     Status: [PASS/WARN]                                                      │
│                                                                              │
│  5. DATA PROTECTION [MEDIUM]                                                 │
│     □ PII handled with appropriate encryption                                │
│     □ Logs sanitized of sensitive data                                       │
│     Status: [PASS/WARN]                                                      │
│                                                                              │
│  FINAL: All PASS → Proceed                                                   │
│         Any FAIL → Block and fix                                             │
│         Any WARN → Document and proceed with caution                         │
│         Any NEEDS_APPROVAL → Get explicit user approval                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

### GATE 5: User Verification (P2)
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  USER VERIFICATION GATE (P2)                                                 │
│                                                                              │
│  Before major changes, verify plan with user:                                │
│                                                                              │
│  □ Present clear summary of proposed changes                                 │
│  □ List files that will be modified                                          │
│  □ Explain WHY these changes solve the objective                             │
│  □ Highlight any risks or trade-offs                                         │
│  □ Get explicit approval: "Proceed with this plan?"                          │
│                                                                              │
│  When to trigger:                                                            │
│  - Changes affect > 3 files                                                  │
│  - Changes touch critical paths (auth, db, API)                              │
│  - Uncertainty about best approach                                           │
│  - Multiple valid solutions exist                                            │
│                                                                              │
│  User approved: [YES/NO/PENDING]                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```
```

---

## BLOCK 2: STEP EXPLANATION PROTOCOL (P3 - Inject During Execution)

```markdown
## STEP EXPLANATION PROTOCOL (P3)

**MANDATORY**: Every step must include high-level explanation.

For EACH implementation step, provide:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  STEP [N]: [Action Name]                                                     │
│                                                                              │
│  WHAT: [1-2 sentences describing the change]                                 │
│                                                                              │
│  WHY: [1-2 sentences explaining the reasoning]                               │
│                                                                              │
│  WHERE: [File path and line numbers]                                         │
│                                                                              │
│  IMPACT: [What this enables or prevents]                                     │
│                                                                              │
│  CERTAINTY: [__%] - [Basis for certainty]                                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Example**:
```
STEP 3: Add input validation to login handler

WHAT: Adding Zod schema validation to the login endpoint to validate
      email format and password requirements before processing.

WHY: Currently the endpoint accepts any input, which could cause crashes
     or security issues from malformed data.

WHERE: src/api/auth/login.ts:45-67

IMPACT: Prevents malformed requests from reaching the database layer,
        improves error messages to users, reduces attack surface.

CERTAINTY: 95% - Read the file, understand the handler, isolated change.
```
```

---

## BLOCK 3: POST-IMPLEMENTATION REVIEW (Inject After All Changes)

```markdown
## ══════════════════════════════════════════════════════════════════════════════
## UNIVERSAL POST-IMPLEMENTATION REVIEW (MANDATORY - USP v1.0)
## ══════════════════════════════════════════════════════════════════════════════

**HARD STOP**: Complete ALL reviews before marking task complete.

### REVIEW 1: Objective Verification
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  OBJECTIVE VERIFICATION                                                      │
│                                                                              │
│  □ Original objective achieved?                                              │
│    Objective: [state original objective]                                     │
│    Status: [ACHIEVED/PARTIAL/FAILED]                                         │
│                                                                              │
│  □ Solution is most efficient approach?                                      │
│    Alternatives considered: [list]                                           │
│    Why this approach: [reason]                                               │
│                                                                              │
│  □ No unnecessary complexity added?                                          │
│    Lines added: [count]                                                      │
│    Could be simpler: [YES/NO - if yes, why not done]                         │
│                                                                              │
│  □ All edge cases handled?                                                   │
│    Edge cases identified: [list]                                             │
│    Coverage: [COMPLETE/PARTIAL]                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### REVIEW 2: Post-Change Security Evaluation
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  POST-CHANGE SECURITY EVALUATION                                             │
│                                                                              │
│  □ Re-run secrets scan on all modified files                                 │
│    Command: grep -rE "(password|secret|api.?key|token)" [files]              │
│    Result: [CLEAN/FOUND - action taken]                                      │
│                                                                              │
│  □ Verify no new injection vectors introduced                                │
│    Checked for: eval, exec, system, innerHTML, SQL concat                    │
│    Result: [CLEAN/FOUND - action taken]                                      │
│                                                                              │
│  □ Check new dependencies for CVEs                                           │
│    Command: npm audit / pip-audit                                            │
│    Result: [CLEAN/WARNINGS - action taken]                                   │
│                                                                              │
│  □ Validate error messages don't leak sensitive data                         │
│    Reviewed error handlers: [YES/NO]                                         │
│    Result: [SAFE/NEEDS_FIX]                                                  │
│                                                                              │
│  Security Status: [APPROVED/NEEDS_REMEDIATION]                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### REVIEW 3: Documentation Update Check (P5)
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DOCUMENTATION UPDATE CHECK (P5)                                             │
│                                                                              │
│  If changes affect:                                                          │
│                                                                              │
│  □ API contracts                                                             │
│    → Update: API docs, OpenAPI spec                                          │
│    Status: [UPDATED/NOT_NEEDED/PENDING]                                      │
│                                                                              │
│  □ Configuration                                                             │
│    → Update: README, config docs, .env.example                               │
│    Status: [UPDATED/NOT_NEEDED/PENDING]                                      │
│                                                                              │
│  □ Architecture                                                              │
│    → Update: architecture.md, diagrams                                       │
│    Status: [UPDATED/NOT_NEEDED/PENDING]                                      │
│                                                                              │
│  □ Dependencies                                                              │
│    → Update: installation docs, requirements                                 │
│    Status: [UPDATED/NOT_NEEDED/PENDING]                                      │
│                                                                              │
│  □ User-facing behavior                                                      │
│    → Update: CHANGELOG, release notes                                        │
│    Status: [UPDATED/NOT_NEEDED/PENDING]                                      │
│                                                                              │
│  Documentation Status: [COMPLETE/PENDING_UPDATES]                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### REVIEW 4: SYNRG-COMMIT Chain
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  SYNRG-COMMIT CHAIN                                                          │
│                                                                              │
│  STEP 1: Assess Commit Readiness                                             │
│  □ All changes tested and verified                                           │
│  □ Security review passed                                                    │
│  □ Documentation updated (if needed)                                         │
│  □ No TODOs or FIXMEs left unaddressed                                       │
│                                                                              │
│  STEP 2: Select Commit Strategy                                              │
│                                                                              │
│  Option A: Invoke /synrg-commit (RECOMMENDED)                                │
│    → Full atomic decomposition                                               │
│    → Senior-level commit messages                                            │
│    → Automatic validation                                                    │
│                                                                              │
│  Option B: Manual commit following protocol                                  │
│    → Format: <type>(<scope>): <summary>                                      │
│    → Include: WHY paragraph, HOW paragraph, IMPACT paragraph                 │
│    → End with: Co-Authored-By: Claude Opus 4.5                               │
│                                                                              │
│  STEP 3: Commit Message Requirements                                         │
│                                                                              │
│  Every commit must be understandable by:                                     │
│  □ Junior developers: WHAT changed (clear description)                       │
│  □ Senior developers: WHY it matters (professional insight)                  │
│  □ Non-technical stakeholders: IMPACT (business value)                       │
│                                                                              │
│  STEP 4: Execute Commit                                                      │
│                                                                              │
│  □ Stage only relevant files: git add [specific files]                       │
│  □ Create commit with full message                                           │
│  □ Verify commit: git log -1                                                 │
│  □ Push to branch: git push                                                  │
│                                                                              │
│  Commit Status: [COMPLETED/PENDING/DEFERRED]                                 │
│  Commit Hash: [hash if completed]                                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### REVIEW 5: Final Quality Gate
```
┌─────────────────────────────────────────────────────────────────────────────┐
│  FINAL QUALITY GATE                                                          │
│                                                                              │
│  All criteria must pass:                                                     │
│                                                                              │
│  □ Objective achieved: [YES/NO]                                              │
│  □ Security approved: [YES/NO]                                               │
│  □ Documentation complete: [YES/NO]                                          │
│  □ Commit completed: [YES/NO]                                                │
│  □ No regressions: [YES/NO]                                                  │
│                                                                              │
│  TASK STATUS: [COMPLETE/BLOCKED - reason]                                    │
└─────────────────────────────────────────────────────────────────────────────┘
```
```

---

## INJECTION INSTRUCTIONS

### For synrg.md
- Add BLOCK 1 after MCP Delegation Enforcement (~line 121)
- Add BLOCK 2 reference in Sub-Agent Execution Protocol
- Add BLOCK 3 before Self-Evolution Protocol

### For all other SYNRG commands
- Add BLOCK 1 at start of execution flow
- Add BLOCK 2 as execution instruction
- Add BLOCK 3 at end before completion

### Compliance Verification
After injection, verify:
- [ ] P1 (Read First): Anti-Memory Checkpoint present
- [ ] P2 (User Verification): User approval gate present
- [ ] P3 (Step Explanations): Explanation protocol present
- [ ] P4 (Minimal Changes): Certainty-gated atomic change present
- [ ] P5 (Documentation): Documentation update check present
- [ ] P6 (No Speculation): Anti-Memory Checkpoint covers this
- [ ] Enterprise Security: Security gate present
- [ ] Branch/Worktree: Git strategy decision present
- [ ] Commit Workflow: SYNRG-COMMIT chain present
