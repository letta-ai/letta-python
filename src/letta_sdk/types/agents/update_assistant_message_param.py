# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .letta_assistant_message_content_union_param import LettaAssistantMessageContentUnionParam

__all__ = ["UpdateAssistantMessageParam"]


class UpdateAssistantMessageParam(TypedDict, total=False):
    content: Required[Union[Iterable[LettaAssistantMessageContentUnionParam], str]]
    """
    The message content sent by the assistant (can be a string or an array of
    content parts)
    """

    message_type: Literal["assistant_message"]
