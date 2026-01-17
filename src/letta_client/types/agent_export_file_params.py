# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AgentExportFileParams"]


class AgentExportFileParams(TypedDict, total=False):
    conversation_id: Optional[str]
    """Conversation ID to export.

    If provided, uses messages from this conversation instead of the agent's global
    message history.
    """

    max_steps: int

    use_legacy_format: bool
    """
    If True, exports using the legacy single-agent 'v1' format with inline
    tools/blocks. If False, exports using the new multi-entity 'v2' format, with
    separate agents, tools, blocks, files, etc.
    """
