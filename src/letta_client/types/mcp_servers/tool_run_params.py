# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ToolRunParams"]


class ToolRunParams(TypedDict, total=False):
    mcp_server_id: Required[str]

    args: Dict[str, object]
    """Arguments to pass to the MCP tool"""
