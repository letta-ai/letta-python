# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentRecompileParams"]


class AgentRecompileParams(TypedDict, total=False):
    dry_run: bool
    """If True, do not persist changes; still returns the compiled system prompt."""

    update_timestamp: bool
    """
    If True, update the in-context memory last edit timestamp embedded in the system
    prompt.
    """
