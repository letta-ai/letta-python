# This file was auto-generated by Fern from our API Definition.

from ...core.unchecked_base_model import UncheckedBaseModel
import typing
from .agents_search_response_agents_item_tool_rules_item_four_type import (
    AgentsSearchResponseAgentsItemToolRulesItemFourType,
)
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class AgentsSearchResponseAgentsItemToolRulesItemFour(UncheckedBaseModel):
    tool_name: str
    type: typing.Optional[AgentsSearchResponseAgentsItemToolRulesItemFourType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
