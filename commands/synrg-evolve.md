---
description: Activate SYNRG self-evolution to integrate patterns and improvements
argument-hint: [integrate|analyze|optimize]
---

# SYNRG Evolution Command
## Force Self-Evolution or Integrate Staged Improvements

You are executing the SYNRG Evolution Protocol - a meta-command that analyzes execution history, identifies patterns, and integrates improvements into the main SYNRG command.

---

## 📅 DOCUMENTATION FRESHNESS PROTOCOL (v1.0)

**MANDATORY for all web searches, API references, and documentation lookups:**

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ⏰ DOCUMENTATION FRESHNESS GATE                                        │
│                                                                         │
│  1. DETERMINE current date from system/context                          │
│  2. SEARCH with current year appended to all queries                    │
│  3. REJECT documentation older than 1 year                              │
│  4. VERIFY 6+ month old docs are still current                          │
│                                                                         │
│  ALWAYS seek the LATEST version - never settle for outdated docs        │
└─────────────────────────────────────────────────────────────────────────┘
```

**Sub-Agent Injection**:
```
📅 DOCUMENTATION FRESHNESS: Determine current date first.
Always search for LATEST docs by appending current year to queries.
Reject docs older than 1 year.
```

---

## 🚨 HARD GATE: MCP Delegation Enforcement (v2.0) - MANDATORY

**ZERO TOLERANCE: ALL MCP tool calls MUST be delegated to MCP-specific agents.**

```
┌─────────────────────────────────────────────────────────────────────────┐
│  🚫 ABSOLUTE RULE: NEVER CALL MCP TOOLS DIRECTLY                        │
│                                                                         │
│  ⛔ DIRECT MCP CALLS ARE FORBIDDEN                                      │
│  ⛔ NO EXCEPTIONS - ALL MCP CALLS GO THROUGH DELEGATE AGENTS            │
│                                                                         │
│  MANDATORY ACTION:                                                      │
│  → n8n MCP tools → Task({ subagent_type: "n8n-mcp-delegate", ... })     │
│  → GitHub MCP tools → Task({ subagent_type: "github-mcp-delegate", ... })│
└─────────────────────────────────────────────────────────────────────────┘
```

**MCP Delegate Agent Registry:**

| MCP Domain | Delegate Agent | Agent File |
|------------|----------------|------------|
| `mcp__n8n-mcp__*` | `n8n-mcp-delegate` | `~/.claude/agents/n8n-mcp-delegate.md` |
| `mcp__n8n-workflows__*` | `github-mcp-delegate` | `~/.claude/agents/github-mcp-delegate.md` |

**Evolution-Specific Delegation:**
```javascript
// When analyzing patterns that involve MCP:
Task({ subagent_type: "n8n-mcp-delegate", prompt: "Analyze workflow for pattern extraction", model: "haiku" })
```

**Enforcement**: Direct MCP calls are FORBIDDEN. Violation requires immediate self-correction.

---

## 🔴 HARD GATE: MANDATORY CONTEXT DELEGATION PROTOCOL (MCDP v1.0)

**ABSOLUTE MANDATE: ALL context operations MUST be delegated to sub-agents.**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  MANDATORY CONTEXT DELEGATION - ZERO EXCEPTIONS                             │
│                                                                             │
│  1. LARGE DOCUMENT READS (>500 tokens expected)                             │
│     → Delegate to: Explore or general-purpose agent                         │
│     → Return: Summary + key findings + references                           │
│                                                                             │
│  2. ALL MCP TOOL CALLS → Covered by MCP Delegation Enforcement              │
│                                                                             │
│  3. ALL CONTEXT GATHERING OPERATIONS                                        │
│     → Delegate to: Explore, general-purpose, or specialized agents          │
│     → Return: Actionable summary, not raw content                           │
│                                                                             │
│  EVOLVE-SPECIFIC: Pattern analysis and SYNRG file reads MUST be delegated   │
│                                                                             │
│  VIOLATION = IMMEDIATE SELF-CORRECTION REQUIRED                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Self-Enforcement Check** (Before EVERY operation):
```
□ MCP call?        → MUST delegate to MCP agent
□ Large file?      → MUST delegate to Explore/general-purpose
□ Context gather?  → MUST delegate to appropriate agent
□ >500 tokens?     → MUST delegate

ANY = YES → DELEGATE. No exceptions.
```

**Full Protocol**: See `~/.claude/skills/mandatory-context-delegation.md`

---

## 🔒 UNIVERSAL SYNRG PROTOCOLS (USP v1.0 - Compact)

**All gates apply. Full specs: `~/.claude/skills/universal-synrg-protocols.md`**

### PRE-IMPLEMENTATION GATES
```
GATE 1: ANTI-MEMORY    - READ current SYNRG state before evolving
GATE 2: GIT_STRATEGY   - Evolution = ALWAYS feature branch + careful review
GATE 3: CERTAINTY      - High certainty on improvements, test before merge
GATE 4: SECURITY       - No security regressions in evolved patterns
GATE 5: USER_VERIFY    - Present evolution plan before applying
```

### POST-IMPLEMENTATION REVIEWS
```
REVIEW 1: OBJECTIVE    - Evolution improves SYNRG system?
REVIEW 2: SECURITY     - No security vulnerabilities introduced
REVIEW 3: DOCS (P5)    - Changelog and version history updated
REVIEW 4: COMMIT       - Use /synrg-commit for evolution changes
REVIEW 5: QUALITY      - All gates passed → COMPLETE
```

---

## 🔴 MANDATORY: Sub-Agent Delegation Protocol (v4.3)

**Evolution tasks should leverage specialized agents when available:**

```
┌─────────────────────────────────────────────────────────────┐
│  AGENT LIBRARY EVOLUTION CHECK                              │
│                                                             │
│  When evolving patterns, also check:                        │
│  1. Should a NEW agent be created for this pattern?         │
│  2. Should existing agents be updated with new patterns?    │
│  3. Are there gaps in agent coverage for detected failures? │
└─────────────────────────────────────────────────────────────┘
```

### Agent Evolution Responsibilities

When patterns are identified:
1. **Pattern → Agent Mapping**: Does this pattern warrant a dedicated agent?
2. **Agent Updates**: Update relevant agent prompts with new patterns
3. **Coverage Analysis**: Identify task types without agent coverage
4. **Auto-Creation**: Create new agents for recurring task types

### Real Delegation for Analysis

```javascript
// Use Task tool for pattern analysis
Task({
  subagent_type: "general-purpose",
  prompt: `Analyze patterns in agents-evolution.md for agent coverage gaps.
  Agent library: ~/.claude/agents/
  Pattern library: /Users/jelalconnor/CODING/N8N/Workflows/.claude/patterns/`,
  model: "haiku"
})
```

---

## 🧠 CLAUDE TOOL SELECTION PROTOCOL (Reference: /synrg)

**When evolving the ecosystem, ensure new patterns create the right tool types:**

| Tool Type | When to Create | Evolution Action |
|-----------|----------------|------------------|
| **SUB-AGENTS** | New domain expertise, recurring focused tasks | Create in ~/.claude/agents/ |
| **SLASH COMMANDS** | New orchestration patterns, multi-phase workflows | Create in ~/.claude/commands/ |
| **HOOKS** | New validation/enforcement rules | Create in project .claude/hooks/ |
| **SKILLS** | New reusable methodologies | Create in project .claude/skills/ |

**Evolution-Specific Responsibilities:**
1. **Pattern → Tool Mapping**: When new pattern emerges, CREATE appropriate tool type
2. **Cross-Command Updates**: NEW tools must be PROPAGATED to all /synrg-* commands
3. **Ecosystem Consistency**: Ensure same patterns use same tool types across system

**Full Protocol**: See `/synrg` command for complete Tool Type Decision Matrix.

---

## Execution Mode Detection

**Automatically determine the mode based on context:**

```javascript
function determineEvolutionMode() {
  // Check for staged improvements
  const stagedImprovements = checkForStagedImprovements();
  const recentErrors = analyzeRecentExecutions();
  const evolutionLog = readEvolutionLog();

  if (stagedImprovements.length > 0) {
    return {
      mode: 'integrate_staged',
      improvements: stagedImprovements,
      action: 'Integrate documented improvements into SYNRG command'
    };
  } else if (recentErrors.patterns.length > 0) {
    return {
      mode: 'analyze_and_evolve',
      patterns: recentErrors.patterns,
      action: 'Analyze recent errors and create new patterns'
    };
  } else {
    return {
      mode: 'review_and_optimize',
      action: 'Review SYNRG command for optimization opportunities'
    };
  }
}
```

---

## Mode 1: Integrate Staged Improvements

**When**: Staged improvements exist (documented patterns ready to integrate)

**Process**:
1. **Read Current SYNRG Command**
   ```bash
   cat ~/.claude/commands/synrg.md
   ```

2. **Review Staged Improvements**
   - Check `.claude/commands/synrg-evolved.md` if it exists
   - Check evolution log: `.claude/commands/synrg.evolution.log`
   - Check recent execution reports
   - Identify ready-to-integrate patterns

3. **Integration Decision Matrix**
   ```javascript
   for (const improvement of stagedImprovements) {
     if (improvement.validated && improvement.generalizes) {
       // High confidence - integrate directly
       await integrateImprovement(improvement);
     } else if (improvement.experimental) {
       // Add as optional protocol, mark as beta
       await addExperimentalSection(improvement);
     } else {
       // Document in evolution log only
       await documentInEvolutionLog(improvement);
     }
   }
   ```

4. **Smart Integration**
   - Find the appropriate section (e.g., "Sub-Agent Execution Protocol")
   - Add new guidance with clear markers:
     - **🆕** for new additions
     - **(NEW)** inline annotations
     - **Added: [DATE]** - Context and reasoning
   - Preserve existing content (additions only, never deletions)
   - Update version number
   - Document in evolution log

5. **Validation**
   - Ensure command syntax is valid
   - Verify no contradictions with existing guidance
   - Check command coherence and readability
   - Create backup: `synrg.v[YYYYMMDD].md`

---

## 🔴 Mode 1.5: Anti-Memory Pattern Detection (v4.1)

**When**: ANY evolution run - this check is MANDATORY before other modes

**Purpose**: Detect and classify memory-related failures for special handling

### Anti-Memory Pattern Recognition

```javascript
async function detectAntiMemoryPatterns(recentErrors) {
  const antiMemoryIndicators = {
    // Pattern: Same configuration worked before, fails now
    crossContextFailure: {
      indicator: (error) =>
        error.previouslySuccessful === true &&
        error.currentContext !== error.previousContext,
      severity: 'CRITICAL',
      action: 'Add to Known Failure Points Registry'
    },

    // Pattern: Configuration syntax contamination
    syntaxContamination: {
      indicator: (error) =>
        error.type === 'syntax' &&
        error.details.includes('expression') ||
        error.details.includes('prefix'),
      severity: 'HIGH',
      action: 'Document reference template, enforce COPY not reconstruct'
    },

    // Pattern: Parameter format mismatch
    formatMismatch: {
      indicator: (error) =>
        error.type === 'validation' &&
        error.expected !== error.actual &&
        similarStructure(error.expected, error.actual),
      severity: 'HIGH',
      action: 'Add format reference to documentation'
    },

    // Pattern: "I know this" confidence failure
    falseConfidenceLoop: {
      indicator: (error) =>
        error.frequency >= 2 &&
        error.configurationSource === 'memory' &&
        error.documentationAvailable === true,
      severity: 'CRITICAL',
      action: 'MANDATORY Anti-Memory Protocol enforcement'
    }
  };

  const detectedPatterns = [];

  for (const error of recentErrors) {
    for (const [patternName, config] of Object.entries(antiMemoryIndicators)) {
      if (config.indicator(error)) {
        detectedPatterns.push({
          name: patternName,
          error: error,
          severity: config.severity,
          action: config.action,
          isAntiMemoryPattern: true
        });
      }
    }
  }

  return detectedPatterns;
}
```

### Anti-Memory Pattern Evolution

When Anti-Memory patterns are detected:

1. **Immediate Actions**:
   - Add to Known Failure Points Registry in `/synrg` command
   - Create reference template in documentation
   - Update all affected SYNRG commands with pattern awareness

2. **Evolution Proposal Format (Anti-Memory)**:
   ```markdown
   ## 🔴 Anti-Memory Pattern: [Name]

   **Classification**: Memory-Related Failure
   **Root Cause**: FALSE CONFIDENCE LOOP / CROSS-CONTEXT DECAY / SYNTAX CONTAMINATION

   **Pattern Details**:
   - First occurrence: [Date/Context]
   - Repeat occurrences: [Count]
   - Common trigger: [Specific configuration/syntax]

   **Reference Template** (COPY EXACTLY):
   \`\`\`json
   [Exact correct configuration]
   \`\`\`

   **Anti-Pattern** (DO NOT USE):
   \`\`\`json
   [Common incorrect variation]
   \`\`\`

   **Integration Requirements**:
   - [ ] Add to Known Failure Points Registry
   - [ ] Update affected slash commands
   - [ ] Add validation hook for pattern detection
   - [ ] Document in agents-evolution.md
   ```

3. **Propagation**: Anti-Memory patterns MUST be propagated to:
   - `/synrg` (Director/Orchestrator)
   - `/synrg-swarm` (Agent Development)
   - `/synrg-refactor` (File Operations)
   - `/synrg-guided` (Execution Checkpoints)
   - All domain-specific SYNRG commands

---

## Mode 2: Analyze and Evolve

**When**: Recent errors exist but no staged improvements

**Process**:
1. **Analyze Recent Executions**
   - Review last 5 SYNRG execution reports
   - Extract error patterns
   - Calculate pattern frequency and severity
   - Identify root causes
   - **🆕 Run Anti-Memory Pattern Detection (Mode 1.5)** first

2. **Pattern Recognition**
   ```javascript
   const patterns = identifyPatterns(recentErrors);

   for (const pattern of patterns) {
     // Perform 5-Why Analysis
     const rootCause = perform5WhyAnalysis(pattern);

     // Check if pattern is systematic
     if (pattern.frequency > 2 || pattern.severity === 'high') {
       // Qualify for integration
       await createEvolutionProposal(pattern, rootCause);
     } else {
       // Document as learning
       await documentLearning(pattern, rootCause);
     }
   }
   ```

3. **Create Evolution Proposals**
   For each qualified pattern:
   ```markdown
   ## Pattern Proposal: [Name]

   **Trigger**: [What conditions cause this error]
   **Root Cause**: [5-Why analysis result]
   **Frequency**: [Count across recent executions]
   **Severity**: [High/Medium/Low]
   **Impact**: [Files/agents affected]

   **Proposed Solution**:
   [Detailed guidance to prevent future occurrences]

   **Implementation Location**:
   - [ ] Sub-Agent Execution Protocol
   - [ ] Validation Requirements
   - [ ] Planning Strategy
   - [ ] Error Recovery
   - [ ] New Section: [Name]

   **Example**:
   [Concrete example showing how to apply the guidance]

   **Validation**:
   - [ ] Generalizes beyond specific case
   - [ ] Clear and actionable
   - [ ] No conflicts with existing guidance
   - [ ] Measurable improvement expected
   ```

4. **Present to User**
   - Show pattern analysis summary
   - Display evolution proposals
   - Ask for approval before integrating
   - Option to stage for later or integrate immediately

5. **Update Evolution Log**
   ```
   [2025-10-17 14:30] EVOLUTION: Analyzed 5 recent executions
   [2025-10-17 14:31] PATTERN-004: API timeout handling (3 occurrences, severity: high)
   [2025-10-17 14:32] INTEGRATED: Added retry logic to Sub-Agent Execution Protocol
   [2025-10-17 14:33] VERSION: Updated to v2.2.0
   ```

---

## Mode 3: Review and Optimize

**When**: No staged improvements or recent errors

**Process**:
1. **Command Health Check**
   - Measure command length (optimal: 5-15K words)
   - Check for redundancy
   - Identify outdated guidance
   - Find opportunities for consolidation

2. **Optimization Opportunities**
   ```javascript
   const optimizations = {
     redundancy: findRedundantSections(),
     outdated: findOutdatedGuidance(),
     missing: findGaps(),
     clarity: assessClarity(),
   };
   ```

3. **Refactoring Proposals**
   - Consolidate similar sections
   - Update examples with recent patterns
   - Add cross-references between related sections
   - Improve clarity and actionability

4. **Present Refactoring Plan**
   - Show optimization opportunities
   - Estimate impact (readability, effectiveness)
   - Get user approval
   - Apply approved changes

---

## Integration Best Practices

### Adding New Protocols

**Template**:
```markdown
## 🆕 [Protocol Name]

**Context**: Learned from [specific execution/issue] ([date])
**Issue**: [What was going wrong]
**Solution**: [New requirement/guidance to prevent future occurrence]

### [Sub-section if needed]

[Detailed guidance]

**Example**:
[Concrete example showing how to apply this guidance]

**Added**: [YYYY-MM-DD] - Based on [X occurrences] of [error pattern]
```

### Updating Existing Sections

**Approach**:
1. Add new bullet points with **🆕** marker
2. Add inline **(NEW)** annotations to modified rules
3. Never remove existing guidance (append only)
4. Add date stamp to new additions

**Example**:
```markdown
When executing sub-agent tasks, **ALWAYS**:
- ✅ Make ONE change at a time
- ✅ Test immediately after each change
- ✅ **🆕 Check if file is auto-generated** before editing (NEW)
```

### Version Management

**Version Numbering**:
- Major (X.0.0): Complete command restructure
- Minor (2.X.0): New protocols/sections added
- Patch (2.1.X): Small improvements/clarifications

**Backup Protocol**:
```bash
# Before any integration
cp ~/.claude/commands/synrg.md \
   ~/.claude/commands/synrg.v$(date +%Y%m%d_%H%M%S).md

# Keep last 10 versions
ls -t ~/.claude/commands/synrg.v*.md | tail -n +11 | xargs rm -f
```

---

## Evolution Metrics Dashboard

After each evolution, present:

```markdown
## SYNRG Evolution Metrics

**Command Version**: 2.1.0 → 2.2.0
**Evolution Date**: 2025-10-17
**Mode**: [integrate_staged | analyze_and_evolve | review_and_optimize]

### Changes Summary
- **Protocols Added**: 3 (Auto-Gen Files, Export Verification, Pragmatic Workarounds)
- **Rules Enhanced**: 7
- **Patterns Documented**: 3
- **Examples Added**: 5

### Pattern Library
- **Total Patterns**: 6 (+3 this version)
- **Auto-Detected**: 3
- **Auto-Resolved**: 2

### Effectiveness Metrics
- **Execution Success Rate**: 75% → 95% (+20%)
- **Error Reduction**: 33 errors → 15 errors (-55%)
- **Pattern Recognition Rate**: 80%
- **Time to Resolution**: -30% average

### Known Patterns
1. ✅ Pattern-001-AutoGeneratedFiles (1 occurrence, 100% resolution)
2. ✅ Pattern-002-ExportMismatch (11 occurrences, 100% resolution)
3. ✅ Pattern-003-MissingImplementation (3 occurrences, 100% resolution)
4. 🆕 Pattern-004-[New Pattern]

### Next Evolution Targets
1. Database migration handling
2. Dependency version conflicts
3. API contract mismatches
```

---

## Self-Evolution Validation

Before finalizing any evolution:

**Validation Checklist**:
- [ ] Does the new guidance address the root cause?
- [ ] Is it generalizable beyond the specific instance?
- [ ] Is it clear and actionable?
- [ ] Does it conflict with existing guidance? (❌ Must resolve)
- [ ] Can it be measured for effectiveness?
- [ ] Is it positioned in the right section?
- [ ] Are examples concrete and helpful?
- [ ] Is the version number updated?
- [ ] Is the evolution log updated?
- [ ] Is a backup created?

**Conflict Resolution**:
```javascript
if (hasConflict(newGuidance, existingGuidance)) {
  // Option 1: Merge - new guidance is refinement of old
  if (isRefinement(newGuidance, existingGuidance)) {
    await mergeGuidance(newGuidance, existingGuidance);
  }
  // Option 2: Supersede - new guidance replaces old (rare)
  else if (isSuperior(newGuidance, existingGuidance)) {
    await deprecateOld(existingGuidance);
    await addNew(newGuidance);
  }
  // Option 3: Coexist - both valid in different contexts
  else {
    await clarifyContexts(newGuidance, existingGuidance);
  }
}
```

---

## Output Format

**Always provide**:
1. **Evolution Summary**: What changed and why
2. **Pattern Analysis**: New patterns identified
3. **Integration Report**: What was added/modified
4. **Metrics**: Before/after effectiveness measures
5. **Version Update**: New version number
6. **Backup Location**: Where old version is saved
7. **Evolution Log**: Updated log entries
8. **Next Steps**: Recommended focus areas for next evolution

---

## Usage Examples

**Automatic Mode Detection**:
```bash
/synrg-evolve
# Automatically detects whether to integrate staged improvements,
# analyze recent errors, or optimize the command
```

**Force Specific Mode**:
```bash
/synrg-evolve integrate
# Force integration of staged improvements

/synrg-evolve analyze
# Force analysis of recent executions

/synrg-evolve optimize
# Force optimization review
```

**With Context**:
```bash
/synrg-evolve analyze --since="2025-10-15"
# Analyze executions since specific date

/synrg-evolve integrate --pattern="Pattern-004"
# Integrate specific pattern only
```

---

**Version**: 1.0.0
**Created**: 2025-10-17
**Purpose**: Meta-command for SYNRG self-evolution
**Compatibility**: Works with SYNRG v2.0.0+