# This file was auto-generated by Fern from our API Definition.

from ...core.unchecked_base_model import UncheckedBaseModel
import typing
from .templates_create_agents_response_agents_item_tool_rules_item_item_max_count_limit_type import (
    TemplatesCreateAgentsResponseAgentsItemToolRulesItemItemMaxCountLimitType,
)
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class TemplatesCreateAgentsResponseAgentsItemToolRulesItemItemMaxCountLimit(UncheckedBaseModel):
    tool_name: str
    type: typing.Optional[TemplatesCreateAgentsResponseAgentsItemToolRulesItemItemMaxCountLimitType] = None
    max_count_limit: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
