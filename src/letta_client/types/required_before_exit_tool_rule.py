# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel


class RequiredBeforeExitToolRule(UncheckedBaseModel):
    """
    Represents a tool rule configuration where this tool must be called before the agent loop can exit.
    """

    tool_name: str = pydantic.Field()
    """
    The name of the tool. Must exist in the database for the user's organization.
    """

    type: typing.Literal["required_before_exit"] = "required_before_exit"
    prompt_template: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional Jinja2 template for generating agent prompt about this tool rule.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
