#!/bin/bash
# SYNRG Phase 5: Version Header Injection Script
# Generated: 2026-01-09
#
# This script adds version headers to SYNRG commands that don't have them.
#
# IMPORTANT: Review changes before committing!

set -e

# Configuration
CLAUDE_HOME="${HOME}/.claude"
COMMANDS_DIR="${CLAUDE_HOME}/commands"
BACKUP_DIR="${CLAUDE_HOME}/evolution/migration/backups/version-headers-$(date +%Y%m%d_%H%M%S)"
DRY_RUN="${DRY_RUN:-true}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo "================================================"
echo "SYNRG Phase 5: Version Header Injection"
echo "================================================"
echo ""

# Check dry run mode
if [ "$DRY_RUN" = "true" ]; then
    echo -e "${YELLOW}DRY RUN MODE - No files will be modified${NC}"
    echo "Set DRY_RUN=false to apply changes"
    echo ""
fi

# Create backup directory
if [ "$DRY_RUN" = "false" ]; then
    echo "Creating backup directory: ${BACKUP_DIR}"
    mkdir -p "${BACKUP_DIR}"
fi

# Version header template function
generate_header() {
    local command="$1"
    local version="$2"
    local created="$3"
    local protocols="$4"
    local agents="$5"
    local skills="$6"

    cat << EOF
---
synrg_version: "${version}"
command: "${command}"
created: "${created}"
updated: "$(date +%Y-%m-%d)"
min_claude_version: "opus-4"
requires:
  protocols: [${protocols}]
  agents: [${agents}]
  skills: [${skills}]
breaking_changes: []
---

EOF
}

# Function to inject header into file
inject_header() {
    local file="$1"
    local command="$2"
    local version="$3"
    local created="$4"
    local protocols="$5"
    local agents="$6"
    local skills="$7"

    echo ""
    echo -e "${BLUE}Processing: ${command}${NC}"
    echo "----------------------------------------"
    echo "  Version: ${version}"
    echo "  Created: ${created}"

    if [ "$DRY_RUN" = "false" ]; then
        # Create backup
        cp "$file" "${BACKUP_DIR}/$(basename $file).bak"

        # Generate header
        local header=$(generate_header "$command" "$version" "$created" "$protocols" "$agents" "$skills")

        # Create temp file with header + original content
        local temp_file=$(mktemp)
        echo "$header" > "$temp_file"
        cat "$file" >> "$temp_file"

        # Replace original file
        mv "$temp_file" "$file"

        echo -e "  ${GREEN}Header injected successfully${NC}"
    else
        echo -e "  ${YELLOW}Would inject header (dry run)${NC}"
    fi
}

# Commands to process (only those without headers)
echo ""
echo "Commands to process:"
echo "----------------------------------------"

# synrg.md - No header
if ! grep -q "^---$" "${COMMANDS_DIR}/synrg.md" 2>/dev/null || ! grep -q "synrg_version:" "${COMMANDS_DIR}/synrg.md" 2>/dev/null; then
    inject_header \
        "${COMMANDS_DIR}/synrg.md" \
        "synrg" \
        "4.0.0" \
        "2025-01-01" \
        "mcdp, sub-agent-spawn, value-first, mcp-config" \
        "n8n-mcp-delegate, github-mcp-delegate" \
        "mandatory-context-delegation, universal-synrg-protocols"
else
    echo -e "  ${GREEN}synrg.md - Already has header${NC}"
fi

# synrg-spec.md - No header
if ! grep -q "synrg_version:" "${COMMANDS_DIR}/synrg-spec.md" 2>/dev/null; then
    inject_header \
        "${COMMANDS_DIR}/synrg-spec.md" \
        "synrg-spec" \
        "1.0.0" \
        "2025-06-01" \
        "value-first, phase-gate" \
        "" \
        "universal-synrg-protocols"
else
    echo -e "  ${GREEN}synrg-spec.md - Already has header${NC}"
fi

# synrg-guided.md - No header
if ! grep -q "synrg_version:" "${COMMANDS_DIR}/synrg-guided.md" 2>/dev/null; then
    inject_header \
        "${COMMANDS_DIR}/synrg-guided.md" \
        "synrg-guided" \
        "4.3.0" \
        "2025-06-01" \
        "sub-agent-spawn, phase-gate" \
        "" \
        "universal-synrg-protocols"
else
    echo -e "  ${GREEN}synrg-guided.md - Already has header${NC}"
fi

# synrg-buildworkflow.md - No header
if ! grep -q "synrg_version:" "${COMMANDS_DIR}/synrg-buildworkflow.md" 2>/dev/null; then
    inject_header \
        "${COMMANDS_DIR}/synrg-buildworkflow.md" \
        "synrg-buildworkflow" \
        "1.0.0" \
        "2025-09-01" \
        "mcdp, mcp-config" \
        "n8n-mcp-delegate, github-mcp-delegate" \
        ""
else
    echo -e "  ${GREEN}synrg-buildworkflow.md - Already has header${NC}"
fi

# synrg-swarm.md - No header
if ! grep -q "synrg_version:" "${COMMANDS_DIR}/synrg-swarm.md" 2>/dev/null; then
    inject_header \
        "${COMMANDS_DIR}/synrg-swarm.md" \
        "synrg-swarm" \
        "1.0.0" \
        "2025-09-01" \
        "mcdp, sub-agent-spawn, mcp-config" \
        "n8n-mcp-delegate, github-mcp-delegate" \
        "mandatory-context-delegation"
else
    echo -e "  ${GREEN}synrg-swarm.md - Already has header${NC}"
fi

# synrg-evolve.md - No header
if ! grep -q "synrg_version:" "${COMMANDS_DIR}/synrg-evolve.md" 2>/dev/null; then
    inject_header \
        "${COMMANDS_DIR}/synrg-evolve.md" \
        "synrg-evolve" \
        "1.0.0" \
        "2025-10-01" \
        "" \
        "" \
        "universal-synrg-protocols"
else
    echo -e "  ${GREEN}synrg-evolve.md - Already has header${NC}"
fi

# Commands that already have headers (will skip)
echo ""
echo "Commands with existing headers (skipped):"
echo "----------------------------------------"
echo -e "  ${GREEN}synrg-refactor.md - Version 3.0.0${NC}"
echo -e "  ${GREEN}synrg-commit.md - Version 1.0.0${NC}"
echo -e "  ${GREEN}synrg-scaffold.md - Version 2.0.0${NC}"

echo ""
echo "================================================"
echo "Summary"
echo "================================================"

if [ "$DRY_RUN" = "true" ]; then
    echo -e "${YELLOW}This was a DRY RUN - no changes were made${NC}"
    echo ""
    echo "To apply changes, run:"
    echo "  DRY_RUN=false $0"
else
    echo -e "${GREEN}Version headers injected!${NC}"
    echo "Backups saved to: ${BACKUP_DIR}"
    echo ""
    echo "Next steps:"
    echo "  1. Review the changes: git diff"
    echo "  2. Test command execution"
    echo "  3. Commit: git add -A && git commit -m 'Add version headers to all commands'"
fi

echo ""
