# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SummaryMessage", "CompactionStats"]


class CompactionStats(BaseModel):
    """Statistics about a memory compaction operation."""

    context_window: int
    """The model's context window size"""

    messages_count_after: int
    """Number of messages after compaction"""

    messages_count_before: int
    """Number of messages before compaction"""

    trigger: str
    """
    What triggered the compaction (e.g., 'context_window_exceeded',
    'post_step_context_check')
    """

    context_tokens_after: Optional[int] = None
    """
    Token count after compaction (message tokens only, does not include tool
    definitions)
    """

    context_tokens_before: Optional[int] = None
    """
    Token count before compaction (from LLM usage stats, includes full context sent
    to LLM)
    """


class SummaryMessage(BaseModel):
    """A message representing a summary of the conversation.

    Sent to the LLM as a user or system message depending on the provider.
    """

    id: str

    date: datetime

    summary: str

    compaction_stats: Optional[CompactionStats] = None
    """Statistics about a memory compaction operation."""

    is_err: Optional[bool] = None

    message_type: Optional[Literal["summary_message"]] = None

    name: Optional[str] = None

    otid: Optional[str] = None

    run_id: Optional[str] = None

    sender_id: Optional[str] = None

    seq_id: Optional[int] = None

    step_id: Optional[str] = None
