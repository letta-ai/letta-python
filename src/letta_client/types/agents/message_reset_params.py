# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MessageResetParams"]


class MessageResetParams(TypedDict, total=False):
    add_default_initial_messages: bool
    """If true, adds the default initial messages after resetting."""
