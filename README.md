# Letta Python SDK

[![pypi](https://img.shields.io/pypi/v/letta-client)](https://pypi.python.org/pypi/letta-client)

Letta is the platform for building stateful agents: open AI with advanced memory that can learn and self-improve over time.

### Quicklinks:
* [**Developer Documentation**](https://docs.letta.com): Learn how to create agents using Python or TypeScript
* [**Python API Reference**](./reference.md): Complete Python SDK documentation
* [**Agent Development Environment (ADE)**](https://docs.letta.com/guides/ade/overview): A no-code UI for building stateful agents
* [**Letta Cloud**](https://app.letta.com/): The fastest way to try Letta

## Get started

Install the Letta Python SDK:

```bash
pip install letta-client
```

## Simple Hello World example

In the example below, we'll create a stateful agent with two memory blocks. We'll initialize the `human` memory block with incorrect information, and correct the agent in our first message - which will trigger the agent to update its own memory with a tool call.

*To run the examples, you'll need to get a `LETTA_API_KEY` from [Letta Cloud](https://app.letta.com/api-keys), or run your own self-hosted server (see [our guide](https://docs.letta.com/guides/selfhosting))*

```python
from letta_client import Letta

client = Letta(api_key="LETTA_API_KEY")
# client = Letta(base_url="http://localhost:8283")  # if self-hosting

agent_state = client.agents.create(
    model="openai/gpt-4o-mini",
    embedding="openai/text-embedding-3-small",
    memory_blocks=[
        {
            "label": "human",
            "value": "The human's name is Chad. They like vibe coding."
        },
        {
            "label": "persona",
            "value": "My name is Sam, a helpful assistant."
        }
    ],
    tools=["web_search", "run_code"]
)

print(agent_state.id)
# agent-d9be...0846

response = client.agents.messages.create(
    agent_id=agent_state.id,
    messages=[
        {
            "role": "user",
            "content": "Hey, nice to meet you, my name is Brad."
        }
    ]
)

# the agent will think, then edit its memory using a tool
for message in response.messages:
    print(message)

# The content of this memory block will be something like
# "The human's name is Brad. They like vibe coding."
# Fetch this block's content with:
human_block = client.agents.blocks.retrieve(agent_id=agent_state.id, block_label="human")
print(human_block.value)
```

## Core concepts in Letta:

Letta is built on the [MemGPT](https://arxiv.org/abs/2310.08560) research paper, which introduced the concept of the "LLM Operating System" for memory management:

1. [**Memory Hierarchy**](https://docs.letta.com/guides/agents/memory): Agents have self-editing memory split between in-context and out-of-context memory
2. [**Memory Blocks**](https://docs.letta.com/guides/agents/memory-blocks): In-context memory is composed of persistent editable blocks
3. [**Agentic Context Engineering**](https://docs.letta.com/guides/agents/context-engineering): Agents control their context window using tools to edit, delete, or search memory
4. [**Perpetual Self-Improving Agents**](https://docs.letta.com/guides/agents/overview): Every agent has a perpetual (infinite) message history

## Local Development

Connect to a local Letta server instead of the cloud:

```python
from letta_client import Letta

client = Letta(base_url="http://localhost:8283")
```

Run Letta locally with Docker:

```bash
docker run \
  -v ~/.letta/.persist/pgdata:/var/lib/postgresql/data \
  -p 8283:8283 \
  -e OPENAI_API_KEY="your_key" \
  letta/letta:latest
```

See the [self-hosting guide](https://docs.letta.com/guides/selfhosting) for more options.

## Key Features

### Memory Management ([full guide](https://docs.letta.com/guides/agents/memory-blocks))

Memory blocks are persistent, editable sections of an agent's context window:

```python
# Create agent with memory blocks
agent = client.agents.create(
    memory_blocks=[
        {"label": "persona", "value": "I'm a helpful assistant."},
        {"label": "human", "value": "User preferences and info."}
    ]
)

# Update blocks manually
client.agents.blocks.update(
    agent_id=agent.id,
    block_label="human",
    value="Updated user information"
)

# Retrieve a block
block = client.agents.blocks.retrieve(agent_id=agent.id, block_label="human")
```

### Multi-agent Shared Memory ([full guide](https://docs.letta.com/guides/agents/multi-agent-shared-memory))

Memory blocks can be attached to multiple agents. All agents will have an up-to-date view on the contents of the memory block -- if one agent modifies it, the other will see it immediately.

Here is how to attach a single memory block to multiple agents:

```python
# Create shared block
shared_block = client.blocks.create(
    label="organization",
    value="Shared team context"
)

# Attach to multiple agents
agent1 = client.agents.create(
    memory_blocks=[{"label": "persona", "value": "I am a supervisor"}],
    block_ids=[shared_block.id]
)

agent2 = client.agents.create(
    memory_blocks=[{"label": "persona", "value": "I am a worker"}],
    block_ids=[shared_block.id]
)
```

### Sleep-time Agents ([full guide](https://docs.letta.com/guides/agents/architectures/sleeptime))

Background agents that share memory with your primary agent:

```python
agent = client.agents.create(
    model="openai/gpt-4o-mini",
    enable_sleeptime=True  # creates a sleep-time agent
)
```

### Agent File Import/Export ([full guide](https://docs.letta.com/guides/agents/agent-file))

Save and share agents with the `.af` file format:

```python
# Import agent
with open('/path/to/agent.af', 'rb') as f:
    agent = client.agents.import_file(file=f)

# Export agent
schema = client.agents.export_file(agent_id=agent.id)
```

### MCP Tools ([full guide](https://docs.letta.com/guides/mcp/overview))

Connect to Model Context Protocol servers:

```python
# First, create an MCP server (example: weather server)
weather_server = client.mcp_servers.create(
    server_name="weather-server",
    config={
        "mcp_server_type": "streamable_http",
        "server_url": "https://weather-mcp.example.com/mcp",
    }
)

# List tools available from the MCP server
tools = client.mcp_servers.tools.list(weather_server.id)

# Create agent with MCP tool
agent = client.agents.create(
    model="openai/gpt-4o-mini",
    tool_ids=[tool.id]
)
```

### Filesystem ([full guide](https://docs.letta.com/guides/agents/filesystem))

Give agents access to files:

```python
# Get an available embedding config
embedding_configs = client.models.embeddings.list()

# Create folder and upload file
folder = client.folders.create(
    name="my_folder",
    embedding_config=embedding_configs[0]
)
with open("file.txt", "rb") as f:
    client.folders.files.upload(file=f, folder_id=folder.id)

# Attach to agent
client.agents.folders.attach(agent_id=agent.id, folder_id=folder.id)
```

### Long-running Agents ([full guide](https://docs.letta.com/guides/agents/long-running))

Background execution with resumable streaming:

```python
stream = client.agents.messages.stream(
    agent_id=agent.id,
    messages=[{"role": "user", "content": "Analyze this dataset"}],
    background=True
)

run_id = None
last_seq_id = None
for chunk in stream:
    run_id = chunk.run_id
    last_seq_id = chunk.seq_id

# Resume if disconnected
for chunk in client.runs.stream(run_id=run_id, starting_after=last_seq_id):
    print(chunk)
```

### Streaming ([full guide](https://docs.letta.com/guides/agents/streaming))

Stream responses in real-time:

```python
stream = client.agents.messages.stream(
    agent_id=agent.id,
    messages=[{"role": "user", "content": "Hello!"}]
)

for chunk in stream:
    print(chunk)
```

### Message Types ([full guide](https://docs.letta.com/guides/agents/message-types))

Agent responses contain different message types. Handle them with the `message_type` discriminator:

```python
messages = client.agents.messages.list(agent_id=agent.id)

for message in messages:
    if message.message_type == "user_message":
        print(f"User: {message.content}")
    elif message.message_type == "assistant_message":
        print(f"Agent: {message.content}")
    elif message.message_type == "reasoning_message":
        print(f"Reasoning: {message.reasoning}")
    elif message.message_type == "tool_call_message":
        print(f"Tool: {message.tool_call.name}")
    elif message.message_type == "tool_return_message":
        print(f"Result: {message.tool_return}")
```

## Python Support

Full type hints and async support:

```python
from letta_client import Letta
from letta_client.types import CreateAgentRequest

# Sync client
client = Letta(token="LETTA_API_KEY")

# Async client
from letta_client import AsyncLetta

async_client = AsyncLetta(token="LETTA_API_KEY")
agent = await async_client.agents.create(
    model="openai/gpt-4o-mini",
    memory_blocks=[...]
)
```

## Error Handling

```python
from letta_client.core.api_error import ApiError

try:
    client.agents.messages.create(agent_id=agent_id, messages=[...])
except ApiError as e:
    print(e.status_code)
    print(e.message)
    print(e.body)
```

## Advanced Configuration

### Retries

```python
response = client.agents.create(
    {...},
    request_options={"max_retries": 3}  # Default: 2
)
```

### Timeouts

```python
response = client.agents.create(
    {...},
    request_options={"timeout_in_seconds": 30}  # Default: 60
)
```

### Custom Headers

```python
response = client.agents.create(
    {...},
    request_options={
        "additional_headers": {
            "X-Custom-Header": "value"
        }
    }
)
```

### Raw Response Access

```python
response = client.agents.with_raw_response.create({...})

print(response.headers["X-My-Header"])
print(response.data)  # access the underlying object
```

### Custom HTTP Client

```python
import httpx
from letta_client import Letta

client = Letta(
    httpx_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    )
)
```

## Runtime Compatibility

Works with:
- Python 3.8+
- Supports async/await
- Compatible with type checkers (mypy, pyright)

## Contributing

Letta is an open source project built by over a hundred contributors. There are many ways to get involved in the Letta OSS project!

* [**Join the Discord**](https://discord.gg/letta): Chat with the Letta devs and other AI developers.
* [**Chat on our forum**](https://forum.letta.com/): If you're not into Discord, check out our developer forum.
* **Follow our socials**: [Twitter/X](https://twitter.com/Letta_AI), [LinkedIn](https://www.linkedin.com/company/letta-ai/), [YouTube](https://www.youtube.com/@letta-ai)

This SDK is generated programmatically. For SDK changes, please [open an issue](https://github.com/letta-ai/letta-python/issues).

README contributions are always welcome!

## Resources

- [Documentation](https://docs.letta.com)
- [Python API Reference](./reference.md)
- [Example Applications](https://github.com/letta-ai/letta-chatbot-example)

## License

MIT

---

***Legal notices**: By using Letta and related Letta services (such as the Letta endpoint or hosted service), you are agreeing to our [privacy policy](https://www.letta.com/privacy-policy) and [terms of service](https://www.letta.com/terms-of-service).*