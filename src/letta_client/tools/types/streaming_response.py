# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.unchecked_base_model import UncheckedBaseModel
from ...types.mcp_tool import McpTool
from .connect_mcp_server_response_event import ConnectMcpServerResponseEvent


class StreamingResponse(UncheckedBaseModel):
    event: ConnectMcpServerResponseEvent
    message: typing.Optional[str] = None
    tools: typing.Optional[McpTool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
