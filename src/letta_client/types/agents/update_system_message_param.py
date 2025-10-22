# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["UpdateSystemMessageParam"]


class UpdateSystemMessageParam(TypedDict, total=False):
    content: Required[str]
    """
    The message content sent by the system (can be a string or an array of
    multi-modal content parts)
    """

    message_type: Literal["system_message"]
