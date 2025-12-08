# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["StdioMcpServer"]


class StdioMcpServer(BaseModel):
    """A Stdio MCP server"""

    args: List[str]
    """The arguments to pass to the command"""

    command: str
    """The command to run (MCP 'local' client will run this command)"""

    server_name: str
    """The name of the MCP server"""

    id: Optional[str] = None
    """The human-friendly ID of the Mcp_server"""

    env: Optional[Dict[str, str]] = None
    """Environment variables to set"""

    mcp_server_type: Optional[Literal["stdio"]] = None
