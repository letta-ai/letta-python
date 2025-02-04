from letta_client import (
    CreateBlock,
)


def test_create_agent(client) -> None:
    agent = client.agents.create(
        memory_blocks=[
            CreateBlock(
                value="username: caren",
                label="human",
            )
        ],
        model="openai/gpt-4",
        embedding="openai/text-embedding-ada-002",
    )
    assert agent is not None
    agents = client.agents.list()
    assert len([a for a in agents if a.id == agent.id]) == 1

    client.agents.delete(agent_id=agent.id)