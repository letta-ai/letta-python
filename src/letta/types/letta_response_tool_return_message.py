# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import datetime as dt
import typing
from .letta_response_tool_return_message_status import LettaResponseToolReturnMessageStatus
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class LettaResponseToolReturnMessage(UniversalBaseModel):
    """
    A message representing the return value of a tool call (generated by Letta executing the requested tool).

    Attributes:
    tool_return (str): The return value of the tool
    status (Literal["success", "error"]): The status of the tool call
    id (str): The ID of the message
    date (datetime): The date the message was created in ISO format
    tool_call_id (str): A unique identifier for the tool call that generated this message
    stdout (Optional[List(str)]): Captured stdout (e.g. prints, logs) from the tool invocation
    stderr (Optional[List(str)]): Captured stderr from the tool invocation
    """

    id: str
    date: dt.datetime
    message_type: typing.Optional[typing.Literal["tool_return_message"]] = None
    tool_return: str
    status: LettaResponseToolReturnMessageStatus
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