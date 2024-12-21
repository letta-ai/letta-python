# Reference
## Tools
<details><summary><code>client.tools.<a href="src/letta/tools/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a tool by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.tools.get(
    tool_id="tool_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tool_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/letta/tools/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a tool by name
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.tools.delete(
    tool_id="tool_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tool_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/letta/tools/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing tool
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.tools.update(
    tool_id="tool_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tool_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the tool.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the function.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Metadata tags.
    
</dd>
</dl>

<dl>
<dd>

**module:** `typing.Optional[str]` — The source code of the function.
    
</dd>
</dl>

<dl>
<dd>

**source_code:** `typing.Optional[str]` — The source code of the function.
    
</dd>
</dl>

<dl>
<dd>

**source_type:** `typing.Optional[str]` — The type of the source code.
    
</dd>
</dl>

<dl>
<dd>

**json_schema:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The JSON schema of the function (auto-generated from source_code if not provided)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/letta/tools/client.py">get_by_name</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a tool ID by name
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.tools.get_by_name(
    tool_name="tool_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/letta/tools/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all tools available to agents belonging to the org of the user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.tools.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/letta/tools/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new tool
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.tools.create(
    source_code="source_code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_code:** `str` — The source code of the function.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the function (auto-generated from source_code if not provided).
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the tool.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Metadata tags.
    
</dd>
</dl>

<dl>
<dd>

**module:** `typing.Optional[str]` — The source code of the function.
    
</dd>
</dl>

<dl>
<dd>

**source_type:** `typing.Optional[str]` — The source type of the function.
    
</dd>
</dl>

<dl>
<dd>

**json_schema:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The JSON schema of the function (auto-generated from source_code if not provided)
    
</dd>
</dl>

<dl>
<dd>

**return_char_limit:** `typing.Optional[int]` — The maximum number of characters in the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/letta/tools/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update a tool
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.tools.upsert(
    source_code="source_code",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_code:** `str` — The source code of the function.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the function (auto-generated from source_code if not provided).
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the tool.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Metadata tags.
    
</dd>
</dl>

<dl>
<dd>

**module:** `typing.Optional[str]` — The source code of the function.
    
</dd>
</dl>

<dl>
<dd>

**source_type:** `typing.Optional[str]` — The source type of the function.
    
</dd>
</dl>

<dl>
<dd>

**json_schema:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The JSON schema of the function (auto-generated from source_code if not provided)
    
</dd>
</dl>

<dl>
<dd>

**return_char_limit:** `typing.Optional[int]` — The maximum number of characters in the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/letta/tools/client.py">add_base_tool</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upsert base tools
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.tools.add_base_tool()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/letta/tools/client.py">run_tool_from_source</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attempt to build a tool from source, then run it on the provided arguments
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.tools.run_tool_from_source(
    source_code="source_code",
    args="args",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_code:** `str` — The source code of the function.
    
</dd>
</dl>

<dl>
<dd>

**args:** `str` — The arguments to pass to the tool (as stringified JSON).
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the tool to run.
    
</dd>
</dl>

<dl>
<dd>

**source_type:** `typing.Optional[str]` — The type of the source code.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/letta/tools/client.py">list_composio_apps</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all Composio apps
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.tools.list_composio_apps()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/letta/tools/client.py">list_composio_actions_by_app</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all Composio actions for a specific app
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.tools.list_composio_actions_by_app(
    composio_app_name="composio_app_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**composio_app_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/letta/tools/client.py">add_composio_tool</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new Composio tool by action name (Composio refers to each tool as an `Action`)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.tools.add_composio_tool(
    composio_action_name="composio_action_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**composio_action_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sources
<details><summary><code>client.sources.<a href="src/letta/sources/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all sources
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.sources.get(
    source_id="source_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sources.<a href="src/letta/sources/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a data source.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.sources.delete(
    source_id="source_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sources.<a href="src/letta/sources/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the name or documentation of an existing data source.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.sources.update(
    source_id="source_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the source.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the source.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Metadata associated with the source.
    
</dd>
</dl>

<dl>
<dd>

**embedding_config:** `typing.Optional[EmbeddingConfig]` — The embedding configuration used by the source.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sources.<a href="src/letta/sources/client.py">get_by_name</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a source by name
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.sources.get_by_name(
    source_name="source_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sources.<a href="src/letta/sources/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all data sources created by a user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.sources.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sources.<a href="src/letta/sources/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new data source.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.sources.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the source.
    
</dd>
</dl>

<dl>
<dd>

**embedding_config:** `typing.Optional[EmbeddingConfig]` — The embedding configuration used by the source.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the source.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Metadata associated with the source.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sources.<a href="src/letta/sources/client.py">attach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach a data source to an existing agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.sources.attach(
    source_id="source_id",
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `str` — The unique identifier of the agent to attach the source to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sources.<a href="src/letta/sources/client.py">detach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach a data source from an existing agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.sources.detach(
    source_id="source_id",
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `str` — The unique identifier of the agent to detach the source from.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agents
<details><summary><code>client.agents.<a href="src/letta/agents/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all agents associated with a given user.
This endpoint retrieves a list of all agents and their configurations associated with the specified user ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the agent
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List of tags to filter agents by
    
</dd>
</dl>

<dl>
<dd>

**match_all_tags:** `typing.Optional[bool]` — If True, only returns agents that match ALL given tags. Otherwise, return agents that have ANY of the passed in tags.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/letta/agents/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new agent with the specified configuration.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import CreateBlock, Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.create(
    memory_blocks=[
        CreateBlock(
            value="value",
            label="label",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**memory_blocks:** `typing.Sequence[CreateBlock]` — The blocks to create in the agent's in-context memory.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the agent.
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.Sequence[str]]` — The tools used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**tool_ids:** `typing.Optional[typing.Sequence[str]]` — The ids of the tools used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**source_ids:** `typing.Optional[typing.Sequence[str]]` — The ids of the sources used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**block_ids:** `typing.Optional[typing.Sequence[str]]` — The ids of the blocks used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**tool_rules:** `typing.Optional[typing.Sequence[CreateAgentRequestToolRulesItem]]` — The tool rules governing the agent.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — The tags associated with the agent.
    
</dd>
</dl>

<dl>
<dd>

**system:** `typing.Optional[str]` — The system prompt used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**agent_type:** `typing.Optional[AgentType]` — The type of agent.
    
</dd>
</dl>

<dl>
<dd>

**llm_config:** `typing.Optional[LlmConfig]` — The LLM configuration used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**embedding_config:** `typing.Optional[EmbeddingConfig]` — The embedding configuration used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**initial_message_sequence:** `typing.Optional[typing.Sequence[MessageCreate]]` — The initial set of messages to put in the agent's in-context memory.
    
</dd>
</dl>

<dl>
<dd>

**include_base_tools:** `typing.Optional[bool]` — The LLM configuration used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the agent.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The metadata of the agent.
    
</dd>
</dl>

<dl>
<dd>

**llm:** `typing.Optional[str]` — The LLM configuration handle used by the agent, specified in the format provider/model-name, as an alternative to specifying llm_config.
    
</dd>
</dl>

<dl>
<dd>

**embedding:** `typing.Optional[str]` — The embedding configuration handle used by the agent, specified in the format provider/model-name.
    
</dd>
</dl>

<dl>
<dd>

**context_window_limit:** `typing.Optional[int]` — The context window limit used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**embedding_chunk_size:** `typing.Optional[int]` — The embedding chunk size used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/letta/agents/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the state of the agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.get(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/letta/agents/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.delete(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/letta/agents/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an exsiting agent
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.update(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the agent.
    
</dd>
</dl>

<dl>
<dd>

**tool_ids:** `typing.Optional[typing.Sequence[str]]` — The ids of the tools used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**source_ids:** `typing.Optional[typing.Sequence[str]]` — The ids of the sources used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**block_ids:** `typing.Optional[typing.Sequence[str]]` — The ids of the blocks used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — The tags associated with the agent.
    
</dd>
</dl>

<dl>
<dd>

**system:** `typing.Optional[str]` — The system prompt used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**tool_rules:** `typing.Optional[typing.Sequence[UpdateAgentToolRulesItem]]` — The tool rules governing the agent.
    
</dd>
</dl>

<dl>
<dd>

**llm_config:** `typing.Optional[LlmConfig]` — The LLM configuration used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**embedding_config:** `typing.Optional[EmbeddingConfig]` — The embedding configuration used by the agent.
    
</dd>
</dl>

<dl>
<dd>

**message_ids:** `typing.Optional[typing.Sequence[str]]` — The ids of the messages in the agent's in-context memory.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The description of the agent.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The metadata of the agent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/letta/agents/client.py">get_agent_memory_block</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a memory block from an agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.get_agent_memory_block(
    agent_id="agent_id",
    block_label="block_label",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**block_label:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/letta/agents/client.py">update_agent_memory_block_by_label</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a memory block from an agent by unlnking it. If the block is not linked to any other agent, it is deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.update_agent_memory_block_by_label(
    agent_id="agent_id",
    block_label="block_label",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**block_label:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` — Value of the block.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Character limit of the block.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the block if it is a template.
    
</dd>
</dl>

<dl>
<dd>

**is_template:** `typing.Optional[bool]` — Whether the block is a template (e.g. saved human/persona options).
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Label of the block (e.g. 'human', 'persona') in the context window.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the block.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Metadata of the block.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/letta/agents/client.py">get_agent_memory_blocks</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the memory blocks of a specific agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.get_agent_memory_blocks(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/letta/agents/client.py">create_agent_message_async</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Asynchronously process a user message and return a job ID.
The actual processing happens in the background, and the status can be checked using the job ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta, MessageCreate

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.create_agent_message_async(
    agent_id="agent_id",
    messages=[
        MessageCreate(
            role="user",
            text="text",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Sequence[MessageCreate]` — The messages to be sent to the agent.
    
</dd>
</dl>

<dl>
<dd>

**assistant_message_tool_name:** `typing.Optional[str]` — The name of the designated message tool.
    
</dd>
</dl>

<dl>
<dd>

**assistant_message_tool_kwarg:** `typing.Optional[str]` — The name of the message argument in the designated message tool.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/letta/agents/client.py">create_version</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a versioned version of an agent
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.create_version(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` — The agent ID of the agent to migrate, if this agent is not a template, it will create a agent template from the agent provided as well
    
</dd>
</dl>

<dl>
<dd>

**return_agent_id:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**migrate_deployed_agents:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.<a href="src/letta/agents/client.py">migrate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Migrate an agent to a new versioned agent template
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.migrate(
    agent_id="agent_id",
    to_template="to_template",
    preserve_core_memories=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**to_template:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**preserve_core_memories:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, str]]` — If you chose to not preserve core memories, you should provide the new variables for the core memories
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Models
<details><summary><code>client.models.<a href="src/letta/models/client.py">list_llms</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.models.list_llms()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/letta/models/client.py">list_embedding_models</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.models.list_embedding_models()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Blocks
<details><summary><code>client.blocks.<a href="src/letta/blocks/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.blocks.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**label:** `typing.Optional[str]` — Labels to include (e.g. human, persona)
    
</dd>
</dl>

<dl>
<dd>

**templates_only:** `typing.Optional[bool]` — Whether to include only templates
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the block
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blocks.<a href="src/letta/blocks/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.blocks.create(
    value="value",
    label="label",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**value:** `str` — Value of the block.
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` — Label of the block.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Character limit of the block.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the block if it is a template.
    
</dd>
</dl>

<dl>
<dd>

**is_template:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the block.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Metadata of the block.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blocks.<a href="src/letta/blocks/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.blocks.get(
    block_id="block_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**block_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blocks.<a href="src/letta/blocks/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.blocks.delete(
    block_id="block_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**block_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blocks.<a href="src/letta/blocks/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.blocks.update(
    block_id="block_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**block_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` — Value of the block.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Character limit of the block.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the block if it is a template.
    
</dd>
</dl>

<dl>
<dd>

**is_template:** `typing.Optional[bool]` — Whether the block is a template (e.g. saved human/persona options).
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Label of the block (e.g. 'human', 'persona') in the context window.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the block.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Metadata of the block.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blocks.<a href="src/letta/blocks/client.py">link_agent_memory_block</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Link a memory block to an agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.blocks.link_agent_memory_block(
    block_id="block_id",
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**block_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `str` — The unique identifier of the agent to attach the source to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blocks.<a href="src/letta/blocks/client.py">unlink_agent_memory_block</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unlink a memory block from an agent
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.blocks.unlink_agent_memory_block(
    block_id="block_id",
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**block_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `str` — The unique identifier of the agent to attach the source to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Jobs
<details><summary><code>client.jobs.<a href="src/letta/jobs/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all jobs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.jobs.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `typing.Optional[str]` — Only list jobs associated with the source.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/letta/jobs/client.py">list_active</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all active jobs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.jobs.list_active()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/letta/jobs/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of a job.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.jobs.get(
    job_id="job_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/letta/jobs/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a job by its job_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.jobs.delete(
    job_id="job_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Health
<details><summary><code>client.health.<a href="src/letta/health/client.py">check</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.health.check()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agents Context
<details><summary><code>client.agents.context.<a href="src/letta/agents/context/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the context window of a specific agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.context.get(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agents Tools
<details><summary><code>client.agents.tools.<a href="src/letta/agents/tools/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get tools from an existing agent
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.tools.list(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.tools.<a href="src/letta/agents/tools/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add tools to an existing agent
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.tools.add(
    agent_id="agent_id",
    tool_id="tool_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tool_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.tools.<a href="src/letta/agents/tools/client.py">remove</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add tools to an existing agent
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.tools.remove(
    agent_id="agent_id",
    tool_id="tool_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tool_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agents Sources
<details><summary><code>client.agents.sources.<a href="src/letta/agents/sources/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the sources associated with an agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.sources.get(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agents Memory
<details><summary><code>client.agents.memory.<a href="src/letta/agents/memory/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the memory state of a specific agent.
This endpoint fetches the current memory state of the agent identified by the user ID and agent ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.memory.get(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agents MemoryBlocks
<details><summary><code>client.agents.memory_blocks.<a href="src/letta/agents/memory_blocks/client.py">remove</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a memory block from an agent by unlnking it. If the block is not linked to any other agent, it is deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.memory_blocks.remove(
    agent_id="agent_id",
    block_label="block_label",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**block_label:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.memory_blocks.<a href="src/letta/agents/memory_blocks/client.py">add</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a memory block and links it to the agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.memory_blocks.add(
    agent_id="agent_id",
    value="value",
    label="label",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` — Value of the block.
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` — Label of the block.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Character limit of the block.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the block if it is a template.
    
</dd>
</dl>

<dl>
<dd>

**is_template:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the block.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Metadata of the block.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agents RecallMemory
<details><summary><code>client.agents.recall_memory.<a href="src/letta/agents/recall_memory/client.py">get_summary</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the summary of the recall memory of a specific agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.recall_memory.get_summary(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agents ArchivalMemory
<details><summary><code>client.agents.archival_memory.<a href="src/letta/agents/archival_memory/client.py">get_summary</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the summary of the archival memory of a specific agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.archival_memory.get_summary(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.archival_memory.<a href="src/letta/agents/archival_memory/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the memories in an agent's archival memory store (paginated query).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.archival_memory.list(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[int]` — Unique ID of the memory to start the query range at.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[int]` — Unique ID of the memory to end the query range at.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — How many results to include in the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.archival_memory.<a href="src/letta/agents/archival_memory/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Insert a memory into an agent's archival memory store.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.archival_memory.create(
    agent_id="agent_id",
    text="text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Text to write to archival memory.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.archival_memory.<a href="src/letta/agents/archival_memory/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a memory from an agent's archival memory store.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.archival_memory.delete(
    agent_id="agent_id",
    memory_id="memory_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**memory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agents Messages
<details><summary><code>client.agents.messages.<a href="src/letta/agents/messages/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve message history for an agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.messages.list(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Message before which to retrieve the returned messages.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**msg_object:** `typing.Optional[bool]` — If true, returns Message objects. If false, return LettaMessage objects.
    
</dd>
</dl>

<dl>
<dd>

**assistant_message_tool_name:** `typing.Optional[str]` — The name of the designated message tool.
    
</dd>
</dl>

<dl>
<dd>

**assistant_message_tool_kwarg:** `typing.Optional[str]` — The name of the message argument in the designated message tool.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.messages.<a href="src/letta/agents/messages/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Process a user message and return the agent's response.
This endpoint accepts a message from a user and processes it through the agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta, MessageCreate

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.messages.create(
    agent_id="agent_id",
    messages=[
        MessageCreate(
            role="user",
            text="text",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Sequence[MessageCreate]` — The messages to be sent to the agent.
    
</dd>
</dl>

<dl>
<dd>

**assistant_message_tool_name:** `typing.Optional[str]` — The name of the designated message tool.
    
</dd>
</dl>

<dl>
<dd>

**assistant_message_tool_kwarg:** `typing.Optional[str]` — The name of the message argument in the designated message tool.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agents.messages.<a href="src/letta/agents/messages/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the details of a message associated with an agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.messages.update(
    agent_id="agent_id",
    message_id="message_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[MessageRole]` — The role of the participant.
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` — The text of the message.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the participant.
    
</dd>
</dl>

<dl>
<dd>

**tool_calls:** `typing.Optional[typing.Sequence[LettaSchemasOpenaiChatCompletionsToolCallInput]]` — The list of tool calls requested.
    
</dd>
</dl>

<dl>
<dd>

**tool_call_id:** `typing.Optional[str]` — The id of the tool call.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agents Memory Messages
<details><summary><code>client.agents.memory.messages.<a href="src/letta/agents/memory/messages/client.py">list_in_context</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the messages in the context of a specific agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.agents.memory.messages.list_in_context(
    agent_id="agent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sources Files
<details><summary><code>client.sources.files.<a href="src/letta/sources/files/client.py">upload</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a file to a data source.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.sources.files.upload(
    source_id="source_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sources.files.<a href="src/letta/sources/files/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List paginated files associated with a data source.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.sources.files.list(
    source_id="source_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of files to return
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Pagination cursor to fetch the next set of results
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sources.files.<a href="src/letta/sources/files/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a data source.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.sources.files.delete(
    source_id="source_id",
    file_id="file_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sources Passages
<details><summary><code>client.sources.passages.<a href="src/letta/sources/passages/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all passages associated with a data source.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta import Letta

client = Letta(
    token="YOUR_TOKEN",
)
client.sources.passages.list(
    source_id="source_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

