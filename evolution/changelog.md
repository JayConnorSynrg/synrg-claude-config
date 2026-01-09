# SYNRG Evolution Changelog

All notable changes to the SYNRG command system will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned - Phase 4: Extension Points
- Add `<!-- EXTENSION: custom-agents -->` markers
- Create hook registration system
- Document extension API

### Planned - Phase 5: Version Infrastructure
- Add version headers to all commands
- Implement compatibility checking
- Create migration scripts

### Planned - Phase 6: Sub-Agent Chaining
- Create command registry API
- Implement inter-command communication
- Add dependency resolution

---

## [1.2.0] - 2026-01-09

### Added - Phase 3: Path Variables Infrastructure

Created path variable system for portability (87 paths identified across 10 files):

**Core Variables Defined:**
| Variable | Resolves To |
|----------|-------------|
| `${HOME}` | User home directory |
| `${CLAUDE_HOME}` | `${HOME}/.claude` |
| `${SYNRG_HOME}` | `${HOME}/.local/synrg` |
| `${CODING_ROOT}` | `${HOME}/CODING` |

**Derived Variables:**
| Variable | Resolves To |
|----------|-------------|
| `${CLAUDE_AGENTS}` | `${CLAUDE_HOME}/agents` |
| `${CLAUDE_COMMANDS}` | `${CLAUDE_HOME}/commands` |
| `${CLAUDE_SKILLS}` | `${CLAUDE_HOME}/skills` |
| `${CLAUDE_PROTOCOLS}` | `${CLAUDE_HOME}/protocols` |

**Infrastructure Files Created:**
- `config/paths.yaml` v1.1.0 - Updated with resolver configuration
- `config/path-resolver.md` - Variable syntax documentation
- `evolution/migration/phase3-path-variables.yaml` - Complete migration manifest
- `evolution/migration/migrate-paths.sh` - Executable migration script

**Paths Identified by File:**
| File | Paths Found |
|------|-------------|
| synrg.md | 25 |
| synrg-swarm.md | 12 |
| synrg-evolve.md | 12 |
| synrg-buildworkflow.md | 7 |
| synrg-guided.md | 7 |
| synrg-refactor.md | 7 |
| synrg-spec.md | 6 |
| synrg-commit.md | 5 |
| synrg-scaffold.md | 4 |
| CLAUDE.md | 2 |

### Notes
- Infrastructure is ready but NOT applied to commands yet
- Original commands remain unchanged (backward compatible)
- Run `DRY_RUN=false ~/.claude/evolution/migration/migrate-paths.sh` to apply
- Phase 4 will add extension point markers

---

## [1.1.0] - 2026-01-09

### Added - Phase 2: Protocol Extraction
Extracted 6 standalone protocol modules from SYNRG commands (2,331 total lines):

| Protocol | File | Lines | Source Commands |
|----------|------|-------|-----------------|
| MCDP | `mcdp.yaml` | 165 | synrg, synrg-refactor, synrg-swarm, synrg-buildworkflow |
| Sub-Agent Spawn | `sub-agent-spawn.yaml` | 675 | synrg, synrg-guided, synrg-refactor |
| Value-First | `value-first.yaml` | 280 | synrg, synrg-spec |
| Git Commit | `git-commit.yaml` | 450 | synrg-commit |
| Phase Gate | `phase-gate.yaml` | 406 | synrg-spec, synrg-scaffold |
| MCP Config | `mcp-config.yaml` | 355 | synrg, synrg-buildworkflow, synrg-swarm |

### Added - Protocol Infrastructure
- `protocols/loader.md` - Protocol import syntax documentation
- Updated `protocols/index.yaml` to v1.1.0 with extraction status

### Protocol Import Syntax (Future Use)
```markdown
<!-- PROTOCOL_IMPORT: mcdp -->
<!-- PROTOCOL_IMPORT: sub-agent-spawn -->
```

### Notes
- Original commands remain unchanged (backward compatible)
- Protocols are extracted copies, not replacements yet
- Phase 3 will implement path variables for command integration

---

## [1.0.0] - 2026-01-09

### Added
- Initial GitHub repository setup at https://github.com/JayConnorSynrg/synrg-claude-config
- Phase 1 directory structure:
  - `protocols/` - For extracted protocol modules
  - `templates/` - For command-specific templates
  - `config/` - For centralized configuration
  - `evolution/` - For version tracking and migration
- Registry files:
  - `protocols/index.yaml` - Protocol extraction queue
  - `config/paths.yaml` - Centralized path configuration
  - `config/dependencies.yaml` - Inter-command dependency manifest
  - `evolution/changelog.md` - This file
- Modularity analysis of all 9 SYNRG commands (avg score: 5.2/10)

### Identified Issues (Pre-Refactor Baseline)
- 12+ hardcoded absolute paths across commands
- MCDP duplicated in 4 commands (~100% duplication)
- No version markers in any command file
- Zero extension points defined
- Monolithic architecture (largest: synrg.md at 5,800 lines)

### Commands Included
| Command | Lines | Modularity Score |
|---------|-------|------------------|
| /synrg | 5,800 | 4.8/10 |
| /synrg-guided | ~2,500 | 5.0/10 |
| /synrg-commit | ~1,500 | 5.0/10 |
| /synrg-refactor | 3,149 | 4.0/10 |
| /synrg-spec | ~2,000 | 6.5/10 |
| /synrg-scaffold | ~1,800 | 6.2/10 |
| /synrg-buildworkflow | ~800 | 4.9/10 |
| /synrg-swarm | ~2,200 | 6.5/10 |
| /synrg-evolve | ~400 | 5.3/10 |

### Agents Included
- agency-automation-expert
- fashion-brand-operations
- full-stack-dev-expert
- github-code-pattern-analyzer
- github-docs-extractor
- github-insights-synthesizer
- github-mcp-delegate
- github-repo-director
- github-structure-analyzer
- n8n-connection-fixer
- n8n-expression-debugger
- n8n-mcp-delegate
- n8n-node-validator
- n8n-pattern-retriever
- n8n-version-researcher
- n8n-workflow-expert

### Skills Included
- certainty-gated-atomic-change
- commit-message-craft
- enterprise-security-review
- git-strategy-decision
- mandatory-context-delegation
- universal-synrg-protocols

### Hooks Included
- synrg-commit-reminder.py
- synrg-security-gate.py
- synrg-hooks.json

---

## Migration Guide

### From Pre-1.0 (Unversioned)
No migration required. This is the initial versioned release capturing the existing command set.

### Future Migrations
Migration guides will be added to `evolution/migration/` as breaking changes are introduced.
