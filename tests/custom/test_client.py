from pydantic import BaseModel
from typing import List, Type

from letta_client import CreateBlock, MessageCreate
from letta_client.client import BaseTool

class InventoryItem(BaseModel):
    sku: str  # Unique product identifier
    name: str  # Product name
    price: float  # Current price
    category: str  # Product category (e.g., "Electronics", "Clothing")

class InventoryEntry(BaseModel):
    timestamp: int  # Unix timestamp of the transaction
    item: InventoryItem  # The product being updated
    transaction_id: str  # Unique identifier for this inventory update

class InventoryEntryData(BaseModel):
    data: InventoryEntry
    quantity_change: int  # Change in quantity (positive for additions, negative for removals)

class ManageInventoryTool(BaseTool):
    name: str = "manage_inventory"
    args_schema: Type[BaseModel] = InventoryEntryData
    description: str = "Update inventory catalogue with a new data entry"
    tags: List[str] = ["inventory", "shop"]

    def run(self, data: InventoryEntry, quantity_change: int) -> bool:
        """
        Implementation of the manage_inventory tool
        """
        print(f"Updated inventory for {data.item.name} with a quantity change of {quantity_change}")
        return True


def test_create_agent(client) -> None:
    agent = client.agents.create(
        memory_blocks=[
            CreateBlock(
                value="username: caren",
                label="human",
            )
        ],
        model="anthropic/claude-3-5-sonnet-20241022",
        embedding="openai/text-embedding-ada-002",
    )
    assert agent is not None
    agents = client.agents.list()
    assert len([a for a in agents if a.id == agent.id]) == 1

    response = client.agents.messages.create_stream(
        agent_id=agent.id,
        messages=[
            MessageCreate(
                role="user",
                content="Please answer this question in just one word: what is my name?",
            )
        ],
        stream_tokens=True,
    )
    counter = 0
    messages = {}
    for chunk in response:
        print(chunk.model_dump_json(indent=2, exclude={"id", "date", "otid", "sender_id", "completion_tokens", "prompt_tokens", "total_tokens", "step_count", "steps_messages", "run_ids"}))
        counter += 1
        if chunk.message_type not in messages:
            messages[chunk.message_type] = 0
        messages[chunk.message_type] += 1
    print(f"Total messages: {counter}")
    print(messages)
    client.agents.delete(agent_id=agent.id)


def test_create_agent_with_tools(client) -> None:
    def manage_inventory_mock(data: InventoryEntry, quantity_change: int) -> bool:
        """
        Implementation of the manage_inventory tool
        """
        print(f"Updated inventory for {data.item.name} with a quantity change of {quantity_change}")
        return True
    
    tool_from_func = client.tools.upsert_from_function(
        func=manage_inventory_mock,
        args_schema=InventoryEntryData,
    )
    assert tool_from_func is not None

    tool_from_class = client.tools.add(
        tool=ManageInventoryTool(),
    )
    assert tool_from_class is not None
    
    for tool in [tool_from_func, tool_from_class]:
        tool_return = client.tools.run_tool_from_source(
            source_code=tool.source_code,
            args={
                "data": InventoryEntry(
                    timestamp=0,
                    item=InventoryItem(
                        name="Item 1",
                        sku="328jf84htgwoeidfnw4",
                        price=9.99,
                        category="Grocery",
                    ),
                    transaction_id="1234",
                ),
                "quantity_change": 10,
            },
            args_json_schema=InventoryEntryData.model_json_schema(),
        )
        assert tool_return is not None
        assert tool_return.tool_return == 'True'
