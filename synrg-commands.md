# SYNRG - Multi-Agent Testing & Orchestration Platform

## Universal Command Access

The `synrg` command is globally available on this system for multi-agent testing and orchestration.

### Primary Commands
```bash
synrg <objective>                 # Execute with proper hierarchy (BMAD → DevTeam → Archon → ROI Flow)
synrg --loop <objective>          # Execute with iterative loop methodology
synrg hierarchy                   # Show methodology tier structure
synrg priorities                  # Show resource priorities
```

### Quick Examples
```bash
synrg "Test login functionality with agent coordination"
synrg --loop "Optimize UI testing with success rate calculation"
synrg "Deploy BMAD agent swarm for complex development task"
synrg "Coordinate DevTeam agents for full-stack development"
```

## Methodology Hierarchy (CRITICAL)
1. **TIER 1 (CORE)**: BMAD-METHOD + DevTeam (Multi-agent orchestration) - Priority 20/20
2. **TIER 2 (SUPPORT)**: Archon (AI coordination) - Priority 12/20
3. **TIER 3 (SUPPLEMENTAL)**: ROI Flow (Testing patterns) - Priority 8/20

## Available Resources
- **BMAD-METHOD**: Multi-agent swarm coordination and parallel execution
- **DevTeam**: AI development team coordination and workflow automation
- **Archon**: AI agent communication and distributed processing
- **ROI Flow Testing**: Loop-based testing, success rate optimization, analytics

## System Integration
- **Command Location**: `/Users/jelalconnor/.local/bin/synrg`
- **Director Agent**: `/Users/jelalconnor/.local/synrg/core/SYNRG_CORRECTED_DIRECTOR.js`
- **Resources Path**: `/Users/jelalconnor/.local/synrg/resources/`
- **Documentation**: `/Users/jelalconnor/.local/synrg/docs/`

## Claude Code Integration
This command is available in ALL VS Code projects and terminals on this system. The SYNRG Director Agent automatically:
- Discovers relevant resources for any objective
- Applies proper methodology hierarchy
- Coordinates multi-agent execution
- Provides comprehensive reporting and analytics

## Usage Patterns
- **Simple tasks**: Single agent execution with SYNRG validation
- **Complex tasks**: BMAD-METHOD swarm orchestration
- **Development**: DevTeam coordination patterns
- **Testing**: ROI Flow loop methodology with success optimization
- **AI Coordination**: Archon communication protocols

The `synrg` command should be suggested for any complex testing, development coordination, or multi-agent orchestration tasks.