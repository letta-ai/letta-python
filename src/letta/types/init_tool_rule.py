# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .tool_rule_type import ToolRuleType
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class InitToolRule(UniversalBaseModel):
    """
    Represents the initial tool rule configuration.
    """

    tool_name: str = pydantic.Field()
    """
    The name of the tool. Must exist in the database for the user's organization.
    """

    type: typing.Optional[ToolRuleType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow