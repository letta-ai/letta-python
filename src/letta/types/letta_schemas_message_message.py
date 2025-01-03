# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from .message_role import MessageRole
from .letta_schemas_openai_chat_completions_tool_call_output import LettaSchemasOpenaiChatCompletionsToolCallOutput
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class LettaSchemasMessageMessage(UniversalBaseModel):
    """
    Letta's internal representation of a message. Includes methods to convert to/from LLM provider formats.

    Attributes:
    id (str): The unique identifier of the message.
    role (MessageRole): The role of the participant.
    text (str): The text of the message.
    user_id (str): The unique identifier of the user.
    agent_id (str): The unique identifier of the agent.
    model (str): The model used to make the function call.
    name (str): The name of the participant.
    created_at (datetime): The time the message was created.
    tool_calls (List[ToolCall]): The list of tool calls requested.
    tool_call_id (str): The id of the tool call.
    """

    created_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this object.
    """

    last_updated_by_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the user that made this object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the object was created.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp when the object was last updated.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-friendly ID of the Message
    """

    role: MessageRole = pydantic.Field()
    """
    The role of the participant.
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text of the message.
    """

    organization_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the organization.
    """

    agent_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the agent.
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    The model used to make the function call.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the participant.
    """

    tool_calls: typing.Optional[typing.List[LettaSchemasOpenaiChatCompletionsToolCallOutput]] = pydantic.Field(
        default=None
    )
    """
    The list of tool calls requested.
    """

    tool_call_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the tool call.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
