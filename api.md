# Shared Types

```python
from letta.types import Block, Job
```

# Agents

Types:

```python
from letta.types import (
    Agentstate,
    AgentState,
    Archivalmemorysummary,
    Contextwindowoverview,
    Memory,
    Recallmemorysummary,
    AgentListResponse,
    AgentDeleteResponse,
    AgentMigrateResponse,
    AgentVersionTemplateResponse,
)
```

Methods:

- <code title="post /v1/agents/">client.agents.<a href="./src/letta/resources/agents/agents.py">create</a>(\*\*<a href="src/letta/types/agent_create_params.py">params</a>) -> <a href="./src/letta/types/agent_state.py">AgentState</a></code>
- <code title="get /v1/agents/{agent_id}">client.agents.<a href="./src/letta/resources/agents/agents.py">retrieve</a>(agent_id) -> <a href="./src/letta/types/agent_state.py">AgentState</a></code>
- <code title="patch /v1/agents/{agent_id}">client.agents.<a href="./src/letta/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/letta/types/agent_update_params.py">params</a>) -> <a href="./src/letta/types/agent_state.py">AgentState</a></code>
- <code title="get /v1/agents/">client.agents.<a href="./src/letta/resources/agents/agents.py">list</a>(\*\*<a href="src/letta/types/agent_list_params.py">params</a>) -> <a href="./src/letta/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /v1/agents/{agent_id}">client.agents.<a href="./src/letta/resources/agents/agents.py">delete</a>(agent_id) -> <a href="./src/letta/types/agent_delete_response.py">object</a></code>
- <code title="patch /v1/agents/{agent_id}/add-tool/{tool_id}">client.agents.<a href="./src/letta/resources/agents/agents.py">add_tool</a>(tool_id, \*, agent_id) -> <a href="./src/letta/types/agent_state.py">AgentState</a></code>
- <code title="get /v1/agents/{agent_id}/context">client.agents.<a href="./src/letta/resources/agents/agents.py">context</a>(agent_id) -> <a href="./src/letta/types/contextwindowoverview.py">Contextwindowoverview</a></code>
- <code title="post /v1/agents/{agent_id}/migrate">client.agents.<a href="./src/letta/resources/agents/agents.py">migrate</a>(agent_id, \*\*<a href="src/letta/types/agent_migrate_params.py">params</a>) -> <a href="./src/letta/types/agent_migrate_response.py">AgentMigrateResponse</a></code>
- <code title="patch /v1/agents/{agent_id}/remove-tool/{tool_id}">client.agents.<a href="./src/letta/resources/agents/agents.py">remove_tool</a>(tool_id, \*, agent_id) -> <a href="./src/letta/types/agent_state.py">AgentState</a></code>
- <code title="post /v1/agents/{agent_id}/version-template">client.agents.<a href="./src/letta/resources/agents/agents.py">version_template</a>(agent_id, \*\*<a href="src/letta/types/agent_version_template_params.py">params</a>) -> <a href="./src/letta/types/agent_version_template_response.py">AgentVersionTemplateResponse</a></code>

## Messages

Types:

```python
from letta.types.agents import MessageCreateResponse, MessageListResponse
```

Methods:

- <code title="post /v1/agents/{agent_id}/messages">client.agents.messages.<a href="./src/letta/resources/agents/messages.py">create</a>(agent_id, \*\*<a href="src/letta/types/agents/message_create_params.py">params</a>) -> <a href="./src/letta/types/agents/message_create_response.py">MessageCreateResponse</a></code>
- <code title="patch /v1/agents/{agent_id}/messages/{message_id}">client.agents.messages.<a href="./src/letta/resources/agents/messages.py">update</a>(message_id, \*, agent_id, \*\*<a href="src/letta/types/agents/message_update_params.py">params</a>) -> <a href="./src/letta/types/agents/memory/messageoutput.py">Messageoutput</a></code>
- <code title="get /v1/agents/{agent_id}/messages">client.agents.messages.<a href="./src/letta/resources/agents/messages.py">list</a>(agent_id, \*\*<a href="src/letta/types/agents/message_list_params.py">params</a>) -> <a href="./src/letta/types/agents/message_list_response.py">MessageListResponse</a></code>

## Tools

Types:

```python
from letta.types.agents import ToolRetrieveResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/tools">client.agents.tools.<a href="./src/letta/resources/agents/tools.py">retrieve</a>(agent_id) -> <a href="./src/letta/types/agents/tool_retrieve_response.py">ToolRetrieveResponse</a></code>

## Sources

Types:

```python
from letta.types.agents import SourceRetrieveResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/sources">client.agents.sources.<a href="./src/letta/resources/agents/sources.py">retrieve</a>(agent_id) -> <a href="./src/letta/types/agents/source_retrieve_response.py">SourceRetrieveResponse</a></code>

## Memory

Methods:

- <code title="get /v1/agents/{agent_id}/memory">client.agents.memory.<a href="./src/letta/resources/agents/memory/memory.py">retrieve</a>(agent_id) -> <a href="./src/letta/types/memory.py">Memory</a></code>
- <code title="patch /v1/agents/{agent_id}/memory">client.agents.memory.<a href="./src/letta/resources/agents/memory/memory.py">update</a>(agent_id, \*\*<a href="src/letta/types/agents/memory_update_params.py">params</a>) -> <a href="./src/letta/types/memory.py">Memory</a></code>

### Messages

Types:

```python
from letta.types.agents.memory import Messageoutput, MessageRetrieveResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/memory/messages">client.agents.memory.messages.<a href="./src/letta/resources/agents/memory/messages.py">retrieve</a>(agent_id) -> <a href="./src/letta/types/agents/memory/message_retrieve_response.py">MessageRetrieveResponse</a></code>

### Label

Methods:

- <code title="patch /v1/agents/{agent_id}/memory/label">client.agents.memory.label.<a href="./src/letta/resources/agents/memory/label.py">update</a>(agent_id, \*\*<a href="src/letta/types/agents/memory/label_update_params.py">params</a>) -> <a href="./src/letta/types/memory.py">Memory</a></code>

### Block

Methods:

- <code title="post /v1/agents/{agent_id}/memory/block">client.agents.memory.block.<a href="./src/letta/resources/agents/memory/block.py">create</a>(agent_id, \*\*<a href="src/letta/types/agents/memory/block_create_params.py">params</a>) -> <a href="./src/letta/types/memory.py">Memory</a></code>
- <code title="delete /v1/agents/{agent_id}/memory/block/{block_label}">client.agents.memory.block.<a href="./src/letta/resources/agents/memory/block.py">delete</a>(block_label, \*, agent_id) -> <a href="./src/letta/types/memory.py">Memory</a></code>

### Limit

Methods:

- <code title="patch /v1/agents/{agent_id}/memory/limit">client.agents.memory.limit.<a href="./src/letta/resources/agents/memory/limit.py">update</a>(agent_id, \*\*<a href="src/letta/types/agents/memory/limit_update_params.py">params</a>) -> <a href="./src/letta/types/memory.py">Memory</a></code>

### Recall

Methods:

- <code title="get /v1/agents/{agent_id}/memory/recall">client.agents.memory.recall.<a href="./src/letta/resources/agents/memory/recall.py">retrieve</a>(agent_id) -> <a href="./src/letta/types/recallmemorysummary.py">Recallmemorysummary</a></code>

### Archival

Methods:

- <code title="get /v1/agents/{agent_id}/memory/archival">client.agents.memory.archival.<a href="./src/letta/resources/agents/memory/archival.py">retrieve</a>(agent_id) -> <a href="./src/letta/types/archivalmemorysummary.py">Archivalmemorysummary</a></code>

## Archival

Types:

```python
from letta.types.agents import (
    ArchivalCreateResponse,
    ArchivalRetrieveResponse,
    ArchivalDeleteResponse,
)
```

Methods:

- <code title="post /v1/agents/{agent_id}/archival">client.agents.archival.<a href="./src/letta/resources/agents/archival.py">create</a>(agent_id, \*\*<a href="src/letta/types/agents/archival_create_params.py">params</a>) -> <a href="./src/letta/types/agents/archival_create_response.py">ArchivalCreateResponse</a></code>
- <code title="get /v1/agents/{agent_id}/archival">client.agents.archival.<a href="./src/letta/resources/agents/archival.py">retrieve</a>(agent_id, \*\*<a href="src/letta/types/agents/archival_retrieve_params.py">params</a>) -> <a href="./src/letta/types/agents/archival_retrieve_response.py">ArchivalRetrieveResponse</a></code>
- <code title="delete /v1/agents/{agent_id}/archival/{memory_id}">client.agents.archival.<a href="./src/letta/resources/agents/archival.py">delete</a>(memory_id, \*, agent_id) -> <a href="./src/letta/types/agents/archival_delete_response.py">object</a></code>

# Tools

Types:

```python
from letta.types import Tool, ToolListResponse, ToolDeleteResponse, ToolAddBaseToolsResponse
```

Methods:

- <code title="post /v1/tools/">client.tools.<a href="./src/letta/resources/tools.py">create</a>(\*\*<a href="src/letta/types/tool_create_params.py">params</a>) -> <a href="./src/letta/types/tool.py">Tool</a></code>
- <code title="get /v1/tools/{tool_id}">client.tools.<a href="./src/letta/resources/tools.py">retrieve</a>(tool_id) -> <a href="./src/letta/types/tool.py">Tool</a></code>
- <code title="patch /v1/tools/{tool_id}">client.tools.<a href="./src/letta/resources/tools.py">update</a>(tool_id, \*\*<a href="src/letta/types/tool_update_params.py">params</a>) -> <a href="./src/letta/types/tool.py">Tool</a></code>
- <code title="get /v1/tools/">client.tools.<a href="./src/letta/resources/tools.py">list</a>(\*\*<a href="src/letta/types/tool_list_params.py">params</a>) -> <a href="./src/letta/types/tool_list_response.py">ToolListResponse</a></code>
- <code title="delete /v1/tools/{tool_id}">client.tools.<a href="./src/letta/resources/tools.py">delete</a>(tool_id) -> <a href="./src/letta/types/tool_delete_response.py">object</a></code>
- <code title="post /v1/tools/add-base-tools">client.tools.<a href="./src/letta/resources/tools.py">add_base_tools</a>() -> <a href="./src/letta/types/tool_add_base_tools_response.py">ToolAddBaseToolsResponse</a></code>

# ToolsName

Types:

```python
from letta.types import ToolsNameRetrieveResponse
```

Methods:

- <code title="get /v1/tools/name/{tool_name}">client.tools_name.<a href="./src/letta/resources/tools_name.py">retrieve</a>(tool_name) -> str</code>

# Sources

Types:

```python
from letta.types import Source, SourceListResponse, SourceDeleteResponse
```

Methods:

- <code title="post /v1/sources/">client.sources.<a href="./src/letta/resources/sources/sources.py">create</a>(\*\*<a href="src/letta/types/source_create_params.py">params</a>) -> <a href="./src/letta/types/source.py">Source</a></code>
- <code title="get /v1/sources/{source_id}">client.sources.<a href="./src/letta/resources/sources/sources.py">retrieve</a>(source_id) -> <a href="./src/letta/types/source.py">Source</a></code>
- <code title="patch /v1/sources/{source_id}">client.sources.<a href="./src/letta/resources/sources/sources.py">update</a>(source_id, \*\*<a href="src/letta/types/source_update_params.py">params</a>) -> <a href="./src/letta/types/source.py">Source</a></code>
- <code title="get /v1/sources/">client.sources.<a href="./src/letta/resources/sources/sources.py">list</a>() -> <a href="./src/letta/types/source_list_response.py">SourceListResponse</a></code>
- <code title="delete /v1/sources/{source_id}">client.sources.<a href="./src/letta/resources/sources/sources.py">delete</a>(source_id) -> <a href="./src/letta/types/source_delete_response.py">object</a></code>
- <code title="post /v1/sources/{source_id}/attach">client.sources.<a href="./src/letta/resources/sources/sources.py">attach</a>(source_id, \*\*<a href="src/letta/types/source_attach_params.py">params</a>) -> <a href="./src/letta/types/source.py">Source</a></code>
- <code title="post /v1/sources/{source_id}/detach">client.sources.<a href="./src/letta/resources/sources/sources.py">detach</a>(source_id, \*\*<a href="src/letta/types/source_detach_params.py">params</a>) -> <a href="./src/letta/types/source.py">Source</a></code>
- <code title="post /v1/sources/{source_id}/upload">client.sources.<a href="./src/letta/resources/sources/sources.py">upload</a>(source_id, \*\*<a href="src/letta/types/source_upload_params.py">params</a>) -> <a href="./src/letta/types/shared/job.py">Job</a></code>

## Passages

Types:

```python
from letta.types.sources import Passage, PassageListResponse
```

Methods:

- <code title="get /v1/sources/{source_id}/passages">client.sources.passages.<a href="./src/letta/resources/sources/passages.py">list</a>(source_id) -> <a href="./src/letta/types/sources/passage_list_response.py">PassageListResponse</a></code>

## Files

Types:

```python
from letta.types.sources import Filemetadata, FileListResponse
```

Methods:

- <code title="get /v1/sources/{source_id}/files">client.sources.files.<a href="./src/letta/resources/sources/files.py">list</a>(source_id, \*\*<a href="src/letta/types/sources/file_list_params.py">params</a>) -> <a href="./src/letta/types/sources/file_list_response.py">FileListResponse</a></code>
- <code title="delete /v1/sources/{source_id}/{file_id}">client.sources.files.<a href="./src/letta/resources/sources/files.py">delete</a>(file_id, \*, source_id) -> None</code>

# Models

Types:

```python
from letta.types import Embeddingconfig, Llmconfig, ModelListResponse
```

Methods:

- <code title="get /v1/models/">client.models.<a href="./src/letta/resources/models/models.py">list</a>() -> <a href="./src/letta/types/model_list_response.py">ModelListResponse</a></code>

## Embedding

Types:

```python
from letta.types.models import EmbeddingRetrieveResponse
```

Methods:

- <code title="get /v1/models/embedding">client.models.embedding.<a href="./src/letta/resources/models/embedding.py">retrieve</a>() -> <a href="./src/letta/types/models/embedding_retrieve_response.py">EmbeddingRetrieveResponse</a></code>

# Blocks

Types:

```python
from letta.types import Block, BlockListResponse
```

Methods:

- <code title="post /v1/blocks/">client.blocks.<a href="./src/letta/resources/blocks.py">create</a>(\*\*<a href="src/letta/types/block_create_params.py">params</a>) -> <a href="./src/letta/types/block.py">Block</a></code>
- <code title="get /v1/blocks/{block_id}">client.blocks.<a href="./src/letta/resources/blocks.py">retrieve</a>(block_id) -> <a href="./src/letta/types/block.py">Block</a></code>
- <code title="patch /v1/blocks/{block_id}">client.blocks.<a href="./src/letta/resources/blocks.py">update</a>(block_id, \*\*<a href="src/letta/types/block_update_params.py">params</a>) -> <a href="./src/letta/types/block.py">Block</a></code>
- <code title="get /v1/blocks/">client.blocks.<a href="./src/letta/resources/blocks.py">list</a>(\*\*<a href="src/letta/types/block_list_params.py">params</a>) -> <a href="./src/letta/types/block_list_response.py">BlockListResponse</a></code>
- <code title="delete /v1/blocks/{block_id}">client.blocks.<a href="./src/letta/resources/blocks.py">delete</a>(block_id) -> <a href="./src/letta/types/block.py">Block</a></code>

# Jobs

Types:

```python
from letta.types import JobListResponse
```

Methods:

- <code title="get /v1/jobs/{job_id}">client.jobs.<a href="./src/letta/resources/jobs/jobs.py">retrieve</a>(job_id) -> <a href="./src/letta/types/shared/job.py">Job</a></code>
- <code title="get /v1/jobs/">client.jobs.<a href="./src/letta/resources/jobs/jobs.py">list</a>(\*\*<a href="src/letta/types/job_list_params.py">params</a>) -> <a href="./src/letta/types/job_list_response.py">JobListResponse</a></code>
- <code title="delete /v1/jobs/{job_id}">client.jobs.<a href="./src/letta/resources/jobs/jobs.py">delete</a>(job_id) -> <a href="./src/letta/types/shared/job.py">Job</a></code>

## Active

Types:

```python
from letta.types.jobs import ActiveListResponse
```

Methods:

- <code title="get /v1/jobs/active">client.jobs.active.<a href="./src/letta/resources/jobs/active.py">list</a>() -> <a href="./src/letta/types/jobs/active_list_response.py">ActiveListResponse</a></code>

# Health

Types:

```python
from letta.types import Health
```

Methods:

- <code title="get /v1/health/">client.health.<a href="./src/letta/resources/health.py">retrieve</a>() -> <a href="./src/letta/types/health.py">Health</a></code>
