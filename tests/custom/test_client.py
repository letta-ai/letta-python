import os
import pytest
from typing import Generator
from letta import (
    AgentState,
    CreateBlock,
    EmbeddingConfig,
    Letta,
    LettaEnvironment,
    LlmConfig,
    MessageCreate,
)
from letta.core.request_options import RequestOptions


@pytest.fixture(scope="session")
def client() -> Generator[Letta, None, None]:
    api_key = os.getenv('LETTA_API_KEY')
    if not api_key:
        raise ValueError("LETTA_API_KEY environment variable must be set")
    
    client = Letta(
        environment=LettaEnvironment.LETTA_CLOUD,
        token=api_key,
    )
    yield client


@pytest.mark.skip(reason="Temporarily skipping this test")
def test_create_agent_default(client) -> None:
    agent = client.agents.create(
        memory_blocks=[
            CreateBlock(
                value="username: caren",
                label="human",
            )
        ],
        llm_config=LlmConfig(
            model="gpt-4",
            model_endpoint_type="openai",
            model_endpoint="https://api.openai.com/v1",
            model_wrapper=None,
            context_window=8192,
        ),
        embedding_config=EmbeddingConfig(
            embedding_model="text-embedding-ada-002",
            embedding_endpoint_type="openai",
            embedding_endpoint="https://api.openai.com/v1",
            embedding_dim=1536,
            embedding_chunk_size=300,
        ),
    )
    assert agent is not None
    agents = client.agents.list()
    assert len([a for a in agents if a.id == agent.id]) == 1

    client.agents.delete(agent_id=agent.id)


@pytest.mark.skip(reason="Temporarily skipping this test")
def test_create_agent_with_handle(client) -> None:
    agent = client.agents.create(
        memory_blocks=[
            CreateBlock(
                value="username: caren",
                label="human",
            )
        ],
        llm="openai/gpt-4",
        embedding="openai/text-embedding-ada-002",
    )
    assert agent is not None
    agents = client.agents.list()
    assert len([a for a in agents if a.id == agent.id]) == 1

    client.agents.delete(agent_id=agent.id)


@pytest.mark.skip(reason="Temporarily skipping this test")
def test_create_agent_with_template(client) -> None:
    agent = client.agents.create(
        memory_blocks=[
            CreateBlock(
                value="username: caren",
                label="human",
            )
        ],
        from_template="fern-testing:latest",
    )
    assert agent is not None
    agents = client.agents.list()
    assert len([a for a in agents if a.id == agent.id]) == 1

    client.agents.delete(agent_id=agent.id)


@pytest.mark.skip(reason="Temporarily skipping this test")
def test_delete_agent(client) -> None:
    agent = client.agents.create(
        memory_blocks=[
            CreateBlock(
                value="username: caren",
                label="human",
            )
        ],
        llm="openai/gpt-4",
        embedding="openai/text-embedding-ada-002",
    )
    assert agent is not None
    agents = client.agents.list()
    assert len([a for a in agents if a.id == agent.id]) == 1

    client.agents.delete(agent_id=agent.id)

    agents = client.agents.list()
    assert len([a for a in agents if a.id == agent.id]) == 0


@pytest.fixture(scope="module")
def agent(client) -> Generator[AgentState, None, None]:
    agent = client.agents.create(
        memory_blocks=[
            CreateBlock(
                value="username: caren",
                label="human",
            )
        ],
        llm="openai/gpt-4",
        embedding="openai/text-embedding-ada-002",
    )

    yield agent

    client.agents.delete(agent_id=agent.id)


@pytest.mark.skip(reason="Temporarily skipping this test")
def test_send_message(client, agent) -> None:
    message_text = "Hello, how are you today?"
    response = client.agents.messages.create(
        agent_id=agent.id,
        messages=[
            MessageCreate(
                role="user",
                text=message_text,
            ),
        ],
    )
    assert len(response.messages) == 3
    assert response.usage.step_count == 1
    assert [message.message_type for message in response.messages] == [
        "reasoning_message",
        "tool_call_message",
        "tool_return_message",
    ]

    messages = client.agents.messages.list(agent_id=agent.id)
    assert len(messages) > 0
    user_message = [msg for msg in messages if msg.message_type == "user_message"][-1]
    assert message_text in user_message.message


@pytest.mark.skip(reason="Temporarily skipping this test")
def test_send_message_with_streaming(client, agent) -> None:
    message_text = "Hello, how are you today?"
    response = client.agents.messages.stream(
        agent_id=agent.id,
        messages=[
            MessageCreate(
                role="user",
                text=message_text,
            ),
        ],
        request_options=RequestOptions(additional_headers={"Accept": "text/event-stream"}),
    )
    messages = []
    for chunk in response:
        messages.append(chunk)

    assert len(messages) == 4
    assert messages.pop().step_count == 1
    assert [message.message_type for message in messages] == [
        "reasoning_message",
        "tool_call_message",
        "tool_return_message",
    ]

    messages = client.agents.messages.list(agent_id=agent.id)
    assert len(messages) > 0
    user_message = [msg for msg in messages if msg.message_type == "user_message"][-1]
    assert message_text in user_message.message
