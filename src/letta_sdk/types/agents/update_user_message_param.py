# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .letta_user_message_content_union_param import LettaUserMessageContentUnionParam

__all__ = ["UpdateUserMessageParam"]


class UpdateUserMessageParam(TypedDict, total=False):
    content: Required[Union[Iterable[LettaUserMessageContentUnionParam], str]]
    """
    The message content sent by the user (can be a string or an array of multi-modal
    content parts)
    """

    message_type: Literal["user_message"]
