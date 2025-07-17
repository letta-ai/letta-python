# Reference
## Tools
<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">retrieve</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.tools.retrieve(
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">delete</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">modify</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.tools.modify(
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

**tags:** `typing.Optional[typing.Sequence[str]]` — Metadata tags.
    
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

**args_json_schema:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The args JSON schema of the function.
    
</dd>
</dl>

<dl>
<dd>

**return_char_limit:** `typing.Optional[int]` — The maximum number of characters in the response.
    
</dd>
</dl>

<dl>
<dd>

**pip_requirements:** `typing.Optional[typing.Sequence[PipRequirement]]` — Optional list of pip packages required by this tool.
    
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">count</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a count of all tools available to agents belonging to the org of the user.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.tools.count()

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

**include_base_tools:** `typing.Optional[bool]` — Include built-in Letta tools in the count
    
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">list</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

**after:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">create</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

**args_json_schema:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The args JSON schema of the function.
    
</dd>
</dl>

<dl>
<dd>

**return_char_limit:** `typing.Optional[int]` — The maximum number of characters in the response.
    
</dd>
</dl>

<dl>
<dd>

**pip_requirements:** `typing.Optional[typing.Sequence[PipRequirement]]` — Optional list of pip packages required by this tool.
    
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">upsert</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

**args_json_schema:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The args JSON schema of the function.
    
</dd>
</dl>

<dl>
<dd>

**return_char_limit:** `typing.Optional[int]` — The maximum number of characters in the response.
    
</dd>
</dl>

<dl>
<dd>

**pip_requirements:** `typing.Optional[typing.Sequence[PipRequirement]]` — Optional list of pip packages required by this tool.
    
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">upsert_base_tools</a>()</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.tools.upsert_base_tools()

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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">run_tool_from_source</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.tools.run_tool_from_source(
    source_code="source_code",
    args={"key": "value"},
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

**args:** `typing.Dict[str, typing.Optional[typing.Any]]` — The arguments to pass to the tool.
    
</dd>
</dl>

<dl>
<dd>

**env_vars:** `typing.Optional[typing.Dict[str, str]]` — The environment variables to pass to the tool.
    
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

**args_json_schema:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The args JSON schema of the function.
    
</dd>
</dl>

<dl>
<dd>

**json_schema:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The JSON schema of the function (auto-generated from source_code if not provided)
    
</dd>
</dl>

<dl>
<dd>

**pip_requirements:** `typing.Optional[typing.Sequence[PipRequirement]]` — Optional list of pip packages required by this tool.
    
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">list_composio_apps</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">list_composio_actions_by_app</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">add_composio_tool</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">list_mcp_servers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all configured MCP servers
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.tools.list_mcp_servers()

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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">add_mcp_server</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new MCP server to the Letta MCP server config
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
from letta_client import Letta, StdioServerConfig

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.tools.add_mcp_server(
    request=StdioServerConfig(
        server_name="server_name",
        command="command",
        args=["args"],
    ),
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

**request:** `AddMcpServerRequest` 
    
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">list_mcp_tools_by_server</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all tools for a specific MCP server
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.tools.list_mcp_tools_by_server(
    mcp_server_name="mcp_server_name",
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

**mcp_server_name:** `str` 
    
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">add_mcp_tool</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Register a new MCP tool as a Letta server by MCP server + tool name
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.tools.add_mcp_tool(
    mcp_server_name="mcp_server_name",
    mcp_tool_name="mcp_tool_name",
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

**mcp_server_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**mcp_tool_name:** `str` 
    
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">delete_mcp_server</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new MCP server to the Letta MCP server config
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.tools.delete_mcp_server(
    mcp_server_name="mcp_server_name",
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

**mcp_server_name:** `str` 
    
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">update_mcp_server</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing MCP server configuration
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
from letta_client import Letta, UpdateStdioMcpServer

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.tools.update_mcp_server(
    mcp_server_name="mcp_server_name",
    request=UpdateStdioMcpServer(),
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

**mcp_server_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `UpdateMcpServerRequest` 
    
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">test_mcp_server</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Test connection to an MCP server without adding it.
Returns the list of available tools if successful.
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
from letta_client import Letta, StdioServerConfig

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.tools.test_mcp_server(
    request=StdioServerConfig(
        server_name="server_name",
        command="command",
        args=["args"],
    ),
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

**request:** `TestMcpServerRequest` 
    
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
<details><summary><code>client.sources.<a href="src/letta_client/sources/client.py">count</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Count all data sources created by a user.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.sources.count()

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

<details><summary><code>client.sources.<a href="src/letta_client/sources/client.py">retrieve</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.sources.retrieve(
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

<details><summary><code>client.sources.<a href="src/letta_client/sources/client.py">delete</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

<details><summary><code>client.sources.<a href="src/letta_client/sources/client.py">modify</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.sources.modify(
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

**instructions:** `typing.Optional[str]` — Instructions for how to use the source.
    
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

<details><summary><code>client.sources.<a href="src/letta_client/sources/client.py">retrieve_by_name</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.sources.retrieve_by_name(
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

<details><summary><code>client.sources.<a href="src/letta_client/sources/client.py">get_sources_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get aggregated metadata for all sources in an organization.

Returns structured metadata including:
- Total number of sources
- Total number of files across all sources
- Total size of all files
- Per-source breakdown with file details (file_name, file_size per file) if include_detailed_per_source_metadata is True
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.sources.get_sources_metadata()

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

**include_detailed_per_source_metadata:** `typing.Optional[bool]` 
    
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

<details><summary><code>client.sources.<a href="src/letta_client/sources/client.py">list</a>()</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

<details><summary><code>client.sources.<a href="src/letta_client/sources/client.py">create</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

**description:** `typing.Optional[str]` — The description of the source.
    
</dd>
</dl>

<dl>
<dd>

**instructions:** `typing.Optional[str]` — Instructions for how to use the source.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Metadata associated with the source.
    
</dd>
</dl>

<dl>
<dd>

**embedding:** `typing.Optional[str]` — The handle for the embedding config used by the source.
    
</dd>
</dl>

<dl>
<dd>

**embedding_chunk_size:** `typing.Optional[int]` — The chunk size of the embedding.
    
</dd>
</dl>

<dl>
<dd>

**embedding_config:** `typing.Optional[EmbeddingConfig]` — (Legacy) The embedding configuration used by the source.
    
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

<details><summary><code>client.sources.<a href="src/letta_client/sources/client.py">get_agents_for_source</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all agent IDs that have the specified source attached.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.sources.get_agents_for_source(
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

<details><summary><code>client.sources.<a href="src/letta_client/sources/client.py">get_file_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve metadata for a specific file by its ID.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.sources.get_file_metadata(
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

**include_content:** `typing.Optional[bool]` — Whether to include full file content
    
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
<details><summary><code>client.agents.<a href="src/letta_client/agents/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all agents associated with a given user.

This endpoint retrieves a list of all agents and their configurations
associated with the specified user ID.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

**match_all_tags:** `typing.Optional[bool]` — If True, only returns agents that match ALL given tags. Otherwise, return agents that have ANY of the passed-in tags.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit for pagination
    
</dd>
</dl>

<dl>
<dd>

**query_text:** `typing.Optional[str]` — Search agents by name
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Search agents by project ID
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` — Search agents by template ID
    
</dd>
</dl>

<dl>
<dd>

**base_template_id:** `typing.Optional[str]` — Search agents by base template ID
    
</dd>
</dl>

<dl>
<dd>

**identity_id:** `typing.Optional[str]` — Search agents by identity ID
    
</dd>
</dl>

<dl>
<dd>

**identifier_keys:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Search agents by identifier keys
    
</dd>
</dl>

<dl>
<dd>

**include_relationships:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include in the response. If not provided, all relationships are loaded by default. Using this can optimize performance by reducing unnecessary joins.
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` — Whether to sort agents oldest to newest (True) or newest to oldest (False, default)
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[str]` — Field to sort by. Options: 'created_at' (default), 'last_run_completion'
    
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

<details><summary><code>client.agents.<a href="src/letta_client/agents/client.py">create</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.create()

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

**name:** `typing.Optional[str]` — The name of the agent.
    
</dd>
</dl>

<dl>
<dd>

**memory_blocks:** `typing.Optional[typing.Sequence[CreateBlock]]` — The blocks to create in the agent's in-context memory.
    
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

**include_base_tools:** `typing.Optional[bool]` — If true, attaches the Letta core tools (e.g. core_memory related functions).
    
</dd>
</dl>

<dl>
<dd>

**include_multi_agent_tools:** `typing.Optional[bool]` — If true, attaches the Letta multi-agent tools (e.g. sending a message to another agent).
    
</dd>
</dl>

<dl>
<dd>

**include_base_tool_rules:** `typing.Optional[bool]` — If true, attaches the Letta base tool rules (e.g. deny all tools not explicitly allowed).
    
</dd>
</dl>

<dl>
<dd>

**include_default_source:** `typing.Optional[bool]` — If true, automatically creates and attaches a default data source for this agent.
    
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

**model:** `typing.Optional[str]` — The LLM configuration handle used by the agent, specified in the format provider/model-name, as an alternative to specifying llm_config.
    
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

**max_tokens:** `typing.Optional[int]` — The maximum number of tokens to generate, including reasoning step. If not set, the model will use its default value.
    
</dd>
</dl>

<dl>
<dd>

**max_reasoning_tokens:** `typing.Optional[int]` — The maximum number of tokens to generate for reasoning step. If not set, the model will use its default value.
    
</dd>
</dl>

<dl>
<dd>

**enable_reasoner:** `typing.Optional[bool]` — Whether to enable internal extended thinking step for a reasoner model.
    
</dd>
</dl>

<dl>
<dd>

**from_template:** `typing.Optional[str]` — The template id used to configure the agent
    
</dd>
</dl>

<dl>
<dd>

**template:** `typing.Optional[bool]` — Whether the agent is a template
    
</dd>
</dl>

<dl>
<dd>

**project:** `typing.Optional[str]` — Deprecated: Project should now be passed via the X-Project header instead of in the request body. If using the sdk, this can be done via the new x_project field below.
    
</dd>
</dl>

<dl>
<dd>

**tool_exec_environment_variables:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — The environment variables for tool execution specific to this agent.
    
</dd>
</dl>

<dl>
<dd>

**memory_variables:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — The variables that should be set for the agent.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — The id of the project the agent belongs to.
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` — The id of the template the agent belongs to.
    
</dd>
</dl>

<dl>
<dd>

**base_template_id:** `typing.Optional[str]` — The base template id of the agent.
    
</dd>
</dl>

<dl>
<dd>

**identity_ids:** `typing.Optional[typing.Sequence[str]]` — The ids of the identities associated with this agent.
    
</dd>
</dl>

<dl>
<dd>

**message_buffer_autoclear:** `typing.Optional[bool]` — If set to True, the agent will not remember previous messages (though the agent will still retain state via core memory blocks and archival/recall memory). Not recommended unless you have an advanced use case.
    
</dd>
</dl>

<dl>
<dd>

**enable_sleeptime:** `typing.Optional[bool]` — If set to True, memory management will move to a background agent thread.
    
</dd>
</dl>

<dl>
<dd>

**response_format:** `typing.Optional[CreateAgentRequestResponseFormat]` — The response format for the agent.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — The timezone of the agent (IANA format).
    
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

<details><summary><code>client.agents.<a href="src/letta_client/agents/client.py">count</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the count of all agents associated with a given user.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.count()

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

<details><summary><code>client.agents.<a href="src/letta_client/agents/client.py">export_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Export the serialized JSON representation of an agent, formatted with indentation.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.export_file(
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

<details><summary><code>client.agents.<a href="src/letta_client/agents/client.py">import_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import a serialized agent file and recreate the agent in the system.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.import_file()

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

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**append_copy_suffix:** `typing.Optional[bool]` — If set to True, appends "_copy" to the end of the agent name.
    
</dd>
</dl>

<dl>
<dd>

**override_existing_tools:** `typing.Optional[bool]` — If set to True, existing tools can get their source code overwritten by the uploaded tool definitions. Note that Letta core tools can never be updated externally.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — The project ID to associate the uploaded agent with.
    
</dd>
</dl>

<dl>
<dd>

**strip_messages:** `typing.Optional[bool]` — If set to True, strips all messages from the agent before importing.
    
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

<details><summary><code>client.agents.<a href="src/letta_client/agents/client.py">retrieve</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.retrieve(
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

**include_relationships:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include in the response. If not provided, all relationships are loaded by default. Using this can optimize performance by reducing unnecessary joins.
    
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

<details><summary><code>client.agents.<a href="src/letta_client/agents/client.py">delete</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

<details><summary><code>client.agents.<a href="src/letta_client/agents/client.py">modify</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing agent
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.modify(
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

**tool_exec_environment_variables:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — The environment variables for tool execution specific to this agent.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — The id of the project the agent belongs to.
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` — The id of the template the agent belongs to.
    
</dd>
</dl>

<dl>
<dd>

**base_template_id:** `typing.Optional[str]` — The base template id of the agent.
    
</dd>
</dl>

<dl>
<dd>

**identity_ids:** `typing.Optional[typing.Sequence[str]]` — The ids of the identities associated with this agent.
    
</dd>
</dl>

<dl>
<dd>

**message_buffer_autoclear:** `typing.Optional[bool]` — If set to True, the agent will not remember previous messages (though the agent will still retain state via core memory blocks and archival/recall memory). Not recommended unless you have an advanced use case.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — The LLM configuration handle used by the agent, specified in the format provider/model-name, as an alternative to specifying llm_config.
    
</dd>
</dl>

<dl>
<dd>

**embedding:** `typing.Optional[str]` — The embedding configuration handle used by the agent, specified in the format provider/model-name.
    
</dd>
</dl>

<dl>
<dd>

**enable_sleeptime:** `typing.Optional[bool]` — If set to True, memory management will move to a background agent thread.
    
</dd>
</dl>

<dl>
<dd>

**response_format:** `typing.Optional[UpdateAgentResponseFormat]` — The response format for the agent.
    
</dd>
</dl>

<dl>
<dd>

**last_run_completion:** `typing.Optional[dt.datetime]` — The timestamp when the agent last completed a run.
    
</dd>
</dl>

<dl>
<dd>

**last_run_duration_ms:** `typing.Optional[int]` — The duration in milliseconds of the agent's last run.
    
</dd>
</dl>

<dl>
<dd>

**timezone:** `typing.Optional[str]` — The timezone of the agent (IANA format).
    
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

<details><summary><code>client.agents.<a href="src/letta_client/agents/client.py">close_all_open_files</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Closes all currently open files for a given agent.

This endpoint updates the file state for the agent so that no files are marked as open.
Typically used to reset the working memory view for the agent.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.close_all_open_files(
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

<details><summary><code>client.agents.<a href="src/letta_client/agents/client.py">summarize_agent_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Summarize an agent's conversation history to a target message length.

This endpoint summarizes the current message history for a given agent,
truncating and compressing it down to the specified `max_message_length`.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.summarize_agent_conversation(
    agent_id="agent_id",
    max_message_length=1,
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

**max_message_length:** `int` — Maximum number of messages to retain after summarization.
    
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

<details><summary><code>client.agents.<a href="src/letta_client/agents/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>This endpoint is only available on Letta Cloud.</Note>

Search deployed agents.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.search()

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

**search:** `typing.Optional[typing.Sequence[AgentsSearchRequestSearchItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**combinator:** `typing.Optional[typing.Literal["AND"]]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[AgentsSearchRequestSortBy]` 
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` 
    
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

## Groups
<details><summary><code>client.groups.<a href="src/letta_client/groups/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch all multi-agent groups matching query.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.groups.list()

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

**manager_type:** `typing.Optional[ManagerType]` — Search groups by manager type
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit for pagination
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Search groups by project id
    
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

<details><summary><code>client.groups.<a href="src/letta_client/groups/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new multi-agent group with the specified configuration.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.groups.create(
    agent_ids=["agent_ids"],
    description="description",
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

**agent_ids:** `typing.Sequence[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**manager_config:** `typing.Optional[GroupCreateManagerConfig]` — 
    
</dd>
</dl>

<dl>
<dd>

**shared_block_ids:** `typing.Optional[typing.Sequence[str]]` — 
    
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

<details><summary><code>client.groups.<a href="src/letta_client/groups/client.py">count</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the count of all groups associated with a given user.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.groups.count()

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

<details><summary><code>client.groups.<a href="src/letta_client/groups/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the group by id.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.groups.retrieve(
    group_id="group_id",
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

**group_id:** `str` 
    
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

<details><summary><code>client.groups.<a href="src/letta_client/groups/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a multi-agent group.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.groups.delete(
    group_id="group_id",
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

**group_id:** `str` 
    
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

<details><summary><code>client.groups.<a href="src/letta_client/groups/client.py">modify</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new multi-agent group with the specified configuration.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.groups.modify(
    group_id="group_id",
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

**group_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**agent_ids:** `typing.Optional[typing.Sequence[str]]` — 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — 
    
</dd>
</dl>

<dl>
<dd>

**manager_config:** `typing.Optional[GroupUpdateManagerConfig]` — 
    
</dd>
</dl>

<dl>
<dd>

**shared_block_ids:** `typing.Optional[typing.Sequence[str]]` — 
    
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

## Identities
<details><summary><code>client.identities.<a href="src/letta_client/identities/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all identities in the database
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.identities.list()

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

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**identifier_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**identity_type:** `typing.Optional[IdentityType]` 
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` 
    
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

<details><summary><code>client.identities.<a href="src/letta_client/identities/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.identities.create(
    identifier_key="identifier_key",
    name="name",
    identity_type="org",
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

**identifier_key:** `str` — External, user-generated identifier key of the identity.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the identity.
    
</dd>
</dl>

<dl>
<dd>

**identity_type:** `IdentityType` — The type of the identity.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — The project id of the identity, if applicable.
    
</dd>
</dl>

<dl>
<dd>

**agent_ids:** `typing.Optional[typing.Sequence[str]]` — The agent ids that are associated with the identity.
    
</dd>
</dl>

<dl>
<dd>

**block_ids:** `typing.Optional[typing.Sequence[str]]` — The IDs of the blocks associated with the identity.
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[typing.Sequence[IdentityProperty]]` — List of properties associated with the identity.
    
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

<details><summary><code>client.identities.<a href="src/letta_client/identities/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.identities.upsert(
    identifier_key="identifier_key",
    name="name",
    identity_type="org",
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

**identifier_key:** `str` — External, user-generated identifier key of the identity.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The name of the identity.
    
</dd>
</dl>

<dl>
<dd>

**identity_type:** `IdentityType` — The type of the identity.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — The project id of the identity, if applicable.
    
</dd>
</dl>

<dl>
<dd>

**agent_ids:** `typing.Optional[typing.Sequence[str]]` — The agent ids that are associated with the identity.
    
</dd>
</dl>

<dl>
<dd>

**block_ids:** `typing.Optional[typing.Sequence[str]]` — The IDs of the blocks associated with the identity.
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[typing.Sequence[IdentityProperty]]` — List of properties associated with the identity.
    
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

<details><summary><code>client.identities.<a href="src/letta_client/identities/client.py">count</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get count of all identities for a user
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.identities.count()

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

<details><summary><code>client.identities.<a href="src/letta_client/identities/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.identities.retrieve(
    identity_id="identity_id",
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

**identity_id:** `str` 
    
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

<details><summary><code>client.identities.<a href="src/letta_client/identities/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an identity by its identifier key
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.identities.delete(
    identity_id="identity_id",
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

**identity_id:** `str` 
    
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

<details><summary><code>client.identities.<a href="src/letta_client/identities/client.py">modify</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.identities.modify(
    identity_id="identity_id",
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

**identity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**identifier_key:** `typing.Optional[str]` — External, user-generated identifier key of the identity.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the identity.
    
</dd>
</dl>

<dl>
<dd>

**identity_type:** `typing.Optional[IdentityType]` — The type of the identity.
    
</dd>
</dl>

<dl>
<dd>

**agent_ids:** `typing.Optional[typing.Sequence[str]]` — The agent ids that are associated with the identity.
    
</dd>
</dl>

<dl>
<dd>

**block_ids:** `typing.Optional[typing.Sequence[str]]` — The IDs of the blocks associated with the identity.
    
</dd>
</dl>

<dl>
<dd>

**properties:** `typing.Optional[typing.Sequence[IdentityProperty]]` — List of properties associated with the identity.
    
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
<details><summary><code>client.models.<a href="src/letta_client/models/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List available LLM models using the asynchronous implementation for improved performance
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.models.list()

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

**provider_category:** `typing.Optional[
    typing.Union[ProviderCategory, typing.Sequence[ProviderCategory]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**provider_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**provider_type:** `typing.Optional[ProviderType]` 
    
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

## EmbeddingModels
<details><summary><code>client.embedding_models.<a href="src/letta_client/embedding_models/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List available embedding models using the asynchronous implementation for improved performance
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.embedding_models.list()

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
<details><summary><code>client.blocks.<a href="src/letta_client/blocks/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

**identity_id:** `typing.Optional[str]` — Search agents by identifier id
    
</dd>
</dl>

<dl>
<dd>

**identifier_keys:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Search agents by identifier keys
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of blocks to return
    
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

<details><summary><code>client.blocks.<a href="src/letta_client/blocks/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

**preserve_on_migration:** `typing.Optional[bool]` — Preserve the block on template migration.
    
</dd>
</dl>

<dl>
<dd>

**read_only:** `typing.Optional[bool]` — Whether the agent has read-only access to the block.
    
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

<details><summary><code>client.blocks.<a href="src/letta_client/blocks/client.py">count</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Count all blocks created by a user.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.blocks.count()

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

<details><summary><code>client.blocks.<a href="src/letta_client/blocks/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.blocks.retrieve(
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

<details><summary><code>client.blocks.<a href="src/letta_client/blocks/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

<details><summary><code>client.blocks.<a href="src/letta_client/blocks/client.py">modify</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.blocks.modify(
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

**preserve_on_migration:** `typing.Optional[bool]` — Preserve the block on template migration.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Label of the block (e.g. 'human', 'persona') in the context window.
    
</dd>
</dl>

<dl>
<dd>

**read_only:** `typing.Optional[bool]` — Whether the agent has read-only access to the block.
    
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

## Jobs
<details><summary><code>client.jobs.<a href="src/letta_client/jobs/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all jobs.
TODO (cliandy): implementation for pagination
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

**before:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit for pagination
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` — Whether to sort jobs oldest to newest (True, default) or newest to oldest (False)
    
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

<details><summary><code>client.jobs.<a href="src/letta_client/jobs/client.py">list_active</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

**source_id:** `typing.Optional[str]` — Only list jobs associated with the source.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit for pagination
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` — Whether to sort jobs oldest to newest (True, default) or newest to oldest (False)
    
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

<details><summary><code>client.jobs.<a href="src/letta_client/jobs/client.py">retrieve</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.jobs.retrieve(
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

<details><summary><code>client.jobs.<a href="src/letta_client/jobs/client.py">delete</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

<details><summary><code>client.jobs.<a href="src/letta_client/jobs/client.py">cancel_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a job by its job_id.

This endpoint marks a job as cancelled, which will cause any associated
agent execution to terminate as soon as possible.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.jobs.cancel_job(
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
<details><summary><code>client.health.<a href="src/letta_client/health/client.py">check</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

## Providers
<details><summary><code>client.providers.<a href="src/letta_client/providers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all custom providers in the database
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.providers.list()

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

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**provider_type:** `typing.Optional[ProviderType]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` 
    
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

<details><summary><code>client.providers.<a href="src/letta_client/providers/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new custom provider
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.providers.create(
    name="name",
    provider_type="anthropic",
    api_key="api_key",
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

**name:** `str` — The name of the provider.
    
</dd>
</dl>

<dl>
<dd>

**provider_type:** `ProviderType` — The type of the provider.
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `str` — API key or secret key used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**access_key:** `typing.Optional[str]` — Access key used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Region used for requests to the provider.
    
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

<details><summary><code>client.providers.<a href="src/letta_client/providers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an existing custom provider
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.providers.delete(
    provider_id="provider_id",
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

**provider_id:** `str` 
    
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

<details><summary><code>client.providers.<a href="src/letta_client/providers/client.py">modify</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing custom provider
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.providers.modify(
    provider_id="provider_id",
    api_key="api_key",
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

**provider_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**api_key:** `str` — API key or secret key used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**access_key:** `typing.Optional[str]` — Access key used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Region used for requests to the provider.
    
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

<details><summary><code>client.providers.<a href="src/letta_client/providers/client.py">check</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.providers.check()

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

## Runs
<details><summary><code>client.runs.<a href="src/letta_client/runs/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all runs.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.runs.list()

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

**agent_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The unique identifier of the agent associated with the run.
    
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

<details><summary><code>client.runs.<a href="src/letta_client/runs/client.py">list_active</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all active runs.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.runs.list_active()

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

**agent_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — The unique identifier of the agent associated with the run.
    
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

<details><summary><code>client.runs.<a href="src/letta_client/runs/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of a run.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.runs.retrieve(
    run_id="run_id",
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

**run_id:** `str` 
    
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

<details><summary><code>client.runs.<a href="src/letta_client/runs/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a run by its run_id.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.runs.delete(
    run_id="run_id",
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

**run_id:** `str` 
    
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

## Steps
<details><summary><code>client.steps.<a href="src/letta_client/steps/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List steps with optional pagination and date filters.
Dates should be provided in ISO 8601 format (e.g. 2025-01-29T15:01:19-08:00)
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.steps.list()

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

**before:** `typing.Optional[str]` — Return steps before this step ID
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Return steps after this step ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of steps to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — Sort order (asc or desc)
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Return steps after this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Return steps before this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` — Filter by the name of the model used for the step
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Filter by the ID of the agent that performed the step
    
</dd>
</dl>

<dl>
<dd>

**trace_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by trace ids returned by the server
    
</dd>
</dl>

<dl>
<dd>

**feedback:** `typing.Optional[StepsListRequestFeedback]` — Filter by feedback
    
</dd>
</dl>

<dl>
<dd>

**has_feedback:** `typing.Optional[bool]` — Filter by whether steps have feedback (true) or not (false)
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by tags
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Filter by the project ID that is associated with the step (cloud only).
    
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

<details><summary><code>client.steps.<a href="src/letta_client/steps/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a step by ID.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.steps.retrieve(
    step_id="step_id",
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

**step_id:** `str` 
    
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

## Tags
<details><summary><code>client.tags.<a href="src/letta_client/tags/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all tags in the database
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.tags.list()

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

**after:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**query_text:** `typing.Optional[str]` 
    
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

## Telemetry
<details><summary><code>client.telemetry.<a href="src/letta_client/telemetry/client.py">retrieve_provider_trace</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.telemetry.retrieve_provider_trace(
    step_id="step_id",
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

**step_id:** `str` 
    
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

## Batches
<details><summary><code>client.batches.<a href="src/letta_client/batches/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all batch runs.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.batches.list()

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

<details><summary><code>client.batches.<a href="src/letta_client/batches/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit a batch of agent messages for asynchronous processing.
Creates a job that will fan out messages to all listed agents and process them in parallel.
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
from letta_client import Letta, LettaBatchRequest, MessageCreate, TextContent

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.batches.create(
    requests=[
        LettaBatchRequest(
            messages=[
                MessageCreate(
                    role="user",
                    content=[
                        TextContent(
                            text="text",
                        )
                    ],
                )
            ],
            agent_id="agent_id",
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

**requests:** `typing.Sequence[LettaBatchRequest]` — List of requests to be processed in batch.
    
</dd>
</dl>

<dl>
<dd>

**callback_url:** `typing.Optional[str]` — Optional URL to call via POST when the batch completes. The callback payload will be a JSON object with the following fields: {'job_id': string, 'status': string, 'completed_at': string}. Where 'job_id' is the unique batch job identifier, 'status' is the final batch status (e.g., 'completed', 'failed'), and 'completed_at' is an ISO 8601 timestamp indicating when the batch job completed.
    
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

<details><summary><code>client.batches.<a href="src/letta_client/batches/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of a batch run.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.batches.retrieve(
    batch_id="batch_id",
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

**batch_id:** `str` 
    
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

<details><summary><code>client.batches.<a href="src/letta_client/batches/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a batch run.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.batches.cancel(
    batch_id="batch_id",
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

**batch_id:** `str` 
    
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

## Messages
<details><summary><code>client.messages.<a href="src/letta_client/messages/client.py">list_batch_messages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get messages for a specific batch job.

Returns messages associated with the batch in chronological order.

Pagination:
- For the first page, omit the cursor parameter
- For subsequent pages, use the ID of the last message from the previous response as the cursor
- Results will include messages before/after the cursor based on sort_descending
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.messages.list_batch_messages(
    batch_id="batch_id",
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

**batch_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to return
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Message ID to use as pagination cursor (get messages before/after this ID) depending on sort_descending.
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Filter messages by agent ID
    
</dd>
</dl>

<dl>
<dd>

**sort_descending:** `typing.Optional[bool]` — Sort messages by creation time (true=newest first)
    
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

## Voice
<details><summary><code>client.voice.<a href="src/letta_client/voice/client.py">create_voice_chat_completions</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.voice.create_voice_chat_completions(
    agent_id="agent_id",
    request={"key": "value"},
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

**request:** `typing.Dict[str, typing.Optional[typing.Any]]` 
    
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

## Templates
<details><summary><code>client.templates.<a href="src/letta_client/templates/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all templates
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.templates.list()

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

**offset:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 
    
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

## ClientSideAccessTokens
<details><summary><code>client.client_side_access_tokens.<a href="src/letta_client/client_side_access_tokens/client.py">client_side_access_tokens_list_client_side_access_tokens</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all client side access tokens for the current account. This is only available for cloud users.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.client_side_access_tokens.client_side_access_tokens_list_client_side_access_tokens()

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

**agent_id:** `typing.Optional[str]` — The agent ID to filter tokens by. If provided, only tokens for this agent will be returned.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[float]` — The offset for pagination. Defaults to 0.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — The number of tokens to return per page. Defaults to 10.
    
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

<details><summary><code>client.client_side_access_tokens.<a href="src/letta_client/client_side_access_tokens/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new client side access token with the specified configuration.
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
from letta_client import Letta
from letta_client.client_side_access_tokens import (
    ClientSideAccessTokensCreateRequestPolicyItem,
)

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.client_side_access_tokens.create(
    policy=[
        ClientSideAccessTokensCreateRequestPolicyItem(
            id="id",
            access=["read_messages"],
        )
    ],
    hostname="hostname",
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

**policy:** `typing.Sequence[ClientSideAccessTokensCreateRequestPolicyItem]` 
    
</dd>
</dl>

<dl>
<dd>

**hostname:** `str` — The hostname of the client side application. Please specify the full URL including the protocol (http or https).
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[str]` — The expiration date of the token. If not provided, the token will expire in 5 minutes
    
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

<details><summary><code>client.client_side_access_tokens.<a href="src/letta_client/client_side_access_tokens/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a client side access token.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.client_side_access_tokens.delete(
    token="token",
    request={"key": "value"},
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

**token:** `str` — The access token to delete
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
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

## Projects
<details><summary><code>client.projects.<a href="src/letta_client/projects/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all projects
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.projects.list()

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

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[str]` 
    
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

## Agents Context
<details><summary><code>client.agents.context.<a href="src/letta_client/agents/context/client.py">retrieve</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.context.retrieve(
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
<details><summary><code>client.agents.tools.<a href="src/letta_client/agents/tools/client.py">list</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

<details><summary><code>client.agents.tools.<a href="src/letta_client/agents/tools/client.py">attach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach a tool to an agent.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.tools.attach(
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

<details><summary><code>client.agents.tools.<a href="src/letta_client/agents/tools/client.py">detach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach a tool from an agent.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.tools.detach(
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
<details><summary><code>client.agents.sources.<a href="src/letta_client/agents/sources/client.py">attach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach a source to an agent.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.sources.attach(
    agent_id="agent_id",
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

**agent_id:** `str` 
    
</dd>
</dl>

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

<details><summary><code>client.agents.sources.<a href="src/letta_client/agents/sources/client.py">detach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach a source from an agent.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.sources.detach(
    agent_id="agent_id",
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

**agent_id:** `str` 
    
</dd>
</dl>

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

<details><summary><code>client.agents.sources.<a href="src/letta_client/agents/sources/client.py">list</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.sources.list(
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

## Agents CoreMemory
<details><summary><code>client.agents.core_memory.<a href="src/letta_client/agents/core_memory/client.py">retrieve</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.core_memory.retrieve(
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

## Agents Blocks
<details><summary><code>client.agents.blocks.<a href="src/letta_client/agents/blocks/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a core memory block from an agent.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.blocks.retrieve(
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

<details><summary><code>client.agents.blocks.<a href="src/letta_client/agents/blocks/client.py">modify</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a core memory block of an agent.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.blocks.modify(
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

**preserve_on_migration:** `typing.Optional[bool]` — Preserve the block on template migration.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Label of the block (e.g. 'human', 'persona') in the context window.
    
</dd>
</dl>

<dl>
<dd>

**read_only:** `typing.Optional[bool]` — Whether the agent has read-only access to the block.
    
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

<details><summary><code>client.agents.blocks.<a href="src/letta_client/agents/blocks/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the core memory blocks of a specific agent.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.blocks.list(
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

<details><summary><code>client.agents.blocks.<a href="src/letta_client/agents/blocks/client.py">attach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach a core memory block to an agent.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.blocks.attach(
    agent_id="agent_id",
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

**agent_id:** `str` 
    
</dd>
</dl>

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

<details><summary><code>client.agents.blocks.<a href="src/letta_client/agents/blocks/client.py">detach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach a core memory block from an agent.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.blocks.detach(
    agent_id="agent_id",
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

**agent_id:** `str` 
    
</dd>
</dl>

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

## Agents Passages
<details><summary><code>client.agents.passages.<a href="src/letta_client/agents/passages/client.py">list</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.passages.list(
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

**after:** `typing.Optional[str]` — Unique ID of the memory to start the query range at.
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Unique ID of the memory to end the query range at.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — How many results to include in the response.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search passages by text
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` — Whether to sort passages oldest to newest (True, default) or newest to oldest (False)
    
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

<details><summary><code>client.agents.passages.<a href="src/letta_client/agents/passages/client.py">create</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.passages.create(
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

<details><summary><code>client.agents.passages.<a href="src/letta_client/agents/passages/client.py">delete</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.passages.delete(
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

<details><summary><code>client.agents.passages.<a href="src/letta_client/agents/passages/client.py">modify</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify a memory in the agent's archival memory store.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.passages.modify(
    agent_id="agent_id",
    memory_id="memory_id",
    id="id",
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

**id:** `str` — The unique identifier of the passage.
    
</dd>
</dl>

<dl>
<dd>

**created_by_id:** `typing.Optional[str]` — The id of the user that made this object.
    
</dd>
</dl>

<dl>
<dd>

**last_updated_by_id:** `typing.Optional[str]` — The id of the user that made this object.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` — The timestamp when the object was created.
    
</dd>
</dl>

<dl>
<dd>

**updated_at:** `typing.Optional[dt.datetime]` — The timestamp when the object was last updated.
    
</dd>
</dl>

<dl>
<dd>

**is_deleted:** `typing.Optional[bool]` — Whether this passage is deleted or not.
    
</dd>
</dl>

<dl>
<dd>

**passage_update_agent_id:** `typing.Optional[str]` — The unique identifier of the agent associated with the passage.
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[str]` — The data source of the passage.
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `typing.Optional[str]` — The unique identifier of the file associated with the passage.
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `typing.Optional[str]` — The name of the file (only for source passages).
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — The metadata of the passage.
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` — The text of the passage.
    
</dd>
</dl>

<dl>
<dd>

**embedding:** `typing.Optional[typing.Sequence[float]]` — The embedding of the passage.
    
</dd>
</dl>

<dl>
<dd>

**embedding_config:** `typing.Optional[EmbeddingConfig]` — The embedding configuration used by the passage.
    
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
<details><summary><code>client.agents.messages.<a href="src/letta_client/agents/messages/client.py">list</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

**after:** `typing.Optional[str]` — Message after which to retrieve the returned messages.
    
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

**group_id:** `typing.Optional[str]` — Group ID to filter messages by.
    
</dd>
</dl>

<dl>
<dd>

**use_assistant_message:** `typing.Optional[bool]` — Whether to use assistant messages
    
</dd>
</dl>

<dl>
<dd>

**assistant_message_tool_name:** `typing.Optional[str]` — The name of the designated message tool.
    
</dd>
</dl>

<dl>
<dd>

**assistant_message_tool_kwarg:** `typing.Optional[str]` — The name of the message argument.
    
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

<details><summary><code>client.agents.messages.<a href="src/letta_client/agents/messages/client.py">create</a>(...)</code></summary>
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
from letta_client import Letta, MessageCreate, TextContent

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.messages.create(
    agent_id="agent_id",
    messages=[
        MessageCreate(
            role="user",
            content=[
                TextContent(
                    text="text",
                )
            ],
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

**max_steps:** `typing.Optional[int]` — Maximum number of steps the agent should take to process the request.
    
</dd>
</dl>

<dl>
<dd>

**use_assistant_message:** `typing.Optional[bool]` — Whether the server should parse specific tool call arguments (default `send_message`) as `AssistantMessage` objects.
    
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

**include_return_message_types:** `typing.Optional[typing.Sequence[MessageType]]` — Only return specified message types in the response. If `None` (default) returns all messages.
    
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

<details><summary><code>client.agents.messages.<a href="src/letta_client/agents/messages/client.py">modify</a>(...)</code></summary>
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
from letta_client import Letta, UpdateSystemMessage

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.messages.modify(
    agent_id="agent_id",
    message_id="message_id",
    request=UpdateSystemMessage(
        content="content",
    ),
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

**request:** `MessagesModifyRequest` 
    
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

<details><summary><code>client.agents.messages.<a href="src/letta_client/agents/messages/client.py">create_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Process a user message and return the agent's response.
This endpoint accepts a message from a user and processes it through the agent.
It will stream the steps of the response always, and stream the tokens if 'stream_tokens' is set to True.
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
from letta_client import Letta, MessageCreate, TextContent

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
response = client.agents.messages.create_stream(
    agent_id="agent_id",
    messages=[
        MessageCreate(
            role="user",
            content=[
                TextContent(
                    text="text",
                )
            ],
        )
    ],
)
for chunk in response:
    yield chunk

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

**max_steps:** `typing.Optional[int]` — Maximum number of steps the agent should take to process the request.
    
</dd>
</dl>

<dl>
<dd>

**use_assistant_message:** `typing.Optional[bool]` — Whether the server should parse specific tool call arguments (default `send_message`) as `AssistantMessage` objects.
    
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

**include_return_message_types:** `typing.Optional[typing.Sequence[MessageType]]` — Only return specified message types in the response. If `None` (default) returns all messages.
    
</dd>
</dl>

<dl>
<dd>

**stream_tokens:** `typing.Optional[bool]` — Flag to determine if individual tokens should be streamed. Set to True for token streaming (requires stream_steps = True).
    
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

<details><summary><code>client.agents.messages.<a href="src/letta_client/agents/messages/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel runs associated with an agent. If run_ids are passed in, cancel those in particular.

Note to cancel active runs associated with an agent, redis is required.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.messages.cancel(
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

**request:** `typing.Optional[typing.Sequence[str]]` 
    
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

<details><summary><code>client.agents.messages.<a href="src/letta_client/agents/messages/client.py">create_async</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Asynchronously process a user message and return a run object.
The actual processing happens in the background, and the status can be checked using the run ID.

This is "asynchronous" in the sense that it's a background job and explicitly must be fetched by the run ID.
This is more like `send_message_job`
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
from letta_client import Letta, MessageCreate, TextContent

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.messages.create_async(
    agent_id="agent_id",
    messages=[
        MessageCreate(
            role="user",
            content=[
                TextContent(
                    text="text",
                )
            ],
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

**max_steps:** `typing.Optional[int]` — Maximum number of steps the agent should take to process the request.
    
</dd>
</dl>

<dl>
<dd>

**use_assistant_message:** `typing.Optional[bool]` — Whether the server should parse specific tool call arguments (default `send_message`) as `AssistantMessage` objects.
    
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

**include_return_message_types:** `typing.Optional[typing.Sequence[MessageType]]` — Only return specified message types in the response. If `None` (default) returns all messages.
    
</dd>
</dl>

<dl>
<dd>

**callback_url:** `typing.Optional[str]` — Optional callback URL to POST to when the job completes
    
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

<details><summary><code>client.agents.messages.<a href="src/letta_client/agents/messages/client.py">reset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resets the messages for an agent
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.messages.reset(
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

**add_default_initial_messages:** `typing.Optional[bool]` — If true, adds the default initial messages after resetting.
    
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

<details><summary><code>client.agents.messages.<a href="src/letta_client/agents/messages/client.py">preview_raw_payload</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Inspect the raw LLM request payload without sending it.

This endpoint processes the message through the agent loop up until
the LLM request, then returns the raw request payload that would
be sent to the LLM provider. Useful for debugging and inspection.
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
from letta_client import Letta, LettaRequest, MessageCreate, TextContent

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.messages.preview_raw_payload(
    agent_id="agent_id",
    request=LettaRequest(
        messages=[
            MessageCreate(
                role="user",
                content=[
                    TextContent(
                        text="text",
                    )
                ],
            )
        ],
    ),
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

**request:** `MessagesPreviewRawPayloadRequest` 
    
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

## Agents Groups
<details><summary><code>client.agents.groups.<a href="src/letta_client/agents/groups/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the groups for an agent
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.groups.list(
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

**manager_type:** `typing.Optional[str]` — Manager type to filter groups by
    
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

## Agents Templates
<details><summary><code>client.agents.templates.<a href="src/letta_client/agents/templates/client.py">create_version</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>This endpoint is only available on Letta Cloud.</Note>

Creates a new version of the template version of the agent.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.templates.create_version(
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

**return_agent_state:** `typing.Optional[TemplatesCreateVersionRequestReturnAgentState]` 
    
</dd>
</dl>

<dl>
<dd>

**migrate_deployed_agents:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` 
    
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

<details><summary><code>client.agents.templates.<a href="src/letta_client/agents/templates/client.py">migrate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>This endpoint is only available on Letta Cloud.</Note>

Migrate an agent to a new versioned agent template.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.templates.migrate(
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

<details><summary><code>client.agents.templates.<a href="src/letta_client/agents/templates/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>This endpoint is only available on Letta Cloud.</Note>

Creates a template from an agent.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.templates.create(
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

**project:** `typing.Optional[str]` 
    
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

## Agents MemoryVariables
<details><summary><code>client.agents.memory_variables.<a href="src/letta_client/agents/memory_variables/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Note>This endpoint is only available on Letta Cloud.</Note>

Returns the memory variables associated with an agent.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.agents.memory_variables.list(
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

## Blocks Agents
<details><summary><code>client.blocks.agents.<a href="src/letta_client/blocks/agents/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all agents associated with the specified block.
Raises a 404 if the block does not exist.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.blocks.agents.list(
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

**include_relationships:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Specify which relational fields (e.g., 'tools', 'sources', 'memory') to include in the response. If not provided, all relationships are loaded by default. Using this can optimize performance by reducing unnecessary joins.
    
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

## Groups Messages
<details><summary><code>client.groups.messages.<a href="src/letta_client/groups/messages/client.py">list</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.groups.messages.list(
    group_id="group_id",
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

**group_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Message after which to retrieve the returned messages.
    
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

**use_assistant_message:** `typing.Optional[bool]` — Whether to use assistant messages
    
</dd>
</dl>

<dl>
<dd>

**assistant_message_tool_name:** `typing.Optional[str]` — The name of the designated message tool.
    
</dd>
</dl>

<dl>
<dd>

**assistant_message_tool_kwarg:** `typing.Optional[str]` — The name of the message argument.
    
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

<details><summary><code>client.groups.messages.<a href="src/letta_client/groups/messages/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Process a user message and return the group's response.
This endpoint accepts a message from a user and processes it through through agents in the group based on the specified pattern
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
from letta_client import Letta, MessageCreate, TextContent

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.groups.messages.create(
    group_id="group_id",
    messages=[
        MessageCreate(
            role="user",
            content=[
                TextContent(
                    text="text",
                )
            ],
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

**group_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Sequence[MessageCreate]` — The messages to be sent to the agent.
    
</dd>
</dl>

<dl>
<dd>

**max_steps:** `typing.Optional[int]` — Maximum number of steps the agent should take to process the request.
    
</dd>
</dl>

<dl>
<dd>

**use_assistant_message:** `typing.Optional[bool]` — Whether the server should parse specific tool call arguments (default `send_message`) as `AssistantMessage` objects.
    
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

**include_return_message_types:** `typing.Optional[typing.Sequence[MessageType]]` — Only return specified message types in the response. If `None` (default) returns all messages.
    
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

<details><summary><code>client.groups.messages.<a href="src/letta_client/groups/messages/client.py">create_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Process a user message and return the group's responses.
This endpoint accepts a message from a user and processes it through agents in the group based on the specified pattern.
It will stream the steps of the response always, and stream the tokens if 'stream_tokens' is set to True.
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
from letta_client import Letta, MessageCreate, TextContent

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
response = client.groups.messages.create_stream(
    group_id="group_id",
    messages=[
        MessageCreate(
            role="user",
            content=[
                TextContent(
                    text="text",
                )
            ],
        )
    ],
)
for chunk in response:
    yield chunk

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

**group_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Sequence[MessageCreate]` — The messages to be sent to the agent.
    
</dd>
</dl>

<dl>
<dd>

**max_steps:** `typing.Optional[int]` — Maximum number of steps the agent should take to process the request.
    
</dd>
</dl>

<dl>
<dd>

**use_assistant_message:** `typing.Optional[bool]` — Whether the server should parse specific tool call arguments (default `send_message`) as `AssistantMessage` objects.
    
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

**include_return_message_types:** `typing.Optional[typing.Sequence[MessageType]]` — Only return specified message types in the response. If `None` (default) returns all messages.
    
</dd>
</dl>

<dl>
<dd>

**stream_tokens:** `typing.Optional[bool]` — Flag to determine if individual tokens should be streamed. Set to True for token streaming (requires stream_steps = True).
    
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

<details><summary><code>client.groups.messages.<a href="src/letta_client/groups/messages/client.py">modify</a>(...)</code></summary>
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
from letta_client import Letta, UpdateSystemMessage

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.groups.messages.modify(
    group_id="group_id",
    message_id="message_id",
    request=UpdateSystemMessage(
        content="content",
    ),
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

**group_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `MessagesModifyRequest` 
    
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

<details><summary><code>client.groups.messages.<a href="src/letta_client/groups/messages/client.py">reset</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the group messages for all agents that are part of the multi-agent group.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.groups.messages.reset(
    group_id="group_id",
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

**group_id:** `str` 
    
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

## Identities Properties
<details><summary><code>client.identities.properties.<a href="src/letta_client/identities/properties/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from letta_client import IdentityProperty, Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.identities.properties.upsert(
    identity_id="identity_id",
    request=[
        IdentityProperty(
            key="key",
            value="value",
            type="string",
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

**identity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Sequence[IdentityProperty]` 
    
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

## Runs Messages
<details><summary><code>client.runs.messages.<a href="src/letta_client/runs/messages/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get messages associated with a run with filtering options.

Args:
    run_id: ID of the run
    before: A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.
    after: A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.
    limit: Maximum number of messages to return
    order: Sort order by the created_at timestamp of the objects. asc for ascending order and desc for descending order.
    role: Filter by role (user/assistant/system/tool)
    return_message_object: Whether to return Message objects or LettaMessage objects
    user_id: ID of the user making the request

Returns:
    A list of messages associated with the run. Default is List[LettaMessage].
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.runs.messages.list(
    run_id="run_id",
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

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — Sort order by the created_at timestamp of the objects. asc for ascending order and desc for descending order.
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[MessageRole]` — Filter by role
    
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

## Runs Usage
<details><summary><code>client.runs.usage.<a href="src/letta_client/runs/usage/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get usage statistics for a run.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.runs.usage.retrieve(
    run_id="run_id",
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

**run_id:** `str` 
    
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

## Runs Steps
<details><summary><code>client.runs.steps.<a href="src/letta_client/runs/steps/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get messages associated with a run with filtering options.

Args:
    run_id: ID of the run
    before: A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.
    after: A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.
    limit: Maximum number of steps to return
    order: Sort order by the created_at timestamp of the objects. asc for ascending order and desc for descending order.

Returns:
    A list of steps associated with the run.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.runs.steps.list(
    run_id="run_id",
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

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[str]` — Sort order by the created_at timestamp of the objects. asc for ascending order and desc for descending order.
    
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
<details><summary><code>client.sources.files.<a href="src/letta_client/sources/files/client.py">upload</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

**duplicate_handling:** `typing.Optional[DuplicateFileHandling]` — How to handle duplicate filenames
    
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

<details><summary><code>client.sources.files.<a href="src/letta_client/sources/files/client.py">list</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

**after:** `typing.Optional[str]` — Pagination cursor to fetch the next set of results
    
</dd>
</dl>

<dl>
<dd>

**include_content:** `typing.Optional[bool]` — Whether to include full file content
    
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

<details><summary><code>client.sources.files.<a href="src/letta_client/sources/files/client.py">delete</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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
<details><summary><code>client.sources.passages.<a href="src/letta_client/sources/passages/client.py">list</a>(...)</code></summary>
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
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

**after:** `typing.Optional[str]` — Message after which to retrieve the returned messages.
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Steps Feedback
<details><summary><code>client.steps.feedback.<a href="src/letta_client/steps/feedback/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add feedback to a step.
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.steps.feedback.create(
    step_id="step_id",
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

**step_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**feedback:** `typing.Optional[FeedbackType]` 
    
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

## Templates Agents
<details><summary><code>client.templates.agents.<a href="src/letta_client/templates/agents/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an Agent or multiple Agents from a template
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
from letta_client import Letta

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.templates.agents.create(
    project="project",
    template_version="template_version",
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

**project:** `str` — The project slug
    
</dd>
</dl>

<dl>
<dd>

**template_version:** `str` — The template version, formatted as {template-name}:{version-number} or {template-name}:latest
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — The tags to assign to the agent
    
</dd>
</dl>

<dl>
<dd>

**agent_name:** `typing.Optional[str]` — The name of the agent, optional otherwise a random one will be assigned
    
</dd>
</dl>

<dl>
<dd>

**initial_message_sequence:** `typing.Optional[typing.Sequence[AgentsCreateRequestInitialMessageSequenceItem]]` — Set an initial sequence of messages, if not provided, the agent will start with the default message sequence, if an empty array is provided, the agent will start with no messages
    
</dd>
</dl>

<dl>
<dd>

**memory_variables:** `typing.Optional[typing.Dict[str, str]]` — The memory variables to assign to the agent
    
</dd>
</dl>

<dl>
<dd>

**tool_variables:** `typing.Optional[typing.Dict[str, str]]` — The tool variables to assign to the agent
    
</dd>
</dl>

<dl>
<dd>

**identity_ids:** `typing.Optional[typing.Sequence[str]]` — The identity ids to assign to the agent
    
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

