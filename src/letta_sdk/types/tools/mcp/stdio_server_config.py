# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel
from .mcp_server_type import McpServerType

__all__ = ["StdioServerConfig"]


class StdioServerConfig(BaseModel):
    args: List[str]
    """The arguments to pass to the command"""

    command: str
    """The command to run (MCP 'local' client will run this command)"""

    server_name: str
    """The name of the server"""

    env: Optional[Dict[str, str]] = None
    """Environment variables to set"""

    type: Optional[McpServerType] = None
