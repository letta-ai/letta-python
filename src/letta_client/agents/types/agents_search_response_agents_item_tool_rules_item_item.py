# This file was auto-generated by Fern from our API Definition.

import typing
from .agents_search_response_agents_item_tool_rules_item_item_children import (
    AgentsSearchResponseAgentsItemToolRulesItemItemChildren,
)
from .agents_search_response_agents_item_tool_rules_item_item_one import (
    AgentsSearchResponseAgentsItemToolRulesItemItemOne,
)
from .agents_search_response_agents_item_tool_rules_item_item_two import (
    AgentsSearchResponseAgentsItemToolRulesItemItemTwo,
)
from .agents_search_response_agents_item_tool_rules_item_item_child_output_mapping import (
    AgentsSearchResponseAgentsItemToolRulesItemItemChildOutputMapping,
)
from .agents_search_response_agents_item_tool_rules_item_item_tool_name import (
    AgentsSearchResponseAgentsItemToolRulesItemItemToolName,
)

AgentsSearchResponseAgentsItemToolRulesItemItem = typing.Union[
    AgentsSearchResponseAgentsItemToolRulesItemItemChildren,
    AgentsSearchResponseAgentsItemToolRulesItemItemOne,
    AgentsSearchResponseAgentsItemToolRulesItemItemTwo,
    AgentsSearchResponseAgentsItemToolRulesItemItemChildOutputMapping,
    AgentsSearchResponseAgentsItemToolRulesItemItemToolName,
]
