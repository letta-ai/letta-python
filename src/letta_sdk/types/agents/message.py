# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .tool_return import ToolReturn
from .message_role import MessageRole
from .text_content import TextContent
from .image_content import ImageContent
from .reasoning_content import ReasoningContent
from .tool_call_content import ToolCallContent
from .tool_return_content import ToolReturnContent
from .omitted_reasoning_content import OmittedReasoningContent
from .redacted_reasoning_content import RedactedReasoningContent

__all__ = ["Message", "Content", "ToolCall", "ToolCallFunction"]

Content: TypeAlias = Annotated[
    Union[
        TextContent,
        ImageContent,
        ToolCallContent,
        ToolReturnContent,
        ReasoningContent,
        RedactedReasoningContent,
        OmittedReasoningContent,
    ],
    PropertyInfo(discriminator="type"),
]


class ToolCallFunction(BaseModel):
    arguments: str

    name: str

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ToolCall(BaseModel):
    id: str

    function: ToolCallFunction

    type: Literal["function"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Message(BaseModel):
    role: MessageRole
    """The role of the participant."""

    id: Optional[str] = None
    """The human-friendly ID of the Message"""

    agent_id: Optional[str] = None
    """The unique identifier of the agent."""

    approval_request_id: Optional[str] = None
    """
    The id of the approval request if this message is associated with a tool call
    request.
    """

    approve: Optional[bool] = None
    """Whether tool call is approved."""

    batch_item_id: Optional[str] = None
    """The id of the LLMBatchItem that this message is associated with"""

    content: Optional[List[Content]] = None
    """The content of the message."""

    created_at: Optional[datetime] = None
    """The timestamp when the object was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this object."""

    denial_reason: Optional[str] = None
    """The reason the tool call request was denied."""

    group_id: Optional[str] = None
    """The multi-agent group that the message was sent in"""

    is_err: Optional[bool] = None
    """Whether this message is part of an error step.

    Used only for debugging purposes.
    """

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this object."""

    model: Optional[str] = None
    """The model used to make the function call."""

    name: Optional[str] = None
    """For role user/assistant: the (optional) name of the participant.

    For role tool/function: the name of the function called.
    """

    otid: Optional[str] = None
    """The offline threading id associated with this message"""

    sender_id: Optional[str] = None
    """The id of the sender of the message, can be an identity id or agent id"""

    step_id: Optional[str] = None
    """The id of the step that this message was created in."""

    tool_call_id: Optional[str] = None
    """The ID of the tool call. Only applicable for role tool."""

    tool_calls: Optional[List[ToolCall]] = None
    """The list of tool calls requested. Only applicable for role assistant."""

    tool_returns: Optional[List[ToolReturn]] = None
    """Tool execution return information for prior tool calls"""

    updated_at: Optional[datetime] = None
    """The timestamp when the object was last updated."""
