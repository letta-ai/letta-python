# This file was auto-generated by Fern from our API Definition.

import typing
from .templates_create_agents_response_agents_item_tool_rules_item_item_children import (
    TemplatesCreateAgentsResponseAgentsItemToolRulesItemItemChildren,
)
from .templates_create_agents_response_agents_item_tool_rules_item_item_one import (
    TemplatesCreateAgentsResponseAgentsItemToolRulesItemItemOne,
)
from .templates_create_agents_response_agents_item_tool_rules_item_item_two import (
    TemplatesCreateAgentsResponseAgentsItemToolRulesItemItemTwo,
)
from .templates_create_agents_response_agents_item_tool_rules_item_item_child_output_mapping import (
    TemplatesCreateAgentsResponseAgentsItemToolRulesItemItemChildOutputMapping,
)
from .templates_create_agents_response_agents_item_tool_rules_item_item_tool_name import (
    TemplatesCreateAgentsResponseAgentsItemToolRulesItemItemToolName,
)

TemplatesCreateAgentsResponseAgentsItemToolRulesItemItem = typing.Union[
    TemplatesCreateAgentsResponseAgentsItemToolRulesItemItemChildren,
    TemplatesCreateAgentsResponseAgentsItemToolRulesItemItemOne,
    TemplatesCreateAgentsResponseAgentsItemToolRulesItemItemTwo,
    TemplatesCreateAgentsResponseAgentsItemToolRulesItemItemChildOutputMapping,
    TemplatesCreateAgentsResponseAgentsItemToolRulesItemItemToolName,
]
