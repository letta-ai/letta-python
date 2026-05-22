# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from typing import Union, Optional

from datetime import datetime

from ..._utils import PropertyInfo

from ..._types import SequenceNotStr

__all__ = ["PassageCreateParams"]

class PassageCreateParams(TypedDict, total=False):
    text: Required[str]
    """Text to write to archival memory."""

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format = "iso8601")]
    """Optional timestamp for the memory (defaults to current UTC time)."""

    tags: Optional[SequenceNotStr[str]]
    """Optional list of tags to attach to the memory."""