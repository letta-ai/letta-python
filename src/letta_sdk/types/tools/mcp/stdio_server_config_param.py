# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr
from .mcp_server_type import McpServerType

__all__ = ["StdioServerConfigParam"]


class StdioServerConfigParam(TypedDict, total=False):
    args: Required[SequenceNotStr[str]]
    """The arguments to pass to the command"""

    command: Required[str]
    """The command to run (MCP 'local' client will run this command)"""

    server_name: Required[str]
    """The name of the server"""

    env: Optional[Dict[str, str]]
    """Environment variables to set"""

    type: McpServerType
