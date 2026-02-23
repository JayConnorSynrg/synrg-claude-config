# SYNRG-AIODebug Command
## AIO Voice System Health & Evolution Engine

**Purpose**: Comprehensive diagnostics, log analysis, and evolution for the complete AIO Voice System ecosystem.

**Trigger**: `/synrg-AIODebug` or when user mentions "AIO Voice System" + debug/health/check/fix

---

## AIO Voice System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         AIO VOICE SYSTEM ECOSYSTEM                           │
├─────────────────────────────────────────────────────────────────────────────┤
│  RAILWAY INFRASTRUCTURE (4 Services - All Online)                            │
│  ┌────────────────┐ ┌────────────────┐ ┌────────────────┐ ┌──────────────┐ │
│  │ voice-agent-   │ │ livekit-voice- │ │ Postgres       │ │ voice-agent- │ │
│  │ relay          │ │ agent          │ │ + volume       │ │ client       │ │
│  │ (WebSocket)    │ │ (Python Agent) │ │ (Database)     │ │ (React UI)   │ │
│  └───────┬────────┘ └───────┬────────┘ └───────┬────────┘ └──────┬───────┘ │
│           │                     │                                           │
├───────────┼─────────────────────┼───────────────────────────────────────────┤
│  AUDIO PIPELINE                 │                                           │
│  ┌──────────┐    ┌──────────┐   │   ┌──────────┐                           │
│  │ Recall.ai│───▶│ LiveKit  │◀──┴──▶│ Deepgram │                           │
│  │ (capture)│    │ (stream) │       │ (STT)    │                           │
│  │ us-west-2│    │ Cloud    │       │ nova-3   │                           │
│  └──────────┘    └──────────┘       └──────────┘                           │
├─────────────────────────────────────────────────────────────────────────────┤
│  INTELLIGENCE LAYER                                                          │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │  Fireworks LLM (deepseek-v3p1) - Function Calling + Reasoning        │   │
│  │  max_tool_steps: 10 | parallel_tool_calls: true | Composio SDK       │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────────────────────────┤
│  N8N TOOL BACKENDS (12 workflows in AIO folder)                             │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐         │
│  │  Drive   │ │  Email   │ │ VectorDB │ │ Context  │ │ TTS/Bot  │         │
│  │ IamjzfF  │ │ kBuTRrX  │ │ jKM/z02K │ │ ouWMjcK  │ │ gjYS/kUc │         │
│  │ Sec: B   │ │ Sec: B   │ │ Sec: B/C │ │ Sec: A   │ │ Primary  │         │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘         │
├─────────────────────────────────────────────────────────────────────────────┤
│  DATA LAYER (PostgreSQL - NI3jbq1U8xPst3j3)                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │ Tables: tool_executions, audit_trail, training_metrics,             │    │
│  │         user_session_analytics, tool_calls, session_context         │    │
│  │ Views: v_tool_success_rates, v_user_engagement, v_active_sessions   │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
├─────────────────────────────────────────────────────────────────────────────┤
│  OUTPUT LAYER                                                                │
│  ┌──────────┐    ┌──────────┐    ┌──────────────────────┐                  │
│  │ Cartesia │───▶│ LiveKit  │───▶│ Web Client (React)   │                  │
│  │ (TTS)    │    │ (stream) │    │ VoiceOrb + Waveform  │                  │
│  │ sonic-3  │    │          │    │ Zustand + OGL        │                  │
│  └──────────┘    └──────────┘    └──────────────────────┘                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Complete Component Registry

### Infrastructure (Railway - 4 Services)

| Service | Type | Purpose | Health Check |
|---------|------|---------|--------------|
| `voice-agent-relay` | Custom | WebSocket relay between LiveKit and clients | Online status |
| `livekit-voice-agent` | GitHub | Python voice agent (Fireworks deepseek-v3p1 + Composio tools) | `railway logs` + worker registration |
| `Postgres` | Managed | Database with `postgres-volume` | Connection test |
| `voice-agent-client` | GitHub | React web UI (client-v2: WebGLOrb, AgentEventBus, ToolCallCard) | HTTP 200 on index |

**Local configs**: Only `livekit-voice-agent` and `voice-agent-client` have local `railway.json` files. Postgres is Railway-managed. Relay may be deployed separately.

### External APIs

| Component | Service | Health Check | Config |
|-----------|---------|--------------|--------|
| LLM | Fireworks | API response | `deepseek-v3p1` (sole provider — Cerebras removed 2026-02-20) |
| STT | Deepgram | LiveKit plugin | `nova-3` |
| TTS | Cartesia | LiveKit plugin | `sonic-3` |
| Audio Capture | Recall.ai | Bot status API | `us-west-2.recall.ai` |
| Tool Execution | Composio SDK | `composio_router.py` circuit breakers | 100% dynamic discovery via `connected_accounts.list()` |

### n8n Workflows (AIO Folder)

**Source**: `jayconnorexe.app.n8n.cloud/projects/vaRklvnINMqrVVkS/folders/Pm4TxSTXoxmkGy6q`

| Workflow | ID | Type | Status |
|----------|----|----|--------|
| Teams Voice Bot - Recall.ai + OpenAI TTS | `gjYSN6xNjLw8qsA1` | Primary Bot | Active |
| Teams Voice Bot - Launcher v4.2 | `kUcUSyPgz4Z9mYBt` | Pre-Init | Active |
| Teams Voice Bot v3.0 - Agent Orchestrator | `d3CxEaYk5mkC8sLo` | Legacy | Inactive |
| Voice Session Summary Generator | `WEfjWyowdTgoVlvM` | Utility | Active |
| TTS Agent Sub-Workflow | `DdwpUSXz7GCZuhlC` | TTS Output | Active |
| Voice Tool: Send Gmail | `kBuTRrXTJF1EEBEs` | Email Tool | Active |
| Voice Tool: Add to Vector DB | `jKMw735r3nAN6O7u` | Vector Write | Active |
| Voice Tool: Query Vector DB | `z02K1a54akYXMkyj` | Vector Read | Active |
| Callback No-Op (LiveKit) | `Y6CuLuSu87qKQzK1` | Callback | Active |
| Agent Context Access - Universal Query | `ouWMjcKzbj6nrYXz` | Context Tool | Active |
| Recall.ai Bot Event Handler | `ZtHr8tzwDhwEr2o0` | Event Handler | Active |
| Google Drive Document Repository | `IamjzfFxjHviJvJg` | Drive Tool | Active |

**Total: 12 workflows (11 active, 1 inactive)**

### Python Tools → n8n Workflow Mapping

| Tool | Python File | n8n Workflow | Webhook |
|------|-------------|--------------|---------|
| `send_email` | `email_tool.py` | `kBuTRrXTJF1EEBEs` | `/execute-gmail` |
| `search_drive` | `google_drive_tool.py` | `IamjzfFxjHviJvJg` | `/drive-document-repo` |
| `list_files` | `google_drive_tool.py` | `IamjzfFxjHviJvJg` | `/drive-document-repo` |
| `get_file` | `google_drive_tool.py` | `IamjzfFxjHviJvJg` | `/drive-document-repo` |
| `query_db` | `database_tool.py` | `z02K1a54akYXMkyj` | `/database-query` |
| `knowledge_base` (store) | `vector_store_tool.py` | `jKMw735r3nAN6O7u` | `/vector-store` |
| `knowledge_base` (search) | `vector_store_tool.py` | `z02K1a54akYXMkyj` | `/database-query` |
| `check_context` | `agent_context_tool.py` | `ouWMjcKzbj6nrYXz` | `/agent-context-access` |
| `recall` | `async_wrappers.py` | N/A (memory only) | N/A |
| `memory_status` | `async_wrappers.py` | N/A (memory only) | N/A |
| `recall_drive` | `async_wrappers.py` | N/A (memory only) | N/A |

### Tool Security Ratings

| Rating | Tools | Policy |
|--------|-------|--------|
| **A** | `check_context`, `recall`, `memory_status`, `recall_drive` | No external calls |
| **B** | `send_email`, `search_drive`, `list_files`, `get_file`, `query_db` | Authenticated API |
| **C** | `knowledge_base` (store) | Needs confirmation for writes |

### Database (PostgreSQL)

| Table | Purpose | Health Query |
|-------|---------|--------------|
| `tool_executions` | Tool call tracking | `SELECT COUNT(*) WHERE created_at > NOW() - INTERVAL '1h'` |
| `audit_trail` | Compliance logging | `SELECT * ORDER BY timestamp DESC LIMIT 10` |
| `session_context` | User session state | `SELECT * FROM v_active_sessions` |
| `tool_calls` | Detailed call logs | `SELECT status, COUNT(*) GROUP BY status` |

### Web Components (client-v2 — deployed 2026-02-22)

**Repo**: `JayConnorSynrg/synrg-voice-agent-client` | **Branch**: `main` | **Commit**: `396764b`
**Live URL**: `voice-agent-client-production.up.railway.app`
**Railway Service ID**: `53e95284-93b6-45ee-b176-32fff75e08cd`

| Component | File | Purpose |
|-----------|------|---------|
| WebGLOrb | `WebGLOrb.tsx` | 3D WebGL orb with OGL (listening/thinking/speaking states) |
| LiveWaveform | `LiveWaveform.tsx` | Audio waveform visualization (user input volume) |
| TranscriptCycler | `TranscriptCycler.tsx` | Animated message cycling with tool call interleaving |
| ToolCallPanel | `ToolCallCard.tsx` | Dual side panels — neumorphic cards with 3 status animations |
| AgentEventBus | `lib/eventBus.ts` | 13-event singleton dispatcher; `window.__dispatchAgentEvent` (dev-only) |
| useLiveKitAgent | `hooks/useLiveKitAgent.ts` | LiveKit room connection + 13 data message event handlers |
| useStore | `lib/store.ts` | Zustand store — agentState, messages, toolCalls, volumes |
| SessionReplay | `SessionReplay.tsx` | Scripted replay for demos (dev URL: `?replay=<scriptId>`) |
| DevTestPanel | `DevTestPanel.tsx` | Stress-test panel (dev URL: `?devtest=1`) |
| DemoRunner | `DemoRunner.tsx` | Auto-demo runner — **strictly `import.meta.env.DEV` gated** |

**13 Event Types Handled** (all compatible with Python agent):
`agent.state`, `transcript.user`, `transcript.assistant`, `tool.call`, `tool.executing`,
`tool.completed`, `tool.error`, `tool_result`, `composio.searching`, `composio.executing`,
`composio.completed`, `composio.error`, `error`

**Deploy method**: `git push origin main` to `synrg-voice-agent-client` → Railway auto-deploys
**Do NOT use** `railway up` from client-v2 dir (uploads 144MB node_modules)

### Compliance

| Item | Location | Status |
|------|----------|--------|
| Audit Reports | `compliance/audit-reports/` | 100% (17/17 checks) |
| Retention Scripts | `scripts/compliance/retention-automation.sql` | Active |
| GDPR Docs | `compliance/gdpr/` | Available |

---

## Quick Reference

```bash
# Full ecosystem health check
/synrg-AIODebug

# Check specific component
/synrg-AIODebug --component=railway
/synrg-AIODebug --component=n8n
/synrg-AIODebug --component=database
/synrg-AIODebug --component=recall
/synrg-AIODebug --component=web
/synrg-AIODebug --component=compliance

# Analyze recent logs for issues
/synrg-AIODebug --logs

# Simulate voice interaction
/synrg-AIODebug --simulate "list my drive files"

# Auto-fix detected issues
/synrg-AIODebug --auto-fix

# Evolution mode - learn from errors
/synrg-AIODebug --evolve

# Security audit
/synrg-AIODebug --security
```

---

## Change Proliferation Protocol

**CRITICAL**: When making ANY change to the AIO Voice System, run full ecosystem verification. Changes must proliferate proactively, not reactively after errors.

### On Every AIO Change

```javascript
async function onAIOChange(changeType, component, details) {
  // 1. Document the change
  const change = {
    timestamp: new Date().toISOString(),
    type: changeType,  // 'code' | 'workflow' | 'config' | 'credential'
    component: component,
    details: details
  };

  // 2. Identify affected components
  const affected = mapAffectedComponents(change);

  // 3. Run targeted verification
  for (const comp of affected) {
    await verifyComponent(comp);
  }

  // 4. Update documentation
  await propagateToDocumentation(change);

  // 5. Verify end-to-end
  await runE2ESimulation();
}
```

### Dependency Map (What Affects What)

| Changed | Must Verify |
|---------|-------------|
| `config.py` | Railway deploy → Agent registration → All tools |
| `async_wrappers.py` | Tool schemas → LLM function calling → n8n webhooks |
| `google_drive_tool.py` | Drive webhook (`IamjzfFxjHviJvJg`) → Memory storage |
| n8n workflow nodes | Webhook response format → Python tool parsing |
| n8n credentials | OAuth status → Execution success → Tool availability |
| System prompt | LLM behavior → Tool selection → User experience |
| Database schema | Analytics views → Compliance reports → Query tools |

### Workflow Audit Checklist

For each workflow in AIO folder, verify:

```markdown
## Workflow: [Name] ([ID])

### Documentation
- [ ] Purpose documented in this skill file
- [ ] Webhook endpoints documented
- [ ] Input/output schema documented
- [ ] Error handling documented

### Configuration
- [ ] Active status correct
- [ ] Credentials valid (not expired)
- [ ] Environment variables set
- [ ] Timeout values appropriate

### Connections
- [ ] All nodes connected properly
- [ ] No orphan nodes
- [ ] Error outputs wired
- [ ] Respond nodes in all paths

### Integration
- [ ] Python tool matches webhook contract
- [ ] Response parsing handles all cases
- [ ] Memory offer pattern implemented (if applicable)
- [ ] Security rating assigned
```

### Auto-Proliferation Triggers

| Event | Action |
|-------|--------|
| Code pushed to `voice-agent-poc/` | Deploy to Railway + verify tools load |
| Workflow modified in n8n | Update skill file + test webhook |
| Credential re-authenticated | Run full webhook tests |
| System prompt changed | Run behavior simulation |
| New tool added | Update registry + security rating + test |

---

## Health Check Protocol

### Phase 1: Infrastructure Health

```javascript
async function checkInfrastructure() {
  const checks = {
    railway: await checkAllRailwayServices(),
    n8n: await checkN8nWorkflows(),
    webhooks: await testWebhookEndpoints(),
    database: await checkPostgresHealth(),
    recall: await checkRecallApiStatus()
  };

  return {
    status: allHealthy(checks) ? 'HEALTHY' : 'DEGRADED',
    components: checks,
    timestamp: new Date().toISOString()
  };
}
```

#### Railway Services Check (4 Services)
```bash
# Check current linked service
railway status

# Check all 4 services via dashboard or API
# Services: voice-agent-relay, livekit-voice-agent, Postgres, voice-agent-client

# Agent logs (most critical)
railway logs 2>&1 | grep -E "registered|error|Error|failed|tools loaded" | tail -30

# Database connection test
railway connect  # Opens psql shell to Postgres

# Expected states:
# - voice-agent-relay: Online (WebSocket relay active)
# - livekit-voice-agent: Online + Worker registered + 10 tools loaded
# - Postgres: Online + postgres-volume mounted
# - voice-agent-client: Online + HTTP 200
```

#### n8n Workflow Audit
```javascript
// Delegate to n8n-mcp-delegate
// Source folder: jayconnorexe.app.n8n.cloud/projects/vaRklvnINMqrVVkS/folders/Pm4TxSTXoxmkGy6q
Task({
  subagent_type: "n8n-mcp-delegate",
  prompt: `Audit ALL 12 AIO Voice System workflows:

    PRIMARY BOT:
    - gjYSN6xNjLw8qsA1 (Recall.ai + OpenAI TTS)
    - kUcUSyPgz4Z9mYBt (Launcher v4.2)

    TOOLS:
    - IamjzfFxjHviJvJg (Drive) - check OAuth credential ylMLH2SMUpGQpUUr
    - kBuTRrXTJF1EEBEs (Send Gmail)
    - jKMw735r3nAN6O7u (Add to Vector DB)
    - z02K1a54akYXMkyj (Query Vector DB)
    - ouWMjcKzbj6nrYXz (Context Access)

    UTILITIES:
    - DdwpUSXz7GCZuhlC (TTS Sub-Workflow)
    - WEfjWyowdTgoVlvM (Session Summary)
    - Y6CuLuSu87qKQzK1 (Callback No-Op)
    - ZtHr8tzwDhwEr2o0 (Event Handler)

    LEGACY (verify inactive):
    - d3CxEaYk5mkC8sLo (v3.0 Orchestrator)

    For each: active status, recent executions, failed executions in 24h
    Return: status table, credential health, error summary`,
  model: "haiku"
})
```

#### Database Health Check
```sql
-- Connection test
SELECT 1 AS ping;

-- Recent activity
SELECT COUNT(*) AS recent_calls
FROM tool_calls
WHERE created_at > NOW() - INTERVAL '1 hour';

-- Tool success rates
SELECT * FROM v_tool_success_rates;

-- Active sessions
SELECT * FROM v_active_sessions;

-- Error frequency
SELECT
  tool_name,
  COUNT(*) FILTER (WHERE status = 'error') AS errors,
  COUNT(*) AS total,
  ROUND(COUNT(*) FILTER (WHERE status = 'error')::numeric / COUNT(*) * 100, 2) AS error_rate
FROM tool_calls
WHERE created_at > NOW() - INTERVAL '24 hours'
GROUP BY tool_name
HAVING COUNT(*) > 0;
```

#### Recall.ai Integration Check
```bash
# Test bot status endpoint (requires active bot_id)
curl -s -X GET "https://us-west-2.recall.ai/api/v1/bot/{bot_id}/" \
  -H "Authorization: Token $RECALL_API_KEY" | jq '.status_changes[-1]'

# Expected: {"code": "in_call_recording"} or {"code": "in_call_not_recording"}
```

#### Webhook Endpoint Tests
```bash
# Drive list test
curl -s -X POST 'https://jayconnorexe.app.n8n.cloud/webhook/drive-document-repo' \
  -H 'Content-Type: application/json' \
  -d '{"operation":"list","limit":3}' | jq '.result.count // .error'

# Context access test
curl -s -X POST 'https://jayconnorexe.app.n8n.cloud/webhook/agent-context-access' \
  -H 'Content-Type: application/json' \
  -d '{"context_type":"session_context"}' | jq '.status // .error'

# Expected: numeric count for drive, "success" for context
```

---

### Phase 2: Log Analysis

```javascript
async function analyzeLogs() {
  // Get Railway logs
  const railwayLogs = await Bash({
    command: "railway logs 2>&1 | tail -200"
  });

  const analysis = {
    errors: extractErrors(railwayLogs),
    warnings: extractWarnings(railwayLogs),
    toolCalls: extractToolCalls(railwayLogs),
    agentSpeech: extractAgentSpeech(railwayLogs),
    performance: analyzeLatency(railwayLogs)
  };

  return analysis;
}
```

#### Error Pattern Detection

| Pattern | Severity | Likely Cause | Auto-Fix |
|---------|----------|--------------|----------|
| `EAUTH` | HIGH | OAuth expired | Prompt reauth |
| `got an unexpected keyword argument` | HIGH | Schema mismatch | Update tool def |
| `"type": "function"` in speech | CRITICAL | LLM not using function calling | Check model |
| `Tool X failed` | MEDIUM | Webhook/API error | Check endpoint |
| `languages.json not found` | LOW | Turn detector missing | Ignore |
| `Connection refused` | HIGH | Service down | Check Railway |
| `ETIMEDOUT` | MEDIUM | Network/API slow | Retry or check |
| `401 Unauthorized` | HIGH | Credential issue | Check secrets |
| `500 Internal Server Error` | HIGH | n8n workflow error | Check execution |

#### Performance Metrics

```javascript
function analyzePerformance(logs) {
  return {
    avgToolLatency: extractAvgLatency(logs, 'Tool .* completed in'),
    sttLatency: extractLatency(logs, 'STT latency'),
    ttsLatency: extractLatency(logs, 'TTS latency'),
    totalTurnLatency: extractLatency(logs, 'Total latency'),
    healthyThresholds: {
      tool: '<3000ms',
      stt: '<500ms',
      tts: '<500ms',
      total: '<2000ms',
      recallOutput: '<500ms'
    }
  };
}
```

---

### Phase 3: Security Audit

```javascript
async function runSecurityAudit() {
  const audit = {
    credentials: await checkCredentialHealth(),
    compliance: await checkComplianceStatus(),
    toolSecurity: await auditToolSecurityRatings()
  };

  return audit;
}
```

#### Credential Health Check

| Credential | ID | Check Method |
|------------|----|----|
| Google Drive OAuth | `ylMLH2SMUpGQpUUr` | n8n execution history for EAUTH |
| PostgreSQL | `NI3jbq1U8xPst3j3` | Connection test |
| OpenAI | `6BIzzQu5jAD5jKlH` | API call test |
| Gmail | `kHDxu9JVLxm6iyMo` | Send test (dry-run) |

#### Tool Security Ratings

| Rating | Tools | Policy |
|--------|-------|--------|
| **A** (Highest) | `check_context`, `recall`, `memory_status` | No external calls |
| **B** (Standard) | `send_email`, `search_drive`, `list_files`, `get_file`, `query_db` | Authenticated API |
| **C** (Review) | `knowledge_base` (store) | Needs confirmation for writes |

#### Compliance Check
```bash
# Run compliance audit script
bash /Users/jelalconnor/CODING/N8N/Workflows/scripts/compliance/audit-compliance.sh

# Check latest audit report
cat compliance/audit-reports/audit-$(date +%Y-%m-%d).json | jq '.summary'
```

---

### Phase 4: Agent Behavior Simulation

```javascript
async function simulateInteraction(userMessage) {
  const scenarios = [
    {
      input: userMessage,
      expectedBehavior: inferExpectedBehavior(userMessage),
      toolsRequired: inferRequiredTools(userMessage)
    }
  ];

  for (const scenario of scenarios) {
    const result = await validateScenario(scenario);
    if (!result.valid) {
      return {
        status: 'BEHAVIOR_ISSUE',
        scenario,
        issue: result.issue,
        fix: result.suggestedFix
      };
    }
  }

  return { status: 'BEHAVIOR_VALID', scenarios };
}
```

#### Expected Behavior Matrix

| User Intent | Expected Tool | Expected Speech Pattern |
|-------------|---------------|------------------------|
| "list files" / "what files" | `list_files` | "Checking your files" → file names |
| "search for X" | `search_drive` | "Searching Drive" → results |
| "email X about Y" | Confirm first → `send_email` | "Should I send" → "Done" |
| "what did we discuss" | `recall` or `check_context` | Summary of context |
| "save this to knowledge base" | Confirm first → `knowledge_base` | "Should I save" → "Saved" |

---

### Phase 5: Evolution & Fix

```javascript
async function evolveFromErrors(analysis) {
  const evolutions = [];

  for (const error of analysis.errors) {
    const pattern = matchKnownPattern(error);

    if (pattern) {
      evolutions.push({
        type: 'KNOWN_PATTERN',
        error: error.message,
        fix: pattern.fix,
        autoApplicable: pattern.confidence > 0.9
      });
    } else {
      evolutions.push({
        type: 'NEW_PATTERN',
        error: error.message,
        action: 'Document in pattern library',
        file: '.claude/patterns/aio-voice-errors.md'
      });
    }
  }

  return evolutions;
}
```

---

## Known Issues & Fixes

### Issue: LLM Outputs JSON as Speech

**Detection**: `Agent said: { "type": "function"` in logs

**Root Cause**: Model doesn't support function calling properly

**Fix**:
```python
# In config.py - use 70b model
cerebras_model: str = Field(default="llama-3.3-70b", alias="CEREBRAS_MODEL")
```

### Issue: Google Drive OAuth Expired

**Detection**: `EAUTH` error in n8n executions

**Fix**: Manual re-authentication in n8n UI
1. Go to n8n → Credentials
2. Find `JayConnor@synrgscaling.com` (ID: `ylMLH2SMUpGQpUUr`)
3. Click Reconnect → Complete OAuth flow

### Issue: Tool Schema Mismatch

**Detection**: `got an unexpected keyword argument` in logs

**Root Cause**: `raw_schema` breaking LiveKit tool binding

**Fix**: Remove `raw_schema`, use type hints only in `async_wrappers.py`

### Issue: Empty Webhook Response

**Detection**: 200 status but empty body from n8n

**Root Cause**: Respond node not in execution path or expression returns undefined

**Fix**: Check n8n workflow execution logs for which nodes ran

### Issue: Recall.ai Audio Output Fails

**Detection**: Audio not playing in meeting

**Root Cause**: Bot not in active call state or audio format invalid

**Fix**:
1. Verify bot status is `in_call_recording` or `in_call_not_recording`
2. Audio must be MP3 format, base64 encoded
3. Use POST to `/output_audio/` endpoint

### Issue: Database Connection Timeout

**Detection**: `ETIMEDOUT` or `ECONNREFUSED` to PostgreSQL

**Fix**:
1. Check Railway service status
2. Verify `NI3jbq1U8xPst3j3` credential in n8n
3. Test direct connection with psql

### Issue: Web Client WebSocket Disconnect

**Detection**: StatusIndicator shows disconnected

**Fix**:
1. Check LiveKit Cloud status
2. Verify LiveKit credentials in agent config
3. Check browser console for connection errors

---

## Output Format

### Health Report

```markdown
# AIO Voice System Health Report
**Generated**: [timestamp]
**Overall Status**: [HEALTHY | DEGRADED | CRITICAL]

## Infrastructure
| Component | Status | Details |
|-----------|--------|---------|
| Railway Agent | ✅/⚠️/❌ | [deployment id, uptime] |
| Railway Client | ✅/⚠️/❌ | [deployment id] |
| PostgreSQL | ✅/⚠️/❌ | [connection status] |
| n8n Workflows | ✅/⚠️/❌ | [X active, Y failed] |
| Recall.ai | ✅/⚠️/❌ | [API status] |

## Tool Health
| Tool | Webhook | Recent Calls | Error Rate |
|------|---------|--------------|------------|
| Drive | ✅/❌ | [count] | [%] |
| Email | ✅/❌ | [count] | [%] |
| Context | ✅/❌ | [count] | [%] |

## Recent Errors
| Time | Component | Error | Severity |
|------|-----------|-------|----------|
| [time] | [component] | [error] | [HIGH/MED/LOW] |

## Performance
| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| Tool Latency | [ms] | <3000ms | ✅/⚠️ |
| Total Turn | [ms] | <2000ms | ✅/⚠️ |
| Webhook Response | [ms] | <1000ms | ✅/⚠️ |

## Security & Compliance
| Check | Status | Last Audit |
|-------|--------|------------|
| Credentials | ✅/⚠️ | [date] |
| Compliance | [%] | [date] |
| Tool Ratings | [A/B/C summary] | N/A |

## Recommendations
1. [Action item with priority]
2. [Action item with priority]

## Auto-Fix Available
- [ ] [Fix 1 - HIGH confidence]
- [ ] [Fix 2 - MEDIUM confidence]
```

---

## Execution Protocol

### MANDATORY: After Any AIO Change

When ANY code, workflow, or config change is made to AIO Voice System:

```bash
# 1. Deploy if code changed
# Agent: git push origin main → JayConnorSynrg/livekit-voice-agent → Railway auto-deploys
# Client: git push origin main → JayConnorSynrg/synrg-voice-agent-client → Railway auto-deploys
# NOTE: Do NOT use `railway up` for client-v2 (uploads 144MB node_modules even with .railwayignore)

# 2. Run full ecosystem audit
/synrg-AIODebug

# 3. If issues found, fix and re-audit
/synrg-AIODebug --auto-fix

# 4. Update documentation
# Skill file auto-updates on --evolve
```

**Change triggers requiring full audit:**
- Python tool code modified
- n8n workflow nodes changed
- System prompt updated
- Config values changed
- Credentials re-authenticated
- Database schema modified

### Standard Run (`/synrg-AIODebug`)

1. **Infrastructure Check** (parallel)
   - Railway deployment status (all services)
   - n8n workflow status
   - Webhook endpoint tests
   - Database connectivity
   - Recall.ai API status (if bot active)

2. **Log Analysis**
   - Fetch last 200 lines from Railway
   - Pattern match for errors
   - Extract performance metrics

3. **Security Check**
   - Credential health
   - Compliance status
   - Tool security audit

4. **Generate Report**
   - Health status table
   - Error summary
   - Recommendations

5. **Offer Evolution**
   - If errors found: "Run with `--auto-fix` to apply fixes"
   - If new patterns: "Run with `--evolve` to document patterns"

### Auto-Fix Run (`/synrg-AIODebug --auto-fix`)

1. Run standard checks
2. For each HIGH confidence fix:
   - Apply fix
   - Validate
   - Report result
3. For MEDIUM confidence:
   - Present fix
   - Ask for confirmation
4. Redeploy if code changed

### Evolution Run (`/synrg-AIODebug --evolve`)

1. Run standard checks
2. Identify new error patterns
3. Document in `.claude/patterns/aio-voice-errors.md`
4. Update CLAUDE.md with new known issues
5. Chain to `/synrg-evolve integrate`

### Security Run (`/synrg-AIODebug --security`)

1. Check all credential expiration
2. Run compliance audit script
3. Review tool security ratings
4. Generate security report
5. Recommend upgrades for C-rated tools

---

## Chain Integration

### Chains FROM
```
/synrg "AIO Voice System" → /synrg-AIODebug
User: "debug voice system" → /synrg-AIODebug
User: "check AIO health" → /synrg-AIODebug
Railway error alert → /synrg-AIODebug --logs
Compliance audit due → /synrg-AIODebug --security
```

### Chains TO
```
/synrg-AIODebug → /synrg-commit (after auto-fix)
/synrg-AIODebug → /synrg-evolve (new patterns)
/synrg-AIODebug → Railway deploy (code changes)
/synrg-AIODebug → /n8n-debug (workflow issues)
```

---

## File Locations

| Purpose | Path |
|---------|------|
| Voice Agent Code | `voice-agent-poc/livekit-voice-agent/src/` |
| System Prompt | `src/agent.py` (SYSTEM_PROMPT) |
| Tool Wrappers | `src/tools/async_wrappers.py` |
| Composio Router | `src/tools/composio_router.py` (SDK-only, dynamic discovery) |
| Config | `src/config.py` |
| Web Client (client-v2) | `voice-agent-poc/client-v2/src/` |
| Event Bus | `voice-agent-poc/client-v2/src/lib/eventBus.ts` |
| Zustand Store | `voice-agent-poc/client-v2/src/lib/store.ts` |
| LiveKit Hook | `voice-agent-poc/client-v2/src/hooks/useLiveKitAgent.ts` |
| E2E Tests | `voice-agent-poc/client-v2/e2e/` |
| Database Schema | `voice-agent-poc/database/schema.sql` |
| Error Patterns | `.claude/patterns/aio-voice-errors.md` |
| Tools Registry | `docs/AIO-TOOLS-REGISTRY.md` |
| Recall.ai Pattern | `.claude/patterns/api-integration/recall-ai-audio-output.md` |
| Compliance | `compliance/` |
| Audit Scripts | `scripts/compliance/` |

---

## Workflow Documentation (Audit Reference)

### Primary Bot Workflows

#### gjYSN6xNjLw8qsA1 - Teams Voice Bot (Recall.ai + OpenAI TTS)
- **Purpose**: Main voice bot receiving audio from Recall.ai, processing with LLM, outputting TTS
- **Webhook**: N/A (triggered by Recall.ai events)
- **Credentials**: Recall.ai API, OpenAI
- **Python Integration**: None (separate from LiveKit agent)
- **Last Audit**: TBD

#### kUcUSyPgz4Z9mYBt - Launcher v4.2 (Agent Pre-Init)
- **Purpose**: Initialize voice bot session, create Recall.ai bot
- **Webhook**: `/launcher`
- **Credentials**: Recall.ai API
- **Python Integration**: None (external trigger)
- **Last Audit**: TBD

### Tool Workflows

#### IamjzfFxjHviJvJg - Google Drive Document Repository
- **Purpose**: List, search, get documents from Google Drive
- **Webhook**: `/drive-document-repo`
- **Credentials**: Google Drive OAuth (`ylMLH2SMUpGQpUUr`)
- **Python Integration**: `google_drive_tool.py` → `async_wrappers.py`
- **Response Format**: `{result: {files: [], count: N}, memory_offer: {...}}`
- **Last Audit**: 2026-01-29 (OAuth re-auth)

#### kBuTRrXTJF1EEBEs - Voice Tool: Send Gmail
- **Purpose**: Send emails via Gmail
- **Webhook**: `/execute-gmail`
- **Credentials**: Gmail OAuth (`kHDxu9JVLxm6iyMo`)
- **Python Integration**: `email_tool.py` → `async_wrappers.py`
- **Security**: WRITE operation - requires confirmation
- **Last Audit**: TBD

#### jKMw735r3nAN6O7u - Voice Tool: Add to Vector DB
- **Purpose**: Store content in vector database
- **Webhook**: `/vector-store`
- **Credentials**: PostgreSQL (`NI3jbq1U8xPst3j3`)
- **Python Integration**: `vector_store_tool.py` → `async_wrappers.py`
- **Security**: WRITE operation - requires confirmation
- **Last Audit**: TBD

#### z02K1a54akYXMkyj - Voice Tool: Query Vector DB
- **Purpose**: Search vector database for relevant content
- **Webhook**: `/database-query`
- **Credentials**: PostgreSQL (`NI3jbq1U8xPst3j3`)
- **Python Integration**: `database_tool.py` → `async_wrappers.py`
- **Security**: READ operation - immediate
- **Last Audit**: TBD

#### ouWMjcKzbj6nrYXz - Agent Context Access
- **Purpose**: Retrieve session context, conversation history
- **Webhook**: `/agent-context-access`
- **Credentials**: PostgreSQL (`NI3jbq1U8xPst3j3`)
- **Python Integration**: `agent_context_tool.py` → `async_wrappers.py`
- **Security**: READ operation - immediate
- **Last Audit**: TBD

### Utility Workflows

#### DdwpUSXz7GCZuhlC - TTS Agent Sub-Workflow
- **Purpose**: Convert text to speech and output to Recall.ai bot
- **Webhook**: N/A (called as sub-workflow)
- **Credentials**: Recall.ai API
- **Python Integration**: None (n8n internal)
- **Last Audit**: TBD

#### WEfjWyowdTgoVlvM - Voice Session Summary Generator
- **Purpose**: Generate meeting summaries after voice session ends
- **Webhook**: N/A (triggered by session end)
- **Credentials**: OpenAI
- **Python Integration**: None
- **Last Audit**: TBD

#### Y6CuLuSu87qKQzK1 - Callback No-Op (LiveKit)
- **Purpose**: Acknowledge LiveKit callbacks without action
- **Webhook**: `/livekit-callback`
- **Credentials**: None
- **Python Integration**: LiveKit agent callbacks
- **Last Audit**: TBD

#### ZtHr8tzwDhwEr2o0 - Recall.ai Bot Event Handler
- **Purpose**: Handle Recall.ai bot lifecycle events
- **Webhook**: `/recall-events`
- **Credentials**: Recall.ai API
- **Python Integration**: None (event-driven)
- **Last Audit**: TBD

### Legacy (Inactive)

#### d3CxEaYk5mkC8sLo - Teams Voice Bot v3.0 Agent Orchestrator
- **Purpose**: Previous version orchestrator (superseded by v4.2)
- **Status**: INACTIVE - do not activate
- **Migration**: Functionality moved to `gjYSN6xNjLw8qsA1` + `kUcUSyPgz4Z9mYBt`

---

## Credentials Quick Reference

| Service | Credential ID | Status |
|---------|---------------|--------|
| Google Drive | `ylMLH2SMUpGQpUUr` | Monitor for OAuth expiry |
| PostgreSQL | `NI3jbq1U8xPst3j3` | Active |
| OpenAI | `6BIzzQu5jAD5jKlH` | Active |
| Gmail | `kHDxu9JVLxm6iyMo` | Active |
| Google Sheets | `fzaSSwZ4tI357WUU` | Active |
| Google Docs | `iNIP35ChYNUUqOCh` | Active |

---

**Version**: 2.3.0
**Created**: 2026-01-29
**Updated**: 2026-02-22
**Ecosystem**: Railway (4 services) + n8n (12 workflows) + LiveKit + Fireworks + Deepgram + Cartesia + Composio + Recall.ai + React client-v2
**Railway Services**: `voice-agent-relay`, `livekit-voice-agent`, `Postgres`, `voice-agent-client`
**Client URL**: `voice-agent-client-production.up.railway.app` | **Commit**: `396764b` | **Branch**: `main`
**LLM**: Fireworks `deepseek-v3p1` (Cerebras removed 2026-02-20 — do not reference Cerebras)
**n8n Folder**: `jayconnorexe.app.n8n.cloud/projects/vaRklvnINMqrVVkS/folders/Pm4TxSTXoxmkGy6q`

### Changelog
- **v2.3.0** (2026-02-22): Updated LLM to Fireworks deepseek-v3p1; expanded Web Components for client-v2 (AgentEventBus, ToolCallPanel, 13-event system); added Composio SDK to External APIs; updated File Locations with client-v2 paths; added Railway service ID and live URL
- **v2.2.0** (2026-01-30): Initial release with Cerebras LLM (now removed)
