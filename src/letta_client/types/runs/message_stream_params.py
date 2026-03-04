# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MessageStreamParams"]


class MessageStreamParams(TypedDict, total=False):
    batch_size: Optional[int]
    """Number of entries to read per batch."""

    include_pings: Optional[bool]
    """
    Whether to include periodic keepalive ping messages in the stream to prevent
    connection timeouts.
    """

    poll_interval: Optional[float]
    """Seconds to wait between polls when no new data."""

    starting_after: int
    """Sequence id to use as a cursor for pagination.

    Response will start streaming after this chunk sequence id
    """
