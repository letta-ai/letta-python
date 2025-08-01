# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel


class ToolReturnContent(UncheckedBaseModel):
    type: typing.Literal["tool_return"] = "tool_return"
    tool_call_id: str = pydantic.Field()
    """
    References the ID of the ToolCallContent that initiated this tool call.
    """

    content: str = pydantic.Field()
    """
    The content returned by the tool execution.
    """

    is_error: bool = pydantic.Field()
    """
    Indicates whether the tool execution resulted in an error.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
