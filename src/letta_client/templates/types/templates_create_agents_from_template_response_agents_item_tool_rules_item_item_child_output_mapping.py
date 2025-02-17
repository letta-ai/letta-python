# This file was auto-generated by Fern from our API Definition.

from ...core.unchecked_base_model import UncheckedBaseModel
import typing
from .templates_create_agents_from_template_response_agents_item_tool_rules_item_item_child_output_mapping_type import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemToolRulesItemItemChildOutputMappingType,
)
from .templates_create_agents_from_template_response_agents_item_tool_rules_item_item_child_output_mapping_default_child import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemToolRulesItemItemChildOutputMappingDefaultChild,
)
from .templates_create_agents_from_template_response_agents_item_tool_rules_item_item_child_output_mapping_require_output_mapping import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemToolRulesItemItemChildOutputMappingRequireOutputMapping,
)
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class TemplatesCreateAgentsFromTemplateResponseAgentsItemToolRulesItemItemChildOutputMapping(UncheckedBaseModel):
    tool_name: str
    type: typing.Optional[
        TemplatesCreateAgentsFromTemplateResponseAgentsItemToolRulesItemItemChildOutputMappingType
    ] = None
    default_child: typing.Optional[
        TemplatesCreateAgentsFromTemplateResponseAgentsItemToolRulesItemItemChildOutputMappingDefaultChild
    ] = None
    child_output_mapping: typing.Optional[typing.Optional[typing.Any]] = None
    require_output_mapping: typing.Optional[
        TemplatesCreateAgentsFromTemplateResponseAgentsItemToolRulesItemItemChildOutputMappingRequireOutputMapping
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
