# SYNRG Command Chaining Protocol

This document defines the protocol for chaining SYNRG commands together, enabling complex multi-step workflows.

## Overview

Command chaining allows one SYNRG command to invoke another as part of its workflow. This enables:
- Complex multi-step operations
- Reusable workflow patterns
- Automatic post-processing (e.g., auto-commit after refactor)
- Dependency-aware execution

## Chaining Syntax

### In-Command Chaining

Commands can chain to other commands using the `CHAIN` directive:

```markdown
<!-- CHAIN: synrg-commit -->
<!-- CHAIN_IF: changes.length > 0 THEN synrg-commit -->
<!-- CHAIN_WITH: synrg-commit { message_hint: "Refactoring complete" } -->
```

### Explicit Chain Invocation

From within a command's execution:

```
CHAIN_INVOKE: {
  command: "synrg-commit",
  input: {
    changes: ${CHANGES},
    message_hint: "Auto-commit from synrg-refactor"
  },
  on_success: "continue",
  on_failure: "halt"
}
```

## Chain Execution Model

### Execution Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Command A  │────▶│  Command B  │────▶│  Command C  │
│  (synrg)    │     │ (refactor)  │     │  (commit)   │
└─────────────┘     └─────────────┘     └─────────────┘
      │                   │                   │
      ▼                   ▼                   ▼
   Output A            Output B            Output C
      │                   │                   │
      └───────────────────┴───────────────────┘
                          │
                          ▼
                   Final Result
```

### Context Passing

Each command in a chain receives:
1. **Original objective** - The user's initial request
2. **Chain context** - Accumulated state from previous commands
3. **Previous output** - Direct output from the preceding command

```yaml
chain_context:
  original_objective: "Refactor auth module and commit"
  chain_position: 2
  chain_depth: 3
  previous_outputs:
    - command: "synrg"
      output: { ... }
    - command: "synrg-refactor"
      output: { ... }
  accumulated_state:
    files_modified: [...]
    validation_passed: true
```

## Chaining Patterns

### Pattern 1: Sequential Chain

Execute commands in strict order:

```yaml
pattern: sequential
chain:
  - synrg-spec
  - synrg-scaffold
  - synrg-commit
behavior: Each command waits for previous to complete
```

### Pattern 2: Conditional Chain

Chain based on conditions:

```yaml
pattern: conditional
chain:
  - command: synrg-refactor
    then:
      - if: "changes.length > 0"
        chain: synrg-commit
      - if: "errors.length > 0"
        chain: synrg-evolve
```

### Pattern 3: Parallel-Then-Merge

Run commands in parallel, then merge results:

```yaml
pattern: parallel-merge
parallel:
  - synrg-refactor --target=src/
  - synrg-refactor --target=lib/
merge_with: synrg-commit
```

### Pattern 4: Fallback Chain

Try alternatives on failure:

```yaml
pattern: fallback
primary: synrg-refactor
fallback:
  - synrg-refactor --conservative
  - manual-intervention
```

## Dependency Resolution

### Automatic Resolution

When chaining, dependencies are automatically resolved:

```
synrg-spec requires: [value-first, phase-gate]
synrg-scaffold requires: [phase-gate]

Chain: synrg-spec → synrg-scaffold

Resolution:
1. Load value-first protocol
2. Load phase-gate protocol
3. Execute synrg-spec
4. phase-gate already loaded (shared)
5. Execute synrg-scaffold
```

### Conflict Resolution

When commands have conflicting requirements:

| Conflict Type | Resolution |
|---------------|------------|
| Version mismatch | Use highest compatible version |
| Mutual exclusion | Error - cannot chain |
| Resource contention | Queue execution |

## Chain Validation

Before executing a chain, validate:

```python
def validate_chain(chain):
    errors = []

    # Check chain exists
    for cmd in chain:
        if not registry.exists(cmd):
            errors.append(f"Unknown command: {cmd}")

    # Check chaining allowed
    for i in range(len(chain) - 1):
        current = chain[i]
        next_cmd = chain[i + 1]
        if next_cmd not in registry.get(current).can_chain_to:
            errors.append(f"Cannot chain {current} → {next_cmd}")

    # Check depth
    if len(chain) > chaining.max_depth:
        errors.append(f"Chain depth {len(chain)} exceeds max {chaining.max_depth}")

    # Check circular references
    if has_cycle(chain):
        errors.append("Circular chain detected")

    return errors
```

## Inter-Command Communication

### Message Format

Commands communicate using a standard message format:

```yaml
chain_message:
  # Metadata
  id: "msg-uuid"
  timestamp: "2026-01-09T12:00:00Z"
  source_command: "synrg-refactor"
  target_command: "synrg-commit"

  # Payload
  payload:
    type: "execution_result"
    data:
      files_modified: [...]
      validation_status: "passed"

  # Control
  control:
    action: "chain_continue"  # chain_continue | chain_halt | chain_retry
    timeout_ms: 30000
```

### State Persistence

Chain state is persisted to allow recovery:

```
~/.claude/chain-state/
├── active/
│   └── chain-{uuid}.yaml    # Currently executing chains
├── completed/
│   └── chain-{uuid}.yaml    # Completed chain logs
└── failed/
    └── chain-{uuid}.yaml    # Failed chain logs with error info
```

## Error Handling

### Chain Failure Strategies

| Strategy | Behavior |
|----------|----------|
| `halt` | Stop chain immediately, report error |
| `continue` | Log error, continue to next command |
| `rollback` | Undo changes from all commands in chain |
| `retry` | Retry failed command up to N times |

### Rollback Protocol

When rollback is triggered:

1. **Collect rollback instructions** from each completed command
2. **Execute in reverse order**
3. **Verify state restoration**
4. **Report rollback status**

```yaml
rollback_instruction:
  command: "synrg-refactor"
  action: "restore_files"
  data:
    backup_path: "~/.claude/backups/chain-{uuid}/"
    files: [...]
```

## Usage Examples

### Example 1: Auto-Commit After Refactor

```markdown
User: /synrg-refactor src/auth/ --auto-commit

Chain executed:
1. synrg-refactor analyzes and modifies src/auth/
2. If changes made → chains to synrg-commit
3. synrg-commit creates atomic commits
4. Returns combined result
```

### Example 2: Full Development Workflow

```markdown
User: /synrg "Build user authentication system"

Chain executed:
1. synrg analyzes objective
2. Determines spec needed → chains to synrg-spec
3. synrg-spec creates specification
4. Needs project structure → chains to synrg-scaffold
5. Returns to synrg for implementation
6. Implementation complete → chains to synrg-commit
```

### Example 3: Conditional Evolution

```markdown
After synrg execution with errors:

Chain executed:
1. synrg detects repeated error pattern
2. Chains to synrg-evolve with error data
3. synrg-evolve updates command patterns
4. Returns evolution report
```

## Configuration

### Enable/Disable Chaining

```yaml
# In command file or config
chaining:
  enabled: true
  auto_commit: true
  max_depth: 5
  timeout_ms: 300000
```

### Chain Permissions

Commands can restrict what can chain to them:

```yaml
# In synrg-commit
chain_permissions:
  allow_from:
    - synrg
    - synrg-refactor
    - synrg-scaffold
  deny_from:
    - synrg-evolve  # Evolution shouldn't auto-commit
```

## Best Practices

### DO
- Keep chains short (2-4 commands)
- Use conditional chaining for optional steps
- Implement proper rollback for destructive operations
- Log chain execution for debugging
- Validate chains before execution

### DON'T
- Create circular chains
- Chain commands with incompatible outputs/inputs
- Skip validation steps in chains
- Ignore chain timeouts
- Chain without user awareness (for destructive ops)
