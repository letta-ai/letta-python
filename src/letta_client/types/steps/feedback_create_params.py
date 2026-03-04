# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["FeedbackCreateParams"]


class FeedbackCreateParams(TypedDict, total=False):
    feedback: Optional[Literal["positive", "negative"]]
    """Whether this feedback is positive or negative"""

    tags: Optional[SequenceNotStr[str]]
    """Feedback tags to add to the step"""
