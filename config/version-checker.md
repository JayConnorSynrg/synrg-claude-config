# SYNRG Version Compatibility Checker

This document defines the version checking system for SYNRG commands, ensuring compatibility between components.

## Version Header Format

All SYNRG commands should include a YAML frontmatter version header:

```yaml
---
synrg_version: "4.0.0"
command: "synrg"
created: "2025-01-01"
updated: "2026-01-09"
min_claude_version: "opus-4"
requires:
  protocols:
    - mcdp@1.0.0
    - sub-agent-spawn@1.0.0
  agents:
    - n8n-mcp-delegate
    - github-mcp-delegate
  skills:
    - mandatory-context-delegation
breaking_changes:
  - version: "4.0.0"
    description: "Added MCDP mandatory delegation"
---
```

## Semantic Versioning

All versions follow [Semantic Versioning](https://semver.org/):

```
MAJOR.MINOR.PATCH

MAJOR - Breaking changes, incompatible API changes
MINOR - New features, backward compatible
PATCH - Bug fixes, backward compatible
```

### Version Bump Guidelines

| Change Type | Version Bump | Example |
|-------------|--------------|---------|
| Breaking protocol change | MAJOR | 1.0.0 → 2.0.0 |
| New agent requirement | MINOR | 1.0.0 → 1.1.0 |
| Bug fix, typo correction | PATCH | 1.0.0 → 1.0.1 |
| New optional feature | MINOR | 1.0.0 → 1.1.0 |
| Remove deprecated feature | MAJOR | 1.0.0 → 2.0.0 |

## Compatibility Checking

### Pre-Execution Check

Before executing a SYNRG command, verify:

1. **Protocol Compatibility**
   ```
   For each required protocol:
     - Check protocol exists
     - Check version >= minimum required
     - If incompatible: HALT with upgrade instructions
   ```

2. **Agent Availability**
   ```
   For each required agent:
     - Check agent file exists at ${CLAUDE_AGENTS}/{agent}.md
     - Check agent version >= minimum required
     - If missing: WARN and suggest installation
   ```

3. **Skill Availability**
   ```
   For each required skill:
     - Check skill file exists at ${CLAUDE_SKILLS}/{skill}.md
     - If missing: WARN and suggest installation
   ```

### Compatibility Check Pseudocode

```python
def check_compatibility(command):
    versions = load_yaml("config/versions.yaml")
    command_info = versions["commands"][command]

    errors = []
    warnings = []

    # Check protocols
    for protocol, min_version in command_info["dependencies"]["protocols"]:
        protocol_info = versions["protocols"].get(protocol)
        if not protocol_info:
            errors.append(f"Missing protocol: {protocol}")
        elif not version_satisfies(protocol_info["current_version"], min_version):
            errors.append(f"Protocol {protocol} version {protocol_info['current_version']} < {min_version}")

    # Check agents
    for agent in command_info["dependencies"]["agents"]:
        agent_path = f"$CLAUDE_AGENTS/{agent}.md"
        if not file_exists(agent_path):
            warnings.append(f"Missing agent: {agent}")

    # Check skills
    for skill in command_info["dependencies"]["skills"]:
        skill_path = f"$CLAUDE_SKILLS/{skill}.md"
        if not file_exists(skill_path):
            warnings.append(f"Missing skill: {skill}")

    return errors, warnings
```

## Version Comparison

### Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `>=` | Greater than or equal | `>=1.0.0` matches 1.0.0, 1.1.0, 2.0.0 |
| `>` | Greater than | `>1.0.0` matches 1.0.1, 1.1.0, 2.0.0 |
| `=` | Exact match | `=1.0.0` matches only 1.0.0 |
| `~` | Compatible (same major) | `~1.0.0` matches 1.0.x, 1.1.x |
| `^` | Compatible (same major.minor) | `^1.0.0` matches 1.0.x |

### Version Satisfaction Logic

```python
def version_satisfies(current, requirement):
    op, required = parse_requirement(requirement)

    current_parts = parse_version(current)
    required_parts = parse_version(required)

    if op == ">=":
        return current_parts >= required_parts
    elif op == ">":
        return current_parts > required_parts
    elif op == "=":
        return current_parts == required_parts
    elif op == "~":
        return current_parts[0] == required_parts[0]
    elif op == "^":
        return (current_parts[0] == required_parts[0] and
                current_parts[1] == required_parts[1])
```

## Breaking Change Documentation

When introducing breaking changes:

1. **Increment MAJOR version**
2. **Document in breaking_changes array**
3. **Create migration guide**
4. **Update min_compatible version**

### Breaking Change Entry Format

```yaml
breaking_changes:
  - version: "2.0.0"
    description: "Changed MCDP delegation to be mandatory"
    migration: "evolution/migration/v1-to-v2.md"
    affected_commands:
      - synrg
      - synrg-refactor
```

## Current Version Status

| Command | Version | Has Header | Dependencies |
|---------|---------|------------|--------------|
| synrg | 4.0.0 | No | mcdp, sub-agent-spawn, value-first, mcp-config |
| synrg-refactor | 3.0.0 | Yes | mcdp, sub-agent-spawn |
| synrg-commit | 1.0.0 | Yes | git-commit |
| synrg-spec | 1.0.0 | No | value-first, phase-gate |
| synrg-scaffold | 2.0.0 | Yes | phase-gate |
| synrg-guided | 4.3.0 | No | sub-agent-spawn, phase-gate |
| synrg-buildworkflow | 1.0.0 | No | mcdp, mcp-config |
| synrg-swarm | 1.0.0 | No | mcdp, sub-agent-spawn, mcp-config |
| synrg-evolve | 1.0.0 | No | (none) |

## Adding Version Headers

To add version headers to commands:

1. **Backup command file**
2. **Insert YAML frontmatter at line 1**
3. **Validate header syntax**
4. **Update versions.yaml**

### Header Injection Script

```bash
# See evolution/migration/inject-version-headers.sh
```

## Upgrade Notifications

When a user runs an outdated command:

```
⚠️ SYNRG VERSION NOTICE
━━━━━━━━━━━━━━━━━━━━━━
Command: synrg-refactor
Current: 3.0.0
Latest:  3.1.0

Changes in 3.1.0:
- Added security analysis agent
- Improved parallel batching

Run 'synrg upgrade synrg-refactor' to update
```

## Deprecation Warnings

When using deprecated features:

```
⚠️ DEPRECATION WARNING
━━━━━━━━━━━━━━━━━━━━━━
Feature: Direct MCP calls without delegation
Deprecated in: synrg 4.0.0
Removal planned: synrg 5.0.0

Use MCDP delegation instead. See:
~/.claude/protocols/mcdp.yaml
```
