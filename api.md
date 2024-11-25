# Shared Types

```python
from letta.types import Block, Job
```

# Tools

Types:

```python
from letta.types import (
    Tool,
    ToolListResponse,
    ToolDeleteResponse,
    ToolAddBaseToolsResponse,
    ToolRetrieveByNameResponse,
)
```

Methods:

- <code title="post /v1/tools/">client.tools.<a href="./src/letta/resources/tools.py">create</a>(\*\*<a href="src/letta/types/tool_create_params.py">params</a>) -> <a href="./src/letta/types/tool.py">Tool</a></code>
- <code title="get /v1/tools/{tool_id}">client.tools.<a href="./src/letta/resources/tools.py">retrieve</a>(tool_id) -> <a href="./src/letta/types/tool.py">Tool</a></code>
- <code title="patch /v1/tools/{tool_id}">client.tools.<a href="./src/letta/resources/tools.py">update</a>(tool_id, \*\*<a href="src/letta/types/tool_update_params.py">params</a>) -> <a href="./src/letta/types/tool.py">Tool</a></code>
- <code title="get /v1/tools/">client.tools.<a href="./src/letta/resources/tools.py">list</a>(\*\*<a href="src/letta/types/tool_list_params.py">params</a>) -> <a href="./src/letta/types/tool_list_response.py">ToolListResponse</a></code>
- <code title="delete /v1/tools/{tool_id}">client.tools.<a href="./src/letta/resources/tools.py">delete</a>(tool_id) -> <a href="./src/letta/types/tool_delete_response.py">object</a></code>
- <code title="post /v1/tools/add-base-tools">client.tools.<a href="./src/letta/resources/tools.py">add_base_tools</a>() -> <a href="./src/letta/types/tool_add_base_tools_response.py">ToolAddBaseToolsResponse</a></code>
- <code title="get /v1/tools/name/{tool_name}">client.tools.<a href="./src/letta/resources/tools.py">retrieve_by_name</a>(tool_name) -> str</code>

# Sources

Types:

```python
from letta.types import FileMetadata, Passage, Source, SourceRetrieveResponse, SourceListResponse
```

Methods:

- <code title="post /v1/sources/">client.sources.<a href="./src/letta/resources/sources/sources.py">create</a>(\*\*<a href="src/letta/types/source_create_params.py">params</a>) -> <a href="./src/letta/types/source.py">Source</a></code>
- <code title="get /v1/sources/name/{source_name}">client.sources.<a href="./src/letta/resources/sources/sources.py">retrieve</a>(source_name) -> str</code>
- <code title="patch /v1/sources/{source_id}">client.sources.<a href="./src/letta/resources/sources/sources.py">update</a>(source_id, \*\*<a href="src/letta/types/source_update_params.py">params</a>) -> <a href="./src/letta/types/source.py">Source</a></code>
- <code title="get /v1/sources/">client.sources.<a href="./src/letta/resources/sources/sources.py">list</a>() -> <a href="./src/letta/types/source_list_response.py">SourceListResponse</a></code>
- <code title="delete /v1/sources/{source_id}/{file_id}">client.sources.<a href="./src/letta/resources/sources/sources.py">delete</a>(file_id, \*, source_id) -> None</code>
- <code title="post /v1/sources/{source_id}/attach">client.sources.<a href="./src/letta/resources/sources/sources.py">attach</a>(source_id, \*\*<a href="src/letta/types/source_attach_params.py">params</a>) -> <a href="./src/letta/types/source.py">Source</a></code>
- <code title="post /v1/sources/{source_id}/detach">client.sources.<a href="./src/letta/resources/sources/sources.py">detach</a>(source_id, \*\*<a href="src/letta/types/source_detach_params.py">params</a>) -> <a href="./src/letta/types/source.py">Source</a></code>
- <code title="post /v1/sources/{source_id}/upload">client.sources.<a href="./src/letta/resources/sources/sources.py">upload</a>(source_id, \*\*<a href="src/letta/types/source_upload_params.py">params</a>) -> <a href="./src/letta/types/shared/job.py">Job</a></code>

## Passages

Types:

```python
from letta.types.sources import PassageListResponse
```

Methods:

- <code title="get /v1/sources/{source_id}/passages">client.sources.passages.<a href="./src/letta/resources/sources/passages.py">list</a>(source_id) -> <a href="./src/letta/types/sources/passage_list_response.py">PassageListResponse</a></code>

## Files

Types:

```python
from letta.types.sources import FileListResponse
```

Methods:

- <code title="get /v1/sources/{source_id}/files">client.sources.files.<a href="./src/letta/resources/sources/files.py">list</a>(source_id, \*\*<a href="src/letta/types/sources/file_list_params.py">params</a>) -> <a href="./src/letta/types/sources/file_list_response.py">FileListResponse</a></code>

# Agents

Types:

```python
from letta.types import AgentState, AgentListResponse, AgentDeleteResponse, AgentMigrateResponse
```

Methods:

- <code title="post /v1/agents/">client.agents.<a href="./src/letta/resources/agents/agents.py">create</a>(\*\*<a href="src/letta/types/agent_create_params.py">params</a>) -> <a href="./src/letta/types/agent_state.py">AgentState</a></code>
- <code title="get /v1/agents/{agent_id}">client.agents.<a href="./src/letta/resources/agents/agents.py">retrieve</a>(agent_id) -> <a href="./src/letta/types/agent_state.py">AgentState</a></code>
- <code title="patch /v1/agents/{agent_id}">client.agents.<a href="./src/letta/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/letta/types/agent_update_params.py">params</a>) -> <a href="./src/letta/types/agent_state.py">AgentState</a></code>
- <code title="get /v1/agents/">client.agents.<a href="./src/letta/resources/agents/agents.py">list</a>(\*\*<a href="src/letta/types/agent_list_params.py">params</a>) -> <a href="./src/letta/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /v1/agents/{agent_id}">client.agents.<a href="./src/letta/resources/agents/agents.py">delete</a>(agent_id) -> <a href="./src/letta/types/agent_delete_response.py">object</a></code>
- <code title="post /v1/agents/{agent_id}/migrate">client.agents.<a href="./src/letta/resources/agents/agents.py">migrate</a>(agent_id, \*\*<a href="src/letta/types/agent_migrate_params.py">params</a>) -> <a href="./src/letta/types/agent_migrate_response.py">AgentMigrateResponse</a></code>

## Messages

Types:

```python
from letta.types.agents import MessageCreateResponse, MessageUpdateResponse, MessageListResponse
```

Methods:

- <code title="post /v1/agents/{agent_id}/messages">client.agents.messages.<a href="./src/letta/resources/agents/messages.py">create</a>(agent_id, \*\*<a href="src/letta/types/agents/message_create_params.py">params</a>) -> <a href="./src/letta/types/agents/message_create_response.py">MessageCreateResponse</a></code>
- <code title="patch /v1/agents/{agent_id}/messages/{message_id}">client.agents.messages.<a href="./src/letta/resources/agents/messages.py">update</a>(message_id, \*, agent_id, \*\*<a href="src/letta/types/agents/message_update_params.py">params</a>) -> <a href="./src/letta/types/agents/message_update_response.py">MessageUpdateResponse</a></code>
- <code title="get /v1/agents/{agent_id}/messages">client.agents.messages.<a href="./src/letta/resources/agents/messages.py">list</a>(agent_id, \*\*<a href="src/letta/types/agents/message_list_params.py">params</a>) -> <a href="./src/letta/types/agents/message_list_response.py">MessageListResponse</a></code>
