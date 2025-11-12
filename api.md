# Letta

Types:

```python
from letta_client.types import HealthResponse
```

Methods:

- <code title="get /v1/health/">client.<a href="./src/letta_client/_client.py">health</a>() -> <a href="./src/letta_client/types/health_response.py">HealthResponse</a></code>

# Agents

Types:

```python
from letta_client.types import (
    AgentEnvironmentVariable,
    AgentState,
    AgentType,
    AnthropicModelSettings,
    AzureModelSettings,
    BedrockModelSettings,
    ChildToolRule,
    ConditionalToolRule,
    ContinueToolRule,
    DeepseekModelSettings,
    GoogleAIModelSettings,
    GoogleVertexModelSettings,
    GroqModelSettings,
    InitToolRule,
    JsonObjectResponseFormat,
    JsonSchemaResponseFormat,
    LettaMessageContentUnion,
    MaxCountPerStepToolRule,
    MessageCreate,
    OpenAIModelSettings,
    ParentToolRule,
    RequiredBeforeExitToolRule,
    RequiresApprovalToolRule,
    TerminalToolRule,
    TextResponseFormat,
    TogetherModelSettings,
    XaiModelSettings,
    AgentExportFileResponse,
    AgentImportFileResponse,
)
```

Methods:

- <code title="post /v1/agents/">client.agents.<a href="./src/letta_client/resources/agents/agents.py">create</a>(\*\*<a href="src/letta_client/types/agent_create_params.py">params</a>) -> <a href="./src/letta_client/types/agent_state.py">AgentState</a></code>
- <code title="get /v1/agents/{agent_id}">client.agents.<a href="./src/letta_client/resources/agents/agents.py">retrieve</a>(agent_id, \*\*<a href="src/letta_client/types/agent_retrieve_params.py">params</a>) -> <a href="./src/letta_client/types/agent_state.py">AgentState</a></code>
- <code title="patch /v1/agents/{agent_id}">client.agents.<a href="./src/letta_client/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/letta_client/types/agent_update_params.py">params</a>) -> <a href="./src/letta_client/types/agent_state.py">AgentState</a></code>
- <code title="get /v1/agents/">client.agents.<a href="./src/letta_client/resources/agents/agents.py">list</a>(\*\*<a href="src/letta_client/types/agent_list_params.py">params</a>) -> <a href="./src/letta_client/types/agent_state.py">SyncArrayPage[AgentState]</a></code>
- <code title="delete /v1/agents/{agent_id}">client.agents.<a href="./src/letta_client/resources/agents/agents.py">delete</a>(agent_id) -> object</code>
- <code title="get /v1/agents/{agent_id}/export">client.agents.<a href="./src/letta_client/resources/agents/agents.py">export_file</a>(agent_id, \*\*<a href="src/letta_client/types/agent_export_file_params.py">params</a>) -> str</code>
- <code title="post /v1/agents/import">client.agents.<a href="./src/letta_client/resources/agents/agents.py">import_file</a>(\*\*<a href="src/letta_client/types/agent_import_file_params.py">params</a>) -> <a href="./src/letta_client/types/agent_import_file_response.py">AgentImportFileResponse</a></code>

## Messages

Types:

```python
from letta_client.types.agents import (
    ApprovalCreate,
    ApprovalRequestMessage,
    ApprovalResponseMessage,
    ApprovalReturn,
    AssistantMessage,
    EventMessage,
    HiddenReasoningMessage,
    ImageContent,
    InternalMessage,
    JobStatus,
    JobType,
    LettaAssistantMessageContentUnion,
    LettaRequest,
    LettaResponse,
    LettaStreamingRequest,
    LettaStreamingResponse,
    LettaUserMessageContentUnion,
    Message,
    MessageRole,
    MessageType,
    OmittedReasoningContent,
    ReasoningContent,
    ReasoningMessage,
    RedactedReasoningContent,
    Run,
    SummaryMessage,
    SystemMessage,
    TextContent,
    ToolCall,
    ToolCallContent,
    ToolCallDelta,
    ToolCallMessage,
    ToolReturn,
    ToolReturnContent,
    UpdateAssistantMessage,
    UpdateReasoningMessage,
    UpdateSystemMessage,
    UpdateUserMessage,
    UserMessage,
    MessageUpdateResponse,
    MessageCancelResponse,
)
```

Methods:

- <code title="post /v1/agents/{agent_id}/messages">client.agents.messages.<a href="./src/letta_client/resources/agents/messages.py">create</a>(agent_id, \*\*<a href="src/letta_client/types/agents/message_create_params.py">params</a>) -> <a href="./src/letta_client/types/agents/letta_response.py">LettaResponse</a></code>
- <code title="patch /v1/agents/{agent_id}/messages/{message_id}">client.agents.messages.<a href="./src/letta_client/resources/agents/messages.py">update</a>(message_id, \*, agent_id, \*\*<a href="src/letta_client/types/agents/message_update_params.py">params</a>) -> <a href="./src/letta_client/types/agents/message_update_response.py">MessageUpdateResponse</a></code>
- <code title="get /v1/agents/{agent_id}/messages">client.agents.messages.<a href="./src/letta_client/resources/agents/messages.py">list</a>(agent_id, \*\*<a href="src/letta_client/types/agents/message_list_params.py">params</a>) -> <a href="./src/letta_client/types/agents/message.py">SyncArrayPage[Message]</a></code>
- <code title="post /v1/agents/{agent_id}/messages/cancel">client.agents.messages.<a href="./src/letta_client/resources/agents/messages.py">cancel</a>(agent_id, \*\*<a href="src/letta_client/types/agents/message_cancel_params.py">params</a>) -> <a href="./src/letta_client/types/agents/message_cancel_response.py">MessageCancelResponse</a></code>
- <code title="post /v1/agents/{agent_id}/messages/async">client.agents.messages.<a href="./src/letta_client/resources/agents/messages.py">create_async</a>(agent_id, \*\*<a href="src/letta_client/types/agents/message_create_async_params.py">params</a>) -> <a href="./src/letta_client/types/agents/run.py">Run</a></code>
- <code title="patch /v1/agents/{agent_id}/reset-messages">client.agents.messages.<a href="./src/letta_client/resources/agents/messages.py">reset</a>(agent_id, \*\*<a href="src/letta_client/types/agents/message_reset_params.py">params</a>) -> <a href="./src/letta_client/types/agent_state.py">AgentState</a></code>
- <code title="post /v1/agents/{agent_id}/messages/stream">client.agents.messages.<a href="./src/letta_client/resources/agents/messages.py">stream</a>(agent_id, \*\*<a href="src/letta_client/types/agents/message_stream_params.py">params</a>) -> <a href="./src/letta_client/types/agents/letta_streaming_response.py">LettaStreamingResponse</a></code>
- <code title="post /v1/agents/{agent_id}/summarize">client.agents.messages.<a href="./src/letta_client/resources/agents/messages.py">summarize</a>(agent_id) -> None</code>

## Blocks

Types:

```python
from letta_client.types.agents import Block, BlockUpdate
```

Methods:

- <code title="get /v1/agents/{agent_id}/core-memory/blocks/{block_label}">client.agents.blocks.<a href="./src/letta_client/resources/agents/blocks.py">retrieve</a>(block_label, \*, agent_id) -> <a href="./src/letta_client/types/block_response.py">BlockResponse</a></code>
- <code title="patch /v1/agents/{agent_id}/core-memory/blocks/{block_label}">client.agents.blocks.<a href="./src/letta_client/resources/agents/blocks.py">update</a>(block_label, \*, agent_id, \*\*<a href="src/letta_client/types/agents/block_update_params.py">params</a>) -> <a href="./src/letta_client/types/block_response.py">BlockResponse</a></code>
- <code title="get /v1/agents/{agent_id}/core-memory/blocks">client.agents.blocks.<a href="./src/letta_client/resources/agents/blocks.py">list</a>(agent_id, \*\*<a href="src/letta_client/types/agents/block_list_params.py">params</a>) -> <a href="./src/letta_client/types/block_response.py">SyncArrayPage[BlockResponse]</a></code>
- <code title="patch /v1/agents/{agent_id}/core-memory/blocks/attach/{block_id}">client.agents.blocks.<a href="./src/letta_client/resources/agents/blocks.py">attach</a>(block_id, \*, agent_id) -> <a href="./src/letta_client/types/agent_state.py">AgentState</a></code>
- <code title="patch /v1/agents/{agent_id}/core-memory/blocks/detach/{block_id}">client.agents.blocks.<a href="./src/letta_client/resources/agents/blocks.py">detach</a>(block_id, \*, agent_id) -> <a href="./src/letta_client/types/agent_state.py">AgentState</a></code>

## Tools

Methods:

- <code title="get /v1/agents/{agent_id}/tools">client.agents.tools.<a href="./src/letta_client/resources/agents/tools.py">list</a>(agent_id, \*\*<a href="src/letta_client/types/agents/tool_list_params.py">params</a>) -> <a href="./src/letta_client/types/tool.py">SyncArrayPage[Tool]</a></code>
- <code title="patch /v1/agents/{agent_id}/tools/attach/{tool_id}">client.agents.tools.<a href="./src/letta_client/resources/agents/tools.py">attach</a>(tool_id, \*, agent_id) -> <a href="./src/letta_client/types/agent_state.py">Optional[AgentState]</a></code>
- <code title="patch /v1/agents/{agent_id}/tools/detach/{tool_id}">client.agents.tools.<a href="./src/letta_client/resources/agents/tools.py">detach</a>(tool_id, \*, agent_id) -> <a href="./src/letta_client/types/agent_state.py">Optional[AgentState]</a></code>
- <code title="patch /v1/agents/{agent_id}/tools/approval/{tool_name}">client.agents.tools.<a href="./src/letta_client/resources/agents/tools.py">update_approval</a>(tool_name, \*, agent_id, \*\*<a href="src/letta_client/types/agents/tool_update_approval_params.py">params</a>) -> <a href="./src/letta_client/types/agent_state.py">Optional[AgentState]</a></code>

## Folders

Types:

```python
from letta_client.types.agents import FolderListResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/folders">client.agents.folders.<a href="./src/letta_client/resources/agents/folders.py">list</a>(agent_id, \*\*<a href="src/letta_client/types/agents/folder_list_params.py">params</a>) -> <a href="./src/letta_client/types/agents/folder_list_response.py">SyncArrayPage[FolderListResponse]</a></code>
- <code title="patch /v1/agents/{agent_id}/folders/attach/{folder_id}">client.agents.folders.<a href="./src/letta_client/resources/agents/folders.py">attach</a>(folder_id, \*, agent_id) -> <a href="./src/letta_client/types/agent_state.py">AgentState</a></code>
- <code title="patch /v1/agents/{agent_id}/folders/detach/{folder_id}">client.agents.folders.<a href="./src/letta_client/resources/agents/folders.py">detach</a>(folder_id, \*, agent_id) -> <a href="./src/letta_client/types/agent_state.py">AgentState</a></code>

## Files

Types:

```python
from letta_client.types.agents import FileListResponse, FileCloseAllResponse, FileOpenResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/files">client.agents.files.<a href="./src/letta_client/resources/agents/files.py">list</a>(agent_id, \*\*<a href="src/letta_client/types/agents/file_list_params.py">params</a>) -> <a href="./src/letta_client/types/agents/file_list_response.py">SyncNextFilesPage[FileListResponse]</a></code>
- <code title="patch /v1/agents/{agent_id}/files/{file_id}/close">client.agents.files.<a href="./src/letta_client/resources/agents/files.py">close</a>(file_id, \*, agent_id) -> object</code>
- <code title="patch /v1/agents/{agent_id}/files/close-all">client.agents.files.<a href="./src/letta_client/resources/agents/files.py">close_all</a>(agent_id) -> <a href="./src/letta_client/types/agents/file_close_all_response.py">FileCloseAllResponse</a></code>
- <code title="patch /v1/agents/{agent_id}/files/{file_id}/open">client.agents.files.<a href="./src/letta_client/resources/agents/files.py">open</a>(file_id, \*, agent_id) -> <a href="./src/letta_client/types/agents/file_open_response.py">FileOpenResponse</a></code>

## Groups

Methods:

- <code title="get /v1/agents/{agent_id}/groups">client.agents.groups.<a href="./src/letta_client/resources/agents/groups.py">list</a>(agent_id, \*\*<a href="src/letta_client/types/agents/group_list_params.py">params</a>) -> <a href="./src/letta_client/types/group.py">SyncArrayPage[Group]</a></code>

## Archives

Methods:

- <code title="patch /v1/agents/{agent_id}/archives/attach/{archive_id}">client.agents.archives.<a href="./src/letta_client/resources/agents/archives.py">attach</a>(archive_id, \*, agent_id) -> object</code>
- <code title="patch /v1/agents/{agent_id}/archives/detach/{archive_id}">client.agents.archives.<a href="./src/letta_client/resources/agents/archives.py">detach</a>(archive_id, \*, agent_id) -> object</code>

## Identities

Methods:

- <code title="patch /v1/agents/{agent_id}/identities/attach/{identity_id}">client.agents.identities.<a href="./src/letta_client/resources/agents/identities.py">attach</a>(identity_id, \*, agent_id) -> object</code>
- <code title="patch /v1/agents/{agent_id}/identities/detach/{identity_id}">client.agents.identities.<a href="./src/letta_client/resources/agents/identities.py">detach</a>(identity_id, \*, agent_id) -> object</code>

# Tools

Types:

```python
from letta_client.types import (
    NpmRequirement,
    PipRequirement,
    Tool,
    ToolCreate,
    ToolReturnMessage,
    ToolType,
    ToolUpsertBaseToolsResponse,
)
```

Methods:

- <code title="post /v1/tools/">client.tools.<a href="./src/letta_client/resources/tools.py">create</a>(\*\*<a href="src/letta_client/types/tool_create_params.py">params</a>) -> <a href="./src/letta_client/types/tool.py">Tool</a></code>
- <code title="get /v1/tools/{tool_id}">client.tools.<a href="./src/letta_client/resources/tools.py">retrieve</a>(tool_id) -> <a href="./src/letta_client/types/tool.py">Tool</a></code>
- <code title="patch /v1/tools/{tool_id}">client.tools.<a href="./src/letta_client/resources/tools.py">update</a>(tool_id, \*\*<a href="src/letta_client/types/tool_update_params.py">params</a>) -> <a href="./src/letta_client/types/tool.py">Tool</a></code>
- <code title="get /v1/tools/">client.tools.<a href="./src/letta_client/resources/tools.py">list</a>(\*\*<a href="src/letta_client/types/tool_list_params.py">params</a>) -> <a href="./src/letta_client/types/tool.py">SyncArrayPage[Tool]</a></code>
- <code title="delete /v1/tools/{tool_id}">client.tools.<a href="./src/letta_client/resources/tools.py">delete</a>(tool_id) -> object</code>
- <code title="put /v1/tools/">client.tools.<a href="./src/letta_client/resources/tools.py">upsert</a>(\*\*<a href="src/letta_client/types/tool_upsert_params.py">params</a>) -> <a href="./src/letta_client/types/tool.py">Tool</a></code>
- <code title="post /v1/tools/add-base-tools">client.tools.<a href="./src/letta_client/resources/tools.py">upsert_base_tools</a>() -> <a href="./src/letta_client/types/tool_upsert_base_tools_response.py">ToolUpsertBaseToolsResponse</a></code>

# Blocks

Types:

```python
from letta_client.types import BlockResponse, CreateBlock
```

Methods:

- <code title="post /v1/blocks/">client.blocks.<a href="./src/letta_client/resources/blocks/blocks.py">create</a>(\*\*<a href="src/letta_client/types/block_create_params.py">params</a>) -> <a href="./src/letta_client/types/block_response.py">BlockResponse</a></code>
- <code title="get /v1/blocks/{block_id}">client.blocks.<a href="./src/letta_client/resources/blocks/blocks.py">retrieve</a>(block_id) -> <a href="./src/letta_client/types/block_response.py">BlockResponse</a></code>
- <code title="patch /v1/blocks/{block_id}">client.blocks.<a href="./src/letta_client/resources/blocks/blocks.py">update</a>(block_id, \*\*<a href="src/letta_client/types/block_update_params.py">params</a>) -> <a href="./src/letta_client/types/block_response.py">BlockResponse</a></code>
- <code title="get /v1/blocks/">client.blocks.<a href="./src/letta_client/resources/blocks/blocks.py">list</a>(\*\*<a href="src/letta_client/types/block_list_params.py">params</a>) -> <a href="./src/letta_client/types/block_response.py">SyncArrayPage[BlockResponse]</a></code>
- <code title="delete /v1/blocks/{block_id}">client.blocks.<a href="./src/letta_client/resources/blocks/blocks.py">delete</a>(block_id) -> object</code>

## Agents

Methods:

- <code title="get /v1/blocks/{block_id}/agents">client.blocks.agents.<a href="./src/letta_client/resources/blocks/agents.py">list</a>(block_id, \*\*<a href="src/letta_client/types/blocks/agent_list_params.py">params</a>) -> <a href="./src/letta_client/types/agent_state.py">SyncArrayPage[AgentState]</a></code>

# Archives

Types:

```python
from letta_client.types import Archive, VectorDBProvider
```

Methods:

- <code title="post /v1/archives/">client.archives.<a href="./src/letta_client/resources/archives/archives.py">create</a>(\*\*<a href="src/letta_client/types/archive_create_params.py">params</a>) -> <a href="./src/letta_client/types/archive.py">Archive</a></code>
- <code title="get /v1/archives/{archive_id}">client.archives.<a href="./src/letta_client/resources/archives/archives.py">retrieve</a>(archive_id) -> <a href="./src/letta_client/types/archive.py">Archive</a></code>
- <code title="patch /v1/archives/{archive_id}">client.archives.<a href="./src/letta_client/resources/archives/archives.py">update</a>(archive_id, \*\*<a href="src/letta_client/types/archive_update_params.py">params</a>) -> <a href="./src/letta_client/types/archive.py">Archive</a></code>
- <code title="get /v1/archives/">client.archives.<a href="./src/letta_client/resources/archives/archives.py">list</a>(\*\*<a href="src/letta_client/types/archive_list_params.py">params</a>) -> <a href="./src/letta_client/types/archive.py">SyncArrayPage[Archive]</a></code>
- <code title="delete /v1/archives/{archive_id}">client.archives.<a href="./src/letta_client/resources/archives/archives.py">delete</a>(archive_id) -> <a href="./src/letta_client/types/archive.py">Archive</a></code>

## Passages

Types:

```python
from letta_client.types.archives import PassageCreateResponse
```

Methods:

- <code title="post /v1/archives/{archive_id}/passages">client.archives.passages.<a href="./src/letta_client/resources/archives/passages.py">create</a>(archive_id, \*\*<a href="src/letta_client/types/archives/passage_create_params.py">params</a>) -> <a href="./src/letta_client/types/archives/passage_create_response.py">PassageCreateResponse</a></code>
- <code title="delete /v1/archives/{archive_id}/passages/{passage_id}">client.archives.passages.<a href="./src/letta_client/resources/archives/passages.py">delete</a>(passage_id, \*, archive_id) -> None</code>

# Folders

Types:

```python
from letta_client.types import Folder
```

Methods:

- <code title="post /v1/folders/">client.folders.<a href="./src/letta_client/resources/folders/folders.py">create</a>(\*\*<a href="src/letta_client/types/folder_create_params.py">params</a>) -> <a href="./src/letta_client/types/folder.py">Folder</a></code>
- <code title="get /v1/folders/{folder_id}">client.folders.<a href="./src/letta_client/resources/folders/folders.py">retrieve</a>(folder_id) -> <a href="./src/letta_client/types/folder.py">Folder</a></code>
- <code title="patch /v1/folders/{folder_id}">client.folders.<a href="./src/letta_client/resources/folders/folders.py">update</a>(folder_id, \*\*<a href="src/letta_client/types/folder_update_params.py">params</a>) -> <a href="./src/letta_client/types/folder.py">Folder</a></code>
- <code title="get /v1/folders/">client.folders.<a href="./src/letta_client/resources/folders/folders.py">list</a>(\*\*<a href="src/letta_client/types/folder_list_params.py">params</a>) -> <a href="./src/letta_client/types/folder.py">SyncArrayPage[Folder]</a></code>
- <code title="delete /v1/folders/{folder_id}">client.folders.<a href="./src/letta_client/resources/folders/folders.py">delete</a>(folder_id) -> object</code>

## Files

Types:

```python
from letta_client.types.folders import FileListResponse, FileUploadResponse
```

Methods:

- <code title="get /v1/folders/{folder_id}/files">client.folders.files.<a href="./src/letta_client/resources/folders/files.py">list</a>(folder_id, \*\*<a href="src/letta_client/types/folders/file_list_params.py">params</a>) -> <a href="./src/letta_client/types/folders/file_list_response.py">SyncArrayPage[FileListResponse]</a></code>
- <code title="delete /v1/folders/{folder_id}/{file_id}">client.folders.files.<a href="./src/letta_client/resources/folders/files.py">delete</a>(file_id, \*, folder_id) -> None</code>
- <code title="post /v1/folders/{folder_id}/upload">client.folders.files.<a href="./src/letta_client/resources/folders/files.py">upload</a>(folder_id, \*\*<a href="src/letta_client/types/folders/file_upload_params.py">params</a>) -> <a href="./src/letta_client/types/folders/file_upload_response.py">FileUploadResponse</a></code>

## Agents

Types:

```python
from letta_client.types.folders import AgentListResponse
```

Methods:

- <code title="get /v1/folders/{folder_id}/agents">client.folders.agents.<a href="./src/letta_client/resources/folders/agents.py">list</a>(folder_id, \*\*<a href="src/letta_client/types/folders/agent_list_params.py">params</a>) -> <a href="./src/letta_client/types/folders/agent_list_response.py">AgentListResponse</a></code>

# Models

Types:

```python
from letta_client.types import (
    EmbeddingConfig,
    EmbeddingModel,
    LlmConfig,
    Model,
    ProviderCategory,
    ProviderType,
    ModelListResponse,
)
```

Methods:

- <code title="get /v1/models/">client.models.<a href="./src/letta_client/resources/models/models.py">list</a>(\*\*<a href="src/letta_client/types/model_list_params.py">params</a>) -> <a href="./src/letta_client/types/model_list_response.py">ModelListResponse</a></code>

## Embeddings

Types:

```python
from letta_client.types.models import EmbeddingListResponse
```

Methods:

- <code title="get /v1/models/embedding">client.models.embeddings.<a href="./src/letta_client/resources/models/embeddings.py">list</a>() -> <a href="./src/letta_client/types/models/embedding_list_response.py">EmbeddingListResponse</a></code>

# McpServers

Types:

```python
from letta_client.types import (
    CreateSseMcpServer,
    CreateStdioMcpServer,
    CreateStreamableHTTPMcpServer,
    McpToolExecuteRequest,
    SseMcpServer,
    StdioMcpServer,
    StreamableHTTPMcpServer,
    ToolExecutionResult,
    UpdateSseMcpServer,
    UpdateStdioMcpServer,
    UpdateStreamableHTTPMcpServer,
    McpServerCreateResponse,
    McpServerRetrieveResponse,
    McpServerUpdateResponse,
    McpServerListResponse,
)
```

Methods:

- <code title="post /v1/mcp-servers/">client.mcp_servers.<a href="./src/letta_client/resources/mcp_servers/mcp_servers.py">create</a>(\*\*<a href="src/letta_client/types/mcp_server_create_params.py">params</a>) -> <a href="./src/letta_client/types/mcp_server_create_response.py">McpServerCreateResponse</a></code>
- <code title="get /v1/mcp-servers/{mcp_server_id}">client.mcp_servers.<a href="./src/letta_client/resources/mcp_servers/mcp_servers.py">retrieve</a>(mcp_server_id) -> <a href="./src/letta_client/types/mcp_server_retrieve_response.py">McpServerRetrieveResponse</a></code>
- <code title="patch /v1/mcp-servers/{mcp_server_id}">client.mcp_servers.<a href="./src/letta_client/resources/mcp_servers/mcp_servers.py">update</a>(mcp_server_id, \*\*<a href="src/letta_client/types/mcp_server_update_params.py">params</a>) -> <a href="./src/letta_client/types/mcp_server_update_response.py">McpServerUpdateResponse</a></code>
- <code title="get /v1/mcp-servers/">client.mcp_servers.<a href="./src/letta_client/resources/mcp_servers/mcp_servers.py">list</a>() -> <a href="./src/letta_client/types/mcp_server_list_response.py">McpServerListResponse</a></code>
- <code title="delete /v1/mcp-servers/{mcp_server_id}">client.mcp_servers.<a href="./src/letta_client/resources/mcp_servers/mcp_servers.py">delete</a>(mcp_server_id) -> None</code>
- <code title="get /v1/mcp-servers/connect/{mcp_server_id}">client.mcp_servers.<a href="./src/letta_client/resources/mcp_servers/mcp_servers.py">connect</a>(mcp_server_id) -> object</code>
- <code title="patch /v1/mcp-servers/{mcp_server_id}/refresh">client.mcp_servers.<a href="./src/letta_client/resources/mcp_servers/mcp_servers.py">refresh</a>(mcp_server_id, \*\*<a href="src/letta_client/types/mcp_server_refresh_params.py">params</a>) -> object</code>

## Tools

Types:

```python
from letta_client.types.mcp_servers import ToolListResponse
```

Methods:

- <code title="get /v1/mcp-servers/{mcp_server_id}/tools/{tool_id}">client.mcp_servers.tools.<a href="./src/letta_client/resources/mcp_servers/tools.py">retrieve</a>(tool_id, \*, mcp_server_id) -> <a href="./src/letta_client/types/tool.py">Tool</a></code>
- <code title="get /v1/mcp-servers/{mcp_server_id}/tools">client.mcp_servers.tools.<a href="./src/letta_client/resources/mcp_servers/tools.py">list</a>(mcp_server_id) -> <a href="./src/letta_client/types/mcp_servers/tool_list_response.py">ToolListResponse</a></code>
- <code title="post /v1/mcp-servers/{mcp_server_id}/tools/{tool_id}/run">client.mcp_servers.tools.<a href="./src/letta_client/resources/mcp_servers/tools.py">run</a>(tool_id, \*, mcp_server_id, \*\*<a href="src/letta_client/types/mcp_servers/tool_run_params.py">params</a>) -> <a href="./src/letta_client/types/tool_execution_result.py">ToolExecutionResult</a></code>

# Runs

Types:

```python
from letta_client.types import Job, StopReasonType
```

Methods:

- <code title="get /v1/runs/{run_id}">client.runs.<a href="./src/letta_client/resources/runs/runs.py">retrieve</a>(run_id) -> <a href="./src/letta_client/types/agents/run.py">Run</a></code>
- <code title="get /v1/runs/">client.runs.<a href="./src/letta_client/resources/runs/runs.py">list</a>(\*\*<a href="src/letta_client/types/run_list_params.py">params</a>) -> <a href="./src/letta_client/types/agents/run.py">SyncArrayPage[Run]</a></code>

## Messages

Methods:

- <code title="get /v1/runs/{run_id}/messages">client.runs.messages.<a href="./src/letta_client/resources/runs/messages.py">list</a>(run_id, \*\*<a href="src/letta_client/types/runs/message_list_params.py">params</a>) -> <a href="./src/letta_client/types/agents/message.py">SyncArrayPage[Message]</a></code>
- <code title="post /v1/runs/{run_id}/stream">client.runs.messages.<a href="./src/letta_client/resources/runs/messages.py">stream</a>(run_id, \*\*<a href="src/letta_client/types/runs/message_stream_params.py">params</a>) -> object</code>

## Usage

Types:

```python
from letta_client.types.runs import UsageRetrieveResponse
```

Methods:

- <code title="get /v1/runs/{run_id}/usage">client.runs.usage.<a href="./src/letta_client/resources/runs/usage.py">retrieve</a>(run_id) -> <a href="./src/letta_client/types/runs/usage_retrieve_response.py">UsageRetrieveResponse</a></code>

## Steps

Methods:

- <code title="get /v1/runs/{run_id}/steps">client.runs.steps.<a href="./src/letta_client/resources/runs/steps.py">list</a>(run_id, \*\*<a href="src/letta_client/types/runs/step_list_params.py">params</a>) -> <a href="./src/letta_client/types/step.py">SyncArrayPage[Step]</a></code>

# Steps

Types:

```python
from letta_client.types import ProviderTrace, Step
```

Methods:

- <code title="get /v1/steps/{step_id}">client.steps.<a href="./src/letta_client/resources/steps/steps.py">retrieve</a>(step_id) -> <a href="./src/letta_client/types/step.py">Step</a></code>
- <code title="get /v1/steps/">client.steps.<a href="./src/letta_client/resources/steps/steps.py">list</a>(\*\*<a href="src/letta_client/types/step_list_params.py">params</a>) -> <a href="./src/letta_client/types/step.py">SyncArrayPage[Step]</a></code>

## Metrics

Types:

```python
from letta_client.types.steps import MetricRetrieveResponse
```

Methods:

- <code title="get /v1/steps/{step_id}/metrics">client.steps.metrics.<a href="./src/letta_client/resources/steps/metrics.py">retrieve</a>(step_id) -> <a href="./src/letta_client/types/steps/metric_retrieve_response.py">MetricRetrieveResponse</a></code>

## Trace

Methods:

- <code title="get /v1/steps/{step_id}/trace">client.steps.trace.<a href="./src/letta_client/resources/steps/trace.py">retrieve</a>(step_id) -> <a href="./src/letta_client/types/provider_trace.py">Optional[ProviderTrace]</a></code>

## Feedback

Methods:

- <code title="patch /v1/steps/{step_id}/feedback">client.steps.feedback.<a href="./src/letta_client/resources/steps/feedback.py">create</a>(step_id, \*\*<a href="src/letta_client/types/steps/feedback_create_params.py">params</a>) -> <a href="./src/letta_client/types/step.py">Step</a></code>

## Messages

Types:

```python
from letta_client.types.steps import MessageListResponse
```

Methods:

- <code title="get /v1/steps/{step_id}/messages">client.steps.messages.<a href="./src/letta_client/resources/steps/messages.py">list</a>(step_id, \*\*<a href="src/letta_client/types/steps/message_list_params.py">params</a>) -> <a href="./src/letta_client/types/steps/message_list_response.py">SyncArrayPage[MessageListResponse]</a></code>

# Templates

## Agents

Methods:

- <code title="post /v1/templates/{template_version}/agents">client.templates.agents.<a href="./src/letta_client/resources/templates/agents.py">create</a>(template_version, \*\*<a href="src/letta_client/types/templates/agent_create_params.py">params</a>) -> None</code>

# Tags

Types:

```python
from letta_client.types import TagListResponse
```

Methods:

- <code title="get /v1/tags/">client.tags.<a href="./src/letta_client/resources/tags.py">list</a>(\*\*<a href="src/letta_client/types/tag_list_params.py">params</a>) -> <a href="./src/letta_client/types/tag_list_response.py">TagListResponse</a></code>

# Identities

Types:

```python
from letta_client.types import Identity, IdentityProperty, IdentityType
```

Methods:

- <code title="post /v1/identities/">client.identities.<a href="./src/letta_client/resources/identities/identities.py">create</a>(\*\*<a href="src/letta_client/types/identity_create_params.py">params</a>) -> <a href="./src/letta_client/types/identity.py">Identity</a></code>
- <code title="get /v1/identities/{identity_id}">client.identities.<a href="./src/letta_client/resources/identities/identities.py">retrieve</a>(identity_id) -> <a href="./src/letta_client/types/identity.py">Identity</a></code>
- <code title="patch /v1/identities/{identity_id}">client.identities.<a href="./src/letta_client/resources/identities/identities.py">update</a>(identity_id, \*\*<a href="src/letta_client/types/identity_update_params.py">params</a>) -> <a href="./src/letta_client/types/identity.py">Identity</a></code>
- <code title="get /v1/identities/">client.identities.<a href="./src/letta_client/resources/identities/identities.py">list</a>(\*\*<a href="src/letta_client/types/identity_list_params.py">params</a>) -> <a href="./src/letta_client/types/identity.py">SyncArrayPage[Identity]</a></code>
- <code title="delete /v1/identities/{identity_id}">client.identities.<a href="./src/letta_client/resources/identities/identities.py">delete</a>(identity_id) -> object</code>
- <code title="put /v1/identities/">client.identities.<a href="./src/letta_client/resources/identities/identities.py">upsert</a>(\*\*<a href="src/letta_client/types/identity_upsert_params.py">params</a>) -> <a href="./src/letta_client/types/identity.py">Identity</a></code>

## Properties

Methods:

- <code title="put /v1/identities/{identity_id}/properties">client.identities.properties.<a href="./src/letta_client/resources/identities/properties.py">upsert</a>(identity_id, \*\*<a href="src/letta_client/types/identities/property_upsert_params.py">params</a>) -> object</code>

## Agents

Methods:

- <code title="get /v1/identities/{identity_id}/agents">client.identities.agents.<a href="./src/letta_client/resources/identities/agents.py">list</a>(identity_id, \*\*<a href="src/letta_client/types/identities/agent_list_params.py">params</a>) -> <a href="./src/letta_client/types/agent_state.py">SyncArrayPage[AgentState]</a></code>

## Blocks

Methods:

- <code title="get /v1/identities/{identity_id}/blocks">client.identities.blocks.<a href="./src/letta_client/resources/identities/blocks.py">list</a>(identity_id, \*\*<a href="src/letta_client/types/identities/block_list_params.py">params</a>) -> <a href="./src/letta_client/types/block_response.py">SyncArrayPage[BlockResponse]</a></code>

# Groups

Types:

```python
from letta_client.types import (
    DynamicManager,
    Group,
    ManagerType,
    RoundRobinManager,
    SleeptimeManager,
    SupervisorManager,
    VoiceSleeptimeManager,
)
```

Methods:

- <code title="post /v1/groups/">client.groups.<a href="./src/letta_client/resources/groups/groups.py">create</a>(\*\*<a href="src/letta_client/types/group_create_params.py">params</a>) -> <a href="./src/letta_client/types/group.py">Group</a></code>
- <code title="get /v1/groups/{group_id}">client.groups.<a href="./src/letta_client/resources/groups/groups.py">retrieve</a>(group_id) -> <a href="./src/letta_client/types/group.py">Group</a></code>
- <code title="patch /v1/groups/{group_id}">client.groups.<a href="./src/letta_client/resources/groups/groups.py">update</a>(group_id, \*\*<a href="src/letta_client/types/group_update_params.py">params</a>) -> <a href="./src/letta_client/types/group.py">Group</a></code>
- <code title="get /v1/groups/">client.groups.<a href="./src/letta_client/resources/groups/groups.py">list</a>(\*\*<a href="src/letta_client/types/group_list_params.py">params</a>) -> <a href="./src/letta_client/types/group.py">SyncArrayPage[Group]</a></code>
- <code title="delete /v1/groups/{group_id}">client.groups.<a href="./src/letta_client/resources/groups/groups.py">delete</a>(group_id) -> object</code>

## Messages

Types:

```python
from letta_client.types.groups import MessageUpdateResponse
```

Methods:

- <code title="post /v1/groups/{group_id}/messages">client.groups.messages.<a href="./src/letta_client/resources/groups/messages.py">create</a>(group_id, \*\*<a href="src/letta_client/types/groups/message_create_params.py">params</a>) -> <a href="./src/letta_client/types/agents/letta_response.py">LettaResponse</a></code>
- <code title="patch /v1/groups/{group_id}/messages/{message_id}">client.groups.messages.<a href="./src/letta_client/resources/groups/messages.py">update</a>(message_id, \*, group_id, \*\*<a href="src/letta_client/types/groups/message_update_params.py">params</a>) -> <a href="./src/letta_client/types/groups/message_update_response.py">MessageUpdateResponse</a></code>
- <code title="get /v1/groups/{group_id}/messages">client.groups.messages.<a href="./src/letta_client/resources/groups/messages.py">list</a>(group_id, \*\*<a href="src/letta_client/types/groups/message_list_params.py">params</a>) -> <a href="./src/letta_client/types/agents/message.py">SyncArrayPage[Message]</a></code>
- <code title="patch /v1/groups/{group_id}/reset-messages">client.groups.messages.<a href="./src/letta_client/resources/groups/messages.py">reset</a>(group_id) -> object</code>
- <code title="post /v1/groups/{group_id}/messages/stream">client.groups.messages.<a href="./src/letta_client/resources/groups/messages.py">stream</a>(group_id, \*\*<a href="src/letta_client/types/groups/message_stream_params.py">params</a>) -> object</code>

# Batches

Types:

```python
from letta_client.types import BatchJob
```

Methods:

- <code title="post /v1/messages/batches">client.batches.<a href="./src/letta_client/resources/batches/batches.py">create</a>(\*\*<a href="src/letta_client/types/batch_create_params.py">params</a>) -> <a href="./src/letta_client/types/batch_job.py">BatchJob</a></code>
- <code title="get /v1/messages/batches/{batch_id}">client.batches.<a href="./src/letta_client/resources/batches/batches.py">retrieve</a>(batch_id) -> <a href="./src/letta_client/types/batch_job.py">BatchJob</a></code>
- <code title="get /v1/messages/batches">client.batches.<a href="./src/letta_client/resources/batches/batches.py">list</a>(\*\*<a href="src/letta_client/types/batch_list_params.py">params</a>) -> <a href="./src/letta_client/types/batch_job.py">SyncArrayPage[BatchJob]</a></code>
- <code title="patch /v1/messages/batches/{batch_id}/cancel">client.batches.<a href="./src/letta_client/resources/batches/batches.py">cancel</a>(batch_id) -> object</code>

## Messages

Methods:

- <code title="get /v1/messages/batches/{batch_id}/messages">client.batches.messages.<a href="./src/letta_client/resources/batches/messages.py">list</a>(batch_id, \*\*<a href="src/letta_client/types/batches/message_list_params.py">params</a>) -> <a href="./src/letta_client/types/agents/internal_message.py">SyncObjectPage[InternalMessage]</a></code>
