# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["UpdateStdioMcpServerParam"]


class UpdateStdioMcpServerParam(TypedDict, total=False):
    args: Optional[SequenceNotStr[str]]
    """The arguments to pass to the command"""

    command: Optional[str]
    """The command to run the MCP server"""

    env: Optional[Dict[str, str]]
    """Environment variables to set"""

    server_name: Optional[str]
    """The name of the MCP server"""
