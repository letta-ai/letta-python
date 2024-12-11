# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageUpdateParams", "ToolCall", "ToolCallFunction"]


class MessageUpdateParams(TypedDict, total=False):
    agent_id: Required[str]

    created_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp when the object was created."""

    created_by_id: Optional[str]
    """The id of the user that made this object."""

    last_updated_by_id: Optional[str]
    """The id of the user that made this object."""

    name: Optional[str]
    """The name of the participant."""

    role: Optional[Literal["assistant", "user", "tool", "function", "system"]]
    """The role of the participant."""

    text: Optional[str]
    """The text of the message."""

    tool_call_id: Optional[str]
    """The id of the tool call."""

    tool_calls: Optional[Iterable[ToolCall]]
    """The list of tool calls requested."""

    updated_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp when the object was last updated."""


class ToolCallFunction(TypedDict, total=False):
    arguments: Required[str]
    """The arguments to pass to the function (JSON dump)"""

    name: Required[str]
    """The name of the function to call"""


class ToolCall(TypedDict, total=False):
    id: Required[str]
    """The ID of the tool call"""

    function: Required[ToolCallFunction]
    """The arguments and name for the function"""

    type: str
