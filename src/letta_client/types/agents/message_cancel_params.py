# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import Optional

from ..._types import SequenceNotStr

__all__ = ["MessageCancelParams"]

class MessageCancelParams(TypedDict, total=False):
    run_ids: Optional[SequenceNotStr[str]]
    """Optional list of run IDs to cancel"""