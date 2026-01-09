---
name: certainty-gated-atomic-change
description: Atomic change protocol with certainty validation gates - prevents speculative large changes
version: 1.0.0
---

# CERTAINTY-GATED ATOMIC CHANGE PROTOCOL (CGAC v1.0)

## Core Philosophy

> "When uncertain, scope INWARD and dissect - never compensate with larger changes."

The AI must work from **smallest possible changes** to larger ones, with explicit certainty validation at each step. Large changes are ONLY permitted after atomic changes have been validated.

---

## CERTAINTY CLASSIFICATION

### Certainty Levels

| Level | Threshold | Action Required |
|-------|-----------|-----------------|
| **HIGH** | >= 90% | Proceed with change |
| **MEDIUM** | 70-89% | VALIDATE GATE required before proceeding |
| **LOW** | 50-69% | DISSECTION required - scope inward |
| **UNCERTAIN** | < 50% | STOP - request user clarification or read more files |

### Certainty Factors

Calculate certainty based on:

```
CERTAINTY = (Evidence_Score + Understanding_Score + Isolation_Score) / 3

Evidence_Score:
  - 100%: Have READ the exact file/function being modified
  - 75%: Have READ related files, inferring target
  - 50%: Have searched but not read target
  - 25%: Working from memory/assumptions

Understanding_Score:
  - 100%: Understand full call chain and side effects
  - 75%: Understand immediate context
  - 50%: Understand purpose but not implementation
  - 25%: Unclear on purpose or implementation

Isolation_Score:
  - 100%: Change affects only target, no dependencies
  - 75%: Change affects <3 files, known dependencies
  - 50%: Change affects multiple files, some unknown deps
  - 25%: Change has cascading/unknown effects
```

---

## ATOMIC CHANGE HIERARCHY

Changes must be attempted in this order. Never skip levels.

### Level 1: MICRO-ATOMIC (Single Expression)
```
Scope: One line, one expression, one value
Examples:
  - Fix typo in string
  - Change numeric constant
  - Update single import path
  - Fix operator (== to ===)

Certainty Required: >= 70%
Validation: Visual diff review
```

### Level 2: ATOMIC (Single Statement/Block)
```
Scope: One function, one block, one config section
Examples:
  - Add parameter validation
  - Fix conditional logic
  - Add error handling to one function
  - Update one config block

Certainty Required: >= 80%
Validation: Test the specific function/block
```

### Level 3: MOLECULAR (Related Statements)
```
Scope: Multiple related changes in same file
Examples:
  - Rename variable across file
  - Update function signature + callers in file
  - Add new function + call site

Certainty Required: >= 85%
Validation: Run file-level tests, check imports
```

### Level 4: COMPOUND (Multi-File)
```
Scope: Changes spanning 2-5 files
Examples:
  - Add new API endpoint (route + handler + types)
  - Refactor shared utility
  - Update interface + implementations

Certainty Required: >= 90%
Validation: Run integration tests, verify all callers
```

### Level 5: STRUCTURAL (Architecture)
```
Scope: Changes affecting >5 files or core patterns
Examples:
  - Change authentication flow
  - Migrate database schema
  - Restructure module boundaries

Certainty Required: >= 95% + USER APPROVAL
Validation: Full test suite, staged rollout plan
```

---

## VALIDATE GATE PROTOCOL

When certainty drops below 90% for next change:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ VALIDATE GATE TRIGGERED                                                      │
│                                                                              │
│ Current certainty: [X]%                                                      │
│ Reason for uncertainty: [specific reason]                                    │
│                                                                              │
│ REQUIRED ACTIONS:                                                            │
│                                                                              │
│ 1. STOP current implementation path                                          │
│                                                                              │
│ 2. DISSECT the uncertainty:                                                  │
│    □ What specific information is missing?                                   │
│    □ What file(s) need to be READ?                                          │
│    □ What assumption am I making?                                            │
│                                                                              │
│ 3. GATHER evidence:                                                          │
│    □ Read the specific files involved                                        │
│    □ Trace the call chain                                                    │
│    □ Identify all side effects                                               │
│                                                                              │
│ 4. RE-EVALUATE certainty after gathering                                     │
│                                                                              │
│ 5. IF still < 90%:                                                           │
│    □ Reduce scope to smaller atomic unit                                     │
│    □ OR ask user for clarification                                           │
│    □ NEVER proceed with uncertain large changes                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## INWARD SCOPING PROTOCOL

When uncertain, ALWAYS scope inward (not outward):

### WRONG: Compensatory Expansion
```
Uncertainty about function X
  → "I'll refactor the whole module to be safer"
  → WRONG: This increases risk, not certainty
```

### RIGHT: Inward Dissection
```
Uncertainty about function X
  → "Let me understand X better"
  → Read X's implementation
  → Read X's callers
  → Read X's dependencies
  → Now I understand X with high certainty
  → Make minimal change to X only
```

### Dissection Questions

When uncertain, ask yourself:

1. **What exactly am I uncertain about?**
   - The syntax? → Read language docs
   - The behavior? → Read the implementation
   - The side effects? → Trace the call chain
   - The requirements? → Ask the user

2. **What is the smallest thing I can verify?**
   - Can I verify one line works?
   - Can I verify one function works?
   - Can I test in isolation?

3. **What would make me 100% certain?**
   - Reading which file?
   - Understanding which concept?
   - Getting which user confirmation?

---

## CHANGE ESCALATION RULES

### Rule 1: Sequential Validation
```
Complete Level N validation before attempting Level N+1
Exception: NONE
```

### Rule 2: Certainty Preservation
```
If certainty drops during implementation:
  → STOP at current level
  → Do NOT proceed to larger changes
  → Re-enter VALIDATE GATE
```

### Rule 3: Rollback Readiness
```
At each level, know how to undo:
  Level 1-2: Simple revert
  Level 3-4: Git stash/branch
  Level 5: Full rollback plan required
```

### Rule 4: User Escalation
```
If 3 consecutive VALIDATE GATEs triggered:
  → Present findings to user
  → Ask for direction
  → Do NOT continue guessing
```

---

## ANTI-PATTERNS TO AVOID

### 1. Speculative Refactoring
```
BAD: "While I'm here, let me also clean up..."
GOOD: "I'll make only the requested change"
```

### 2. Defensive Over-Engineering
```
BAD: "I'm not sure this will work, so I'll add fallbacks everywhere"
GOOD: "I'll verify it works, then add only necessary handling"
```

### 3. Assumption Cascades
```
BAD: "I assume X, therefore Y, therefore Z, so I'll change A, B, C"
GOOD: "Let me verify X before making any changes"
```

### 4. Scope Creep Under Uncertainty
```
BAD: "Since I'm uncertain about the fix, I'll rewrite the module"
GOOD: "Since I'm uncertain, I'll read more code first"
```

---

## IMPLEMENTATION CHECKLIST

Before EVERY change, complete:

```
□ Certainty calculated: ___%
□ Change level identified: Level ___
□ Certainty meets threshold for level: YES/NO
□ If NO: VALIDATE GATE entered
□ Evidence gathered (files read): [list files]
□ Atomic unit identified: [specific change]
□ Rollback method known: [method]
□ Proceed with change: YES/NO
```

---

## INTEGRATION WITH OTHER PROTOCOLS

This protocol integrates with:

- **Anti-Memory Protocol**: Forces file reading to increase Evidence_Score
- **Enterprise Security Gate**: Security check after certainty validation
- **Git Strategy Decision**: Branch decision based on change level
- **Value-First Analysis**: Certainty assessment is part of value analysis
