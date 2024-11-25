# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SourceAttachParams"]


class SourceAttachParams(TypedDict, total=False):
    agent_id: Required[str]
    """The unique identifier of the agent to attach the source to."""
