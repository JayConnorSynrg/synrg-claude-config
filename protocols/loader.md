# SYNRG Protocol Loader

This document defines the protocol loading mechanism for SYNRG commands. It serves as a template for how extracted protocols can be referenced and imported into commands.

## Protocol Import Syntax

Commands can reference protocols using the following syntax:

```markdown
<!-- PROTOCOL_IMPORT: [protocol_id] -->
```

When Claude encounters this marker, it should:
1. Locate the protocol in `~/.claude/protocols/[protocol_id].yaml`
2. Load the protocol rules into working context
3. Apply the protocol constraints during execution

## Available Protocols

| Protocol ID | File | Purpose |
|-------------|------|---------|
| `mcdp` | `mcdp.yaml` | Mandatory Context Delegation - enforces sub-agent delegation |
| `sub-agent-spawn` | `sub-agent-spawn.yaml` | Rules for spawning and managing sub-agents |
| `mcp-config` | `mcp-config.yaml` | MCP server configuration and delegation patterns |
| `phase-gate` | `phase-gate.yaml` | Phase transition gates and approval requirements |
| `value-first` | `value-first.yaml` | Value-first analysis and prioritization |
| `git-commit` | `git-commit.yaml` | Git commit workflow and message formatting |

## Usage Example

In a SYNRG command file:

```markdown
# SYNRG-EXAMPLE Command

## Protocol Dependencies
<!-- PROTOCOL_IMPORT: mcdp -->
<!-- PROTOCOL_IMPORT: sub-agent-spawn -->

## Command Logic
[Command-specific content here]

The imported protocols above are automatically enforced during execution.
```

## Protocol Resolution Order

1. Check `~/.claude/protocols/[id].yaml`
2. If not found, check `~/.claude/protocols/index.yaml` for path override
3. If still not found, log warning and continue without protocol

## Inline Protocol Override

Commands can override specific protocol rules inline:

```markdown
<!-- PROTOCOL_IMPORT: mcdp -->
<!-- PROTOCOL_OVERRIDE: mcdp.context_threshold = 1000 -->
```

## Protocol Composition

Multiple protocols can be composed with precedence:

```markdown
<!-- PROTOCOL_IMPORT: mcdp, sub-agent-spawn, phase-gate -->
<!-- PROTOCOL_PRECEDENCE: mcdp > phase-gate > sub-agent-spawn -->
```

## Version Compatibility

Each protocol file specifies its version. Commands can require specific versions:

```markdown
<!-- PROTOCOL_IMPORT: mcdp@1.0.0 -->
```

Or minimum versions:

```markdown
<!-- PROTOCOL_IMPORT: mcdp@>=1.0.0 -->
```

## Migration Notes

### Current State (v1.0.0)
Protocols are extracted but commands still contain embedded copies. This is intentional to:
- Maintain backward compatibility
- Allow gradual migration
- Preserve existing command functionality

### Future State (v2.0.0)
Commands will use import syntax and embedded copies will be removed. Migration scripts in `evolution/migration/` will handle the transition.

## Protocol File Schema

All protocol YAML files follow this structure:

```yaml
# Protocol Header
id: string          # Unique identifier
name: string        # Human-readable name
version: string     # Semantic version
extracted_from:     # Source commands
  - string[]

description: |
  Multi-line description

# Protocol-specific content
# (varies by protocol type)

# Metadata
metadata:
  created: date
  last_modified: date
  author: string
```

## Validation

To validate protocol files:

```bash
# Check all protocols
for f in ~/.claude/protocols/*.yaml; do
  echo "Validating: $f"
  # YAML syntax check would go here
done
```

## Integration with SYNRG Commands

### Phase 3 Migration Path

When Phase 3 (Path Variables) is complete, commands will reference protocols as:

```markdown
<!-- PROTOCOL_IMPORT: ${PROTOCOL_DIR}/mcdp.yaml -->
```

Where `${PROTOCOL_DIR}` resolves via `config/paths.yaml`.
