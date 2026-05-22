# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageStreamParams"]


class MessageStreamParams(TypedDict, total=False):
    agent_id: Optional[str]
    """Agent ID for agent-direct mode with 'default' conversation.

    Use with conversation_id='default' in the URL path.
    """

    batch_size: Optional[int]
    """Number of entries to read per batch."""

    include_pings: Optional[bool]
    """
    Whether to include periodic keepalive ping messages in the stream to prevent
    connection timeouts.
    """

    otid: Optional[str]
    """Offline threading ID to look up the run_id.

    Bypasses active run lookup if run_id not provided.
    """

    poll_interval: Optional[float]
    """Seconds to wait between polls when no new data."""

    body_run_id: Annotated[Optional[str], PropertyInfo(alias="run_id")]
    """Run ID to stream directly, bypassing run lookup.

    Use for recovery from duplicate requests.
    """

    starting_after: int
    """Sequence id to use as a cursor for pagination.

    Response will start streaming after this chunk sequence id
    """
