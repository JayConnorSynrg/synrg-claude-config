# SYNRG Path Resolver

This document defines the path variable system for SYNRG commands, enabling portability across different environments.

## Path Variables

### Core Variables

| Variable | Default Value | Description |
|----------|---------------|-------------|
| `${HOME}` | `/Users/jelalconnor` | User home directory |
| `${CLAUDE_HOME}` | `${HOME}/.claude` | Claude configuration root |
| `${SYNRG_HOME}` | `${HOME}/.local/synrg` | SYNRG platform installation |
| `${CODING_ROOT}` | `${HOME}/CODING` | Primary coding directory |

### Derived Variables

| Variable | Resolves To | Description |
|----------|-------------|-------------|
| `${CLAUDE_AGENTS}` | `${CLAUDE_HOME}/agents` | Agent definitions |
| `${CLAUDE_COMMANDS}` | `${CLAUDE_HOME}/commands` | Slash commands |
| `${CLAUDE_SKILLS}` | `${CLAUDE_HOME}/skills` | Skills library |
| `${CLAUDE_PROTOCOLS}` | `${CLAUDE_HOME}/protocols` | Extracted protocols |
| `${CLAUDE_CONFIG}` | `${CLAUDE_HOME}/config` | Configuration files |

### Project Variables

| Variable | Resolves To | Description |
|----------|-------------|-------------|
| `${N8N_WORKFLOWS}` | `${CODING_ROOT}/N8N/Workflows` | N8N workflows project |
| `${N8N_AGENTS}` | `${CODING_ROOT}/N8N/AGENTS` | N8N agent definitions |
| `${N8N_PATTERNS}` | `${N8N_WORKFLOWS}/.claude/patterns` | N8N pattern library |

## Resolution Order

1. Check environment variables first
2. Fall back to `config/paths.yaml` definitions
3. Fall back to hardcoded defaults

## Usage in Commands

### Current Syntax (Pre-Migration)
```markdown
Read the file at ~/.claude/agents/n8n-mcp-delegate.md
```

### Future Syntax (Post-Migration)
```markdown
Read the file at ${CLAUDE_AGENTS}/n8n-mcp-delegate.md
```

## Variable Substitution Rules

### Rule 1: Absolute User Paths
```
/Users/jelalconnor/...  →  ${HOME}/...
```

### Rule 2: Tilde Home Paths
```
~/.claude/...  →  ${CLAUDE_HOME}/...
~/CODING/...   →  ${CODING_ROOT}/...
~/.local/synrg/...  →  ${SYNRG_HOME}/...
```

### Rule 3: Derived Paths
```
${CLAUDE_HOME}/agents/...  →  ${CLAUDE_AGENTS}/...
${CLAUDE_HOME}/commands/...  →  ${CLAUDE_COMMANDS}/...
${CLAUDE_HOME}/skills/...  →  ${CLAUDE_SKILLS}/...
```

## Environment Detection

Commands should detect the environment at runtime:

```yaml
# Runtime resolution pseudocode
resolve_path(template):
  1. If contains ${HOME}: replace with $HOME env var
  2. If contains ${CLAUDE_HOME}: replace with $HOME/.claude
  3. If contains ${SYNRG_HOME}: replace with $HOME/.local/synrg
  4. If contains ${CODING_ROOT}: replace with $HOME/CODING
  5. Apply derived variable substitutions
  6. Return resolved path
```

## Portability Guidelines

### DO
- Use `${CLAUDE_HOME}` for all .claude directory references
- Use `${HOME}` for user-specific paths
- Define project-specific variables for external resources
- Document any new variables in this file

### DON'T
- Hardcode `/Users/username/` paths
- Use `~` notation in command content (shell-specific)
- Assume directory structures exist without validation
- Create circular variable references

## Migration Status

| Command | Paths Found | Status |
|---------|-------------|--------|
| synrg.md | 25 | pending |
| synrg-refactor.md | 7 | pending |
| synrg-commit.md | 5 | pending |
| synrg-spec.md | 6 | pending |
| synrg-scaffold.md | 4 | pending |
| synrg-guided.md | 7 | pending |
| synrg-buildworkflow.md | 7 | pending |
| synrg-swarm.md | 12 | pending |
| synrg-evolve.md | 12 | pending |
| CLAUDE.md | 2 | pending |
| **Total** | **87** | **pending** |

## Validation

To validate all paths resolve correctly:

```bash
# Check for unresolved variables
grep -r '\${[A-Z_]*}' ~/.claude/commands/ | grep -v '^#'

# Check for remaining hardcoded paths
grep -rn '/Users/jelalconnor' ~/.claude/commands/
grep -rn '~/.claude' ~/.claude/commands/
```

## Version History

- v1.0.0 (2026-01-09): Initial path variable system definition
