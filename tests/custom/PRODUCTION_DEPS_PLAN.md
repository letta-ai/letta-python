# Production Dependencies Plan

## Current State (Temporary)

For development convenience, all SDKs are currently listed as required dependencies in `pyproject.toml`:

```toml
[tool.poetry.dependencies]
anthropic = ">=0.64.0"
openai = ">=1.102.0"
google-generativeai = ">=0.8.0"
```

**⚠️ This is temporary and should be changed before production!**

## Production Structure (Recommended)

SDKs should be **optional dependencies** (extras) since users typically only need one SDK:

### Option 1: Poetry Extras (Recommended)

```toml
[tool.poetry.dependencies]
python = "^3.8"
httpx = ">=0.21.2"
httpx-sse = "0.4.0"
pydantic = ">= 1.9.2"
pydantic-core = ">=2.18.2"
typing_extensions = ">= 4.0.0"

# SDKs are optional - users choose which to install
anthropic = { version = ">=0.64.0", optional = true }
openai = { version = ">=1.102.0", optional = true }
google-generativeai = { version = ">=0.8.0", optional = true }
claude-agent-sdk = { version = ">=0.1.0", optional = true }

[tool.poetry.extras]
anthropic = ["anthropic"]
openai = ["openai"]
gemini = ["google-generativeai"]
claude = ["claude-agent-sdk"]
all = ["anthropic", "openai", "google-generativeai", "claude-agent-sdk"]
```

### Installation Examples

Users would install like this:

```bash
# Install with Anthropic SDK support
pip install letta-client[anthropic]

# Install with OpenAI SDK support
pip install letta-client[openai]

# Install with Gemini SDK support
pip install letta-client[gemini]

# Install with multiple SDKs
pip install letta-client[anthropic,openai]

# Install with all SDKs
pip install letta-client[all]

# Install base package only (no SDKs)
pip install letta-client
```

### Option 2: Separate Optional Groups

```toml
[tool.poetry.group.anthropic]
optional = true

[tool.poetry.group.anthropic.dependencies]
anthropic = ">=0.64.0"

[tool.poetry.group.openai]
optional = true

[tool.poetry.group.openai.dependencies]
openai = ">=1.102.0"

[tool.poetry.group.gemini]
optional = true

[tool.poetry.group.gemini.dependencies]
google-generativeai = ">=0.8.0"

[tool.poetry.group.claude]
optional = true

[tool.poetry.group.claude.dependencies]
claude-agent-sdk = ">=0.1.0"
```

Installation:

```bash
poetry install --with anthropic
poetry install --with openai,gemini
poetry install --with all
```

## Rationale

### Why Optional Dependencies?

1. **Smaller install size** - Users only install what they need
2. **Faster installation** - Fewer packages to download
3. **Fewer conflicts** - Less chance of version conflicts
4. **Clearer intent** - Users explicitly choose which SDKs to use
5. **Better packaging** - Standard practice for multi-backend libraries

### Why Not Required?

1. **Not all users need all SDKs** - Most use only 1-2 SDKs
2. **Large dependencies** - Each SDK adds 20-50MB
3. **Version constraints** - SDKs have their own dependency trees
4. **Development overhead** - Harder to maintain compatibility with all SDKs

### Comparison: Other Libraries

Many popular libraries use optional dependencies:

**LangChain**:
```bash
pip install langchain[openai]
pip install langchain[anthropic]
```

**LlamaIndex**:
```bash
pip install llama-index[anthropic]
pip install llama-index[openai]
```

**Haystack**:
```bash
pip install haystack[openai]
pip install haystack[anthropic]
```

## Implementation Checklist

Before production release:

- [ ] Remove SDKs from required dependencies
- [ ] Add SDKs as optional dependencies
- [ ] Define extras in `[tool.poetry.extras]`
- [ ] Update README with installation examples
- [ ] Update documentation
- [ ] Test installation with each extra:
  - [ ] `pip install .[anthropic]`
  - [ ] `pip install .[openai]`
  - [ ] `pip install .[gemini]`
  - [ ] `pip install .[claude]`
  - [ ] `pip install .[all]`
- [ ] Test that imports work without extras (should gracefully skip)
- [ ] Update CI/CD to test with different extras
- [ ] Add migration guide for existing users

## Testing Strategy

### Test Matrix

Test that memory integration works with:

| Installation | Anthropic | OpenAI | Gemini | Claude |
|--------------|-----------|--------|--------|--------|
| Base only | Skip | Skip | Skip | Skip |
| `[anthropic]` | ✅ | Skip | Skip | Skip |
| `[openai]` | Skip | ✅ | Skip | Skip |
| `[gemini]` | Skip | Skip | ✅ | Skip |
| `[claude]` | Skip | Skip | Skip | ✅ |
| `[all]` | ✅ | ✅ | ✅ | ✅ |

### Graceful Degradation

The library should handle missing SDKs gracefully:

```python
# User has only OpenAI installed
from letta_client.memory import memory
from openai import AsyncOpenAI

# This works
async with memory(agent="test", client=letta):
    await openai_client.chat.completions.create(...)

# This gracefully skips (no Anthropic installed)
from anthropic import AsyncAnthropic  # ImportError
```

## Documentation Updates Needed

1. **README.md**
   - Add installation section with extras
   - Show examples for each SDK

2. **docs/installation.md**
   - Detailed installation instructions
   - Explain why extras are used

3. **docs/quickstart.md**
   - Update examples to show correct installation
   - Add "Prerequisites" section

4. **Contributing Guide**
   - How to install all extras for development
   - Testing with different configurations

## Migration Path

For users upgrading from temp version to production version:

### Before (Temporary)
```bash
pip install letta-client
# Gets all SDKs automatically
```

### After (Production)
```bash
# Choose which SDKs you need
pip install letta-client[anthropic,openai]
```

### Communication

In release notes:

```markdown
## Breaking Change: SDK Dependencies

SDKs are now optional dependencies. Install with extras:

- `pip install letta-client[anthropic]` for Anthropic SDK
- `pip install letta-client[openai]` for OpenAI SDK
- `pip install letta-client[gemini]` for Gemini SDK
- `pip install letta-client[all]` for all SDKs

See [installation guide](docs/installation.md) for details.
```

## Timeline

1. **Now (Development)**: Keep as required dependencies for convenience
2. **Before PR**: Move to optional dependencies
3. **Before Release**: Test all installation combinations
4. **Release**: Update docs and announce changes

## Summary

- ✅ **Current**: All SDKs required (temporary)
- 🎯 **Production**: SDKs as optional extras
- 📦 **Benefit**: Smaller installs, faster, fewer conflicts
- 📚 **Pattern**: Industry standard (LangChain, LlamaIndex, etc.)
