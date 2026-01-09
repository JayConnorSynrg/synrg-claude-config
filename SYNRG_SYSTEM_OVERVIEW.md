# SYNRG System Overview

**Last Updated:** 2025-11-21
**Purpose:** Clarify the relationship between SYNRG components

---

## Two-Tier Architecture

SYNRG operates on two levels that complement each other:

### Tier 1: Enterprise Orchestrator (`/synrg` command)

**What it is:**
- Comprehensive 149KB ruleset (4,524 lines)
- Full enterprise multi-agent coordination system
- Self-evolving with value-first analysis

**When to use:**
- Complex tasks requiring architectural analysis
- Multi-agent parallel execution needed
- Value-first pre-change analysis required
- Need director/orchestrator pattern
- Explicit orchestration requested

**How to invoke:**
```bash
/synrg [your objective or task description]
```

**Key capabilities:**
1. **STEP 2.75: VALUE-FIRST PRE-CHANGE ANALYSIS**
   - Architectural reconnaissance (5 parallel sub-agents)
   - Value quantification (stability, usage, business impact)
   - Change impact prediction
   - Protected structure detection
   - Intelligent decision framework
   - User escalation when needed

2. **Director/Orchestrator Pattern v4.0**
   - Spawns specialized sub-agents in parallel
   - Context-efficient distribution of tasks
   - Consolidated findings and validation
   - Adaptive gap filling

3. **Robustness-First Manifesto**
   - Zero tolerance for regressions
   - Quality-first decision framework
   - Auto-generated file detection
   - Protected structure preservation

4. **Interactive Context Gathering**
   - Uses AskUserQuestion tool
   - Gathers scope, constraints, preferences
   - Testing and validation requirements
   - Technical preferences

**Location:** `~/.claude/commands/synrg.md`

---

### Tier 2: Operational Protocol (`.claude/claude.md`)

**What it is:**
- Comprehensive operational protocol (330+ lines)
- Core execution principles
- Validation and testing standards
- Context management and consolidation rules

**When it applies:**
- Automatically when working in SYNRG projects
- Background protocol for all SYNRG work
- Provides consistent execution standards

**How it activates:**
- Automatically loaded in project context
- No explicit invocation needed

**Key capabilities:**
1. **Fundamental SYNRG Loop**
   ```javascript
   while (!solved && iteration < MAX) {
     test → detect regression → analyze → fix → validate → checkpoint
   }
   ```

2. **Mandatory Rules**
   - ALWAYS test with screenshots
   - ALWAYS check for regression
   - ALWAYS revert detrimental fixes
   - ALWAYS validate with evidence
   - NEVER skip validation
   - NEVER make multiple changes at once
   - NEVER proceed past failures

3. **Reality Check Validation**
   - User experience first
   - Three-layer verification (code → integration → user)
   - Comprehensive validation checklist

4. **Incremental Fix-Test-Loop**
   - ONE issue at a time
   - ONE change at a time
   - Immediate validation
   - Rollback on failure

5. **🆕 Context Management & Consolidation Protocol**
   - **80% threshold rule**: Trigger consolidation at 160k+ tokens
   - **Three-tier context priority**: Critical → Valuable → Reference
   - **Vital documentation**: session-state.md, architecture-decisions.md, critical-findings.md
   - **Director/orchestrator consolidation**: Merge sub-agent findings efficiently
   - **Value-first analysis**: Understand → Quantify → Enhance intelligently

6. **🆕 Context Efficiency Through Parallelization**
   - Director/orchestrator pattern for complex tasks
   - 60-70% context reduction per sub-agent
   - Consolidated comprehensive reports
   - Prevents context overflow

**Location:** `~/CODING/SYNRG AGENTS/agent-swarm-native/.claude/claude.md`

**Note:** This operational protocol DEFERS to `/synrg` command for orchestration decisions.

**Archive:** Agent Swarm V1 documentation archived at `~/CODING/SYNRG AGENTS/Deprecated-Agent-Swarm-V1/`

---

### Tier 3: Python Orchestrator Script

**What it is:**
- Interactive Python script
- Archon MCP integration
- Phase-based execution

**When to use:**
- Need interactive orchestration session
- Want Archon integration
- Prefer guided workflow

**How to invoke:**
```bash
cd "/Users/jelalconnor/CODING/SYNRG AGENTS/agent-swarm-native/BMAD-METHOD"
python3 synrg_orchestrator.py
```

**Key capabilities:**
- Interactive context gathering
- Docker-based Archon services
- Phase-based workflow
- Maximum parallelization (50-100+ agents)

**Location:** `~/CODING/SYNRG AGENTS/agent-swarm-native/BMAD-METHOD/synrg_orchestrator.py`

---

## How They Work Together

### Scenario 1: Complex Enterprise Task

```
User: "Refactor the authentication system"

1. Invoke: /synrg refactor authentication system
2. Enterprise Orchestrator activates:
   - Runs VALUE-FIRST analysis
   - Spawns 5 parallel reconnaissance agents
   - Quantifies existing value
   - Predicts change impact
   - Makes intelligent recommendation
   - Gets user approval
3. During execution, Operational Protocol ensures:
   - Every change tested with screenshots
   - No regressions allowed
   - Evidence-based validation
   - Incremental progression
```

### Scenario 2: Working in SYNRG Project

```
User: "Fix this bug in the validation logic"

1. Operational Protocol (.claude/claude.md) applies automatically:
   - Test with screenshots
   - Detect regression
   - Apply fix with safeguards
   - Validate no harm
   - Checkpoint on success
2. No need to invoke /synrg explicitly
3. Basic protocol handles straightforward fixes
```

### Scenario 3: Interactive Orchestration

```
User wants guided workflow with Archon integration

1. Run Python orchestrator:
   cd "/Users/jelalconnor/CODING/SYNRG AGENTS/agent-swarm-native/BMAD-METHOD"
   python3 synrg_orchestrator.py

2. Interactive prompts guide through:
   - Context gathering
   - Archon service startup
   - Phase-based execution
   - Maximum parallelization
```

---

## Decision Tree: Which to Use?

**Use `/synrg` command when:**
- ✅ Complex architectural changes needed
- ✅ Multiple systems affected
- ✅ Need value-first analysis before proceeding
- ✅ Want parallel multi-agent orchestration
- ✅ Require comprehensive impact assessment
- ✅ Need user decision on approach

**Operational Protocol applies when:**
- ✅ Working in SYNRG projects (automatic)
- ✅ Making incremental fixes
- ✅ Need regression protection
- ✅ Want evidence-based validation
- ✅ Following fix-test-loop pattern
- ✅ Context approaching 80% threshold (consolidation needed)
- ✅ Need to preserve critical context across sessions

**Use Python orchestrator when:**
- ✅ Want interactive guided workflow
- ✅ Need Archon MCP integration
- ✅ Prefer terminal-based orchestration
- ✅ Want maximum parallelization setup

---

## Related Commands

| Command | Purpose | Size |
|---------|---------|------|
| **/synrg** | Full enterprise orchestrator with VALUE-FIRST analysis | 149KB |
| **/synrg-refactor** | File restructuring agent with parallel sub-agents | 82KB |
| **/synrg-swarm** | Sub-agent development and task decomposition | 55KB |
| **/synrg-commit** | Git workflow automation with validation | 39KB |
| **/synrg-buildworkflow** | **n8n workflow builder** (10 specialist agents, 95%+ success) | 19KB |
| **/synrg-evolve** | Self-evolution patterns and integration | 10.7KB |

---

## Documentation Locations

- **Enterprise Orchestrator:** `~/.claude/commands/synrg.md`
- **Operational Protocol:** `SYNRG AGENTS/agent-swarm-native/.claude/claude.md`
- **Python Script:** `SYNRG AGENTS/agent-swarm-native/BMAD-METHOD/synrg_orchestrator.py`
- **Implementation Guides:** `SYNRG AGENTS/agent-swarm-native/` (13 docs)
- **Complete Index:** `~/.claude/DOCUMENTATION_INDEX.md`

---

## Summary

**SYNRG is a three-tier system:**
1. **Enterprise Orchestrator** (`/synrg`) - Comprehensive multi-agent coordination with value-first analysis
2. **Operational Protocol** (`.claude/claude.md`) - Core execution principles and validation standards
3. **Python Script** (`synrg_orchestrator.py`) - Interactive guided orchestration

Each tier serves a specific purpose and they work together to provide robust, intelligent, and validated multi-agent orchestration at any scale.
