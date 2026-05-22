# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._types import SequenceNotStr

from typing import Optional, Dict

from typing_extensions import Literal, TypedDict, Required

__all__ = ["CreateStdioMcpServerParam"]

class CreateStdioMcpServerParam(TypedDict, total=False):
    """Create a new Stdio MCP server"""
    args: Required[SequenceNotStr[str]]
    """The arguments to pass to the command"""

    command: Required[str]
    """The command to run (MCP 'local' client will run this command)"""

    env: Optional[Dict[str, str]]
    """Environment variables to set"""

    mcp_server_type: Literal["stdio"]