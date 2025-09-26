# Reference
## Archives
<details><summary><code>client.archives.<a href="src/letta_client/archives/client.py">list_archives</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all archives for the current organization with optional filters and pagination.
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
client.archives.list_archives()

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

**before:** `typing.Optional[str]` — Archive ID cursor for pagination. Returns archives that come before this archive ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Archive ID cursor for pagination. Returns archives that come after this archive ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of archives to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListArchivesRequestOrder]` — Sort order for archives by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by archive name (exact match)
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Only archives attached to this agent ID
    
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

<details><summary><code>client.archives.<a href="src/letta_client/archives/client.py">create_archive</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new archive.
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
client.archives.create_archive(
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

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

<details><summary><code>client.archives.<a href="src/letta_client/archives/client.py">modify_archive</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing archive's name and/or description.
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
client.archives.modify_archive(
    archive_id="archive_id",
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

**archive_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

**npm_requirements:** `typing.Optional[typing.Sequence[NpmRequirement]]` — Optional list of npm packages required by this tool.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — A dictionary of additional metadata for the tool.
    
</dd>
</dl>

<dl>
<dd>

**default_requires_approval:** `typing.Optional[bool]` — Whether or not to require approval before executing this tool.
    
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

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by specific tool names
    
</dd>
</dl>

<dl>
<dd>

**tool_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by specific tool IDs - accepts repeated params or comma-separated values
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search tool names (case-insensitive partial match)
    
</dd>
</dl>

<dl>
<dd>

**tool_types:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by tool type(s) - accepts repeated params or comma-separated values
    
</dd>
</dl>

<dl>
<dd>

**exclude_tool_types:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Tool type(s) to exclude - accepts repeated params or comma-separated values
    
</dd>
</dl>

<dl>
<dd>

**return_only_letta_tools:** `typing.Optional[bool]` — Count only tools with tool_type starting with 'letta_'
    
</dd>
</dl>

<dl>
<dd>

**exclude_letta_tools:** `typing.Optional[bool]` — Exclude built-in Letta tools from the count
    
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

Get a list of all tools available to agents.
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

**before:** `typing.Optional[str]` — Tool ID cursor for pagination. Returns tools that come before this tool ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Tool ID cursor for pagination. Returns tools that come after this tool ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of tools to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ToolsListRequestOrder]` — Sort order for tools by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by single tool name
    
</dd>
</dl>

<dl>
<dd>

**names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by specific tool names
    
</dd>
</dl>

<dl>
<dd>

**tool_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by specific tool IDs - accepts repeated params or comma-separated values
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search tool names (case-insensitive partial match)
    
</dd>
</dl>

<dl>
<dd>

**tool_types:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by tool type(s) - accepts repeated params or comma-separated values
    
</dd>
</dl>

<dl>
<dd>

**exclude_tool_types:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Tool type(s) to exclude - accepts repeated params or comma-separated values
    
</dd>
</dl>

<dl>
<dd>

**return_only_letta_tools:** `typing.Optional[bool]` — Return only tools with tool_type starting with 'letta_'
    
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

**npm_requirements:** `typing.Optional[typing.Sequence[NpmRequirement]]` — Optional list of npm packages required by this tool.
    
</dd>
</dl>

<dl>
<dd>

**default_requires_approval:** `typing.Optional[bool]` — Whether or not to require approval before executing this tool.
    
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

**npm_requirements:** `typing.Optional[typing.Sequence[NpmRequirement]]` — Optional list of npm packages required by this tool.
    
</dd>
</dl>

<dl>
<dd>

**default_requires_approval:** `typing.Optional[bool]` — Whether or not to require approval before executing this tool.
    
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

**npm_requirements:** `typing.Optional[typing.Sequence[NpmRequirement]]` — Optional list of npm packages required by this tool.
    
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">list_composio_apps</a>()</code></summary>
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">list_mcp_servers</a>()</code></summary>
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

Delete a MCP server configuration
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

<details><summary><code>client.tools.<a href="src/letta_client/tools/client.py">connect_mcp_server</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Connect to an MCP server with support for OAuth via SSE.
Returns a stream of events handling authorization state and exchange if OAuth is required.
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
response = client.tools.connect_mcp_server(
    request=StdioServerConfig(
        server_name="server_name",
        command="command",
        args=["args"],
    ),
)
for chunk in response.data:
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

**request:** `ConnectMcpServerRequest` 
    
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

## Folders
<details><summary><code>client.folders.<a href="src/letta_client/folders/client.py">count</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Count all data folders created by a user.
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
client.folders.count()

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

<details><summary><code>client.folders.<a href="src/letta_client/folders/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a folder by ID
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
client.folders.retrieve(
    folder_id="folder_id",
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

**folder_id:** `str` 
    
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

<details><summary><code>client.folders.<a href="src/letta_client/folders/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a data folder.
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
client.folders.delete(
    folder_id="folder_id",
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

**folder_id:** `str` 
    
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

<details><summary><code>client.folders.<a href="src/letta_client/folders/client.py">modify</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the name or documentation of an existing data folder.
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
client.folders.modify(
    folder_id="folder_id",
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

**folder_id:** `str` 
    
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

<details><summary><code>client.folders.<a href="src/letta_client/folders/client.py">retrieve_by_name</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**Deprecated**: Please use the list endpoint `GET /v1/folders?name=` instead.


Get a folder by name.
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
client.folders.retrieve_by_name(
    folder_name="folder_name",
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

**folder_name:** `str` 
    
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

<details><summary><code>client.folders.<a href="src/letta_client/folders/client.py">retrieve_metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get aggregated metadata for all folders in an organization.

Returns structured metadata including:
- Total number of folders
- Total number of files across all folders
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
client.folders.retrieve_metadata()

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

<details><summary><code>client.folders.<a href="src/letta_client/folders/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all data folders created by a user.
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
client.folders.list()

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

**before:** `typing.Optional[str]` — Folder ID cursor for pagination. Returns folders that come before this folder ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Folder ID cursor for pagination. Returns folders that come after this folder ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of folders to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[FoldersListRequestOrder]` — Sort order for folders by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Folder name to filter by
    
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

<details><summary><code>client.folders.<a href="src/letta_client/folders/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new data folder.
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
client.folders.create(
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

## Agents
<details><summary><code>client.agents.<a href="src/letta_client/agents/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all agents.
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

**project_id:** `typing.Optional[str]` — Search agents by project ID - this will default to your default project on cloud
    
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

**order:** `typing.Optional[AgentsListRequestOrder]` — Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[AgentsListRequestOrderBy]` — Field to sort by
    
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

Create an agent.
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

**reasoning:** `typing.Optional[bool]` — Whether to enable reasoning for this agent.
    
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

**tool_exec_environment_variables:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Deprecated: use `secrets` field instead.
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — The environment variables for tool execution specific to this agent.
    
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

**max_files_open:** `typing.Optional[int]` — Maximum number of files that can be open at once for this agent. Setting this too high may exceed the context window, which will break the agent.
    
</dd>
</dl>

<dl>
<dd>

**per_file_view_window_char_limit:** `typing.Optional[int]` — The per-file view window character limit for this agent. Setting this too high may exceed the context window, which will break the agent.
    
</dd>
</dl>

<dl>
<dd>

**hidden:** `typing.Optional[bool]` — If set to True, the agent will be hidden.
    
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

Get the total number of agents.
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

Supports two export formats:
- Legacy format (use_legacy_format=true): Single agent with inline tools/blocks
- New format (default): Multi-entity format with separate agents, tools, blocks, files, etc.
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

**max_steps:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**use_legacy_format:** `typing.Optional[bool]` — If true, exports using the legacy single-agent format (v1). If false, exports using the new multi-entity format (v2).
    
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

Import a serialized agent file and recreate the agent(s) in the system.
Returns the IDs of all imported agents.
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

**override_embedding_model:** `typing.Optional[str]` 
    
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

**override_embedding_handle:** `typing.Optional[str]` — Override import with specific embedding handle.
    
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

**env_vars_json:** `typing.Optional[str]` — Environment variables as a JSON string to pass to the agent for tool execution.
    
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

Update an existing agent.
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

**tool_exec_environment_variables:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Deprecated: use `secrets` field instead
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — The environment variables for tool execution specific to this agent.
    
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

**reasoning:** `typing.Optional[bool]` — Whether to enable reasoning for this agent.
    
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

**max_files_open:** `typing.Optional[int]` — Maximum number of files that can be open at once for this agent. Setting this too high may exceed the context window, which will break the agent.
    
</dd>
</dl>

<dl>
<dd>

**per_file_view_window_char_limit:** `typing.Optional[int]` — The per-file view window character limit for this agent. Setting this too high may exceed the context window, which will break the agent.
    
</dd>
</dl>

<dl>
<dd>

**hidden:** `typing.Optional[bool]` — If set to True, the agent will be hidden.
    
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

**before:** `typing.Optional[str]` — Group ID cursor for pagination. Returns groups that come before this group ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Group ID cursor for pagination. Returns groups that come after this group ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of groups to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[GroupsListRequestOrder]` — Sort order for groups by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Field to sort by
    
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

**project_id:** `typing.Optional[str]` — The associated project id.
    
</dd>
</dl>

<dl>
<dd>

**shared_block_ids:** `typing.Optional[typing.Sequence[str]]` — 
    
</dd>
</dl>

<dl>
<dd>

**hidden:** `typing.Optional[bool]` — If set to True, the group will be hidden.
    
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

**project_id:** `typing.Optional[str]` — The associated project id.
    
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

**before:** `typing.Optional[str]` — Identity ID cursor for pagination. Returns identities that come before this identity ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Identity ID cursor for pagination. Returns identities that come after this identity ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of identities to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[IdentitiesListRequestOrder]` — Sort order for identities by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Field to sort by
    
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

<details><summary><code>client.models.<a href="src/letta_client/models/client.py">listembeddingmodels</a>()</code></summary>
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
client.models.listembeddingmodels()

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

**project_id:** `typing.Optional[str]` — Search blocks by project id
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of blocks to return
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Block ID cursor for pagination. Returns blocks that come before this block ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Block ID cursor for pagination. Returns blocks that come after this block ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[BlocksListRequestOrder]` — Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**label_search:** `typing.Optional[str]` — Search blocks by label. If provided, returns blocks that match this label. This is a full-text search on labels.
    
</dd>
</dl>

<dl>
<dd>

**description_search:** `typing.Optional[str]` — Search blocks by description. If provided, returns blocks that match this description. This is a full-text search on block descriptions.
    
</dd>
</dl>

<dl>
<dd>

**value_search:** `typing.Optional[str]` — Search blocks by value. If provided, returns blocks that match this value.
    
</dd>
</dl>

<dl>
<dd>

**connected_to_agents_count_gt:** `typing.Optional[int]` — Filter blocks by the number of connected agents. If provided, returns blocks that have more than this number of connected agents.
    
</dd>
</dl>

<dl>
<dd>

**connected_to_agents_count_lt:** `typing.Optional[int]` — Filter blocks by the number of connected agents. If provided, returns blocks that have less than this number of connected agents.
    
</dd>
</dl>

<dl>
<dd>

**connected_to_agents_count_eq:** `typing.Optional[typing.Union[int, typing.Sequence[int]]]` — Filter blocks by the exact number of connected agents. If provided, returns blocks that have exactly this number of connected agents.
    
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

**project_id:** `typing.Optional[str]` — The associated project id.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The id of the template.
    
</dd>
</dl>

<dl>
<dd>

**is_template:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**base_template_id:** `typing.Optional[str]` — The base template id of the block.
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `typing.Optional[str]` — The id of the deployment.
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `typing.Optional[str]` — The id of the entity within the template.
    
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

**hidden:** `typing.Optional[bool]` — If set to True, the block will be hidden.
    
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

**project_id:** `typing.Optional[str]` — The associated project id.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The id of the template.
    
</dd>
</dl>

<dl>
<dd>

**is_template:** `typing.Optional[bool]` — Whether the block is a template (e.g. saved human/persona options).
    
</dd>
</dl>

<dl>
<dd>

**base_template_id:** `typing.Optional[str]` — The base template id of the block.
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `typing.Optional[str]` — The id of the deployment.
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `typing.Optional[str]` — The id of the entity within the template.
    
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

**hidden:** `typing.Optional[bool]` — If set to True, the block will be hidden.
    
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

**active:** `typing.Optional[bool]` — Filter for active jobs.
    
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

Get a list of all custom providers.
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

**before:** `typing.Optional[str]` — Provider ID cursor for pagination. Returns providers that come before this provider ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Provider ID cursor for pagination. Returns providers that come after this provider ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of providers to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ProvidersListRequestOrder]` — Sort order for providers by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter providers by name
    
</dd>
</dl>

<dl>
<dd>

**provider_type:** `typing.Optional[ProviderType]` — Filter providers by type
    
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

Create a new custom provider.
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

**base_url:** `typing.Optional[str]` — Base URL used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `typing.Optional[str]` — API version used for requests to the provider.
    
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

<details><summary><code>client.providers.<a href="src/letta_client/providers/client.py">retrieve_provider</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a provider by ID.
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
client.providers.retrieve_provider(
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

<details><summary><code>client.providers.<a href="src/letta_client/providers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an existing custom provider.
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

Update an existing custom provider.
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

**base_url:** `typing.Optional[str]` — Base URL used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `typing.Optional[str]` — API version used for requests to the provider.
    
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

<details><summary><code>client.providers.<a href="src/letta_client/providers/client.py">check</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify the API key and additional parameters for a provider.
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
client.providers.check(
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

**base_url:** `typing.Optional[str]` — Base URL used for requests to the provider.
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `typing.Optional[str]` — API version used for requests to the provider.
    
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

**agent_id:** `typing.Optional[str]` — The unique identifier of the agent associated with the run.
    
</dd>
</dl>

<dl>
<dd>

**agent_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — (DEPRECATED) The unique identifiers of the agents associated with the run.
    
</dd>
</dl>

<dl>
<dd>

**background:** `typing.Optional[bool]` — If True, filters for runs that were created in background mode.
    
</dd>
</dl>

<dl>
<dd>

**stop_reason:** `typing.Optional[StopReasonType]` — Filter runs by stop reason.
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Cursor for pagination
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of runs to return
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — Filter for active runs.
    
</dd>
</dl>

<dl>
<dd>

**ascending:** `typing.Optional[bool]` — Whether to sort agents oldest to newest (True) or newest to oldest (False, default)
    
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

**agent_id:** `typing.Optional[str]` — The unique identifier of the agent associated with the run.
    
</dd>
</dl>

<dl>
<dd>

**background:** `typing.Optional[bool]` — If True, filters for runs that were created in background mode.
    
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

<details><summary><code>client.runs.<a href="src/letta_client/runs/client.py">stream</a>(...)</code></summary>
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
response = client.runs.stream(
    run_id="run_id",
)
for chunk in response.data:
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

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[int]` — Sequence id to use as a cursor for pagination. Response will start streaming after this chunk sequence id
    
</dd>
</dl>

<dl>
<dd>

**include_pings:** `typing.Optional[bool]` — Whether to include periodic keepalive ping messages in the stream to prevent connection timeouts.
    
</dd>
</dl>

<dl>
<dd>

**poll_interval:** `typing.Optional[float]` — Seconds to wait between polls when no new data.
    
</dd>
</dl>

<dl>
<dd>

**batch_size:** `typing.Optional[int]` — Number of entries to read per batch.
    
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

**order:** `typing.Optional[StepsListRequestOrder]` — Sort order for steps by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Field to sort by
    
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

Get the list of all agent tags that have been created.
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

**before:** `typing.Optional[str]` — Tag cursor for pagination. Returns tags that come before this tag in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Tag cursor for pagination. Returns tags that come after this tag in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of tags to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[TagsListRequestOrder]` — Sort order for tags. 'asc' for alphabetical order, 'desc' for reverse alphabetical order
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["name"]]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**query_text:** `typing.Optional[str]` — Filter tags by text search. Deprecated, please use name field instead
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter tags by name
    
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

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

**DEPRECATED**: Use `GET /steps/{step_id}/trace` instead.

Retrieve provider trace by step ID.
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
<details><summary><code>client.batches.<a href="src/letta_client/batches/client.py">list</a>(...)</code></summary>
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

**before:** `typing.Optional[str]` — Job ID cursor for pagination. Returns jobs that come before this job ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Job ID cursor for pagination. Returns jobs that come after this job ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of jobs to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[BatchesListRequestOrder]` — Sort order for jobs by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Field to sort by
    
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

<details><summary><code>client.batches.<a href="src/letta_client/batches/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit a batch of agent runs for asynchronous processing.

Creates a job that will fan out messages to all listed agents and process them in parallel.
The request will be rejected if it exceeds 256MB.
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

Retrieve the status and details of a batch run.
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Templates
<details><summary><code>client.templates.<a href="src/letta_client/templates/client.py">createagentsfromtemplate</a>(...)</code></summary>
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
client.templates.createagentsfromtemplate(
    project_id="project_id",
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

**project_id:** `str` — The project id
    
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

**initial_message_sequence:** `typing.Optional[
    typing.Sequence[
        TemplatesCreateAgentsFromTemplateRequestInitialMessageSequenceItem
    ]
]` — Set an initial sequence of messages, if not provided, the agent will start with the default message sequence, if an empty array is provided, the agent will start with no messages
    
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

**exact:** `typing.Optional[str]` — Whether to search for an exact name match
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Specify the version you want to return, otherwise will return the latest version
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**project_slug:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort_by:** `typing.Optional[TemplatesListRequestSortBy]` 
    
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

<details><summary><code>client.templates.<a href="src/letta_client/templates/client.py">savetemplateversion</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Saves the current version of the template as a new version
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
client.templates.savetemplateversion(
    project_id="project_id",
    template_name="template_name",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `str` — The template version, formatted as {template-name}, any version appended will be ignored
    
</dd>
</dl>

<dl>
<dd>

**preserve_environment_variables_on_migration:** `typing.Optional[bool]` — If true, the environment variables will be preserved in the template version when migrating agents
    
</dd>
</dl>

<dl>
<dd>

**preserve_core_memories_on_migration:** `typing.Optional[bool]` — If true, the core memories will be preserved in the template version when migrating agents
    
</dd>
</dl>

<dl>
<dd>

**migrate_agents:** `typing.Optional[bool]` — If true, existing agents attached to this template will be migrated to the new template version
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` — A message to describe the changes made in this template version
    
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

<details><summary><code>client.templates.<a href="src/letta_client/templates/client.py">deletetemplate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes all versions of a template with the specified name
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
client.templates.deletetemplate(
    project_id="project_id",
    template_name="template_name",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `str` — The template name (without version)
    
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

<details><summary><code>client.templates.<a href="src/letta_client/templates/client.py">gettemplatesnapshot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a snapshot of the template version, this will return the template state at a specific version
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
client.templates.gettemplatesnapshot(
    project_id="project_id",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_version:** `str` — The template version, formatted as {template-name}:{version-number} or {template-name}:latest
    
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

<details><summary><code>client.templates.<a href="src/letta_client/templates/client.py">setcurrenttemplatefromsnapshot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the current working version of a template from a snapshot
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
client.templates.setcurrenttemplatefromsnapshot(
    project_id="project_id",
    template_version="template_version",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_version:** `str` — The template name with :current version (e.g., my-template:current)
    
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

<details><summary><code>client.templates.<a href="src/letta_client/templates/client.py">forktemplate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Forks a template version into a new template
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
client.templates.forktemplate(
    project_id="project_id",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_version:** `str` — The template version, formatted as {template-name}:{version-number} or {template-name}:latest
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional custom name for the forked template. If not provided, a random name will be generated.
    
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

<details><summary><code>client.templates.<a href="src/letta_client/templates/client.py">createtemplate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new template from an existing agent or agent file
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
from letta_client.templates import TemplatesCreateTemplateRequestAgentId

client = Letta(
    project="YOUR_PROJECT",
    token="YOUR_TOKEN",
)
client.templates.createtemplate(
    project_id="project_id",
    request=TemplatesCreateTemplateRequestAgentId(
        agent_id="agent_id",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**request:** `TemplatesCreateTemplateRequest` 
    
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

<details><summary><code>client.templates.<a href="src/letta_client/templates/client.py">renametemplate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Renames all versions of a template with the specified name. Versions are automatically stripped from the current template name if accidentally included.
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
client.templates.renametemplate(
    project_id="project_id",
    template_name="template_name",
    new_name="new_name",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `str` — The current template name (version will be automatically stripped if included)
    
</dd>
</dl>

<dl>
<dd>

**new_name:** `str` — The new name for the template
    
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

<details><summary><code>client.templates.<a href="src/letta_client/templates/client.py">updatetemplatedescription</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the description for all versions of a template with the specified name. Versions are automatically stripped from the current template name if accidentally included.
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
client.templates.updatetemplatedescription(
    project_id="project_id",
    template_name="template_name",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `str` — The template name (version will be automatically stripped if included)
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The new description for the template
    
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

<details><summary><code>client.templates.<a href="src/letta_client/templates/client.py">listtemplateversions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all versions of a specific template
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
client.templates.listtemplateversions(
    project_id="project_id",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The template name (without version)
    
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

<details><summary><code>client.templates.<a href="src/letta_client/templates/client.py">migratedeployment</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Migrates a deployment to a specific template version
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
client.templates.migratedeployment(
    project_id="project_id",
    template_name="template_name",
    deployment_id="deployment_id",
    version="version",
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

**project_id:** `str` — The project id
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `str` — The template name (without version)
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `str` — The deployment ID to migrate
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — The target template version to migrate to
    
</dd>
</dl>

<dl>
<dd>

**preserve_tool_variables:** `typing.Optional[bool]` — Whether to preserve existing tool variables during migration
    
</dd>
</dl>

<dl>
<dd>

**preserve_core_memories:** `typing.Optional[bool]` — Whether to preserve existing core memories during migration
    
</dd>
</dl>

<dl>
<dd>

**memory_variables:** `typing.Optional[typing.Dict[str, str]]` — Additional memory variables to apply during migration
    
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

<details><summary><code>client.agents.tools.<a href="src/letta_client/agents/tools/client.py">modify_approval</a>(...)</code></summary>
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
client.agents.tools.modify_approval(
    agent_id="agent_id",
    tool_name="tool_name",
    requires_approval=True,
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

**tool_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**requires_approval:** `bool` 
    
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

## Agents Folders
<details><summary><code>client.agents.folders.<a href="src/letta_client/agents/folders/client.py">attach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach a folder to an agent.
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
client.agents.folders.attach(
    agent_id="agent_id",
    folder_id="folder_id",
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

**folder_id:** `str` 
    
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

<details><summary><code>client.agents.folders.<a href="src/letta_client/agents/folders/client.py">detach</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach a folder from an agent.
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
client.agents.folders.detach(
    agent_id="agent_id",
    folder_id="folder_id",
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

**folder_id:** `str` 
    
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

<details><summary><code>client.agents.folders.<a href="src/letta_client/agents/folders/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the folders associated with an agent.
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
client.agents.folders.list(
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

## Agents Files
<details><summary><code>client.agents.files.<a href="src/letta_client/agents/files/client.py">close_all</a>(...)</code></summary>
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
client.agents.files.close_all(
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

<details><summary><code>client.agents.files.<a href="src/letta_client/agents/files/client.py">open</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Opens a specific file for a given agent.

This endpoint marks a specific file as open in the agent's file state.
The file will be included in the agent's working memory view.
Returns a list of file names that were closed due to LRU eviction.
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
client.agents.files.open(
    agent_id="agent_id",
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

**agent_id:** `str` 
    
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

<details><summary><code>client.agents.files.<a href="src/letta_client/agents/files/client.py">close</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Closes a specific file for a given agent.

This endpoint marks a specific file as closed in the agent's file state.
The file will be removed from the agent's working memory view.
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
client.agents.files.close(
    agent_id="agent_id",
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

**agent_id:** `str` 
    
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

<details><summary><code>client.agents.files.<a href="src/letta_client/agents/files/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the files attached to an agent with their open/closed status (paginated).
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
client.agents.files.list(
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

**cursor:** `typing.Optional[str]` — Pagination cursor from previous response
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items to return (1-100)
    
</dd>
</dl>

<dl>
<dd>

**is_open:** `typing.Optional[bool]` — Filter by open status (true for open files, false for closed files)
    
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

**project_id:** `typing.Optional[str]` — The associated project id.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The id of the template.
    
</dd>
</dl>

<dl>
<dd>

**is_template:** `typing.Optional[bool]` — Whether the block is a template (e.g. saved human/persona options).
    
</dd>
</dl>

<dl>
<dd>

**base_template_id:** `typing.Optional[str]` — The base template id of the block.
    
</dd>
</dl>

<dl>
<dd>

**deployment_id:** `typing.Optional[str]` — The id of the deployment.
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `typing.Optional[str]` — The id of the entity within the template.
    
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

**hidden:** `typing.Optional[bool]` — If set to True, the block will be hidden.
    
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

**tags:** `typing.Optional[typing.Sequence[str]]` — Optional list of tags to attach to the memory.
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` — Optional timestamp for the memory (defaults to current UTC time).
    
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

<details><summary><code>client.agents.passages.<a href="src/letta_client/agents/passages/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search archival memory using semantic (embedding-based) search with optional temporal filtering.

This endpoint allows manual triggering of archival memory searches, enabling users to query
an agent's archival memory store directly via the API. The search uses the same functionality
as the agent's archival_memory_search tool but is accessible for external API usage.
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
client.agents.passages.search(
    agent_id="agent_id",
    query="query",
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

**query:** `str` — String to search for using semantic similarity
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Optional list of tags to filter search results
    
</dd>
</dl>

<dl>
<dd>

**tag_match_mode:** `typing.Optional[PassagesSearchRequestTagMatchMode]` — How to match tags - 'any' to match passages with any of the tags, 'all' to match only passages with all tags
    
</dd>
</dl>

<dl>
<dd>

**top_k:** `typing.Optional[int]` — Maximum number of results to return. Uses system default if not specified
    
</dd>
</dl>

<dl>
<dd>

**start_datetime:** `typing.Optional[dt.datetime]` — Filter results to passages created after this datetime
    
</dd>
</dl>

<dl>
<dd>

**end_datetime:** `typing.Optional[dt.datetime]` — Filter results to passages created before this datetime
    
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

**include_err:** `typing.Optional[bool]` — Whether to include error messages and error statuses. For debugging purposes only.
    
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
                    text="The sky above the port was the color of television, tuned to a dead channel.",
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

**messages:** `typing.Sequence[LettaRequestMessagesItem]` — The messages to be sent to the agent.
    
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

**enable_thinking:** `typing.Optional[str]` — If set to True, enables reasoning before responses or tool calls from the agent.
    
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
                    text="The sky above the port was the color of television, tuned to a dead channel.",
                )
            ],
        )
    ],
)
for chunk in response.data:
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

**messages:** `typing.Sequence[LettaStreamingRequestMessagesItem]` — The messages to be sent to the agent.
    
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

**enable_thinking:** `typing.Optional[str]` — If set to True, enables reasoning before responses or tool calls from the agent.
    
</dd>
</dl>

<dl>
<dd>

**stream_tokens:** `typing.Optional[bool]` — Flag to determine if individual tokens should be streamed, rather than streaming per step.
    
</dd>
</dl>

<dl>
<dd>

**include_pings:** `typing.Optional[bool]` — Whether to include periodic keepalive ping messages in the stream to prevent connection timeouts.
    
</dd>
</dl>

<dl>
<dd>

**background:** `typing.Optional[bool]` — Whether to process the request in the background.
    
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

**run_ids:** `typing.Optional[typing.Sequence[str]]` — Optional list of run IDs to cancel
    
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

<details><summary><code>client.agents.messages.<a href="src/letta_client/agents/messages/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search messages across the entire organization with optional project and template filtering. Returns messages with FTS/vector ranks and total RRF score.

This is a cloud-only feature.
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
client.agents.messages.search()

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

**query:** `typing.Optional[str]` — Text query for full-text search
    
</dd>
</dl>

<dl>
<dd>

**search_mode:** `typing.Optional[MessageSearchRequestSearchMode]` — Search mode to use
    
</dd>
</dl>

<dl>
<dd>

**roles:** `typing.Optional[typing.Sequence[MessageRole]]` — Filter messages by role
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Filter messages by project ID
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` — Filter messages by template ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Filter messages created after this date
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — Filter messages created on or before this date
    
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

**messages:** `typing.Sequence[LettaAsyncRequestMessagesItem]` — The messages to be sent to the agent.
    
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

**enable_thinking:** `typing.Optional[str]` — If set to True, enables reasoning before responses or tool calls from the agent.
    
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

<details><summary><code>client.agents.messages.<a href="src/letta_client/agents/messages/client.py">preview</a>(...)</code></summary>
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
client.agents.messages.preview(
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

**request:** `MessagesPreviewRequest` 
    
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

<details><summary><code>client.agents.messages.<a href="src/letta_client/agents/messages/client.py">summarize</a>(...)</code></summary>
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
client.agents.messages.summarize(
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

**preserve_tool_variables:** `typing.Optional[bool]` — If true, preserves the existing agent's tool environment variables instead of using the template's variables
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

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

## Batches Messages
<details><summary><code>client.batches.messages.<a href="src/letta_client/batches/messages/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get response messages for a specific batch job.
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
client.batches.messages.list(
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

**before:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[MessagesListRequestOrder]` — Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Field to sort by
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Filter messages by agent ID
    
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

**before:** `typing.Optional[str]` — Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of agents to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[AgentsListRequestOrder]` — Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Field to sort by
    
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

## Folders Files
<details><summary><code>client.folders.files.<a href="src/letta_client/folders/files/client.py">upload</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a file to a data folder.
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
client.folders.files.upload(
    folder_id="folder_id",
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

**folder_id:** `str` 
    
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

**name:** `typing.Optional[str]` — Optional custom name to override the uploaded file's name
    
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

<details><summary><code>client.folders.files.<a href="src/letta_client/folders/files/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List paginated files associated with a data folder.
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
client.folders.files.list(
    folder_id="folder_id",
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

**folder_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — File ID cursor for pagination. Returns files that come before this file ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — File ID cursor for pagination. Returns files that come after this file ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of files to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[FilesListRequestOrder]` — Sort order for files by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Field to sort by
    
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

<details><summary><code>client.folders.files.<a href="src/letta_client/folders/files/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a file from a folder.
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
client.folders.files.delete(
    folder_id="folder_id",
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

**folder_id:** `str` 
    
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

## Folders Agents
<details><summary><code>client.folders.agents.<a href="src/letta_client/folders/agents/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all agent IDs that have the specified folder attached.
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
client.folders.agents.list(
    folder_id="folder_id",
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

**folder_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of agents to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[AgentsListRequestOrder]` — Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Field to sort by
    
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

## Folders Passages
<details><summary><code>client.folders.passages.<a href="src/letta_client/folders/passages/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all passages associated with a data folder.
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
client.folders.passages.list(
    folder_id="folder_id",
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

**folder_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Passage ID cursor for pagination. Returns passages that come before this passage ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Passage ID cursor for pagination. Returns passages that come after this passage ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of passages to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[PassagesListRequestOrder]` — Sort order for passages by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Field to sort by
    
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

**before:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to retrieve
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[MessagesListRequestOrder]` — Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Field to sort by
    
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
                    text="The sky above the port was the color of television, tuned to a dead channel.",
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

**messages:** `typing.Sequence[LettaRequestMessagesItem]` — The messages to be sent to the agent.
    
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

**enable_thinking:** `typing.Optional[str]` — If set to True, enables reasoning before responses or tool calls from the agent.
    
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
                    text="The sky above the port was the color of television, tuned to a dead channel.",
                )
            ],
        )
    ],
)
for chunk in response.data:
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

**messages:** `typing.Sequence[LettaStreamingRequestMessagesItem]` — The messages to be sent to the agent.
    
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

**enable_thinking:** `typing.Optional[str]` — If set to True, enables reasoning before responses or tool calls from the agent.
    
</dd>
</dl>

<dl>
<dd>

**stream_tokens:** `typing.Optional[bool]` — Flag to determine if individual tokens should be streamed, rather than streaming per step.
    
</dd>
</dl>

<dl>
<dd>

**include_pings:** `typing.Optional[bool]` — Whether to include periodic keepalive ping messages in the stream to prevent connection timeouts.
    
</dd>
</dl>

<dl>
<dd>

**background:** `typing.Optional[bool]` — Whether to process the request in the background.
    
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

## Identities Agents
<details><summary><code>client.identities.agents.<a href="src/letta_client/identities/agents/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all agents associated with the specified identity.
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
client.identities.agents.list(
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

**before:** `typing.Optional[str]` — Agent ID cursor for pagination. Returns agents that come before this agent ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Agent ID cursor for pagination. Returns agents that come after this agent ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of agents to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[AgentsListRequestOrder]` — Sort order for agents by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Field to sort by
    
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

## Identities Blocks
<details><summary><code>client.identities.blocks.<a href="src/letta_client/identities/blocks/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all blocks associated with the specified identity.
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
client.identities.blocks.list(
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

**before:** `typing.Optional[str]` — Block ID cursor for pagination. Returns blocks that come before this block ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Block ID cursor for pagination. Returns blocks that come after this block ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of blocks to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[BlocksListRequestOrder]` — Sort order for blocks by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Field to sort by
    
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

## Models Embeddings
<details><summary><code>client.models.embeddings.<a href="src/letta_client/models/embeddings/client.py">list</a>()</code></summary>
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
client.models.embeddings.list()

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

## Runs Messages
<details><summary><code>client.runs.messages.<a href="src/letta_client/runs/messages/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get response messages associated with a run.
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

**before:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[MessagesListRequestOrder]` — Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first
    
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

**name:** `typing.Optional[str]` — Optional custom name to override the uploaded file's name
    
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

**check_status_updates:** `typing.Optional[bool]` — Whether to check and update file processing status (from the vector db service). If False, will not fetch and update the status, which may lead to performance gains.
    
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

## Steps Metrics
<details><summary><code>client.steps.metrics.<a href="src/letta_client/steps/metrics/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get step metrics by step ID.
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
client.steps.metrics.retrieve(
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

## Steps Trace
<details><summary><code>client.steps.trace.<a href="src/letta_client/steps/trace/client.py">retrieve</a>(...)</code></summary>
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
client.steps.trace.retrieve(
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

## Steps Feedback
<details><summary><code>client.steps.feedback.<a href="src/letta_client/steps/feedback/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify feedback for a given step.
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

**feedback:** `typing.Optional[FeedbackType]` — Whether this feedback is positive or negative
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Feedback tags to add to the step
    
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

## Steps Messages
<details><summary><code>client.steps.messages.<a href="src/letta_client/steps/messages/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List messages for a given step.
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
client.steps.messages.list(
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

**before:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come before this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Message ID cursor for pagination. Returns messages that come after this message ID in the specified sort order
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to return
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[MessagesListRequestOrder]` — Sort order for messages by creation time. 'asc' for oldest first, 'desc' for newest first
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[typing.Literal["created_at"]]` — Sort by field
    
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

**project:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**template_version:** `str` 
    
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

