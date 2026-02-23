# SYNRG-AIODebug Command

## Command Definition
```
/synrg-aiodebug [--component=<name>] [--logs] [--auto-fix] [--evolve] [--security] [--simulate "<message>"]
```

Comprehensive health diagnostics, log analysis, and evolution engine for the complete AIO Voice System ecosystem (Railway + n8n + LiveKit + Fireworks + Composio + Recall.ai + client-v2).

---

## Invocation Patterns

### Full Ecosystem Health Check
```
/synrg-aiodebug
/synrg-aiodebug created the phased integration plan to get the V2 site deployed and live
```

### Component-Scoped Checks
```
/synrg-aiodebug --component=railway
/synrg-aiodebug --component=n8n
/synrg-aiodebug --component=database
/synrg-aiodebug --component=recall
/synrg-aiodebug --component=web
/synrg-aiodebug --component=compliance
```

### Specialized Modes
```
/synrg-aiodebug --logs                          # Analyze Railway logs for errors
/synrg-aiodebug --auto-fix                      # Apply high-confidence fixes automatically
/synrg-aiodebug --evolve                        # Document new error patterns
/synrg-aiodebug --security                      # Credential + compliance audit
/synrg-aiodebug --simulate "list my drive files" # Validate agent behavior
```

---

## Execution Protocol

### Phase 1: Infrastructure Check (parallel)
```
1. Railway services (4): voice-agent-relay, livekit-voice-agent, Postgres, voice-agent-client
2. n8n workflows (12): AIO folder status, recent failures, credential health
3. Webhook endpoint tests: Drive, Gmail, Context, VectorDB
4. Database connectivity: PostgreSQL NI3jbq1U8xPst3j3
5. Recall.ai API status (if bot active)
```

### Phase 2: Log Analysis
```
1. Fetch last 200 lines from Railway (livekit-voice-agent service)
2. Pattern match: EAUTH | got an unexpected keyword argument | 401 | ETIMEDOUT | 500
3. Extract performance metrics: tool latency, STT/TTS latency
4. Identify LLM behavior issues (JSON output as speech → model issue)
```

### Phase 3: Security Audit (when --security)
```
1. Credential health: Google Drive OAuth (ylMLH2SMUpGQpUUr), Gmail (kHDxu9JVLxm6iyMo)
2. Composio connection status: manageConnections(action="status")
3. Tool security ratings: A (context/recall) | B (drive/email/db) | C (vector write)
4. Compliance check: audit-reports/, GDPR docs
```

### Phase 4: Generate Report
```
Output format: Health Report table → Recent Errors → Performance → Recommendations → Auto-Fix Available
```

---

## AIO System Quick Reference

### Railway Services
| Service | ID | Deploy Source |
|---------|----|----|
| `voice-agent-client` | `53e95284-93b6-45ee-b176-32fff75e08cd` | `JayConnorSynrg/synrg-voice-agent-client` → git push main |
| `livekit-voice-agent` | `95bb0daa-cb07-441b-a3f3-2d6762d8e18b` | `JayConnorSynrg/livekit-voice-agent` → git push main |

**Client live URL**: `voice-agent-client-production.up.railway.app`
**LLM**: Fireworks `deepseek-v3p1` (Cerebras removed 2026-02-20 — do NOT reference Cerebras)
**Composio**: SDK-only via `composio_router.py`, 100% dynamic discovery

### Key n8n Workflows
| Workflow | ID | Purpose |
|----------|----|---------|
| Primary Bot | `gjYSN6xNjLw8qsA1` | Recall.ai + OpenAI TTS |
| Launcher v4.2 | `kUcUSyPgz4Z9mYBt` | Pre-init + client URL |
| Drive Tool | `IamjzfFxjHviJvJg` | Google Drive ops |
| Gmail Tool | `kBuTRrXTJF1EEBEs` | Send email |
| Context Tool | `ouWMjcKzbj6nrYXz` | Session context |

### Known Issue Patterns
| Pattern | Severity | Fix |
|---------|----------|-----|
| `EAUTH` | HIGH | Re-auth Google Drive OAuth `ylMLH2SMUpGQpUUr` in n8n UI |
| `got an unexpected keyword argument` | HIGH | Schema mismatch — update tool def in async_wrappers.py |
| JSON output as speech | CRITICAL | LLM function calling broken — check Fireworks model config |
| `ETIMEDOUT` / `ECONNREFUSED` | HIGH | Railway service down — check dashboard |
| `401 Unauthorized` | HIGH | Credential expired — check n8n credentials |
| Composio auth expired | HIGH | `manageConnections(action="connect", service=X)` — get new auth URL |

---

## Skill File
Full protocol, component registry, health check templates, and workflow documentation:
`~/.claude/skills/synrg-aiodebug/SKILL.md` (v2.3.0)

## Chain Integration
- After auto-fix with code changes → `/synrg-commit`
- New error patterns found → `/synrg-evolve analyze`
- n8n workflow issues → delegate to `n8n-workflow-expert`
