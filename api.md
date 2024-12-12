# Agents

Types:

```python
from letta.types import AgentState, AgentListResponse, AgentMigrateResponse
```

Methods:

- <code title="post /v1/agents/">client.agents.<a href="./src/letta/resources/agents/agents.py">create</a>(\*\*<a href="src/letta/types/agent_create_params.py">params</a>) -> <a href="./src/letta/types/agent_state.py">AgentState</a></code>
- <code title="get /v1/agents/{agent_id}">client.agents.<a href="./src/letta/resources/agents/agents.py">retrieve</a>(agent_id) -> <a href="./src/letta/types/agent_state.py">AgentState</a></code>
- <code title="patch /v1/agents/{agent_id}">client.agents.<a href="./src/letta/resources/agents/agents.py">update</a>(agent_id, \*\*<a href="src/letta/types/agent_update_params.py">params</a>) -> <a href="./src/letta/types/agent_state.py">AgentState</a></code>
- <code title="get /v1/agents/">client.agents.<a href="./src/letta/resources/agents/agents.py">list</a>(\*\*<a href="src/letta/types/agent_list_params.py">params</a>) -> <a href="./src/letta/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /v1/agents/{agent_id}">client.agents.<a href="./src/letta/resources/agents/agents.py">delete</a>(agent_id) -> <a href="./src/letta/types/agent_state.py">AgentState</a></code>
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
