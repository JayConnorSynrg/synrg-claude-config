# SYNRG Extension API

This document defines the extension API for adding custom functionality to SYNRG commands without modifying core files.

## Overview

The extension system allows you to:
- Add custom agents to any command
- Define new validation layers
- Register pattern libraries
- Add custom protocol rules
- Create hook integrations

## Extension Point Markers

Commands contain markers indicating where extensions can be injected:

```markdown
<!-- EXTENSION: {category}-{name} -->
```

### Categories

| Category | Purpose | Example Marker |
|----------|---------|----------------|
| `agents` | Custom agent definitions | `<!-- EXTENSION: agents-mcp-delegates -->` |
| `protocols` | Custom protocol rules | `<!-- EXTENSION: protocols-mcp-patterns -->` |
| `validators` | Custom validation layers | `<!-- EXTENSION: validators-layers -->` |
| `patterns` | Custom pattern libraries | `<!-- EXTENSION: patterns-known-failures -->` |
| `templates` | Custom templates | `<!-- EXTENSION: templates-commit-messages -->` |
| `hooks` | Custom hook registrations | `<!-- EXTENSION: hooks-pre-execution -->` |
| `phases` | Custom workflow phases | `<!-- EXTENSION: phases-evolution -->` |
| `tools` | Custom tool configurations | `<!-- EXTENSION: tools-custom -->` |

## Creating Extensions

### Extension File Structure

```yaml
# ~/.claude/extensions/{category}/{extension-id}.yaml

id: "my-extension"
name: "My Custom Extension"
version: "1.0.0"
category: "{category}"

# Which commands this extension applies to
target_commands:
  - synrg.md
  - synrg-refactor.md

# Which marker to inject at
injection_point: "<!-- EXTENSION: {category}-{name} -->"

# The content to inject
content: |
  [Your extension content here]
  This will be inserted at the marker location.

# Metadata
metadata:
  author: "your-name"
  created: "2026-01-09"
  description: "What this extension does"
  dependencies: []  # Other extensions required
```

### Extension Examples

#### 1. Custom Agent Extension

```yaml
# ~/.claude/extensions/agents/security-analyst.yaml

id: "security-analyst"
name: "Security Analysis Agent"
version: "1.0.0"
category: agents

target_commands:
  - synrg.md
  - synrg-refactor.md

injection_point: "<!-- EXTENSION: agents-reconnaissance -->"

content: |
  - id: security-analyst
    role: "Security vulnerability scanner"
    task: "Analyze code for OWASP Top 10 vulnerabilities"
    tools: ["Grep", "Read", "Glob"]
    deliverable: "Security risk assessment report"

metadata:
  author: "security-team"
  description: "Adds security scanning to reconnaissance phase"
```

#### 2. Custom Validator Extension

```yaml
# ~/.claude/extensions/validators/compliance-layer.yaml

id: "compliance-layer"
name: "Compliance Validation Layer"
version: "1.0.0"
category: validators

target_commands:
  - synrg.md
  - synrg-spec.md

injection_point: "<!-- EXTENSION: validators-layers -->"

content: |
  ### Layer 5: Compliance Validation
  - [ ] GDPR data handling requirements met
  - [ ] SOC2 audit trail present
  - [ ] PCI-DSS requirements for payment data
  - [ ] HIPAA compliance for health data
  - [ ] Accessibility (WCAG 2.1) verified

metadata:
  author: "compliance-team"
  description: "Adds regulatory compliance checks"
```

#### 3. Custom Protocol Extension

```yaml
# ~/.claude/extensions/protocols/cost-tracking.yaml

id: "cost-tracking"
name: "Cost Tracking Protocol"
version: "1.0.0"
category: protocols

target_commands:
  - synrg.md

injection_point: "<!-- EXTENSION: protocols-execution-rules -->"

content: |
  ### Cost Tracking Rules
  1. **Token Budget Enforcement**
     - Track tokens per sub-agent
     - Alert when 80% budget consumed
     - Hard stop at 100% budget

  2. **Cost Attribution**
     - Tag each agent invocation with cost center
     - Report total cost per objective
     - Compare against estimates

metadata:
  author: "platform-team"
  description: "Adds token cost tracking to execution"
```

#### 4. Custom Pattern Extension

```yaml
# ~/.claude/extensions/patterns/react-patterns.yaml

id: "react-patterns"
name: "React Development Patterns"
version: "1.0.0"
category: patterns

target_commands:
  - synrg.md
  - synrg-refactor.md

injection_point: "<!-- EXTENSION: patterns-known-failures -->"

content: |
  | React Hooks | useEffect dependency arrays | hooks-reference.md |
  | React State | Stale closure patterns | state-patterns.md |
  | React Perf | Unnecessary re-renders | perf-guide.md |

metadata:
  author: "frontend-team"
  description: "React-specific anti-patterns"
```

## Hook System

### Hook Types

| Hook Type | Trigger Point | Use Case |
|-----------|---------------|----------|
| `pre-execution` | Before command runs | Validation, setup |
| `post-execution` | After command completes | Cleanup, reporting |
| `validation` | During validation phase | Custom checks |
| `evolution` | During evolution phase | Pattern learning |

### Hook Registration

```yaml
# ~/.claude/extensions/hooks/my-hook.yaml

id: "my-pre-hook"
name: "Pre-Execution Setup Hook"
version: "1.0.0"
category: hooks

hook_type: "pre-execution"
trigger: "always"  # always | on-condition

# Shell script or Python file to execute
executor: "${CLAUDE_HOME}/hooks/my-hook.py"

# Arguments passed to executor
arguments:
  - "${OBJECTIVE}"
  - "${COMMAND_NAME}"

# Expected return codes
success_codes: [0]
failure_action: "abort"  # abort | warn | ignore

metadata:
  author: "platform-team"
  description: "Sets up environment before execution"
```

### Hook Script Example

```python
#!/usr/bin/env python3
# ~/.claude/hooks/my-hook.py

import sys
import json

def main():
    objective = sys.argv[1] if len(sys.argv) > 1 else ""
    command = sys.argv[2] if len(sys.argv) > 2 else ""

    # Perform pre-execution checks
    print(f"Pre-execution hook for: {command}")
    print(f"Objective: {objective}")

    # Return 0 for success, non-zero to abort
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

## Extension Loading

### Load Order

1. **Protocols** - Rules loaded first to establish constraints
2. **Validators** - Validation layers loaded next
3. **Patterns** - Pattern libraries loaded
4. **Agents** - Agent definitions loaded
5. **Templates** - Templates loaded
6. **Hooks** - Hooks registered last

### Conflict Resolution

When multiple extensions target the same injection point:

| Strategy | Behavior |
|----------|----------|
| `first-wins` | First registered extension takes precedence |
| `last-wins` | Last registered extension takes precedence |
| `merge` | Content from all extensions is merged |
| `error` | Raise error on conflict |

Configure in `config/extensions.yaml`:

```yaml
resolution:
  conflict_strategy: "merge"
```

## Validation

Extensions are validated before loading:

1. **Schema validation** - YAML structure matches expected format
2. **Target validation** - Target commands exist
3. **Marker validation** - Injection point markers exist
4. **Dependency validation** - Required extensions are present

### Manual Validation

```bash
# Validate all extensions
synrg extension validate --all

# Validate specific extension
synrg extension validate security-analyst
```

## Extension Commands

```bash
# List all registered extensions
synrg extension list

# Register new extension
synrg extension register ./my-extension.yaml

# Unregister extension
synrg extension unregister my-extension

# Show extension details
synrg extension show my-extension

# Validate extension
synrg extension validate my-extension
```

## Best Practices

### DO
- Use descriptive IDs and names
- Include comprehensive metadata
- Version your extensions
- Document dependencies
- Test extensions before registering

### DON'T
- Override core functionality
- Create circular dependencies
- Use hardcoded paths (use variables)
- Skip validation
- Forget to update version on changes

## Migration from Embedded to Extension

To migrate embedded customizations to extensions:

1. Identify the customization in command file
2. Find the nearest extension point marker
3. Create extension YAML file
4. Register the extension
5. Remove embedded customization (optional)

This maintains backward compatibility while enabling modular management.
