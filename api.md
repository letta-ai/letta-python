# Shared Types

```python
from letta.types import Job, Memory, Passage, Source, Tool
```

# Tools

Types:

```python
from letta.types import (
    ToolListResponse,
    ToolDeleteResponse,
    ToolAddBaseToolsResponse,
    ToolRetrieveByNameResponse,
)
```

Methods:

- <code title="post /v1/tools/">client.tools.<a href="./src/letta/resources/tools.py">create</a>(\*\*<a href="src/letta/types/tool_create_params.py">params</a>) -> <a href="./src/letta/types/shared/tool.py">Tool</a></code>
- <code title="get /v1/tools/{tool_id}">client.tools.<a href="./src/letta/resources/tools.py">retrieve</a>(tool_id) -> <a href="./src/letta/types/shared/tool.py">Tool</a></code>
- <code title="patch /v1/tools/{tool_id}">client.tools.<a href="./src/letta/resources/tools.py">update</a>(tool_id, \*\*<a href="src/letta/types/tool_update_params.py">params</a>) -> <a href="./src/letta/types/shared/tool.py">Tool</a></code>
- <code title="get /v1/tools/">client.tools.<a href="./src/letta/resources/tools.py">list</a>(\*\*<a href="src/letta/types/tool_list_params.py">params</a>) -> <a href="./src/letta/types/tool_list_response.py">ToolListResponse</a></code>
- <code title="delete /v1/tools/{tool_id}">client.tools.<a href="./src/letta/resources/tools.py">delete</a>(tool_id) -> <a href="./src/letta/types/tool_delete_response.py">object</a></code>
- <code title="post /v1/tools/add-base-tools">client.tools.<a href="./src/letta/resources/tools.py">add_base_tools</a>() -> <a href="./src/letta/types/tool_add_base_tools_response.py">ToolAddBaseToolsResponse</a></code>
- <code title="get /v1/tools/name/{tool_name}">client.tools.<a href="./src/letta/resources/tools.py">retrieve_by_name</a>(tool_name) -> str</code>

# Sources

Types:

```python
from letta.types import SourceListResponse, SourceRetrieveByNameResponse
```

Methods:

- <code title="post /v1/sources/">client.sources.<a href="./src/letta/resources/sources/sources.py">create</a>(\*\*<a href="src/letta/types/source_create_params.py">params</a>) -> <a href="./src/letta/types/shared/source.py">Source</a></code>
- <code title="get /v1/sources/{source_id}">client.sources.<a href="./src/letta/resources/sources/sources.py">retrieve</a>(source_id) -> <a href="./src/letta/types/shared/source.py">Source</a></code>
- <code title="patch /v1/sources/{source_id}">client.sources.<a href="./src/letta/resources/sources/sources.py">update</a>(source_id, \*\*<a href="src/letta/types/source_update_params.py">params</a>) -> <a href="./src/letta/types/shared/source.py">Source</a></code>
- <code title="get /v1/sources/">client.sources.<a href="./src/letta/resources/sources/sources.py">list</a>() -> <a href="./src/letta/types/source_list_response.py">SourceListResponse</a></code>
- <code title="delete /v1/sources/{source_id}/{file_id}">client.sources.<a href="./src/letta/resources/sources/sources.py">delete</a>(file_id, \*, source_id) -> None</code>
- <code title="post /v1/sources/{source_id}/attach">client.sources.<a href="./src/letta/resources/sources/sources.py">attach</a>(source_id, \*\*<a href="src/letta/types/source_attach_params.py">params</a>) -> <a href="./src/letta/types/shared/source.py">Source</a></code>
- <code title="post /v1/sources/{source_id}/detach">client.sources.<a href="./src/letta/resources/sources/sources.py">detach</a>(source_id, \*\*<a href="src/letta/types/source_detach_params.py">params</a>) -> <a href="./src/letta/types/shared/source.py">Source</a></code>
- <code title="get /v1/sources/name/{source_name}">client.sources.<a href="./src/letta/resources/sources/sources.py">retrieve_by_name</a>(source_name) -> str</code>
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
from letta.types.sources import Filemetadata, FileListResponse
```

Methods:

- <code title="get /v1/sources/{source_id}/files">client.sources.files.<a href="./src/letta/resources/sources/files.py">list</a>(source_id, \*\*<a href="src/letta/types/sources/file_list_params.py">params</a>) -> <a href="./src/letta/types/sources/file_list_response.py">FileListResponse</a></code>

# Agents

Types:

```python
from letta.types import Agentstate, AgentListResponse, AgentDeleteResponse
```

Methods:

- <code title="post /v1/agents/">client.agents.<a href="./src/letta/resources/agents/agents.py">create</a>(\*\*<a href="src/letta/types/agent_create_params.py">params</a>) -> <a href="./src/letta/types/agentstate.py">Agentstate</a></code>
- <code title="get /v1/agents/{agent_id}">client.agents.<a href="./src/letta/resources/agents/agents.py">retrieve</a>(agent_id) -> <a href="./src/letta/types/agentstate.py">Agentstate</a></code>
- <code title="patch /v1/agents/{agent_id}">client.agents.<a href="./src/letta/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/letta/types/agent_update_params.py">params</a>) -> <a href="./src/letta/types/agentstate.py">Agentstate</a></code>
- <code title="get /v1/agents/">client.agents.<a href="./src/letta/resources/agents/agents.py">list</a>() -> <a href="./src/letta/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /v1/agents/{agent_id}">client.agents.<a href="./src/letta/resources/agents/agents.py">delete</a>(agent_id) -> <a href="./src/letta/types/agent_delete_response.py">object</a></code>

## Context

Types:

```python
from letta.types.agents import Contextwindowoverview
```

Methods:

- <code title="get /v1/agents/{agent_id}/context">client.agents.context.<a href="./src/letta/resources/agents/context.py">retrieve</a>(agent_id) -> <a href="./src/letta/types/agents/contextwindowoverview.py">Contextwindowoverview</a></code>

## Tools

Types:

```python
from letta.types.agents import ToolListResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/tools">client.agents.tools.<a href="./src/letta/resources/agents/tools.py">list</a>(agent_id) -> <a href="./src/letta/types/agents/tool_list_response.py">ToolListResponse</a></code>
- <code title="patch /v1/agents/{agent_id}/add-tool/{tool_id}">client.agents.tools.<a href="./src/letta/resources/agents/tools.py">add</a>(tool_id, \*, agent_id) -> <a href="./src/letta/types/agentstate.py">Agentstate</a></code>
- <code title="patch /v1/agents/{agent_id}/remove-tool/{tool_id}">client.agents.tools.<a href="./src/letta/resources/agents/tools.py">remove</a>(tool_id, \*, agent_id) -> <a href="./src/letta/types/agentstate.py">Agentstate</a></code>

## Sources

Types:

```python
from letta.types.agents import SourceListResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/sources">client.agents.sources.<a href="./src/letta/resources/agents/sources.py">list</a>(agent_id) -> <a href="./src/letta/types/agents/source_list_response.py">SourceListResponse</a></code>

## Memory

Types:

```python
from letta.types.agents import Archivalmemorysummary, Recallmemorysummary
```

Methods:

- <code title="get /v1/agents/{agent_id}/memory">client.agents.memory.<a href="./src/letta/resources/agents/memory/memory.py">retrieve</a>(agent_id) -> <a href="./src/letta/types/shared/memory.py">Memory</a></code>
- <code title="patch /v1/agents/{agent_id}/memory">client.agents.memory.<a href="./src/letta/resources/agents/memory/memory.py">update</a>(agent_id, \*\*<a href="src/letta/types/agents/memory_update_params.py">params</a>) -> <a href="./src/letta/types/shared/memory.py">Memory</a></code>

### Messages

Types:

```python
from letta.types.agents.memory import MessageRetrieveResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/memory/messages">client.agents.memory.messages.<a href="./src/letta/resources/agents/memory/messages.py">retrieve</a>(agent_id) -> <a href="./src/letta/types/agents/memory/message_retrieve_response.py">MessageRetrieveResponse</a></code>

### Recall

Methods:

- <code title="get /v1/agents/{agent_id}/memory/recall">client.agents.memory.recall.<a href="./src/letta/resources/agents/memory/recall.py">retrieve</a>(agent_id) -> <a href="./src/letta/types/agents/recallmemorysummary.py">Recallmemorysummary</a></code>

### Archival

Methods:

- <code title="get /v1/agents/{agent_id}/memory/archival">client.agents.memory.archival.<a href="./src/letta/resources/agents/memory/archival.py">retrieve</a>(agent_id) -> <a href="./src/letta/types/agents/archivalmemorysummary.py">Archivalmemorysummary</a></code>

## Archival

Types:

```python
from letta.types.agents import ArchivalCreateResponse, ArchivalListResponse, ArchivalDeleteResponse
```

Methods:

- <code title="post /v1/agents/{agent_id}/archival">client.agents.archival.<a href="./src/letta/resources/agents/archival.py">create</a>(agent_id, \*\*<a href="src/letta/types/agents/archival_create_params.py">params</a>) -> <a href="./src/letta/types/agents/archival_create_response.py">ArchivalCreateResponse</a></code>
- <code title="get /v1/agents/{agent_id}/archival">client.agents.archival.<a href="./src/letta/resources/agents/archival.py">list</a>(agent_id, \*\*<a href="src/letta/types/agents/archival_list_params.py">params</a>) -> <a href="./src/letta/types/agents/archival_list_response.py">ArchivalListResponse</a></code>
- <code title="delete /v1/agents/{agent_id}/archival/{memory_id}">client.agents.archival.<a href="./src/letta/resources/agents/archival.py">delete</a>(memory_id, \*, agent_id) -> <a href="./src/letta/types/agents/archival_delete_response.py">object</a></code>

## Messages

Types:

```python
from letta.types.agents import Messageoutput, MessageRetrieveResponse, MessageProcessResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/messages">client.agents.messages.<a href="./src/letta/resources/agents/messages.py">retrieve</a>(agent_id, \*\*<a href="src/letta/types/agents/message_retrieve_params.py">params</a>) -> <a href="./src/letta/types/agents/message_retrieve_response.py">MessageRetrieveResponse</a></code>
- <code title="patch /v1/agents/{agent_id}/messages/{message_id}">client.agents.messages.<a href="./src/letta/resources/agents/messages.py">update</a>(message_id, \*, agent_id, \*\*<a href="src/letta/types/agents/message_update_params.py">params</a>) -> <a href="./src/letta/types/agents/messageoutput.py">Messageoutput</a></code>
- <code title="post /v1/agents/{agent_id}/messages">client.agents.messages.<a href="./src/letta/resources/agents/messages.py">process</a>(agent_id, \*\*<a href="src/letta/types/agents/message_process_params.py">params</a>) -> <a href="./src/letta/types/agents/message_process_response.py">object</a></code>

# Models

Types:

```python
from letta.types import Embeddingconfig, Llmconfig, ModelListResponse, ModelEmbeddingResponse
```

Methods:

- <code title="get /v1/models/">client.models.<a href="./src/letta/resources/models.py">list</a>() -> <a href="./src/letta/types/model_list_response.py">ModelListResponse</a></code>
- <code title="get /v1/models/embedding">client.models.<a href="./src/letta/resources/models.py">embedding</a>() -> <a href="./src/letta/types/model_embedding_response.py">ModelEmbeddingResponse</a></code>

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
from letta.types import JobListResponse, JobActiveResponse
```

Methods:

- <code title="get /v1/jobs/{job_id}">client.jobs.<a href="./src/letta/resources/jobs.py">retrieve</a>(job_id) -> <a href="./src/letta/types/shared/job.py">Job</a></code>
- <code title="get /v1/jobs/">client.jobs.<a href="./src/letta/resources/jobs.py">list</a>(\*\*<a href="src/letta/types/job_list_params.py">params</a>) -> <a href="./src/letta/types/job_list_response.py">JobListResponse</a></code>
- <code title="delete /v1/jobs/{job_id}">client.jobs.<a href="./src/letta/resources/jobs.py">delete</a>(job_id) -> <a href="./src/letta/types/shared/job.py">Job</a></code>
- <code title="get /v1/jobs/active">client.jobs.<a href="./src/letta/resources/jobs.py">active</a>() -> <a href="./src/letta/types/job_active_response.py">JobActiveResponse</a></code>

# Health

Types:

```python
from letta.types import Health
```

Methods:

- <code title="get /v1/health/">client.health.<a href="./src/letta/resources/health.py">retrieve</a>() -> <a href="./src/letta/types/health.py">Health</a></code>

# AdminUsers

Types:

```python
from letta.types import User
```

## Keys

Types:

```python
from letta.types.admin_users import APIKey
```

# AdminOrganizations

Types:

```python
from letta.types import Organization
```

# Auth

Types:

```python
from letta.types import AuthResponse
```
