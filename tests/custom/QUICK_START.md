# Letta Memory Integration - Quick Start

## 🎉 All Four Major SDKs Supported!

```
┌─────────────────────────────────────────────────────────────────┐
│                    Letta Memory Integration                      │
│                 Automatic Memory for All SDKs                    │
└─────────────────────────────────────────────────────────────────┘
                                │
                ┌───────────────┼───────────────┐
                │               │               │
                ▼               ▼               ▼
    ┌───────────────┐  ┌───────────────┐  ┌───────────────┐
    │  Claude Agent │  │   Anthropic   │  │    OpenAI     │
    │      SDK      │  │      SDK      │  │      SDK      │
    └───────────────┘  └───────────────┘  └───────────────┘
                │               │               │
                └───────────────┼───────────────┘
                                │
                                ▼
                        ┌───────────────┐
                        │    Gemini     │
                        │      SDK      │
                        └───────────────┘
                                │
                                ▼
                    ✅ Memory Just Works!
```

## Installation

```bash
# Install your preferred SDK(s)
pip install anthropic          # For Anthropic SDK
pip install openai             # For OpenAI SDK
pip install google-generativeai  # For Gemini SDK
pip install claude-agent-sdk   # For Claude Agent SDK
```

## Usage (Universal Pattern)

```python
from letta_client.memory import memory
from letta_client.client import Letta

# Connect to Letta
letta = Letta(base_url="http://localhost:8283", token=None)

# Wrap ANY SDK call in a memory context
async with memory(agent="my_agent", client=letta):
    # Memory automatically works for ALL supported SDKs!
    response = await your_sdk.some_method(...)
```

## SDK-Specific Examples

### Anthropic SDK

```python
from anthropic import AsyncAnthropic

anthropic = AsyncAnthropic(api_key="sk-...")

# Session 1: Introduce yourself
async with memory(agent="assistant", client=letta):
    response = await anthropic.messages.create(
        model="claude-3-5-sonnet-20241022",
        messages=[{"role": "user", "content": "My name is Alice"}]
    )

# Session 2: It remembers!
async with memory(agent="assistant", client=letta):
    response = await anthropic.messages.create(
        model="claude-3-5-sonnet-20241022",
        messages=[{"role": "user", "content": "What is my name?"}]
    )
    # Response: "Your name is Alice!"
```

### OpenAI SDK

```python
from openai import AsyncOpenAI

openai = AsyncOpenAI(api_key="sk-...")

async with memory(agent="assistant", client=letta):
    response = await openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "My name is Bob"}]
    )
```

### Gemini SDK

```python
import google.generativeai as genai

genai.configure(api_key="...")
model = genai.GenerativeModel('gemini-2.5-flash')

async with memory(agent="assistant", client=letta):
    response = await model.generate_content_async("My name is Charlie")
```

### Claude Agent SDK

```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

options = ClaudeAgentOptions(allowed_tools=["Read", "Write"])
client = ClaudeSDKClient(options)

async with memory(agent="assistant", client=letta):
    await client.connect()
    await client.query("My name is David")
    # ... receive responses ...
    await client.disconnect()
```

## Streaming Support

All SDKs support streaming with automatic memory capture:

```python
# Works with streaming for ALL SDKs!
async with memory(agent="assistant", client=letta):
    stream = await client.create_streaming_request(...)

    async for chunk in stream:
        print(chunk.text, end="", flush=True)

    # Memory automatically captured when stream completes!
```

## Features

✅ **Zero Configuration** - Just wrap your code in `memory()`  
✅ **Auto-Detection** - Automatically detects installed SDKs  
✅ **Cross-Session** - Memory persists across sessions  
✅ **Streaming** - Works with streaming responses  
✅ **Multi-SDK** - Use different SDKs with same agent  
✅ **Production Ready** - Error handling, logging, optimizations  

## Test Your Implementation

```bash
# Anthropic
export ANTHROPIC_API_KEY="your-key"
python tests/custom/test_anthropic_interception.py

# OpenAI
export OPENAI_API_KEY="your-key"
python tests/custom/test_openai_interception.py

# Gemini
export GOOGLE_API_KEY="your-key"
python tests/custom/test_gemini_interception.py
```

## What You Get

```
🎯 Session 1: "My name is Alice"
✅ Captured: user + assistant messages
💾 Saved to: Letta agent memory

🎯 Session 2: "What is my name?"
✅ Injected: Previous context from Letta
💬 Response: "Your name is Alice!"
```

## Advanced Options

### Capture-Only Mode

Skip automatic memory injection (reduces latency):

```python
async with memory(agent="assistant", client=letta, capture_only=True):
    # Only captures conversation, doesn't inject memory
    response = await client.some_method(...)
```

### Manual Registration

Register interceptors at startup instead of on-demand:

```python
from letta_client.memory import register

# Register all available SDKs
register()

# Or register specific SDKs
register(providers=["anthropic", "openai"])
```

## Support Matrix

| SDK | Non-Streaming | Streaming | Auto-Detect | Status |
|-----|---------------|-----------|-------------|--------|
| Claude Agent SDK | ✅ | ✅ | ✅ | Complete |
| Anthropic SDK | ✅ | ✅ | ✅ | Complete |
| OpenAI SDK | ✅ | ✅ | ✅ | Complete |
| Gemini SDK | ✅ | ✅ | ✅ | Complete |

## Documentation

- [Integration Summary](./INTEGRATION_SUMMARY.md)
- [All SDKs Summary](./ALL_SDKS_SUMMARY.md)
- [Anthropic Test](./test_anthropic_interception.py)
- [OpenAI Test](./test_openai_interception.py)
- [Gemini Test](./test_gemini_interception.py)
- [Gemini Implementation](./GEMINI_IMPLEMENTATION_SUMMARY.md)

## Questions?

Check the comprehensive documentation or test files for examples!

---

**That's it! Memory integration in one line of code.** ✨
