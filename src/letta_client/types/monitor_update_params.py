# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MonitorUpdateParams"]


class MonitorUpdateParams(TypedDict, total=False):
    command: str

    description: str

    device_id: Optional[str]

    exit_code: Optional[int]

    kind: Literal["command", "websocket", "script", "github_pull_request"]

    output_file: Optional[str]

    persistent: bool

    started_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    status: Literal["running", "completed", "failed"]
