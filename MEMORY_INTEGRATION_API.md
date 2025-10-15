# Letta Memory Integration API Reference

Complete API documentation for the Letta memory integration with Claude Agent SDK.

## Installation

```python
from letta_client.memory import memory, memory_fetch, Letta
```

## Core Functions

### `memory()` - Context Manager

Automatic memory integration context manager.

```python
async with memory(
    agent: str = "letta_agent",
    client: Letta = None,
    auto_inject: bool = True
):
    # Your Claude SDK code here
```

**Parameters:**
- `agent` (str): Agent name for memory storage (default: "letta_agent")
- `client` (Letta): Optional Letta client instance (auto-creates if None)
- `auto_inject` (bool): Auto-inject memory into prompts (default: True)

**Behavior:**
- ✅ Captures user messages and assistant responses
- ✅ Batches messages into single API call per turn
- ✅ Auto-creates Letta client from `LETTA_API_KEY` env var
- ✅ Auto-creates agent if doesn't exist (non-blocking)
- ✅ Injects memory into system prompts (if `auto_inject=True`)

---

### `memory_fetch()` - Manual Memory Retrieval

Fetch and format memory for manual injection.

```python
memory_context: str = memory_fetch(
    agent: str = "letta_agent",
    client: Letta = None
)
```

**Parameters:**
- `agent` (str): Agent name to fetch memory from (default: "letta_agent")
- `client` (Letta): Optional Letta client instance (auto-creates if None)

**Returns:**
- `str`: Formatted memory string ready for injection into prompts
- Empty string if agent doesn't exist or has no memory

**Use Cases:**
- Conditional memory injection based on custom logic
- Periodic memory refresh instead of every request
- Inspecting memory before deciding to use it
- Multi-agent coordination (fetch from multiple agents)

---

### `memory_add()` - Manual Memory Addition

Manually add information to an agent's memory.

```python
success: bool = memory_add(
    content: str,
    agent: str = "letta_agent",
    client: Letta = None
)
```

**Parameters:**
- `content` (str): The content to add to memory
- `agent` (str): Agent name to add memory to (default: "letta_agent")
- `client` (Letta): Optional Letta client instance (auto-creates if None)

**Returns:**
- `bool`: True if successful, False otherwise

**Use Cases:**
- Manually inject user preferences or settings
- Add project context without conversation
- Pre-populate agent memory with background information
- Seed memory for testing or initialization

**Example:**
```python
memory_add(
    "Remember: I always prefer TypeScript and use trailing commas",
    agent="my_agent"
)
```

---

### `memory_query()` - Query Stored Memory

Ask questions about what's stored in an agent's memory.

```python
response: str = memory_query(
    query: str,
    agent: str = "letta_agent",
    client: Letta = None
)
```

**Parameters:**
- `query` (str): The question or query to ask
- `agent` (str): Agent name to query (default: "letta_agent")
- `client` (Letta): Optional Letta client instance (auto-creates if None)

**Returns:**
- `str`: The agent's response based on stored memory
- Empty string if agent doesn't exist or on error

**Use Cases:**
- Search for specific information in memory
- Verify what information has been stored
- Ask about previous conversations or context
- Audit or inspect agent knowledge

**Example:**
```python
response = memory_query(
    "What tasks are we currently working on?",
    agent="my_agent"
)
print(response)
```

---

## Usage Patterns

### 1. Zero-Config (Automatic)

```python
async with memory():
    # Everything automatic: client, agent, injection
    async for msg in query(prompt="Hello"):
        print(msg)
```

### 2. Custom Agent

```python
async with memory(agent="code_assistant"):
    # Separate memory space for different contexts
```

### 3. Local Letta Server

```python
letta = Letta(base_url="http://localhost:8283", token=None)

async with memory(client=letta):
    # Use local Letta instance
```

### 4. Capture-Only (Low Latency)

```python
async with memory(auto_inject=False):
    # ✅ Captures messages
    # ❌ Skips injection
    # ⚡ Lower latency
```

### 5. Manual Memory Control

```python
async with memory(auto_inject=False):
    # Fetch memory manually
    context = memory_fetch(agent="my_agent")

    # Inject based on your logic
    if should_inject:
        system_prompt = f"Assistant prompt\n\n{context}"
```

### 6. Periodic Refresh

```python
async with memory(auto_inject=False):
    turn_count = 0

    for query in queries:
        turn_count += 1

        # Fetch every 5 turns
        if turn_count % 5 == 1:
            context = memory_fetch(agent="my_agent")
            # Update prompt with fresh memory
```

### 7. Selective Injection

```python
async with memory(auto_inject=False):
    # Complex query - use memory
    context = memory_fetch()
    response = query(f"Complex: {context}")

    # Simple query - skip memory
    response = query("What's 2+2?")
```

### 8. Multi-Agent Coordination

```python
# Fetch from multiple agents
backend = memory_fetch(agent="backend_agent")
frontend = memory_fetch(agent="frontend_agent")

combined = f"Backend:\n{backend}\n\nFrontend:\n{frontend}"

async with memory(agent="coordinator"):
    # Use combined context
```

---

## Environment Variables

```bash
# Required for auto-client creation
LETTA_API_KEY=letta-your-api-key

# Optional - for Letta Cloud (default: api.letta.com)
LETTA_BASE_URL=https://your-letta-instance.com
```

---

## Performance Characteristics

### API Call Optimization

**Before optimization:**
- 2 API calls per conversation turn
  - 1 for user message
  - 1 for assistant message

**After optimization:**
- 1 API call per conversation turn
  - Both messages batched together
- **50% reduction in API calls**

### Latency Modes

| Mode | Memory Injection | Latency | Use Case |
|------|-----------------|---------|----------|
| `auto_inject=True` (default) | ✅ Automatic | Higher | Full memory persistence |
| `auto_inject=False` | ❌ Disabled | Lower | Capture-only, analytics |
| `memory_fetch()` manual | ⚙️ Manual | Flexible | Custom logic, periodic refresh |

---

## Error Handling

All errors are caught gracefully and logged. The integration never crashes your application.

**Scenarios handled:**
- ❌ No Letta client → Skips gracefully
- ❌ Agent doesn't exist → Creates automatically (non-blocking)
- ❌ No memory blocks → Empty injection (no error)
- ❌ API errors → Logged and continues
- ❌ Network errors → Logged and continues

---

## Advanced Features

### Non-Blocking Agent Creation

When agent doesn't exist:
1. Quick check (synchronous)
2. Background creation (non-blocking task)
3. Request proceeds immediately
4. Subsequent requests use the agent

### Message Batching

Messages are buffered and sent together:
```
User: "Hello"
Assistant: "Hi there!"
↓
Single API call with both messages
```

### Memory Format

Memory blocks are formatted as:
```markdown
### human
User name: Alice
User preferences: TypeScript, trailing commas

### persona
I am a helpful coding assistant

### conversation_log
user: Help me with TypeScript

assistant: I'd be happy to help!
```

---

## Best Practices

### ✅ Do

- Use descriptive agent names (`code_assistant`, not `agent1`)
- Set `LETTA_API_KEY` in environment variables
- Use `auto_inject=False` for latency-critical applications
- Use `memory_fetch()` for custom memory injection logic
- Create separate agents for different contexts

### ❌ Don't

- Don't commit API keys to version control
- Don't use the same agent for unrelated contexts
- Don't fetch memory on every turn if not needed
- Don't ignore return value of `memory_fetch()` (check for empty string)

---

## Examples

See `examples_memory_usage.py` for complete working examples of all patterns.

---

## Troubleshooting

### Memory not persisting?
- Check `LETTA_API_KEY` is set
- Verify agent exists: `memory_fetch()` to check
- Ensure messages are being captured (check logs)

### High latency?
- Use `auto_inject=False` for capture-only mode
- Use `memory_fetch()` with periodic refresh
- Consider async memory operations

### Agent not found?
- Agent is created automatically on first use
- Check Letta server is running (if using local)
- Verify agent name spelling

---

## Support

For issues or questions:
- GitHub: https://github.com/letta-ai/letta
- Discord: https://discord.gg/letta
- Docs: https://docs.letta.com
