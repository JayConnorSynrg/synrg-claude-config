#!/bin/bash
# SYNRG Phase 3: Path Variables Migration Script
# Generated: 2026-01-09
#
# This script replaces hardcoded paths with ${VARIABLE} syntax
# for improved portability across environments.
#
# IMPORTANT: Review changes before committing!

set -e

# Configuration
CLAUDE_HOME="${HOME}/.claude"
COMMANDS_DIR="${CLAUDE_HOME}/commands"
BACKUP_DIR="${CLAUDE_HOME}/evolution/migration/backups/$(date +%Y%m%d_%H%M%S)"
DRY_RUN="${DRY_RUN:-true}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "================================================"
echo "SYNRG Phase 3: Path Variables Migration"
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

# Function to apply substitutions to a file
migrate_file() {
    local file="$1"
    local filename=$(basename "$file")

    echo ""
    echo "Processing: ${filename}"
    echo "----------------------------------------"

    if [ "$DRY_RUN" = "false" ]; then
        # Create backup
        cp "$file" "${BACKUP_DIR}/${filename}.bak"
    fi

    # Count substitutions
    local count=0

    # Substitution 1: Absolute user paths → ${HOME}
    local matches=$(grep -c "/Users/jelalconnor" "$file" 2>/dev/null || echo "0")
    if [ "$matches" -gt 0 ]; then
        echo "  Found $matches absolute user paths (/Users/jelalconnor)"
        count=$((count + matches))
        if [ "$DRY_RUN" = "false" ]; then
            sed -i '' 's|/Users/jelalconnor|${HOME}|g' "$file"
        fi
    fi

    # Substitution 2: ~/.claude → ${CLAUDE_HOME}
    matches=$(grep -c '~/.claude' "$file" 2>/dev/null || echo "0")
    if [ "$matches" -gt 0 ]; then
        echo "  Found $matches tilde claude paths (~/.claude)"
        count=$((count + matches))
        if [ "$DRY_RUN" = "false" ]; then
            sed -i '' 's|~/.claude|${CLAUDE_HOME}|g' "$file"
        fi
    fi

    # Substitution 3: ~/.local/synrg → ${SYNRG_HOME}
    matches=$(grep -c '~/.local/synrg' "$file" 2>/dev/null || echo "0")
    if [ "$matches" -gt 0 ]; then
        echo "  Found $matches synrg home paths (~/.local/synrg)"
        count=$((count + matches))
        if [ "$DRY_RUN" = "false" ]; then
            sed -i '' 's|~/.local/synrg|${SYNRG_HOME}|g' "$file"
        fi
    fi

    # Substitution 4: ~/CODING → ${CODING_ROOT}
    matches=$(grep -c '~/CODING' "$file" 2>/dev/null || echo "0")
    if [ "$matches" -gt 0 ]; then
        echo "  Found $matches coding root paths (~/CODING)"
        count=$((count + matches))
        if [ "$DRY_RUN" = "false" ]; then
            sed -i '' 's|~/CODING|${CODING_ROOT}|g' "$file"
        fi
    fi

    # Apply derived variable substitutions (only after base substitutions)
    if [ "$DRY_RUN" = "false" ]; then
        # ${CLAUDE_HOME}/agents → ${CLAUDE_AGENTS}
        sed -i '' 's|\${CLAUDE_HOME}/agents|\${CLAUDE_AGENTS}|g' "$file"
        # ${CLAUDE_HOME}/commands → ${CLAUDE_COMMANDS}
        sed -i '' 's|\${CLAUDE_HOME}/commands|\${CLAUDE_COMMANDS}|g' "$file"
        # ${CLAUDE_HOME}/skills → ${CLAUDE_SKILLS}
        sed -i '' 's|\${CLAUDE_HOME}/skills|\${CLAUDE_SKILLS}|g' "$file"
        # ${CLAUDE_HOME}/protocols → ${CLAUDE_PROTOCOLS}
        sed -i '' 's|\${CLAUDE_HOME}/protocols|\${CLAUDE_PROTOCOLS}|g' "$file"
    fi

    if [ "$count" -eq 0 ]; then
        echo -e "  ${GREEN}No hardcoded paths found${NC}"
    else
        echo -e "  ${YELLOW}Total substitutions: ${count}${NC}"
    fi

    return $count
}

# Files to migrate
FILES=(
    "${COMMANDS_DIR}/synrg.md"
    "${COMMANDS_DIR}/synrg-refactor.md"
    "${COMMANDS_DIR}/synrg-commit.md"
    "${COMMANDS_DIR}/synrg-spec.md"
    "${COMMANDS_DIR}/synrg-scaffold.md"
    "${COMMANDS_DIR}/synrg-guided.md"
    "${COMMANDS_DIR}/synrg-buildworkflow.md"
    "${COMMANDS_DIR}/synrg-swarm.md"
    "${COMMANDS_DIR}/synrg-evolve.md"
    "${CLAUDE_HOME}/CLAUDE.md"
)

TOTAL_SUBS=0

# Process each file
for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        migrate_file "$file"
        TOTAL_SUBS=$((TOTAL_SUBS + $?))
    else
        echo -e "${RED}File not found: ${file}${NC}"
    fi
done

echo ""
echo "================================================"
echo "Migration Summary"
echo "================================================"
echo "Files processed: ${#FILES[@]}"
echo "Total substitutions: ${TOTAL_SUBS}"
echo ""

if [ "$DRY_RUN" = "true" ]; then
    echo -e "${YELLOW}This was a DRY RUN - no changes were made${NC}"
    echo ""
    echo "To apply changes, run:"
    echo "  DRY_RUN=false $0"
else
    echo -e "${GREEN}Migration complete!${NC}"
    echo "Backups saved to: ${BACKUP_DIR}"
    echo ""
    echo "Next steps:"
    echo "  1. Review the changes: git diff"
    echo "  2. Test command execution"
    echo "  3. Commit: git add -A && git commit -m 'Apply Phase 3 path variables'"
fi

echo ""
echo "Validation commands:"
echo "  # Check for remaining hardcoded paths:"
echo "  grep -rn '/Users/jelalconnor' ${COMMANDS_DIR}/"
echo "  grep -rn '~/.claude' ${COMMANDS_DIR}/"
echo ""
