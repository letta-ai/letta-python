# Shared Types

```python
from letta_client.types import Job
```

# Tools

Types:

```python
from letta_client.types import (
    ToolCreateResponse,
    ToolRetrieveResponse,
    ToolUpdateResponse,
    ToolListResponse,
    ToolDeleteResponse,
    ToolRetrieveByNameResponse,
)
```

Methods:

- <code title="post /v1/tools/">client.tools.<a href="./src/letta_client/resources/tools.py">create</a>(\*\*<a href="src/letta_client/types/tool_create_params.py">params</a>) -> <a href="./src/letta_client/types/tool_create_response.py">ToolCreateResponse</a></code>
- <code title="get /v1/tools/{tool_id}">client.tools.<a href="./src/letta_client/resources/tools.py">retrieve</a>(tool_id) -> <a href="./src/letta_client/types/tool_retrieve_response.py">ToolRetrieveResponse</a></code>
- <code title="patch /v1/tools/{tool_id}">client.tools.<a href="./src/letta_client/resources/tools.py">update</a>(tool_id, \*\*<a href="src/letta_client/types/tool_update_params.py">params</a>) -> <a href="./src/letta_client/types/tool_update_response.py">ToolUpdateResponse</a></code>
- <code title="get /v1/tools/">client.tools.<a href="./src/letta_client/resources/tools.py">list</a>() -> <a href="./src/letta_client/types/tool_list_response.py">ToolListResponse</a></code>
- <code title="delete /v1/tools/{tool_id}">client.tools.<a href="./src/letta_client/resources/tools.py">delete</a>(tool_id) -> <a href="./src/letta_client/types/tool_delete_response.py">object</a></code>
- <code title="get /v1/tools/name/{tool_name}">client.tools.<a href="./src/letta_client/resources/tools.py">retrieve_by_name</a>(tool_name) -> str</code>

# Sources

Types:

```python
from letta_client.types import (
    Source,
    SourceRetrieveResponse,
    SourceListResponse,
    SourceDeleteResponse,
)
```

Methods:

- <code title="post /v1/sources/">client.sources.<a href="./src/letta_client/resources/sources/sources.py">create</a>(\*\*<a href="src/letta_client/types/source_create_params.py">params</a>) -> <a href="./src/letta_client/types/source.py">Source</a></code>
- <code title="get /v1/sources/name/{source_name}">client.sources.<a href="./src/letta_client/resources/sources/sources.py">retrieve</a>(source_name) -> str</code>
- <code title="patch /v1/sources/{source_id}">client.sources.<a href="./src/letta_client/resources/sources/sources.py">update</a>(source_id, \*\*<a href="src/letta_client/types/source_update_params.py">params</a>) -> <a href="./src/letta_client/types/source.py">Source</a></code>
- <code title="get /v1/sources/">client.sources.<a href="./src/letta_client/resources/sources/sources.py">list</a>() -> <a href="./src/letta_client/types/source_list_response.py">SourceListResponse</a></code>
- <code title="delete /v1/sources/{source_id}">client.sources.<a href="./src/letta_client/resources/sources/sources.py">delete</a>(source_id) -> <a href="./src/letta_client/types/source_delete_response.py">object</a></code>
- <code title="post /v1/sources/{source_id}/attach">client.sources.<a href="./src/letta_client/resources/sources/sources.py">attach</a>(source_id, \*\*<a href="src/letta_client/types/source_attach_params.py">params</a>) -> <a href="./src/letta_client/types/source.py">Source</a></code>
- <code title="post /v1/sources/{source_id}/detach">client.sources.<a href="./src/letta_client/resources/sources/sources.py">detach</a>(source_id, \*\*<a href="src/letta_client/types/source_detach_params.py">params</a>) -> <a href="./src/letta_client/types/source.py">Source</a></code>
- <code title="post /v1/sources/{source_id}/upload">client.sources.<a href="./src/letta_client/resources/sources/sources.py">upload</a>(source_id, \*\*<a href="src/letta_client/types/source_upload_params.py">params</a>) -> <a href="./src/letta_client/types/shared/job.py">Job</a></code>

## Passages

Types:

```python
from letta_client.types.sources import Passage, PassageListResponse
```

Methods:

- <code title="get /v1/sources/{source_id}/passages">client.sources.passages.<a href="./src/letta_client/resources/sources/passages.py">list</a>(source_id) -> <a href="./src/letta_client/types/sources/passage_list_response.py">PassageListResponse</a></code>

## Files

Types:

```python
from letta_client.types.sources import FileMetadata, FileListResponse
```

Methods:

- <code title="get /v1/sources/{source_id}/files">client.sources.files.<a href="./src/letta_client/resources/sources/files.py">list</a>(source_id, \*\*<a href="src/letta_client/types/sources/file_list_params.py">params</a>) -> <a href="./src/letta_client/types/sources/file_list_response.py">FileListResponse</a></code>
- <code title="delete /v1/sources/{source_id}/{file_id}">client.sources.files.<a href="./src/letta_client/resources/sources/files.py">delete</a>(file_id, \*, source_id) -> None</code>

# Agents

Types:

```python
from letta_client.types import (
    AgentState,
    Memory,
    AgentListResponse,
    AgentDeleteResponse,
    AgentMigrateResponse,
)
```

Methods:

- <code title="post /v1/agents/">client.agents.<a href="./src/letta_client/resources/agents/agents.py">create</a>(\*\*<a href="src/letta_client/types/agent_create_params.py">params</a>) -> <a href="./src/letta_client/types/agent_state.py">AgentState</a></code>
- <code title="get /v1/agents/{agent_id}">client.agents.<a href="./src/letta_client/resources/agents/agents.py">retrieve</a>(agent_id) -> <a href="./src/letta_client/types/agent_state.py">AgentState</a></code>
- <code title="patch /v1/agents/{agent_id}">client.agents.<a href="./src/letta_client/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/letta_client/types/agent_update_params.py">params</a>) -> <a href="./src/letta_client/types/agent_state.py">AgentState</a></code>
- <code title="get /v1/agents/">client.agents.<a href="./src/letta_client/resources/agents/agents.py">list</a>() -> <a href="./src/letta_client/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /v1/agents/{agent_id}">client.agents.<a href="./src/letta_client/resources/agents/agents.py">delete</a>(agent_id) -> <a href="./src/letta_client/types/agent_delete_response.py">object</a></code>
- <code title="post /v1/agents/{agent_id}/migrate">client.agents.<a href="./src/letta_client/resources/agents/agents.py">migrate</a>(agent_id, \*\*<a href="src/letta_client/types/agent_migrate_params.py">params</a>) -> <a href="./src/letta_client/types/agent_migrate_response.py">AgentMigrateResponse</a></code>

## Context

Types:

```python
from letta_client.types.agents import ContextWindowOverview
```

Methods:

- <code title="get /v1/agents/{agent_id}/context">client.agents.context.<a href="./src/letta_client/resources/agents/context.py">retrieve</a>(agent_id) -> <a href="./src/letta_client/types/agents/context_window_overview.py">ContextWindowOverview</a></code>

## Tools

Methods:

- <code title="patch /v1/agents/{agent_id}/add-tool/{tool_id}">client.agents.tools.<a href="./src/letta_client/resources/agents/tools.py">add</a>(tool_id, \*, agent_id) -> <a href="./src/letta_client/types/agent_state.py">AgentState</a></code>
- <code title="patch /v1/agents/{agent_id}/remove-tool/{tool_id}">client.agents.tools.<a href="./src/letta_client/resources/agents/tools.py">remove</a>(tool_id, \*, agent_id) -> <a href="./src/letta_client/types/agent_state.py">AgentState</a></code>

## Sources

Types:

```python
from letta_client.types.agents import SourceListResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/sources">client.agents.sources.<a href="./src/letta_client/resources/agents/sources.py">list</a>(agent_id) -> <a href="./src/letta_client/types/agents/source_list_response.py">SourceListResponse</a></code>

## Memory

Types:

```python
from letta_client.types.agents import ArchivalMemorySummary, RecallMemorySummary
```

Methods:

- <code title="get /v1/agents/{agent_id}/memory">client.agents.memory.<a href="./src/letta_client/resources/agents/memory/memory.py">retrieve</a>(agent_id) -> <a href="./src/letta_client/types/memory.py">Memory</a></code>
- <code title="patch /v1/agents/{agent_id}/memory">client.agents.memory.<a href="./src/letta_client/resources/agents/memory/memory.py">update</a>(agent_id, \*\*<a href="src/letta_client/types/agents/memory_update_params.py">params</a>) -> <a href="./src/letta_client/types/memory.py">Memory</a></code>

### Messages

Types:

```python
from letta_client.types.agents.memory import MessageRetrieveResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/memory/messages">client.agents.memory.messages.<a href="./src/letta_client/resources/agents/memory/messages.py">retrieve</a>(agent_id) -> <a href="./src/letta_client/types/agents/memory/message_retrieve_response.py">MessageRetrieveResponse</a></code>

### Recall

Methods:

- <code title="get /v1/agents/{agent_id}/memory/recall">client.agents.memory.recall.<a href="./src/letta_client/resources/agents/memory/recall.py">retrieve</a>(agent_id) -> <a href="./src/letta_client/types/agents/recall_memory_summary.py">RecallMemorySummary</a></code>

### Archival

Methods:

- <code title="get /v1/agents/{agent_id}/memory/archival">client.agents.memory.archival.<a href="./src/letta_client/resources/agents/memory/archival.py">retrieve</a>(agent_id) -> <a href="./src/letta_client/types/agents/archival_memory_summary.py">ArchivalMemorySummary</a></code>

## Archival

Types:

```python
from letta_client.types.agents import (
    ArchivalCreateResponse,
    ArchivalListResponse,
    ArchivalDeleteResponse,
)
```

Methods:

- <code title="post /v1/agents/{agent_id}/archival">client.agents.archival.<a href="./src/letta_client/resources/agents/archival.py">create</a>(agent_id, \*\*<a href="src/letta_client/types/agents/archival_create_params.py">params</a>) -> <a href="./src/letta_client/types/agents/archival_create_response.py">ArchivalCreateResponse</a></code>
- <code title="get /v1/agents/{agent_id}/archival">client.agents.archival.<a href="./src/letta_client/resources/agents/archival.py">list</a>(agent_id, \*\*<a href="src/letta_client/types/agents/archival_list_params.py">params</a>) -> <a href="./src/letta_client/types/agents/archival_list_response.py">ArchivalListResponse</a></code>
- <code title="delete /v1/agents/{agent_id}/archival/{memory_id}">client.agents.archival.<a href="./src/letta_client/resources/agents/archival.py">delete</a>(memory_id, \*, agent_id) -> <a href="./src/letta_client/types/agents/archival_delete_response.py">object</a></code>

## Messages

Types:

```python
from letta_client.types.agents import (
    MessageCreateResponse,
    MessageRetrieveResponse,
    MessageUpdateResponse,
)
```

Methods:

- <code title="post /v1/agents/{agent_id}/messages">client.agents.messages.<a href="./src/letta_client/resources/agents/messages.py">create</a>(agent_id, \*\*<a href="src/letta_client/types/agents/message_create_params.py">params</a>) -> <a href="./src/letta_client/types/agents/message_create_response.py">MessageCreateResponse</a></code>
- <code title="get /v1/agents/{agent_id}/messages">client.agents.messages.<a href="./src/letta_client/resources/agents/messages.py">retrieve</a>(agent_id, \*\*<a href="src/letta_client/types/agents/message_retrieve_params.py">params</a>) -> <a href="./src/letta_client/types/agents/message_retrieve_response.py">MessageRetrieveResponse</a></code>
- <code title="patch /v1/agents/{agent_id}/messages/{message_id}">client.agents.messages.<a href="./src/letta_client/resources/agents/messages.py">update</a>(message_id, \*, agent_id, \*\*<a href="src/letta_client/types/agents/message_update_params.py">params</a>) -> <a href="./src/letta_client/types/agents/message_update_response.py">MessageUpdateResponse</a></code>

## VersionTemplate

Types:

```python
from letta_client.types.agents import VersionTemplateCreateResponse
```

Methods:

- <code title="post /v1/agents/{agent_id}/version-template">client.agents.version_template.<a href="./src/letta_client/resources/agents/version_template.py">create</a>(agent_id, \*\*<a href="src/letta_client/types/agents/version_template_create_params.py">params</a>) -> <a href="./src/letta_client/types/agents/version_template_create_response.py">VersionTemplateCreateResponse</a></code>

# Models

Types:

```python
from letta_client.types import EmbeddingConfig, LlmConfig, ModelListResponse, ModelEmbeddingResponse
```

Methods:

- <code title="get /v1/models/">client.models.<a href="./src/letta_client/resources/models.py">list</a>() -> <a href="./src/letta_client/types/model_list_response.py">ModelListResponse</a></code>
- <code title="get /v1/models/embedding">client.models.<a href="./src/letta_client/resources/models.py">embedding</a>() -> <a href="./src/letta_client/types/model_embedding_response.py">ModelEmbeddingResponse</a></code>

# Blocks

Types:

```python
from letta_client.types import Block, BlockListResponse
```

Methods:

- <code title="post /v1/blocks/">client.blocks.<a href="./src/letta_client/resources/blocks.py">create</a>(\*\*<a href="src/letta_client/types/block_create_params.py">params</a>) -> <a href="./src/letta_client/types/block.py">Block</a></code>
- <code title="get /v1/blocks/{block_id}">client.blocks.<a href="./src/letta_client/resources/blocks.py">retrieve</a>(block_id) -> <a href="./src/letta_client/types/block.py">Block</a></code>
- <code title="patch /v1/blocks/{block_id}">client.blocks.<a href="./src/letta_client/resources/blocks.py">update</a>(block_id, \*\*<a href="src/letta_client/types/block_update_params.py">params</a>) -> <a href="./src/letta_client/types/block.py">Block</a></code>
- <code title="get /v1/blocks/">client.blocks.<a href="./src/letta_client/resources/blocks.py">list</a>(\*\*<a href="src/letta_client/types/block_list_params.py">params</a>) -> <a href="./src/letta_client/types/block_list_response.py">BlockListResponse</a></code>
- <code title="delete /v1/blocks/{block_id}">client.blocks.<a href="./src/letta_client/resources/blocks.py">delete</a>(block_id) -> <a href="./src/letta_client/types/block.py">Block</a></code>

# Jobs

Types:

```python
from letta_client.types import JobListResponse, JobActiveResponse
```

Methods:

- <code title="get /v1/jobs/{job_id}">client.jobs.<a href="./src/letta_client/resources/jobs.py">retrieve</a>(job_id) -> <a href="./src/letta_client/types/shared/job.py">Job</a></code>
- <code title="get /v1/jobs/">client.jobs.<a href="./src/letta_client/resources/jobs.py">list</a>(\*\*<a href="src/letta_client/types/job_list_params.py">params</a>) -> <a href="./src/letta_client/types/job_list_response.py">JobListResponse</a></code>
- <code title="delete /v1/jobs/{job_id}">client.jobs.<a href="./src/letta_client/resources/jobs.py">delete</a>(job_id) -> <a href="./src/letta_client/types/shared/job.py">Job</a></code>
- <code title="get /v1/jobs/active">client.jobs.<a href="./src/letta_client/resources/jobs.py">active</a>() -> <a href="./src/letta_client/types/job_active_response.py">JobActiveResponse</a></code>

# Health

Types:

```python
from letta_client.types import Health
```

Methods:

- <code title="get /v1/health/">client.health.<a href="./src/letta_client/resources/health.py">retrieve</a>() -> <a href="./src/letta_client/types/health.py">Health</a></code>
