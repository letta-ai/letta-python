# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .agents.letta_user_message_content_union import LettaUserMessageContentUnion
from .agents.letta_assistant_message_content_union import LettaAssistantMessageContentUnion

__all__ = [
    "MessageSearchResponse",
    "MessageSearchResponseItem",
    "MessageSearchResponseItemSystemMessageListResult",
    "MessageSearchResponseItemUserMessageListResult",
    "MessageSearchResponseItemReasoningMessageListResult",
    "MessageSearchResponseItemAssistantMessageListResult",
]


class MessageSearchResponseItemSystemMessageListResult(BaseModel):
    """System message list result with agent context.

    Shape is identical to UpdateSystemMessage but includes the owning agent_id and message id.
    """

    content: str
    """
    The message content sent by the system (can be a string or an array of
    multi-modal content parts)
    """

    created_at: datetime
    """The time the message was created in ISO format."""

    message_id: str
    """The unique identifier of the message."""

    agent_id: Optional[str] = None
    """The unique identifier of the agent that owns the message."""

    conversation_id: Optional[str] = None
    """The unique identifier of the conversation that the message belongs to."""

    message_type: Optional[Literal["system_message"]] = None


class MessageSearchResponseItemUserMessageListResult(BaseModel):
    """User message list result with agent context.

    Shape is identical to UpdateUserMessage but includes the owning agent_id and message id.
    """

    content: Union[List[LettaUserMessageContentUnion], str]
    """
    The message content sent by the user (can be a string or an array of multi-modal
    content parts)
    """

    created_at: datetime
    """The time the message was created in ISO format."""

    message_id: str
    """The unique identifier of the message."""

    agent_id: Optional[str] = None
    """The unique identifier of the agent that owns the message."""

    conversation_id: Optional[str] = None
    """The unique identifier of the conversation that the message belongs to."""

    message_type: Optional[Literal["user_message"]] = None


class MessageSearchResponseItemReasoningMessageListResult(BaseModel):
    """Reasoning message list result with agent context.

    Shape is identical to UpdateReasoningMessage but includes the owning agent_id and message id.
    """

    created_at: datetime
    """The time the message was created in ISO format."""

    message_id: str
    """The unique identifier of the message."""

    reasoning: str

    agent_id: Optional[str] = None
    """The unique identifier of the agent that owns the message."""

    conversation_id: Optional[str] = None
    """The unique identifier of the conversation that the message belongs to."""

    message_type: Optional[Literal["reasoning_message"]] = None


class MessageSearchResponseItemAssistantMessageListResult(BaseModel):
    """Assistant message list result with agent context.

    Shape is identical to UpdateAssistantMessage but includes the owning agent_id and message id.
    """

    content: Union[List[LettaAssistantMessageContentUnion], str]
    """
    The message content sent by the assistant (can be a string or an array of
    content parts)
    """

    created_at: datetime
    """The time the message was created in ISO format."""

    message_id: str
    """The unique identifier of the message."""

    agent_id: Optional[str] = None
    """The unique identifier of the agent that owns the message."""

    conversation_id: Optional[str] = None
    """The unique identifier of the conversation that the message belongs to."""

    message_type: Optional[Literal["assistant_message"]] = None


MessageSearchResponseItem: TypeAlias = Annotated[
    Union[
        MessageSearchResponseItemSystemMessageListResult,
        MessageSearchResponseItemUserMessageListResult,
        MessageSearchResponseItemReasoningMessageListResult,
        MessageSearchResponseItemAssistantMessageListResult,
    ],
    PropertyInfo(discriminator="message_type"),
]

MessageSearchResponse: TypeAlias = List[MessageSearchResponseItem]
