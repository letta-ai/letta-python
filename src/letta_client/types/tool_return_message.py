# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .tool_return_message_status import ToolReturnMessageStatus


class ToolReturnMessage(UncheckedBaseModel):
    """
    A message representing the return value of a tool call (generated by Letta executing the requested tool).

    Args:
        id (str): The ID of the message
        date (datetime): The date the message was created in ISO format
        name (Optional[str]): The name of the sender of the message
        tool_return (str): The return value of the tool
        status (Literal["success", "error"]): The status of the tool call
        tool_call_id (str): A unique identifier for the tool call that generated this message
        stdout (Optional[List(str)]): Captured stdout (e.g. prints, logs) from the tool invocation
        stderr (Optional[List(str)]): Captured stderr from the tool invocation
    """

    id: str
    date: dt.datetime
    name: typing.Optional[str] = None
    message_type: typing.Literal["tool_return_message"] = "tool_return_message"
    otid: typing.Optional[str] = None
    sender_id: typing.Optional[str] = None
    step_id: typing.Optional[str] = None
    is_err: typing.Optional[bool] = None
    tool_return: str
    status: ToolReturnMessageStatus
    tool_call_id: str
    stdout: typing.Optional[typing.List[str]] = None
    stderr: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
