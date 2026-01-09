---
name: git-strategy-decision
description: Intelligent branch/worktree decision protocol for all SYNRG commands
version: 1.0.0
---

# GIT STRATEGY DECISION PROTOCOL (GSD v1.0)

## Core Principle

Every implementation must have a deliberate git strategy decided BEFORE coding begins.

---

## DECISION TREE

```
                    ┌─────────────────────┐
                    │ What is the change? │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
        ┌──────────┐    ┌───────────┐    ┌──────────────┐
        │ TRIVIAL  │    │ STANDARD  │    │ SIGNIFICANT  │
        │ <3 files │    │ 3-10 files│    │ >10 files    │
        │ <30 mins │    │ 30m-4hrs  │    │ >4 hours     │
        └────┬─────┘    └─────┬─────┘    └──────┬───────┘
             │                │                  │
             ▼                ▼                  ▼
     ┌───────────────┐ ┌─────────────┐  ┌───────────────┐
     │DIRECT COMMIT  │ │FEATURE      │  │WORKTREE       │
     │on current     │ │BRANCH       │  │+ Feature      │
     │branch         │ │             │  │Branch         │
     └───────────────┘ └─────────────┘  └───────────────┘
```

---

## STRATEGY DEFINITIONS

### 1. DIRECT COMMIT (Trivial Changes)

**When to use:**
- Single file changes
- Typo fixes, comment updates
- Config value changes
- Documentation updates
- Changes take <30 minutes

**Requirements:**
- Current branch is clean (no uncommitted changes)
- Change is isolated with no cascading effects
- Certainty level >= 95%

**Workflow:**
```bash
# Verify clean state
git status

# Make atomic changes
# ... edit files ...

# Commit immediately
git add <specific-files>
git commit -m "<type>(<scope>): <description>"
```

### 2. FEATURE BRANCH (Standard Changes)

**When to use:**
- Multiple related files (3-10)
- New features or significant fixes
- Changes require testing
- Changes take 30 minutes to 4 hours
- Changes might need review

**Requirements:**
- Branch from latest main/develop
- Clear scope and exit criteria
- Certainty level >= 85%

**Naming Convention:**
```
feature/<ticket>-<description>    # New features
fix/<ticket>-<description>        # Bug fixes
refactor/<scope>-<description>    # Code restructuring
chore/<scope>-<description>       # Maintenance tasks
docs/<scope>-<description>        # Documentation
```

**Workflow:**
```bash
# Update base branch
git checkout main && git pull

# Create feature branch
git checkout -b feature/PROJ-123-add-user-auth

# Work and commit atomically
# ... multiple atomic commits ...

# Push and create PR
git push -u origin feature/PROJ-123-add-user-auth
```

### 3. WORKTREE (Significant/Parallel Changes)

**When to use:**
- Large changes (>10 files)
- Changes take >4 hours
- Need to switch contexts frequently
- Experimental or risky changes
- Parallel development required
- Database migrations
- Breaking changes

**Requirements:**
- Isolated from main working directory
- Full rollback plan documented
- User approval required
- Certainty level >= 80% (lower OK due to isolation)

**Workflow:**
```bash
# Create worktree with feature branch
git worktree add ../project-feature-name -b feature/large-change

# Work in isolated directory
cd ../project-feature-name

# When complete, merge and cleanup
git checkout main
git merge feature/large-change
git worktree remove ../project-feature-name
```

---

## PRE-IMPLEMENTATION CHECKLIST

Before ANY implementation:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ GIT STRATEGY DECISION GATE                                                   │
│                                                                              │
│ 1. Current State Assessment                                                  │
│    □ Run: git status                                                         │
│    □ Run: git branch --show-current                                          │
│    □ Any uncommitted changes? YES/NO                                         │
│    □ On correct base branch? YES/NO                                          │
│                                                                              │
│ 2. Change Scope Analysis                                                     │
│    □ Estimated files affected: ___                                           │
│    □ Estimated time: ___                                                     │
│    □ Risk level: LOW/MEDIUM/HIGH                                             │
│    □ Certainty level: ___%                                                   │
│                                                                              │
│ 3. Strategy Selection                                                        │
│    □ Strategy chosen: DIRECT / BRANCH / WORKTREE                             │
│    □ Branch name (if applicable): ___                                        │
│    □ Worktree location (if applicable): ___                                  │
│                                                                              │
│ 4. Execute Strategy                                                          │
│    □ Git commands executed successfully                                      │
│    □ Verified on correct branch                                              │
│    □ Ready to proceed with implementation                                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## BRANCH PROTECTION RULES

### Protected Branches
```
main     → NEVER commit directly (except hotfixes with approval)
master   → NEVER commit directly
develop  → Only via PR from feature branches
release  → Only via release process
```

### Commit Requirements
```
Feature branches:
  - Atomic commits (one logical change per commit)
  - Conventional commit messages
  - Must pass pre-commit hooks

Merge to protected:
  - Squash or rebase preferred
  - Clean commit history
  - All tests passing
```

---

## CONTEXT SWITCHING PROTOCOL

When needing to switch tasks:

```
IF current_work_uncommitted:
    IF current_work_complete_enough:
        → Commit with WIP: prefix
        → git commit -m "WIP: partial implementation of X"
    ELSE:
        → Stash changes
        → git stash push -m "WIP: description"

THEN:
    → Switch to new branch/worktree
    → Complete new task
    → Return and resume (pop stash or continue WIP)
```

---

## ROLLBACK PROCEDURES

### Direct Commit Rollback
```bash
git revert HEAD  # Create reverting commit
# OR
git reset --soft HEAD~1  # Undo commit, keep changes (if not pushed)
```

### Feature Branch Rollback
```bash
git checkout main
git branch -D feature/failed-attempt  # Delete local
git push origin --delete feature/failed-attempt  # Delete remote
```

### Worktree Rollback
```bash
cd /main/project/directory
git worktree remove ../failed-worktree --force
git branch -D feature/failed-experiment
```

---

## INTEGRATION WITH OTHER PROTOCOLS

- **Certainty-Gated Atomic Change**: Git strategy informs change level limits
  - DIRECT COMMIT → Only Level 1-2 changes
  - FEATURE BRANCH → Up to Level 4 changes
  - WORKTREE → Level 5 changes permitted

- **Enterprise Security**: Security review happens on branch before merge

- **SYNRG-COMMIT Chain**: Invoked after strategy execution completes
