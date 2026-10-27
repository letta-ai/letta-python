# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ScheduleListParams"]


class ScheduleListParams(TypedDict, total=False):
    after: str

    conversation_id: str
    """Return only schedules bound to this exact conversation ID."""

    include_completed: Literal["true", "false"]
    """
    When 'true', include schedules that already completed (one-time schedules that
    already fired). Defaults to active and paused schedules.
    """

    limit: str

    name: str
    """Return only schedules with this exact name."""

    schedule_type: Literal["one-time", "recurring"]
    """Filter by schedule kind.

    one-time schedules have a fixed scheduled_at; recurring schedules have a
    cron_expression.
    """

    status: Literal["active", "paused", "completed"]
    """Return only schedules with this status."""
