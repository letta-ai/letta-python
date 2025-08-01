# This file was auto-generated by Fern from our API Definition.

import typing

from ...types.update_ssemcp_server import UpdateSsemcpServer
from ...types.update_stdio_mcp_server import UpdateStdioMcpServer
from ...types.update_streamable_httpmcp_server import UpdateStreamableHttpmcpServer

UpdateMcpServerRequest = typing.Union[UpdateStdioMcpServer, UpdateSsemcpServer, UpdateStreamableHttpmcpServer]
