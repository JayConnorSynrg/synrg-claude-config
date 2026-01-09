# Claude Code Documentation Index

**Last Updated:** 2025-11-22
**Purpose:** Comprehensive index of all Claude Code documentation for quick reference

---

## 🎯 Quick Navigation

- [Core Configuration](#core-configuration)
- [SYNRG Orchestration](#synrg-orchestration)
- [Agent Development](#agent-development)
- [MCP Integration](#mcp-integration)
- [Testing & Validation](#testing--validation)
- [Project-Specific Guides](#project-specific-guides)
- [Framework Documentation](#framework-documentation)

---

## Core Configuration

### Global Instructions
| File | Location | Purpose |
|------|----------|---------|
| **CLAUDE.md** | `~/.claude/` | Global user preferences, decision protocols, system context |
| **settings.json** | `~/.claude/` | Global Claude Code settings |
| **.claude.json** | `~/` | Alternative user-level configuration (51KB) |

### Project-Level Configuration (Standard Structure)
All projects follow this pattern in project root:
```
project/
├── CLAUDE.md              # Project-specific instructions
├── CLAUDE.local.md        # Personal notes (gitignored)
├── .mcp.json              # MCP server configuration
├── .gitignore             # Should exclude CLAUDE.local.md
└── .claude/
    ├── settings.json      # Permissions & tool configs
    ├── rules.md           # Coding standards
    ├── context.md         # Project info & how to run
    ├── prompts.md         # Reusable prompt templates
    ├── agents/            # Project-specific agents (optional)
    └── commands/          # Project-specific slash commands (optional)
```

---

## SYNRG Orchestration

### 🔴 CRITICAL: Two-Tier SYNRG System

**Tier 1: Full Enterprise Orchestrator** (Primary)
- **Location:** `~/.claude/commands/synrg.md` (4,524 lines, 149KB)
- **Trigger:** `/synrg [objective]` slash command
- **Purpose:** Complete enterprise multi-agent coordination
- **Features:**
  - STEP 2.75: VALUE-FIRST PRE-CHANGE ANALYSIS (mandatory)
  - Director/Orchestrator Pattern v4.0 (parallel sub-agents)
  - Interactive Context Gathering (AskUserQuestion)
  - 6-Phase Value Analysis (Reconnaissance → Quantification → Impact → Protection → Decision → Escalation)
  - Robustness-First Manifesto
  - Auto-Generated File Detection
  - Quality-First Decision Framework

**Tier 2: Operational Protocol** (Project-Level)
- **Location:** `~/CODING/SYNRG AGENTS/agent-swarm-native/.claude/claude.md` (330+ lines)
- **Trigger:** Automatic when working in SYNRG projects
- **Purpose:** Core execution principles, validation, and context management
- **Features:**
  - Zero false positives
  - Regression protection
  - Autonomous fix-test loops
  - Evidence-based validation (screenshots)
  - Incremental perfection
  - Reality Check validation protocol
  - **🆕 80% Context Window Management** (consolidation protocol)
  - **🆕 Director/Orchestrator Consolidation** (60-70% context reduction)
  - **🆕 Value-First Analysis Principles** (understand → quantify → enhance)
  - **🆕 Vital Documentation** (session-state.md, architecture-decisions.md, critical-findings.md)

**Python Orchestrator Script:**
```bash
cd "/Users/jelalconnor/CODING/SYNRG AGENTS/agent-swarm-native/BMAD-METHOD" && python3 synrg_orchestrator.py
```

### SYNRG Core Documentation

| Document | Location | Purpose |
|----------|----------|---------|
| **SYNRG System Overview** | `~/.claude/SYNRG_SYSTEM_OVERVIEW.md` | **Three-tier architecture explained, decision tree for which tier to use** |
| **Context Efficiency Rules** | `~/.claude/CONTEXT_EFFICIENCY_RULES.md` | **🆕 Ubiquitous efficiency rules from /synrg for reliable execution** |
| **Operational Protocol** | `SYNRG AGENTS/agent-swarm-native/.claude/claude.md` | Project-specific operational protocol (330+ lines) - DEFERS to /synrg |

### SYNRG V1 Documentation (Archived)

**Status:** Deprecated - Superseded by `/synrg` command v4.0
**Location:** `SYNRG AGENTS/Deprecated-Agent-Swarm-V1/`

| Document | Purpose | Status |
|----------|---------|--------|
| **Archive README** | Explains deprecation and migration path | **READ THIS FIRST** |
| **Hierarchical Architecture** | Original Director → Specialist pattern | Superseded by /synrg v4.0 |
| **Implementation Guide** | V1 setup instructions | Outdated |
| **Parallel Efficiency** | V1 parallelization strategies | Superseded by /synrg v4.0 |
| **Testing Framework** | V1 testing infrastructure | Superseded by /synrg v4.0 |
| **Director Templates** | Software Dev, Clothing Brand, Agency Automation | Superseded by /synrg v4.0 |
| **Agent Templates** | Sub-agent templates | Superseded by /synrg v4.0 |
| **Test Scripts** | V1 validation scripts | Outdated |
| **Integration Docs** | Playwright MCP, Vercel, ZenCoder | Project-specific, archived |

### SYNRG Slash Commands (User-Level)

| Command | Location | Purpose | Size |
|---------|----------|---------|------|
| **/synrg** | `~/.claude/commands/synrg.md` | Multi-agent orchestration director with VALUE-FIRST analysis | 149KB |
| **/synrg-refactor** | `~/.claude/commands/synrg-refactor.md` | File restructuring agent with parallel sub-agents | 82KB |
| **/synrg-swarm** | `~/.claude/commands/synrg-swarm.md` | Sub-agent development and task decomposition | 55KB |
| **/synrg-commit** | `~/.claude/commands/synrg-commit.md` | Git workflow automation with SYNRG validation | 39KB |
| **/synrg-buildworkflow** | `~/.claude/commands/synrg-buildworkflow.md` | **n8n workflow builder** - Orchestrates 10 n8n specialist agents | 19KB |
| **/synrg-evolve** | `~/.claude/commands/synrg-evolve.md` | Self-evolution patterns and integration | 10.7KB |

#### `/synrg-buildworkflow` Details

**Purpose:** Production-ready n8n workflow building orchestrator

**Features:**
- Coordinates 10 specialized n8n agents (architect, builder, validator, troubleshooter, etc.)
- 95%+ success rate target
- 10-15 minute workflow delivery
- 0 errors, 0 warnings quality standard
- Robustness-first, parallel-optimized

**Architecture:**
```
PHASE 1: PRE-BUILD VALIDATION (Parallel)
├─ Credential Manager (CRITICAL)
├─ Discovery Agent (Research)
└─ Architect Agent (Design)

PHASE 2: BUILD + INITIAL VALIDATION (Sequential)
└─ Builder Agent → Validator Agent

PHASE 3: ERROR REDUCTION (Progressive)
└─ Troubleshooter + Error Handler (6→4→2→0 errors)

PHASE 4: FINAL VALIDATION
└─ Optimizer + Documentation + Final Validator
```

**When to use:**
- Building n8n workflows from scratch
- Need production-ready workflow (not prototype)
- Want systematic validation and 0-error delivery
- Coordinating multiple n8n patterns

**Related:** Works with 10 n8n specialist agents (see Agent Development section)

### SYNRG Analysis Documentation

| Document | Location | Purpose |
|----------|----------|---------|
| **CRUD Coverage** | `SYNRG AGENTS/agent-swarm-native/CRUD-COVERAGE-ANALYSIS.md` | CRUD operation analysis |
| **Post-Validation Strategy** | `SYNRG AGENTS/agent-swarm-native/POST-VALIDATION-STRATEGY-ANALYSIS.md` | Validation approaches |
| **Final Implementation Summary** | `SYNRG AGENTS/agent-swarm-native/FINAL_IMPLEMENTATION_SUMMARY.md` | System completion overview |
| **Testing Summary** | `SYNRG AGENTS/agent-swarm-native/TESTING_SUMMARY.md` | Test results |

---

## Agent Development

### Agent Creation Guides

| Document | Location | Purpose |
|----------|----------|---------|
| **CREATE_AGENTS.md** | `SYNRG AGENTS/agent-swarm-native/` | Guide for creating custom agents |
| **Custom Agent Directory Structure** | `SYNRG AGENTS/agent-swarm-native/CUSTOM_AGENT_DIRECTORY_STRUCTURE.md` | Agent organization patterns |
| **Agent Performance Evaluator** | `SYNRG AGENTS/agent-swarm-native/director-templates/analysis-team/agent-performance-evaluator.md` | Evaluation specialist |
| **Custom Agent Designer** | `SYNRG AGENTS/agent-swarm-native/director-templates/analysis-team/custom-agent-designer.md` | Meta-agent for design |
| **Sub-Agent Strategy Architect** | `SYNRG AGENTS/agent-swarm-native/director-templates/analysis-team/sub-agent-strategy-architect.md` | Strategic design |

### User-Level Agents (Available Everywhere)

| Agent | Location | Specialization |
|-------|----------|----------------|
| **full-stack-dev-expert** | `~/.claude/agents/full-stack-dev-expert.md` | Comprehensive software development |
| **fashion-brand-operations** | `~/.claude/agents/fashion-brand-operations.md` | Clothing brand management |
| **agency-automation-expert** | `~/.claude/agents/agency-automation-expert.md` | Business automation |

### Project-Level Agents

**CLAUDE CLI - n8n Specialists (13 agents):**
- Location: `~/CODING/CLAUDE CLI/.claude/agents/`
- **n8n-architect** - Workflow architecture design
- **n8n-builder** - Workflow implementation
- **n8n-credential-manager** - Credential security
- **n8n-data-flow-analyst** - Data transformation
- **n8n-discovery** - Node discovery
- **n8n-documentation** - Workflow documentation
- **n8n-error-handler** - Error handling
- **n8n-optimizer** - Performance optimization
- **n8n-troubleshooter** - Debugging
- **n8n-validator** - Pre-deployment validation
- Plus: AGENT_UPDATE_SUMMARY.md, MCP_INTEGRATION_SUMMARY.md, N8N_MCP_INTEGRATION_GUIDE.md

**SYNRG AGENTS - Multi-Domain Specialists (22 agents):**
- Location: `~/CODING/SYNRG AGENTS/agent-swarm-native/.claude/agents/custom/`
- Organized by domain:
  - `validation-deployment/` (4 agents)
  - `workflow-automation/` (1 agent)
  - `business-sectors/fashion/` (1 agent)
  - `technology-domains/` (6 agents: database, frontend, backend, testing, performance, validation)
  - `compliance-security/` (3 agents)
  - `strategy-orchestration/` (4 agents)

**Archon - Analysis Specialists (2 agents):**
- Location: `~/CODING/SYNRG AGENTS/agent-swarm-native/BMAD-METHOD/Archon/.claude/agents/`
- **codebase-analyst** - Codebase analysis
- **library-researcher** - Library research

---

## MCP Integration

### MCP Setup Guides

| Document | Location | Purpose |
|----------|----------|---------|
| **Playwright MCP Setup** | `SYNRG AGENTS/agent-swarm-native/PLAYWRIGHT_MCP_SETUP.md` | Visual feedback integration (11KB) |
| **Vercel MCP Deployment** | `SYNRG AGENTS/agent-swarm-native/VERCEL_MCP_DEPLOYMENT_SETUP.md` | Deployment automation (14KB) |
| **N8N MCP Integration** | `CLAUDE CLI/.claude/agents/N8N_MCP_INTEGRATION_GUIDE.md` | n8n workflow integration |
| **MCP Integration Summary** | `CLAUDE CLI/.claude/agents/MCP_INTEGRATION_SUMMARY.md` | Overview for CLAUDE CLI |
| **MCP Setup Summary** | `CLAUDE CLI/.claude/MCP_SETUP_SUMMARY.md` | Project-level MCP setup |

### Supabase Integration

| Document | Location | Purpose |
|----------|----------|---------|
| **Supabase Connection Guide** | `HAUNTR/docs/CLAUDE_CODE_SUPABASE_CONNECTION_GUIDE.md` | Working methods for Claude Code |
| **Supabase Connection Contexts** | `HAUNTR/.claude/SUPABASE_CONNECTION_CONTEXTS.md` | AI agent vs app runtime patterns |
| **Supabase MCP Config Rules** | `HAUNTR/SUPABASE_MCP_CONFIG_RULES.md` | Configuration guidelines |

### MCP Configuration Files

| File | Location | Purpose |
|------|----------|---------|
| **mcp.json** | `~/.claude/mcp.json` | User-level MCP servers (Supabase, company-rag) |
| **.mcp.json** | Project roots | Project-specific MCP servers |

---

## Testing & Validation

### Testing Frameworks

| Document | Location | Purpose |
|----------|----------|---------|
| **SYNRG Testing Framework** | `SYNRG AGENTS/agent-swarm-native/TESTING_FRAMEWORK.md` | Comprehensive testing infrastructure (12KB) |
| **Playwright Enhanced Rules** | `SYNRG AGENTS/.../BMAD-METHOD/PLAYWRIGHT_ENHANCED_AGENT_RULES.md` | Playwright best practices |
| **Reality Check Validation Agent** | `SYNRG AGENTS/agent-swarm-native/templates/reality-check-validation-agent.md` | Validation specialist template |

### Test Reports

| Document | Location | Purpose |
|----------|----------|---------|
| **Final Test Report** | `SYNRG AGENTS/agent-swarm-native/FINAL_TEST_REPORT.md` | Comprehensive test results |
| **Testing Summary** | `SYNRG AGENTS/agent-swarm-native/TESTING_SUMMARY.md` | Test execution summary |

---

## Project-Specific Guides

### n8n Workflow Guides

**Canonical Location:** `~/CODING/REPEATABLE PROJECTS/REPEATABLE MVP DELIVERABLE V1/docs/`

| Guide | Purpose |
|-------|---------|
| **n8n-workflow-setup-guide.md** | Workflow creation and setup |
| **n8n-supabase-workflow-setup.md** | Supabase integration patterns |
| **youtube-transcript-extraction-guide.md** | YouTube content processing |
| **workflow-creation-success-guide.md** | Success patterns |

**Note:** These guides have duplicate copies in:
- `CURSOR/Cursor N8N MCP/docs/`
- `IDE CODERS/CURSOR/Cursor-N8N-MCP-BACKUP-20250904-164741/docs/`
- `N8N-Integration/Cursor N8N MCP/docs/`

### Zencoder Variant

| Document | Location | Purpose |
|----------|----------|---------|
| **Zencoder Agent Architecture** | `SYNRG AGENTS/agent-swarm-native/ZENCODER_AGENT_ARCHITECTURE.md` | Zencoder patterns (10KB) |
| **Zencoder Agent Commands** | `SYNRG AGENTS/agent-swarm-native/ZENCODER_AGENT_COMMANDS.md` | Command reference (8KB) |
| **Zencoder Setup Guide** | `SYNRG AGENTS/agent-swarm-native/ZENCODER_SETUP_GUIDE.md` | Setup instructions (7.2KB) |
| **README Zencoder** | `SYNRG AGENTS/agent-swarm-native/README_ZENCODER.md` | Overview (9KB) |

### HR N8N Workflow

| Document | Location | Purpose |
|----------|----------|---------|
| **Agent Evolution Complete** | `HR N8N Workflow/AGENT-EVOLUTION-COMPLETE.md` | n8n agent methodology evolution |

### HAUNTR Project

| Document | Location | Purpose |
|----------|----------|---------|
| **Supabase Connection Guide** | `HAUNTR/docs/CLAUDE_CODE_SUPABASE_CONNECTION_GUIDE.md` | **CRITICAL** - Working Supabase patterns |
| **Agent Architecture** | `HAUNTR-chat-optimization/AGENT_ARCHITECTURE.md` | HAUNTR agent design |
| **Sub-Agent Specifications** | `HAUNTR-chat-optimization/SUB_AGENT_SPECIFICATIONS.md` | Specialized agents |

---

## Framework Documentation

### BMAD-METHOD

**Primary Location:** `~/CODING/FRAMEWORKS/BMAD-METHOD/` (or `SYNRG AGENTS/agent-swarm-native/BMAD-METHOD/`)

| Document | Location | Purpose |
|----------|----------|---------|
| **Core Architecture** | `BMAD-METHOD/docs/core-architecture.md` | Framework architecture |
| **User Guide** | `BMAD-METHOD/docs/user-guide.md` | Usage instructions |
| **CHANGELOG** | `BMAD-METHOD/CHANGELOG.md` | Version history |
| **BMAD Knowledge Base** | `BMAD-METHOD/bmad-core/data/bmad-kb.md` | Core knowledge |

### Archon

**Location:** `~/CODING/SYNRG AGENTS/agent-swarm-native/BMAD-METHOD/Archon/`

| Document | Purpose |
|----------|---------|
| **README.md** | Archon overview |
| **CLAUDE.md** | Beta development guidelines |
| **AGENTS.md** | Same as CLAUDE.md (error handling philosophy) |
| **CONTRIBUTING.md** | Contribution guidelines |
| **ARCHITECTURE.md** | PRP architecture (PRPs/ai_docs/) |

### Archon Slash Commands

**Location:** `~/CODING/SYNRG AGENTS/agent-swarm-native/BMAD-METHOD/Archon/.claude/commands/`

**archon/** (6 commands):
- archon-onboarding.md
- archon-prime.md
- archon-prime-simple.md
- archon-coderabbit-helper.md
- archon-rca.md (root cause analysis)
- archon-alpha-review.md

**prp-any-agent/** (2 commands):
- prp-any-cli-execute.md
- prp-any-cli-create.md

**prp-claude-code/** (4 commands):
- prp-claude-code-create.md
- prp-claude-code-execute.md
- prp-story-task-create.md
- prp-story-task-execute.md

---

## Model & API Documentation

| Document | Location | Purpose |
|----------|----------|---------|
| **Claude Haiku Analysis 2025** | `CLAUDE CLI/OPENROUTER_CLAUDE_HAIKU_ANALYSIS_2025.md` | Cost-benefit analysis for Claude Haiku |
| **Quick Reference** | `CLAUDE CLI/company-rag-system/QUICK_REFERENCE.md` | RAG system reference |

---

## ARK_OS Analysis (Research Documentation)

**Location:** `~/CODING/CLAUDE CLI/`

| Document | Purpose |
|----------|---------|
| **ARK_OS Agentic Framework Analysis** | Agentic framework research |
| **ARK_OS Framework Analysis** | Framework analysis |
| **ARK_OS Framework Analysis Planning** | Research planning |
| **FLOW Analysis Report** | Flow analysis |

---

## Utility Documentation

| Document | Location | Purpose |
|----------|----------|---------|
| **Swarm Initialization Prompt** | `SYNRG AGENTS/agent-swarm-native/SWARM_INITIALIZATION_PROMPT.md` | Swarm startup protocol |
| **Sensitive Keys Template** | `SYNRG AGENTS/agent-swarm-native/sensitive-keys-template.md` | Key management template |
| **Universal Sub-Agent Builder** | `N8N-Integration/VS STUDIO N8N MCP/universal-sub-agent-builder-prompt.md` | Universal agent builder |
| **claude-project-selector.sh** | `Development/claude-project-selector.sh` | Project selection script |

---

## GitHub Workflows

| Workflow | Location | Purpose |
|----------|----------|---------|
| **claude-review.yml** | `.github/workflows/` (Archon, agent-swarm-native) | Automated code review |
| **claude-fix.yml** | `.github/workflows/` (Archon) | Automated fixes |
| **claude-code-review.yml** | `.github/workflows/` (devteam) | Code review workflow |
| **claude.yml** | `.github/workflows/` (devteam) | Generic Claude workflow |

---

## Documentation by Project

### SYNRG AGENTS/agent-swarm-native/
- 25 documentation files
- **Primary**: SYNRG orchestration, agent development, testing
- **Key Files**: HIERARCHICAL_ARCHITECTURE.md, CREATE_AGENTS.md, IMPLEMENTATION_GUIDE.md

### CLAUDE CLI/
- 13 agent files + ARK_OS analysis docs
- **Primary**: n8n workflow development, ARK_OS research
- **Key Files**: n8n agent specs, MCP integration guides

### HAUNTR/
- Database integration, Supabase connection patterns
- **CRITICAL**: CLAUDE_CODE_SUPABASE_CONNECTION_GUIDE.md

### devteam/
- TypeScript CLI tool
- **Primary**: AGENTS.md (beta development guidelines)

### HR N8N Workflow/
- n8n workflow for HR resume analysis
- **Primary**: AGENT-EVOLUTION-COMPLETE.md

### REPEATABLE MVP DELIVERABLE V1/
- **Canonical n8n guides**
- PRD.md, PROJECT-INDEX.md, AVA-CHECKLIST.md

---

## Navigation Quick Reference

### By Task

**Need to create agents?**
→ `SYNRG AGENTS/agent-swarm-native/CREATE_AGENTS.md`

**Need to use SYNRG?**
→ `.claude/claude.md` (SYNRG Master Protocol)
→ Type "SYNRG" or use `/synrg` command

**Need Supabase integration?**
→ `HAUNTR/docs/CLAUDE_CODE_SUPABASE_CONNECTION_GUIDE.md` ⚠️ **READ THIS FIRST**

**Need n8n workflows?**
→ `CLAUDE CLI/.claude/agents/` (10 n8n specialists)
→ `REPEATABLE MVP/docs/` (canonical guides)

**Need testing patterns?**
→ `SYNRG AGENTS/.../TESTING_FRAMEWORK.md`
→ SYNRG Master Protocol validation sections

**Need MCP setup?**
→ Project-specific `.claude/agents/` MCP guides
→ `~/.claude/mcp.json` for user-level servers

### By File Type

**CLAUDE.md files:** Global + 7 project-specific instruction files
**Agent files:** 42 total (3 user-level + 39 project-level)
**Commands:** 36 total (6 user-level + 30 project-level)
**MCP docs:** 10+ integration guides

---

## Total Documentation Count

- **100+ markdown documentation files**
- **42 custom agents**
- **36 slash commands**
- **10+ MCP integration guides**
- **25+ SYNRG-specific docs**
- **13+ n8n workflow guides**

---

## Maintenance Notes

**Last Structure Update:** 2025-11-21 (Added Anthropic-recommended .claude/ structure to all projects)

**Canonical Sources:**
- n8n guides → `REPEATABLE MVP DELIVERABLE V1/docs/`
- BMAD-METHOD → `FRAMEWORKS/BMAD-METHOD/` or `SYNRG AGENTS/.../BMAD-METHOD/`
- SYNRG Protocol → `SYNRG AGENTS/agent-swarm-native/.claude/claude.md`

**Known Duplicates:**
- n8n guides (4 copies - marked above)
- BMAD-METHOD (2 locations)
- Archon (2 locations in agent-swarm-native projects)

---

## End of Index

For updates to this index, regenerate by searching:
```bash
find ~/CODING ~/.claude -name "*.md" -not -path "*/node_modules/*" -not -path "*/.git/*"
```

**Index File Location:** `~/.claude/DOCUMENTATION_INDEX.md`
