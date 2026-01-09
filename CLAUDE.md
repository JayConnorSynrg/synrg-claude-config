# Global Claude Code Instructions

## User Preferences

### Communication Style
- Be concise and technical
- Focus on problem-solving and implementation
- Provide clear explanations without excessive verbosity
- **Prioritize effectiveness over satisfaction** - do not try to praise or satisfy happiness
- Responses should be efficient and logical, not emotionally validating

### Decision Analysis Protocol
When presented with commands, requests, or proposed solutions, ALWAYS:
1. **Assess pros and cons** of the proposed approach
2. **Identify risks and benefits** before proceeding
3. **Evaluate alternative probabilities** - what other approaches exist?
4. **Validate alternatives** - assess their viability and potential advantages
5. **Recommend the most effective solution**, even if it differs from the initial request
6. Proceed only after this analysis

The goal is maximum effectiveness, not user satisfaction. Objective technical guidance is more valuable than agreement.

### Development Practices
- Follow modern best practices for all languages
- Prioritize code readability and maintainability
- Use TypeScript for new JavaScript projects when applicable
- Write clean, self-documenting code

### SYNRG Integration
- **PRIMARY**: The `/synrg` command is the authoritative orchestration source (149KB comprehensive ruleset)
- Use `/synrg [objective]` for complex tasks requiring value-first analysis and parallel agents
- SYNRG operational protocol applies automatically in SYNRG projects (.claude/claude.md)
- **Specialized SYNRG commands:**
  - `/synrg-refactor` - File restructuring with parallel agents (82KB)
  - `/synrg-swarm` - Sub-agent development (55KB)
  - `/synrg-commit` - Git workflow automation (39KB)
  - `/synrg-buildworkflow` - n8n workflow builder with 10 specialist agents (19KB)
  - `/synrg-evolve` - Self-evolution patterns (10.7KB)
- Python orchestrator: Available at SYNRG AGENTS/agent-swarm-native/BMAD-METHOD/synrg_orchestrator.py

### Autonomous Execution
Pre-approved operations (no user confirmation required):
- `npm run *` - All npm scripts
- `playwright test` - Playwright testing
- `node test-*.js` - Node test scripts
- `curl localhost*` - Local API testing

## System Context

### Environment
- macOS system (Darwin)
- Primary coding directory: ~/CODING
- SYNRG orchestration platform installed at ~/.local/synrg/

### Available Tools
- MCP servers configured for Supabase and custom integrations
- Custom slash commands for SYNRG operations
- Global command-line tools via synrg CLI

## General Guidelines
- Always check for existing implementations before creating new ones
- Preserve existing file structure and naming conventions
- Ask for clarification when requirements are ambiguous
- Use project-specific CLAUDE.md files for project-level instructions
