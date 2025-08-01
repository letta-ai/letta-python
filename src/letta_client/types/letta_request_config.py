# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .message_type import MessageType


class LettaRequestConfig(UncheckedBaseModel):
    use_assistant_message: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the server should parse specific tool call arguments (default `send_message`) as `AssistantMessage` objects.
    """

    assistant_message_tool_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the designated message tool.
    """

    assistant_message_tool_kwarg: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the message argument in the designated message tool.
    """

    include_return_message_types: typing.Optional[typing.List[MessageType]] = pydantic.Field(default=None)
    """
    Only return specified message types in the response. If `None` (default) returns all messages.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
