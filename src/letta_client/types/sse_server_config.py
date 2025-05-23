# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
import typing
from .mcp_server_type import McpServerType
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SseServerConfig(UncheckedBaseModel):
    server_name: str = pydantic.Field()
    """
    The name of the server
    """

    type: typing.Optional[McpServerType] = None
    server_url: str = pydantic.Field()
    """
    The URL of the server (MCP SSE client will connect to this URL)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
