# Archives

Types:

```python
from letta_sdk.types import Archive, VectorDBProvider, ArchiveRetrieveResponse
```

Methods:

- <code title="post /v1/archives/">client.archives.<a href="./src/letta_sdk/resources/archives.py">update</a>(\*\*<a href="src/letta_sdk/types/archive_update_params.py">params</a>) -> <a href="./src/letta_sdk/types/archive.py">Archive</a></code>
- <code title="get /v1/archives/">client.archives.<a href="./src/letta_sdk/resources/archives.py">retrieve</a>(\*\*<a href="src/letta_sdk/types/archive_retrieve_params.py">params</a>) -> <a href="./src/letta_sdk/types/archive_retrieve_response.py">ArchiveRetrieveResponse</a></code>

# Tools

Types:

```python
from letta_sdk.types import (
    NpmRequirement,
    PipRequirement,
    Tool,
    ToolCreate,
    ToolReturnMessage,
    ToolType,
    ToolListResponse,
    ToolCountResponse,
    ToolUpsertBaseResponse,
)
```

Methods:

- <code title="post /v1/tools/">client.tools.<a href="./src/letta_sdk/resources/tools/tools.py">create</a>(\*\*<a href="src/letta_sdk/types/tool_create_params.py">params</a>) -> <a href="./src/letta_sdk/types/tool.py">Tool</a></code>
- <code title="get /v1/tools/{tool_id}">client.tools.<a href="./src/letta_sdk/resources/tools/tools.py">retrieve</a>(tool_id) -> <a href="./src/letta_sdk/types/tool.py">Tool</a></code>
- <code title="get /v1/tools/">client.tools.<a href="./src/letta_sdk/resources/tools/tools.py">list</a>(\*\*<a href="src/letta_sdk/types/tool_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/tool_list_response.py">ToolListResponse</a></code>
- <code title="delete /v1/tools/{tool_id}">client.tools.<a href="./src/letta_sdk/resources/tools/tools.py">delete</a>(tool_id) -> object</code>
- <code title="get /v1/tools/count">client.tools.<a href="./src/letta_sdk/resources/tools/tools.py">count</a>(\*\*<a href="src/letta_sdk/types/tool_count_params.py">params</a>) -> <a href="./src/letta_sdk/types/tool_count_response.py">ToolCountResponse</a></code>
- <code title="patch /v1/tools/{tool_id}">client.tools.<a href="./src/letta_sdk/resources/tools/tools.py">modify</a>(tool_id, \*\*<a href="src/letta_sdk/types/tool_modify_params.py">params</a>) -> <a href="./src/letta_sdk/types/tool.py">Tool</a></code>
- <code title="post /v1/tools/run">client.tools.<a href="./src/letta_sdk/resources/tools/tools.py">run</a>(\*\*<a href="src/letta_sdk/types/tool_run_params.py">params</a>) -> <a href="./src/letta_sdk/types/tool_return_message.py">ToolReturnMessage</a></code>
- <code title="put /v1/tools/">client.tools.<a href="./src/letta_sdk/resources/tools/tools.py">upsert</a>(\*\*<a href="src/letta_sdk/types/tool_upsert_params.py">params</a>) -> <a href="./src/letta_sdk/types/tool.py">Tool</a></code>
- <code title="post /v1/tools/add-base-tools">client.tools.<a href="./src/letta_sdk/resources/tools/tools.py">upsert_base</a>() -> <a href="./src/letta_sdk/types/tool_upsert_base_response.py">ToolUpsertBaseResponse</a></code>

## Composio

Methods:

- <code title="post /v1/tools/composio/{composio_action_name}">client.tools.composio.<a href="./src/letta_sdk/resources/tools/composio/composio.py">add</a>(composio_action_name) -> <a href="./src/letta_sdk/types/tool.py">Tool</a></code>

### Apps

Types:

```python
from letta_sdk.types.tools.composio import AppListResponse, AppListActionsResponse
```

Methods:

- <code title="get /v1/tools/composio/apps">client.tools.composio.apps.<a href="./src/letta_sdk/resources/tools/composio/apps.py">list</a>() -> <a href="./src/letta_sdk/types/tools/composio/app_list_response.py">AppListResponse</a></code>
- <code title="get /v1/tools/composio/apps/{composio_app_name}/actions">client.tools.composio.apps.<a href="./src/letta_sdk/resources/tools/composio/apps.py">list_actions</a>(composio_app_name) -> <a href="./src/letta_sdk/types/tools/composio/app_list_actions_response.py">AppListActionsResponse</a></code>

## Mcp

### Servers

Types:

```python
from letta_sdk.types.tools.mcp import (
    McpServerType,
    SseServerConfig,
    StdioServerConfig,
    StreamableHTTPServerConfig,
    ServerUpdateResponse,
    ServerListResponse,
    ServerDeleteResponse,
    ServerAddResponse,
)
```

Methods:

- <code title="patch /v1/tools/mcp/servers/{mcp_server_name}">client.tools.mcp.servers.<a href="./src/letta_sdk/resources/tools/mcp/servers/servers.py">update</a>(mcp_server_name, \*\*<a href="src/letta_sdk/types/tools/mcp/server_update_params.py">params</a>) -> <a href="./src/letta_sdk/types/tools/mcp/server_update_response.py">ServerUpdateResponse</a></code>
- <code title="get /v1/tools/mcp/servers">client.tools.mcp.servers.<a href="./src/letta_sdk/resources/tools/mcp/servers/servers.py">list</a>() -> <a href="./src/letta_sdk/types/tools/mcp/server_list_response.py">ServerListResponse</a></code>
- <code title="delete /v1/tools/mcp/servers/{mcp_server_name}">client.tools.mcp.servers.<a href="./src/letta_sdk/resources/tools/mcp/servers/servers.py">delete</a>(mcp_server_name) -> <a href="./src/letta_sdk/types/tools/mcp/server_delete_response.py">ServerDeleteResponse</a></code>
- <code title="put /v1/tools/mcp/servers">client.tools.mcp.servers.<a href="./src/letta_sdk/resources/tools/mcp/servers/servers.py">add</a>(\*\*<a href="src/letta_sdk/types/tools/mcp/server_add_params.py">params</a>) -> <a href="./src/letta_sdk/types/tools/mcp/server_add_response.py">ServerAddResponse</a></code>
- <code title="post /v1/tools/mcp/servers/connect">client.tools.mcp.servers.<a href="./src/letta_sdk/resources/tools/mcp/servers/servers.py">connect</a>(\*\*<a href="src/letta_sdk/types/tools/mcp/server_connect_params.py">params</a>) -> object</code>
- <code title="post /v1/tools/mcp/servers/{mcp_server_name}/{mcp_tool_name}">client.tools.mcp.servers.<a href="./src/letta_sdk/resources/tools/mcp/servers/servers.py">register_tool</a>(mcp_tool_name, \*, mcp_server_name) -> <a href="./src/letta_sdk/types/tool.py">Tool</a></code>
- <code title="post /v1/tools/mcp/servers/{mcp_server_name}/resync">client.tools.mcp.servers.<a href="./src/letta_sdk/resources/tools/mcp/servers/servers.py">resync</a>(mcp_server_name, \*\*<a href="src/letta_sdk/types/tools/mcp/server_resync_params.py">params</a>) -> object</code>
- <code title="post /v1/tools/mcp/servers/test">client.tools.mcp.servers.<a href="./src/letta_sdk/resources/tools/mcp/servers/servers.py">test</a>(\*\*<a href="src/letta_sdk/types/tools/mcp/server_test_params.py">params</a>) -> object</code>

#### Tools

Types:

```python
from letta_sdk.types.tools.mcp.servers import ToolListResponse
```

Methods:

- <code title="get /v1/tools/mcp/servers/{mcp_server_name}/tools">client.tools.mcp.servers.tools.<a href="./src/letta_sdk/resources/tools/mcp/servers/tools.py">list</a>(mcp_server_name) -> <a href="./src/letta_sdk/types/tools/mcp/servers/tool_list_response.py">ToolListResponse</a></code>
- <code title="post /v1/tools/mcp/servers/{mcp_server_name}/tools/{tool_name}/execute">client.tools.mcp.servers.tools.<a href="./src/letta_sdk/resources/tools/mcp/servers/tools.py">execute</a>(tool_name, \*, mcp_server_name, \*\*<a href="src/letta_sdk/types/tools/mcp/servers/tool_execute_params.py">params</a>) -> object</code>

### OAuth

Methods:

- <code title="get /v1/tools/mcp/oauth/callback/{session_id}">client.tools.mcp.oauth.<a href="./src/letta_sdk/resources/tools/mcp/oauth.py">callback</a>(session_id, \*\*<a href="src/letta_sdk/types/tools/mcp/oauth_callback_params.py">params</a>) -> object</code>

# Sources

Types:

```python
from letta_sdk.types import (
    DuplicateFileHandling,
    FileMetadata,
    FileProcessingStatus,
    OrganizationSourcesStats,
    Passage,
    Source,
    SourceCreate,
    SourceUpdate,
    SourceListResponse,
    SourceCountResponse,
    SourceGetAgentsResponse,
    SourceGetByNameResponse,
    SourceListPassagesResponse,
)
```

Methods:

- <code title="post /v1/sources/">client.sources.<a href="./src/letta_sdk/resources/sources/sources.py">create</a>(\*\*<a href="src/letta_sdk/types/source_create_params.py">params</a>) -> <a href="./src/letta_sdk/types/source.py">Source</a></code>
- <code title="get /v1/sources/{source_id}">client.sources.<a href="./src/letta_sdk/resources/sources/sources.py">retrieve</a>(source_id) -> <a href="./src/letta_sdk/types/source.py">Source</a></code>
- <code title="patch /v1/sources/{source_id}">client.sources.<a href="./src/letta_sdk/resources/sources/sources.py">update</a>(source_id, \*\*<a href="src/letta_sdk/types/source_update_params.py">params</a>) -> <a href="./src/letta_sdk/types/source.py">Source</a></code>
- <code title="get /v1/sources/">client.sources.<a href="./src/letta_sdk/resources/sources/sources.py">list</a>() -> <a href="./src/letta_sdk/types/source_list_response.py">SourceListResponse</a></code>
- <code title="delete /v1/sources/{source_id}">client.sources.<a href="./src/letta_sdk/resources/sources/sources.py">delete</a>(source_id) -> object</code>
- <code title="get /v1/sources/count">client.sources.<a href="./src/letta_sdk/resources/sources/sources.py">count</a>() -> <a href="./src/letta_sdk/types/source_count_response.py">SourceCountResponse</a></code>
- <code title="delete /v1/sources/{source_id}/{file_id}">client.sources.<a href="./src/letta_sdk/resources/sources/sources.py">delete_file</a>(file_id, \*, source_id) -> None</code>
- <code title="get /v1/sources/{source_id}/agents">client.sources.<a href="./src/letta_sdk/resources/sources/sources.py">get_agents</a>(source_id) -> <a href="./src/letta_sdk/types/source_get_agents_response.py">SourceGetAgentsResponse</a></code>
- <code title="get /v1/sources/name/{source_name}">client.sources.<a href="./src/letta_sdk/resources/sources/sources.py">get_by_name</a>(source_name) -> str</code>
- <code title="get /v1/sources/metadata">client.sources.<a href="./src/letta_sdk/resources/sources/sources.py">get_metadata</a>(\*\*<a href="src/letta_sdk/types/source_get_metadata_params.py">params</a>) -> <a href="./src/letta_sdk/types/organization_sources_stats.py">OrganizationSourcesStats</a></code>
- <code title="get /v1/sources/{source_id}/passages">client.sources.<a href="./src/letta_sdk/resources/sources/sources.py">list_passages</a>(source_id, \*\*<a href="src/letta_sdk/types/source_list_passages_params.py">params</a>) -> <a href="./src/letta_sdk/types/source_list_passages_response.py">SourceListPassagesResponse</a></code>
- <code title="post /v1/sources/{source_id}/upload">client.sources.<a href="./src/letta_sdk/resources/sources/sources.py">upload_file</a>(source_id, \*\*<a href="src/letta_sdk/types/source_upload_file_params.py">params</a>) -> <a href="./src/letta_sdk/types/file_metadata.py">FileMetadata</a></code>

## Files

Types:

```python
from letta_sdk.types.sources import FileListResponse
```

Methods:

- <code title="get /v1/sources/{source_id}/files/{file_id}">client.sources.files.<a href="./src/letta_sdk/resources/sources/files.py">retrieve</a>(file_id, \*, source_id, \*\*<a href="src/letta_sdk/types/sources/file_retrieve_params.py">params</a>) -> <a href="./src/letta_sdk/types/file_metadata.py">FileMetadata</a></code>
- <code title="get /v1/sources/{source_id}/files">client.sources.files.<a href="./src/letta_sdk/resources/sources/files.py">list</a>(source_id, \*\*<a href="src/letta_sdk/types/sources/file_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/sources/file_list_response.py">FileListResponse</a></code>

# Folders

Types:

```python
from letta_sdk.types import (
    Folder,
    FolderListResponse,
    FolderCountResponse,
    FolderGetByNameResponse,
    FolderListAgentsResponse,
    FolderListFilesResponse,
    FolderListPassagesResponse,
)
```

Methods:

- <code title="post /v1/folders/">client.folders.<a href="./src/letta_sdk/resources/folders.py">create</a>(\*\*<a href="src/letta_sdk/types/folder_create_params.py">params</a>) -> <a href="./src/letta_sdk/types/folder.py">Folder</a></code>
- <code title="get /v1/folders/{folder_id}">client.folders.<a href="./src/letta_sdk/resources/folders.py">retrieve</a>(folder_id) -> <a href="./src/letta_sdk/types/folder.py">Folder</a></code>
- <code title="patch /v1/folders/{folder_id}">client.folders.<a href="./src/letta_sdk/resources/folders.py">update</a>(folder_id, \*\*<a href="src/letta_sdk/types/folder_update_params.py">params</a>) -> <a href="./src/letta_sdk/types/folder.py">Folder</a></code>
- <code title="get /v1/folders/">client.folders.<a href="./src/letta_sdk/resources/folders.py">list</a>(\*\*<a href="src/letta_sdk/types/folder_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/folder_list_response.py">FolderListResponse</a></code>
- <code title="delete /v1/folders/{folder_id}">client.folders.<a href="./src/letta_sdk/resources/folders.py">delete</a>(folder_id) -> object</code>
- <code title="get /v1/folders/count">client.folders.<a href="./src/letta_sdk/resources/folders.py">count</a>() -> <a href="./src/letta_sdk/types/folder_count_response.py">FolderCountResponse</a></code>
- <code title="delete /v1/folders/{folder_id}/{file_id}">client.folders.<a href="./src/letta_sdk/resources/folders.py">delete_file</a>(file_id, \*, folder_id) -> None</code>
- <code title="get /v1/folders/name/{folder_name}">client.folders.<a href="./src/letta_sdk/resources/folders.py">get_by_name</a>(folder_name) -> str</code>
- <code title="get /v1/folders/{folder_id}/agents">client.folders.<a href="./src/letta_sdk/resources/folders.py">list_agents</a>(folder_id, \*\*<a href="src/letta_sdk/types/folder_list_agents_params.py">params</a>) -> <a href="./src/letta_sdk/types/folder_list_agents_response.py">FolderListAgentsResponse</a></code>
- <code title="get /v1/folders/{folder_id}/files">client.folders.<a href="./src/letta_sdk/resources/folders.py">list_files</a>(folder_id, \*\*<a href="src/letta_sdk/types/folder_list_files_params.py">params</a>) -> <a href="./src/letta_sdk/types/folder_list_files_response.py">FolderListFilesResponse</a></code>
- <code title="get /v1/folders/{folder_id}/passages">client.folders.<a href="./src/letta_sdk/resources/folders.py">list_passages</a>(folder_id, \*\*<a href="src/letta_sdk/types/folder_list_passages_params.py">params</a>) -> <a href="./src/letta_sdk/types/folder_list_passages_response.py">FolderListPassagesResponse</a></code>
- <code title="get /v1/folders/metadata">client.folders.<a href="./src/letta_sdk/resources/folders.py">retrieve_metadata</a>(\*\*<a href="src/letta_sdk/types/folder_retrieve_metadata_params.py">params</a>) -> <a href="./src/letta_sdk/types/organization_sources_stats.py">OrganizationSourcesStats</a></code>
- <code title="post /v1/folders/{folder_id}/upload">client.folders.<a href="./src/letta_sdk/resources/folders.py">upload_file</a>(folder_id, \*\*<a href="src/letta_sdk/types/folder_upload_file_params.py">params</a>) -> <a href="./src/letta_sdk/types/file_metadata.py">FileMetadata</a></code>

# Agents

Types:

```python
from letta_sdk.types import (
    AgentEnvironmentVariable,
    AgentState,
    AgentType,
    ChildToolRule,
    ConditionalToolRule,
    ContinueToolRule,
    InitToolRule,
    JsonObjectResponseFormat,
    JsonSchemaResponseFormat,
    LettaMessageContentUnion,
    MaxCountPerStepToolRule,
    MessageCreate,
    ParentToolRule,
    RequiredBeforeExitToolRule,
    RequiresApprovalToolRule,
    TerminalToolRule,
    TextResponseFormat,
    AgentListResponse,
    AgentCountResponse,
    AgentExportResponse,
    AgentImportResponse,
    AgentListGroupsResponse,
    AgentMigrateResponse,
    AgentRetrieveContextResponse,
    AgentSearchResponse,
)
```

Methods:

- <code title="post /v1/agents/">client.agents.<a href="./src/letta_sdk/resources/agents/agents.py">create</a>(\*\*<a href="src/letta_sdk/types/agent_create_params.py">params</a>) -> <a href="./src/letta_sdk/types/agent_state.py">AgentState</a></code>
- <code title="get /v1/agents/{agent_id}">client.agents.<a href="./src/letta_sdk/resources/agents/agents.py">retrieve</a>(agent_id, \*\*<a href="src/letta_sdk/types/agent_retrieve_params.py">params</a>) -> <a href="./src/letta_sdk/types/agent_state.py">AgentState</a></code>
- <code title="patch /v1/agents/{agent_id}">client.agents.<a href="./src/letta_sdk/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/letta_sdk/types/agent_update_params.py">params</a>) -> <a href="./src/letta_sdk/types/agent_state.py">AgentState</a></code>
- <code title="get /v1/agents/">client.agents.<a href="./src/letta_sdk/resources/agents/agents.py">list</a>(\*\*<a href="src/letta_sdk/types/agent_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /v1/agents/{agent_id}">client.agents.<a href="./src/letta_sdk/resources/agents/agents.py">delete</a>(agent_id) -> object</code>
- <code title="get /v1/agents/count">client.agents.<a href="./src/letta_sdk/resources/agents/agents.py">count</a>() -> <a href="./src/letta_sdk/types/agent_count_response.py">AgentCountResponse</a></code>
- <code title="get /v1/agents/{agent_id}/export">client.agents.<a href="./src/letta_sdk/resources/agents/agents.py">export</a>(agent_id, \*\*<a href="src/letta_sdk/types/agent_export_params.py">params</a>) -> str</code>
- <code title="post /v1/agents/import">client.agents.<a href="./src/letta_sdk/resources/agents/agents.py">import\_</a>(\*\*<a href="src/letta_sdk/types/agent_import_params.py">params</a>) -> <a href="./src/letta_sdk/types/agent_import_response.py">AgentImportResponse</a></code>
- <code title="get /v1/agents/{agent_id}/groups">client.agents.<a href="./src/letta_sdk/resources/agents/agents.py">list_groups</a>(agent_id, \*\*<a href="src/letta_sdk/types/agent_list_groups_params.py">params</a>) -> <a href="./src/letta_sdk/types/agent_list_groups_response.py">AgentListGroupsResponse</a></code>
- <code title="post /v1/agents/{agent_id}/migrate">client.agents.<a href="./src/letta_sdk/resources/agents/agents.py">migrate</a>(agent_id, \*\*<a href="src/letta_sdk/types/agent_migrate_params.py">params</a>) -> <a href="./src/letta_sdk/types/agent_migrate_response.py">AgentMigrateResponse</a></code>
- <code title="patch /v1/agents/{agent_id}/reset-messages">client.agents.<a href="./src/letta_sdk/resources/agents/agents.py">reset_messages</a>(agent_id, \*\*<a href="src/letta_sdk/types/agent_reset_messages_params.py">params</a>) -> <a href="./src/letta_sdk/types/agent_state.py">AgentState</a></code>
- <code title="get /v1/agents/{agent_id}/context">client.agents.<a href="./src/letta_sdk/resources/agents/agents.py">retrieve_context</a>(agent_id) -> <a href="./src/letta_sdk/types/agent_retrieve_context_response.py">AgentRetrieveContextResponse</a></code>
- <code title="post /v1/agents/search">client.agents.<a href="./src/letta_sdk/resources/agents/agents.py">search</a>(\*\*<a href="src/letta_sdk/types/agent_search_params.py">params</a>) -> <a href="./src/letta_sdk/types/agent_search_response.py">AgentSearchResponse</a></code>
- <code title="post /v1/agents/{agent_id}/summarize">client.agents.<a href="./src/letta_sdk/resources/agents/agents.py">summarize</a>(agent_id, \*\*<a href="src/letta_sdk/types/agent_summarize_params.py">params</a>) -> None</code>

## Tools

Types:

```python
from letta_sdk.types.agents import ToolListResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/tools">client.agents.tools.<a href="./src/letta_sdk/resources/agents/tools.py">list</a>(agent_id) -> <a href="./src/letta_sdk/types/agents/tool_list_response.py">ToolListResponse</a></code>
- <code title="patch /v1/agents/{agent_id}/tools/attach/{tool_id}">client.agents.tools.<a href="./src/letta_sdk/resources/agents/tools.py">attach</a>(tool_id, \*, agent_id) -> <a href="./src/letta_sdk/types/agent_state.py">AgentState</a></code>
- <code title="patch /v1/agents/{agent_id}/tools/detach/{tool_id}">client.agents.tools.<a href="./src/letta_sdk/resources/agents/tools.py">detach</a>(tool_id, \*, agent_id) -> <a href="./src/letta_sdk/types/agent_state.py">AgentState</a></code>
- <code title="patch /v1/agents/{agent_id}/tools/approval/{tool_name}">client.agents.tools.<a href="./src/letta_sdk/resources/agents/tools.py">modify_approval</a>(tool_name, \*, agent_id, \*\*<a href="src/letta_sdk/types/agents/tool_modify_approval_params.py">params</a>) -> <a href="./src/letta_sdk/types/agent_state.py">AgentState</a></code>

## Sources

Types:

```python
from letta_sdk.types.agents import SourceListResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/sources">client.agents.sources.<a href="./src/letta_sdk/resources/agents/sources.py">list</a>(agent_id) -> <a href="./src/letta_sdk/types/agents/source_list_response.py">SourceListResponse</a></code>
- <code title="patch /v1/agents/{agent_id}/sources/attach/{source_id}">client.agents.sources.<a href="./src/letta_sdk/resources/agents/sources.py">attach</a>(source_id, \*, agent_id) -> <a href="./src/letta_sdk/types/agent_state.py">AgentState</a></code>
- <code title="patch /v1/agents/{agent_id}/sources/detach/{source_id}">client.agents.sources.<a href="./src/letta_sdk/resources/agents/sources.py">detach</a>(source_id, \*, agent_id) -> <a href="./src/letta_sdk/types/agent_state.py">AgentState</a></code>

## Folders

Types:

```python
from letta_sdk.types.agents import FolderListResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/folders">client.agents.folders.<a href="./src/letta_sdk/resources/agents/folders.py">list</a>(agent_id) -> <a href="./src/letta_sdk/types/agents/folder_list_response.py">FolderListResponse</a></code>
- <code title="patch /v1/agents/{agent_id}/folders/attach/{folder_id}">client.agents.folders.<a href="./src/letta_sdk/resources/agents/folders.py">attach</a>(folder_id, \*, agent_id) -> <a href="./src/letta_sdk/types/agent_state.py">AgentState</a></code>
- <code title="patch /v1/agents/{agent_id}/folders/detach/{folder_id}">client.agents.folders.<a href="./src/letta_sdk/resources/agents/folders.py">detach</a>(folder_id, \*, agent_id) -> <a href="./src/letta_sdk/types/agent_state.py">AgentState</a></code>

## Files

Types:

```python
from letta_sdk.types.agents import FileListResponse, FileCloseAllResponse, FileOpenResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/files">client.agents.files.<a href="./src/letta_sdk/resources/agents/files.py">list</a>(agent_id, \*\*<a href="src/letta_sdk/types/agents/file_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/agents/file_list_response.py">FileListResponse</a></code>
- <code title="patch /v1/agents/{agent_id}/files/{file_id}/close">client.agents.files.<a href="./src/letta_sdk/resources/agents/files.py">close</a>(file_id, \*, agent_id) -> object</code>
- <code title="patch /v1/agents/{agent_id}/files/close-all">client.agents.files.<a href="./src/letta_sdk/resources/agents/files.py">close_all</a>(agent_id) -> <a href="./src/letta_sdk/types/agents/file_close_all_response.py">FileCloseAllResponse</a></code>
- <code title="patch /v1/agents/{agent_id}/files/{file_id}/open">client.agents.files.<a href="./src/letta_sdk/resources/agents/files.py">open</a>(file_id, \*, agent_id) -> <a href="./src/letta_sdk/types/agents/file_open_response.py">FileOpenResponse</a></code>

## CoreMemory

Types:

```python
from letta_sdk.types.agents import Memory, CoreMemoryRetrieveVariablesResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/core-memory">client.agents.core_memory.<a href="./src/letta_sdk/resources/agents/core_memory/core_memory.py">retrieve</a>(agent_id) -> <a href="./src/letta_sdk/types/agents/memory.py">Memory</a></code>
- <code title="get /v1/agents/{agent_id}/core-memory/variables">client.agents.core_memory.<a href="./src/letta_sdk/resources/agents/core_memory/core_memory.py">retrieve_variables</a>(agent_id) -> <a href="./src/letta_sdk/types/agents/core_memory_retrieve_variables_response.py">CoreMemoryRetrieveVariablesResponse</a></code>

### Blocks

Types:

```python
from letta_sdk.types.agents.core_memory import Block, BlockUpdate, BlockListResponse
```

Methods:

- <code title="get /v1/agents/{agent_id}/core-memory/blocks/{block_label}">client.agents.core_memory.blocks.<a href="./src/letta_sdk/resources/agents/core_memory/blocks.py">retrieve</a>(block_label, \*, agent_id) -> <a href="./src/letta_sdk/types/agents/core_memory/block.py">Block</a></code>
- <code title="patch /v1/agents/{agent_id}/core-memory/blocks/{block_label}">client.agents.core_memory.blocks.<a href="./src/letta_sdk/resources/agents/core_memory/blocks.py">update</a>(block_label, \*, agent_id, \*\*<a href="src/letta_sdk/types/agents/core_memory/block_update_params.py">params</a>) -> <a href="./src/letta_sdk/types/agents/core_memory/block.py">Block</a></code>
- <code title="get /v1/agents/{agent_id}/core-memory/blocks">client.agents.core_memory.blocks.<a href="./src/letta_sdk/resources/agents/core_memory/blocks.py">list</a>(agent_id) -> <a href="./src/letta_sdk/types/agents/core_memory/block_list_response.py">BlockListResponse</a></code>
- <code title="patch /v1/agents/{agent_id}/core-memory/blocks/attach/{block_id}">client.agents.core_memory.blocks.<a href="./src/letta_sdk/resources/agents/core_memory/blocks.py">attach</a>(block_id, \*, agent_id) -> <a href="./src/letta_sdk/types/agent_state.py">AgentState</a></code>
- <code title="patch /v1/agents/{agent_id}/core-memory/blocks/detach/{block_id}">client.agents.core_memory.blocks.<a href="./src/letta_sdk/resources/agents/core_memory/blocks.py">detach</a>(block_id, \*, agent_id) -> <a href="./src/letta_sdk/types/agent_state.py">AgentState</a></code>

## ArchivalMemory

Types:

```python
from letta_sdk.types.agents import (
    ArchivalMemoryCreateResponse,
    ArchivalMemoryListResponse,
    ArchivalMemorySearchResponse,
)
```

Methods:

- <code title="post /v1/agents/{agent_id}/archival-memory">client.agents.archival_memory.<a href="./src/letta_sdk/resources/agents/archival_memory.py">create</a>(agent_id, \*\*<a href="src/letta_sdk/types/agents/archival_memory_create_params.py">params</a>) -> <a href="./src/letta_sdk/types/agents/archival_memory_create_response.py">ArchivalMemoryCreateResponse</a></code>
- <code title="get /v1/agents/{agent_id}/archival-memory">client.agents.archival_memory.<a href="./src/letta_sdk/resources/agents/archival_memory.py">list</a>(agent_id, \*\*<a href="src/letta_sdk/types/agents/archival_memory_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/agents/archival_memory_list_response.py">ArchivalMemoryListResponse</a></code>
- <code title="delete /v1/agents/{agent_id}/archival-memory/{memory_id}">client.agents.archival_memory.<a href="./src/letta_sdk/resources/agents/archival_memory.py">delete</a>(memory_id, \*, agent_id) -> object</code>
- <code title="get /v1/agents/{agent_id}/archival-memory/search">client.agents.archival_memory.<a href="./src/letta_sdk/resources/agents/archival_memory.py">search</a>(agent_id, \*\*<a href="src/letta_sdk/types/agents/archival_memory_search_params.py">params</a>) -> <a href="./src/letta_sdk/types/agents/archival_memory_search_response.py">ArchivalMemorySearchResponse</a></code>

## Messages

Types:

```python
from letta_sdk.types.agents import (
    ApprovalCreate,
    ApprovalRequestMessage,
    ApprovalResponseMessage,
    AssistantMessage,
    HiddenReasoningMessage,
    ImageContent,
    JobStatus,
    JobType,
    LettaAssistantMessageContentUnion,
    LettaMessageUnion,
    LettaRequest,
    LettaResponse,
    LettaStreamingRequest,
    LettaUserMessageContentUnion,
    Message,
    MessageRole,
    MessageType,
    OmittedReasoningContent,
    ReasoningContent,
    ReasoningMessage,
    RedactedReasoningContent,
    Run,
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
    MessageListResponse,
    MessageCancelResponse,
    MessagePreviewRawPayloadResponse,
    MessageSearchResponse,
)
```

Methods:

- <code title="patch /v1/agents/{agent_id}/messages/{message_id}">client.agents.messages.<a href="./src/letta_sdk/resources/agents/messages.py">update</a>(message_id, \*, agent_id, \*\*<a href="src/letta_sdk/types/agents/message_update_params.py">params</a>) -> <a href="./src/letta_sdk/types/agents/message_update_response.py">MessageUpdateResponse</a></code>
- <code title="get /v1/agents/{agent_id}/messages">client.agents.messages.<a href="./src/letta_sdk/resources/agents/messages.py">list</a>(agent_id, \*\*<a href="src/letta_sdk/types/agents/message_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/agents/message_list_response.py">MessageListResponse</a></code>
- <code title="post /v1/agents/{agent_id}/messages/cancel">client.agents.messages.<a href="./src/letta_sdk/resources/agents/messages.py">cancel</a>(agent_id, \*\*<a href="src/letta_sdk/types/agents/message_cancel_params.py">params</a>) -> <a href="./src/letta_sdk/types/agents/message_cancel_response.py">MessageCancelResponse</a></code>
- <code title="post /v1/agents/{agent_id}/messages/preview-raw-payload">client.agents.messages.<a href="./src/letta_sdk/resources/agents/messages.py">preview_raw_payload</a>(agent_id, \*\*<a href="src/letta_sdk/types/agents/message_preview_raw_payload_params.py">params</a>) -> <a href="./src/letta_sdk/types/agents/message_preview_raw_payload_response.py">MessagePreviewRawPayloadResponse</a></code>
- <code title="post /v1/agents/messages/search">client.agents.messages.<a href="./src/letta_sdk/resources/agents/messages.py">search</a>(\*\*<a href="src/letta_sdk/types/agents/message_search_params.py">params</a>) -> <a href="./src/letta_sdk/types/agents/message_search_response.py">MessageSearchResponse</a></code>
- <code title="post /v1/agents/{agent_id}/messages">client.agents.messages.<a href="./src/letta_sdk/resources/agents/messages.py">send</a>(agent_id, \*\*<a href="src/letta_sdk/types/agents/message_send_params.py">params</a>) -> <a href="./src/letta_sdk/types/agents/letta_response.py">LettaResponse</a></code>
- <code title="post /v1/agents/{agent_id}/messages/async">client.agents.messages.<a href="./src/letta_sdk/resources/agents/messages.py">send_async</a>(agent_id, \*\*<a href="src/letta_sdk/types/agents/message_send_async_params.py">params</a>) -> <a href="./src/letta_sdk/types/agents/run.py">Run</a></code>
- <code title="post /v1/agents/{agent_id}/messages/stream">client.agents.messages.<a href="./src/letta_sdk/resources/agents/messages.py">send_stream</a>(agent_id, \*\*<a href="src/letta_sdk/types/agents/message_send_stream_params.py">params</a>) -> object</code>

# Groups

Types:

```python
from letta_sdk.types import (
    DynamicManager,
    Group,
    ManagerType,
    RoundRobinManager,
    SleeptimeManager,
    SupervisorManager,
    VoiceSleeptimeManager,
    GroupListResponse,
    GroupCountResponse,
)
```

Methods:

- <code title="post /v1/groups/">client.groups.<a href="./src/letta_sdk/resources/groups/groups.py">create</a>(\*\*<a href="src/letta_sdk/types/group_create_params.py">params</a>) -> <a href="./src/letta_sdk/types/group.py">Group</a></code>
- <code title="get /v1/groups/{group_id}">client.groups.<a href="./src/letta_sdk/resources/groups/groups.py">retrieve</a>(group_id) -> <a href="./src/letta_sdk/types/group.py">Group</a></code>
- <code title="patch /v1/groups/{group_id}">client.groups.<a href="./src/letta_sdk/resources/groups/groups.py">update</a>(group_id, \*\*<a href="src/letta_sdk/types/group_update_params.py">params</a>) -> <a href="./src/letta_sdk/types/group.py">Group</a></code>
- <code title="get /v1/groups/">client.groups.<a href="./src/letta_sdk/resources/groups/groups.py">list</a>(\*\*<a href="src/letta_sdk/types/group_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/group_list_response.py">GroupListResponse</a></code>
- <code title="delete /v1/groups/{group_id}">client.groups.<a href="./src/letta_sdk/resources/groups/groups.py">delete</a>(group_id) -> object</code>
- <code title="get /v1/groups/count">client.groups.<a href="./src/letta_sdk/resources/groups/groups.py">count</a>() -> <a href="./src/letta_sdk/types/group_count_response.py">GroupCountResponse</a></code>
- <code title="patch /v1/groups/{group_id}/reset-messages">client.groups.<a href="./src/letta_sdk/resources/groups/groups.py">reset_messages</a>(group_id) -> object</code>

## Messages

Types:

```python
from letta_sdk.types.groups import MessageUpdateResponse, MessageListResponse
```

Methods:

- <code title="patch /v1/groups/{group_id}/messages/{message_id}">client.groups.messages.<a href="./src/letta_sdk/resources/groups/messages.py">update</a>(message_id, \*, group_id, \*\*<a href="src/letta_sdk/types/groups/message_update_params.py">params</a>) -> <a href="./src/letta_sdk/types/groups/message_update_response.py">MessageUpdateResponse</a></code>
- <code title="get /v1/groups/{group_id}/messages">client.groups.messages.<a href="./src/letta_sdk/resources/groups/messages.py">list</a>(group_id, \*\*<a href="src/letta_sdk/types/groups/message_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/groups/message_list_response.py">MessageListResponse</a></code>
- <code title="post /v1/groups/{group_id}/messages">client.groups.messages.<a href="./src/letta_sdk/resources/groups/messages.py">send</a>(group_id, \*\*<a href="src/letta_sdk/types/groups/message_send_params.py">params</a>) -> <a href="./src/letta_sdk/types/agents/letta_response.py">LettaResponse</a></code>
- <code title="post /v1/groups/{group_id}/messages/stream">client.groups.messages.<a href="./src/letta_sdk/resources/groups/messages.py">send_stream</a>(group_id, \*\*<a href="src/letta_sdk/types/groups/message_send_stream_params.py">params</a>) -> object</code>

# Identities

Types:

```python
from letta_sdk.types import (
    Identity,
    IdentityProperty,
    IdentityType,
    IdentityListResponse,
    IdentityCountResponse,
    IdentityListAgentsResponse,
    IdentityListBlocksResponse,
)
```

Methods:

- <code title="post /v1/identities/">client.identities.<a href="./src/letta_sdk/resources/identities.py">create</a>(\*\*<a href="src/letta_sdk/types/identity_create_params.py">params</a>) -> <a href="./src/letta_sdk/types/identity.py">Identity</a></code>
- <code title="get /v1/identities/{identity_id}">client.identities.<a href="./src/letta_sdk/resources/identities.py">retrieve</a>(identity_id) -> <a href="./src/letta_sdk/types/identity.py">Identity</a></code>
- <code title="get /v1/identities/">client.identities.<a href="./src/letta_sdk/resources/identities.py">list</a>(\*\*<a href="src/letta_sdk/types/identity_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/identity_list_response.py">IdentityListResponse</a></code>
- <code title="delete /v1/identities/{identity_id}">client.identities.<a href="./src/letta_sdk/resources/identities.py">delete</a>(identity_id) -> object</code>
- <code title="get /v1/identities/count">client.identities.<a href="./src/letta_sdk/resources/identities.py">count</a>() -> <a href="./src/letta_sdk/types/identity_count_response.py">IdentityCountResponse</a></code>
- <code title="get /v1/identities/{identity_id}/agents">client.identities.<a href="./src/letta_sdk/resources/identities.py">list_agents</a>(identity_id, \*\*<a href="src/letta_sdk/types/identity_list_agents_params.py">params</a>) -> <a href="./src/letta_sdk/types/identity_list_agents_response.py">IdentityListAgentsResponse</a></code>
- <code title="get /v1/identities/{identity_id}/blocks">client.identities.<a href="./src/letta_sdk/resources/identities.py">list_blocks</a>(identity_id, \*\*<a href="src/letta_sdk/types/identity_list_blocks_params.py">params</a>) -> <a href="./src/letta_sdk/types/identity_list_blocks_response.py">IdentityListBlocksResponse</a></code>
- <code title="patch /v1/identities/{identity_id}">client.identities.<a href="./src/letta_sdk/resources/identities.py">modify</a>(identity_id, \*\*<a href="src/letta_sdk/types/identity_modify_params.py">params</a>) -> <a href="./src/letta_sdk/types/identity.py">Identity</a></code>
- <code title="put /v1/identities/">client.identities.<a href="./src/letta_sdk/resources/identities.py">upsert</a>(\*\*<a href="src/letta_sdk/types/identity_upsert_params.py">params</a>) -> <a href="./src/letta_sdk/types/identity.py">Identity</a></code>
- <code title="put /v1/identities/{identity_id}/properties">client.identities.<a href="./src/letta_sdk/resources/identities.py">upsert_properties</a>(identity_id, \*\*<a href="src/letta_sdk/types/identity_upsert_properties_params.py">params</a>) -> object</code>

# \_InternalTemplates

Methods:

- <code title="post /v1/_internal_templates/agents">client.\_internal_templates.<a href="./src/letta_sdk/resources/_internal_templates/_internal_templates.py">create_agent</a>(\*\*<a href="src/letta_sdk/types/internal_template_create_agent_params.py">params</a>) -> <a href="./src/letta_sdk/types/agent_state.py">AgentState</a></code>
- <code title="post /v1/_internal_templates/blocks">client.\_internal_templates.<a href="./src/letta_sdk/resources/_internal_templates/_internal_templates.py">create_block</a>(\*\*<a href="src/letta_sdk/types/internal_template_create_block_params.py">params</a>) -> <a href="./src/letta_sdk/types/agents/core_memory/block.py">Block</a></code>
- <code title="post /v1/_internal_templates/groups">client.\_internal_templates.<a href="./src/letta_sdk/resources/_internal_templates/_internal_templates.py">create_group</a>(\*\*<a href="src/letta_sdk/types/internal_template_create_group_params.py">params</a>) -> <a href="./src/letta_sdk/types/group.py">Group</a></code>

## Deployment

Types:

```python
from letta_sdk.types._internal_templates import (
    DeploymentDeleteResponse,
    DeploymentListEntitiesResponse,
)
```

Methods:

- <code title="delete /v1/_internal_templates/deployment/{deployment_id}">client.\_internal_templates.deployment.<a href="./src/letta_sdk/resources/_internal_templates/deployment.py">delete</a>(deployment_id) -> <a href="./src/letta_sdk/types/_internal_templates/deployment_delete_response.py">DeploymentDeleteResponse</a></code>
- <code title="get /v1/_internal_templates/deployment/{deployment_id}">client.\_internal_templates.deployment.<a href="./src/letta_sdk/resources/_internal_templates/deployment.py">list_entities</a>(deployment_id, \*\*<a href="src/letta_sdk/types/_internal_templates/deployment_list_entities_params.py">params</a>) -> <a href="./src/letta_sdk/types/_internal_templates/deployment_list_entities_response.py">DeploymentListEntitiesResponse</a></code>

# Models

Types:

```python
from letta_sdk.types import (
    EmbeddingConfig,
    LlmConfig,
    ProviderCategory,
    ProviderType,
    ModelListResponse,
    ModelListEmbeddingResponse,
)
```

Methods:

- <code title="get /v1/models/">client.models.<a href="./src/letta_sdk/resources/models.py">list</a>(\*\*<a href="src/letta_sdk/types/model_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/model_list_response.py">ModelListResponse</a></code>
- <code title="get /v1/models/embedding">client.models.<a href="./src/letta_sdk/resources/models.py">list_embedding</a>() -> <a href="./src/letta_sdk/types/model_list_embedding_response.py">ModelListEmbeddingResponse</a></code>
- <code title="get /v1/models/embeddings">client.models.<a href="./src/letta_sdk/resources/models.py">list_embeddings</a>() -> None</code>

# Blocks

Types:

```python
from letta_sdk.types import (
    CreateBlock,
    BlockListResponse,
    BlockCountResponse,
    BlockListAgentsResponse,
)
```

Methods:

- <code title="post /v1/blocks/">client.blocks.<a href="./src/letta_sdk/resources/blocks.py">create</a>(\*\*<a href="src/letta_sdk/types/block_create_params.py">params</a>) -> <a href="./src/letta_sdk/types/agents/core_memory/block.py">Block</a></code>
- <code title="get /v1/blocks/{block_id}">client.blocks.<a href="./src/letta_sdk/resources/blocks.py">retrieve</a>(block_id) -> <a href="./src/letta_sdk/types/agents/core_memory/block.py">Block</a></code>
- <code title="patch /v1/blocks/{block_id}">client.blocks.<a href="./src/letta_sdk/resources/blocks.py">update</a>(block_id, \*\*<a href="src/letta_sdk/types/block_update_params.py">params</a>) -> <a href="./src/letta_sdk/types/agents/core_memory/block.py">Block</a></code>
- <code title="get /v1/blocks/">client.blocks.<a href="./src/letta_sdk/resources/blocks.py">list</a>(\*\*<a href="src/letta_sdk/types/block_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/block_list_response.py">BlockListResponse</a></code>
- <code title="delete /v1/blocks/{block_id}">client.blocks.<a href="./src/letta_sdk/resources/blocks.py">delete</a>(block_id) -> object</code>
- <code title="get /v1/blocks/count">client.blocks.<a href="./src/letta_sdk/resources/blocks.py">count</a>() -> <a href="./src/letta_sdk/types/block_count_response.py">BlockCountResponse</a></code>
- <code title="get /v1/blocks/{block_id}/agents">client.blocks.<a href="./src/letta_sdk/resources/blocks.py">list_agents</a>(block_id, \*\*<a href="src/letta_sdk/types/block_list_agents_params.py">params</a>) -> <a href="./src/letta_sdk/types/block_list_agents_response.py">BlockListAgentsResponse</a></code>

# Jobs

Types:

```python
from letta_sdk.types import Job, JobListResponse, JobListActiveResponse
```

Methods:

- <code title="get /v1/jobs/{job_id}">client.jobs.<a href="./src/letta_sdk/resources/jobs.py">retrieve</a>(job_id) -> <a href="./src/letta_sdk/types/job.py">Job</a></code>
- <code title="get /v1/jobs/">client.jobs.<a href="./src/letta_sdk/resources/jobs.py">list</a>(\*\*<a href="src/letta_sdk/types/job_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/job_list_response.py">JobListResponse</a></code>
- <code title="delete /v1/jobs/{job_id}">client.jobs.<a href="./src/letta_sdk/resources/jobs.py">delete</a>(job_id) -> <a href="./src/letta_sdk/types/job.py">Job</a></code>
- <code title="patch /v1/jobs/{job_id}/cancel">client.jobs.<a href="./src/letta_sdk/resources/jobs.py">cancel</a>(job_id) -> <a href="./src/letta_sdk/types/job.py">Job</a></code>
- <code title="get /v1/jobs/active">client.jobs.<a href="./src/letta_sdk/resources/jobs.py">list_active</a>(\*\*<a href="src/letta_sdk/types/job_list_active_params.py">params</a>) -> <a href="./src/letta_sdk/types/job_list_active_response.py">JobListActiveResponse</a></code>

# Health

Types:

```python
from letta_sdk.types import HealthCheckResponse
```

Methods:

- <code title="get /v1/health/">client.health.<a href="./src/letta_sdk/resources/health.py">check</a>() -> <a href="./src/letta_sdk/types/health_check_response.py">HealthCheckResponse</a></code>

# Providers

Types:

```python
from letta_sdk.types import Provider, ProviderListResponse
```

Methods:

- <code title="post /v1/providers/">client.providers.<a href="./src/letta_sdk/resources/providers.py">create</a>(\*\*<a href="src/letta_sdk/types/provider_create_params.py">params</a>) -> <a href="./src/letta_sdk/types/provider.py">Provider</a></code>
- <code title="get /v1/providers/{provider_id}">client.providers.<a href="./src/letta_sdk/resources/providers.py">retrieve</a>(provider_id) -> <a href="./src/letta_sdk/types/provider.py">Provider</a></code>
- <code title="patch /v1/providers/{provider_id}">client.providers.<a href="./src/letta_sdk/resources/providers.py">update</a>(provider_id, \*\*<a href="src/letta_sdk/types/provider_update_params.py">params</a>) -> <a href="./src/letta_sdk/types/provider.py">Provider</a></code>
- <code title="get /v1/providers/">client.providers.<a href="./src/letta_sdk/resources/providers.py">list</a>(\*\*<a href="src/letta_sdk/types/provider_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/provider_list_response.py">ProviderListResponse</a></code>
- <code title="delete /v1/providers/{provider_id}">client.providers.<a href="./src/letta_sdk/resources/providers.py">delete</a>(provider_id) -> object</code>
- <code title="post /v1/providers/check">client.providers.<a href="./src/letta_sdk/resources/providers.py">check</a>(\*\*<a href="src/letta_sdk/types/provider_check_params.py">params</a>) -> object</code>

# Runs

Types:

```python
from letta_sdk.types import (
    StopReasonType,
    RunListResponse,
    RunListActiveResponse,
    RunListMessagesResponse,
    RunListStepsResponse,
    RunRetrieveUsageResponse,
)
```

Methods:

- <code title="get /v1/runs/{run_id}">client.runs.<a href="./src/letta_sdk/resources/runs.py">retrieve</a>(run_id) -> <a href="./src/letta_sdk/types/agents/run.py">Run</a></code>
- <code title="get /v1/runs/">client.runs.<a href="./src/letta_sdk/resources/runs.py">list</a>(\*\*<a href="src/letta_sdk/types/run_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/run_list_response.py">RunListResponse</a></code>
- <code title="delete /v1/runs/{run_id}">client.runs.<a href="./src/letta_sdk/resources/runs.py">delete</a>(run_id) -> <a href="./src/letta_sdk/types/agents/run.py">Run</a></code>
- <code title="get /v1/runs/active">client.runs.<a href="./src/letta_sdk/resources/runs.py">list_active</a>(\*\*<a href="src/letta_sdk/types/run_list_active_params.py">params</a>) -> <a href="./src/letta_sdk/types/run_list_active_response.py">RunListActiveResponse</a></code>
- <code title="get /v1/runs/{run_id}/messages">client.runs.<a href="./src/letta_sdk/resources/runs.py">list_messages</a>(run_id, \*\*<a href="src/letta_sdk/types/run_list_messages_params.py">params</a>) -> <a href="./src/letta_sdk/types/run_list_messages_response.py">RunListMessagesResponse</a></code>
- <code title="get /v1/runs/{run_id}/steps">client.runs.<a href="./src/letta_sdk/resources/runs.py">list_steps</a>(run_id, \*\*<a href="src/letta_sdk/types/run_list_steps_params.py">params</a>) -> <a href="./src/letta_sdk/types/run_list_steps_response.py">RunListStepsResponse</a></code>
- <code title="post /v1/runs/{run_id}/stream">client.runs.<a href="./src/letta_sdk/resources/runs.py">retrieve_stream</a>(run_id, \*\*<a href="src/letta_sdk/types/run_retrieve_stream_params.py">params</a>) -> object</code>
- <code title="get /v1/runs/{run_id}/usage">client.runs.<a href="./src/letta_sdk/resources/runs.py">retrieve_usage</a>(run_id) -> <a href="./src/letta_sdk/types/run_retrieve_usage_response.py">RunRetrieveUsageResponse</a></code>

# Steps

Types:

```python
from letta_sdk.types import (
    ProviderTrace,
    Step,
    StepListResponse,
    StepListMessagesResponse,
    StepRetrieveMetricsResponse,
)
```

Methods:

- <code title="get /v1/steps/{step_id}">client.steps.<a href="./src/letta_sdk/resources/steps.py">retrieve</a>(step_id) -> <a href="./src/letta_sdk/types/step.py">Step</a></code>
- <code title="get /v1/steps/">client.steps.<a href="./src/letta_sdk/resources/steps.py">list</a>(\*\*<a href="src/letta_sdk/types/step_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/step_list_response.py">StepListResponse</a></code>
- <code title="get /v1/steps/{step_id}/messages">client.steps.<a href="./src/letta_sdk/resources/steps.py">list_messages</a>(step_id, \*\*<a href="src/letta_sdk/types/step_list_messages_params.py">params</a>) -> <a href="./src/letta_sdk/types/step_list_messages_response.py">StepListMessagesResponse</a></code>
- <code title="get /v1/steps/{step_id}/metrics">client.steps.<a href="./src/letta_sdk/resources/steps.py">retrieve_metrics</a>(step_id) -> <a href="./src/letta_sdk/types/step_retrieve_metrics_response.py">StepRetrieveMetricsResponse</a></code>
- <code title="get /v1/steps/{step_id}/trace">client.steps.<a href="./src/letta_sdk/resources/steps.py">retrieve_trace</a>(step_id) -> <a href="./src/letta_sdk/types/provider_trace.py">Optional[ProviderTrace]</a></code>
- <code title="patch /v1/steps/{step_id}/feedback">client.steps.<a href="./src/letta_sdk/resources/steps.py">update_feedback</a>(step_id, \*\*<a href="src/letta_sdk/types/step_update_feedback_params.py">params</a>) -> <a href="./src/letta_sdk/types/step.py">Step</a></code>

# Tags

Types:

```python
from letta_sdk.types import TagListResponse
```

Methods:

- <code title="get /v1/tags/">client.tags.<a href="./src/letta_sdk/resources/tags.py">list</a>(\*\*<a href="src/letta_sdk/types/tag_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/tag_list_response.py">TagListResponse</a></code>

# Telemetry

Methods:

- <code title="get /v1/telemetry/{step_id}">client.telemetry.<a href="./src/letta_sdk/resources/telemetry.py">retrieve</a>(step_id) -> <a href="./src/letta_sdk/types/provider_trace.py">Optional[ProviderTrace]</a></code>

# Messages

## Batches

Types:

```python
from letta_sdk.types.messages import BatchJob, BatchListResponse, BatchListMessagesResponse
```

Methods:

- <code title="post /v1/messages/batches">client.messages.batches.<a href="./src/letta_sdk/resources/messages/batches.py">create</a>(\*\*<a href="src/letta_sdk/types/messages/batch_create_params.py">params</a>) -> <a href="./src/letta_sdk/types/messages/batch_job.py">BatchJob</a></code>
- <code title="get /v1/messages/batches/{batch_id}">client.messages.batches.<a href="./src/letta_sdk/resources/messages/batches.py">retrieve</a>(batch_id) -> <a href="./src/letta_sdk/types/messages/batch_job.py">BatchJob</a></code>
- <code title="get /v1/messages/batches">client.messages.batches.<a href="./src/letta_sdk/resources/messages/batches.py">list</a>(\*\*<a href="src/letta_sdk/types/messages/batch_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/messages/batch_list_response.py">BatchListResponse</a></code>
- <code title="patch /v1/messages/batches/{batch_id}/cancel">client.messages.batches.<a href="./src/letta_sdk/resources/messages/batches.py">cancel</a>(batch_id) -> object</code>
- <code title="get /v1/messages/batches/{batch_id}/messages">client.messages.batches.<a href="./src/letta_sdk/resources/messages/batches.py">list_messages</a>(batch_id, \*\*<a href="src/letta_sdk/types/messages/batch_list_messages_params.py">params</a>) -> <a href="./src/letta_sdk/types/messages/batch_list_messages_response.py">BatchListMessagesResponse</a></code>

# VoiceBeta

## Chat

Methods:

- <code title="post /v1/voice-beta/{agent_id}/chat/completions">client.voice_beta.chat.<a href="./src/letta_sdk/resources/voice_beta/chat.py">create_completion</a>(agent_id, \*\*<a href="src/letta_sdk/types/voice_beta/chat_create_completion_params.py">params</a>) -> object</code>

# Embeddings

Types:

```python
from letta_sdk.types import EmbeddingGetTotalStorageSizeResponse
```

Methods:

- <code title="get /v1/embeddings/total_storage_size">client.embeddings.<a href="./src/letta_sdk/resources/embeddings.py">get_total_storage_size</a>() -> <a href="./src/letta_sdk/types/embedding_get_total_storage_size_response.py">EmbeddingGetTotalStorageSizeResponse</a></code>

# Templates

Types:

```python
from letta_sdk.types import (
    TemplateCreateResponse,
    TemplateListResponse,
    TemplateDeleteResponse,
    TemplateCreateAgentsResponse,
    TemplateForkResponse,
    TemplateGetSnapshotResponse,
    TemplateListVersionsResponse,
    TemplateRenameResponse,
    TemplateSaveVersionResponse,
    TemplateUpdateDescriptionResponse,
)
```

Methods:

- <code title="post /v1/templates/{project}">client.templates.<a href="./src/letta_sdk/resources/templates.py">create</a>(project, \*\*<a href="src/letta_sdk/types/template_create_params.py">params</a>) -> <a href="./src/letta_sdk/types/template_create_response.py">TemplateCreateResponse</a></code>
- <code title="get /v1/templates">client.templates.<a href="./src/letta_sdk/resources/templates.py">list</a>(\*\*<a href="src/letta_sdk/types/template_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/template_list_response.py">TemplateListResponse</a></code>
- <code title="delete /v1/templates/{project}/{template_name}">client.templates.<a href="./src/letta_sdk/resources/templates.py">delete</a>(template_name, \*, project) -> <a href="./src/letta_sdk/types/template_delete_response.py">TemplateDeleteResponse</a></code>
- <code title="post /v1/templates/{project}/{template_version}/agents">client.templates.<a href="./src/letta_sdk/resources/templates.py">create_agents</a>(template_version, \*, project, \*\*<a href="src/letta_sdk/types/template_create_agents_params.py">params</a>) -> <a href="./src/letta_sdk/types/template_create_agents_response.py">TemplateCreateAgentsResponse</a></code>
- <code title="post /v1/templates/{project}/{template_version}/fork">client.templates.<a href="./src/letta_sdk/resources/templates.py">fork</a>(template_version, \*, project, \*\*<a href="src/letta_sdk/types/template_fork_params.py">params</a>) -> <a href="./src/letta_sdk/types/template_fork_response.py">TemplateForkResponse</a></code>
- <code title="get /v1/templates/{project}/{template_version}/snapshot">client.templates.<a href="./src/letta_sdk/resources/templates.py">get_snapshot</a>(template_version, \*, project) -> <a href="./src/letta_sdk/types/template_get_snapshot_response.py">TemplateGetSnapshotResponse</a></code>
- <code title="get /v1/templates/{project_slug}/{name}/versions">client.templates.<a href="./src/letta_sdk/resources/templates.py">list_versions</a>(name, \*, project_slug, \*\*<a href="src/letta_sdk/types/template_list_versions_params.py">params</a>) -> <a href="./src/letta_sdk/types/template_list_versions_response.py">TemplateListVersionsResponse</a></code>
- <code title="patch /v1/templates/{project}/{template_name}/name">client.templates.<a href="./src/letta_sdk/resources/templates.py">rename</a>(template_name, \*, project, \*\*<a href="src/letta_sdk/types/template_rename_params.py">params</a>) -> <a href="./src/letta_sdk/types/template_rename_response.py">TemplateRenameResponse</a></code>
- <code title="post /v1/templates/{project}/{template_name}">client.templates.<a href="./src/letta_sdk/resources/templates.py">save_version</a>(template_name, \*, project, \*\*<a href="src/letta_sdk/types/template_save_version_params.py">params</a>) -> <a href="./src/letta_sdk/types/template_save_version_response.py">TemplateSaveVersionResponse</a></code>
- <code title="patch /v1/templates/{project}/{template_name}/description">client.templates.<a href="./src/letta_sdk/resources/templates.py">update_description</a>(template_name, \*, project, \*\*<a href="src/letta_sdk/types/template_update_description_params.py">params</a>) -> <a href="./src/letta_sdk/types/template_update_description_response.py">TemplateUpdateDescriptionResponse</a></code>

# ClientSideAccessTokens

Types:

```python
from letta_sdk.types import ClientSideAccessTokenCreateResponse, ClientSideAccessTokenListResponse
```

Methods:

- <code title="post /v1/client-side-access-tokens">client.client_side_access_tokens.<a href="./src/letta_sdk/resources/client_side_access_tokens.py">create</a>(\*\*<a href="src/letta_sdk/types/client_side_access_token_create_params.py">params</a>) -> <a href="./src/letta_sdk/types/client_side_access_token_create_response.py">ClientSideAccessTokenCreateResponse</a></code>
- <code title="get /v1/client-side-access-tokens">client.client_side_access_tokens.<a href="./src/letta_sdk/resources/client_side_access_tokens.py">list</a>(\*\*<a href="src/letta_sdk/types/client_side_access_token_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/client_side_access_token_list_response.py">ClientSideAccessTokenListResponse</a></code>
- <code title="delete /v1/client-side-access-tokens/{token}">client.client_side_access_tokens.<a href="./src/letta_sdk/resources/client_side_access_tokens.py">delete</a>(token, \*\*<a href="src/letta_sdk/types/client_side_access_token_delete_params.py">params</a>) -> object</code>

# Projects

Types:

```python
from letta_sdk.types import ProjectListResponse
```

Methods:

- <code title="get /v1/projects">client.projects.<a href="./src/letta_sdk/resources/projects.py">list</a>(\*\*<a href="src/letta_sdk/types/project_list_params.py">params</a>) -> <a href="./src/letta_sdk/types/project_list_response.py">ProjectListResponse</a></code>
