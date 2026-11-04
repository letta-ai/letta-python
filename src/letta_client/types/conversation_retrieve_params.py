# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConversationRetrieveParams"]


class ConversationRetrieveParams(TypedDict, total=False):
    include_context_message_ids: bool
    """
    Include the ordered IDs of messages still in the active context (defaults to
    true). Set false to skip loading them.
    """
