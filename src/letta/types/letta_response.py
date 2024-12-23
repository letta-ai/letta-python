# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .letta_response_assistant_message import LettaResponseAssistantMessage
from ..core.serialization import FieldMetadata
from .letta_response_letta_usage_statistics import LettaResponseLettaUsageStatistics
import pydantic
from .letta_response_reasoning_message import LettaResponseReasoningMessage
from .letta_response_system_message import LettaResponseSystemMessage
from .letta_response_tool_call import LettaResponseToolCall
from .letta_response_tool_call_delta import LettaResponseToolCallDelta
from .letta_response_tool_call_message import LettaResponseToolCallMessage
from .letta_response_tool_return_message import LettaResponseToolReturnMessage
from .letta_response_user_message import LettaResponseUserMessage
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class LettaResponse(UniversalBaseModel):
    assistant_message: typing_extensions.Annotated[
        typing.Optional[LettaResponseAssistantMessage], FieldMetadata(alias="AssistantMessage")
    ] = None
    letta_usage_statistics: typing_extensions.Annotated[
        typing.Optional[LettaResponseLettaUsageStatistics], FieldMetadata(alias="LettaUsageStatistics")
    ] = pydantic.Field(default=None)
    """
    Usage statistics for the agent interaction.
    
    Attributes:
    completion_tokens (int): The number of tokens generated by the agent.
    prompt_tokens (int): The number of tokens in the prompt.
    total_tokens (int): The total number of tokens processed by the agent.
    step_count (int): The number of steps taken by the agent.
    """

    reasoning_message: typing_extensions.Annotated[
        typing.Optional[LettaResponseReasoningMessage], FieldMetadata(alias="ReasoningMessage")
    ] = pydantic.Field(default=None)
    """
    Representation of an agent's internal reasoning.
    
    Attributes:
    reasoning (str): The internal reasoning of the agent
    id (str): The ID of the message
    date (datetime): The date the message was created in ISO format
    """

    system_message: typing_extensions.Annotated[
        typing.Optional[LettaResponseSystemMessage], FieldMetadata(alias="SystemMessage")
    ] = pydantic.Field(default=None)
    """
    A message generated by the system. Never streamed back on a response, only used for cursor pagination.
    
    Attributes:
    message (str): The message sent by the system
    id (str): The ID of the message
    date (datetime): The date the message was created in ISO format
    """

    tool_call: typing_extensions.Annotated[typing.Optional[LettaResponseToolCall], FieldMetadata(alias="ToolCall")] = (
        None
    )
    tool_call_delta: typing_extensions.Annotated[
        typing.Optional[LettaResponseToolCallDelta], FieldMetadata(alias="ToolCallDelta")
    ] = None
    tool_call_message: typing_extensions.Annotated[
        typing.Optional[LettaResponseToolCallMessage], FieldMetadata(alias="ToolCallMessage")
    ] = pydantic.Field(default=None)
    """
    A message representing a request to call a tool (generated by the LLM to trigger tool execution).
    
    Attributes:
    tool_call (Union[ToolCall, ToolCallDelta]): The tool call
    id (str): The ID of the message
    date (datetime): The date the message was created in ISO format
    """

    tool_return_message: typing_extensions.Annotated[
        typing.Optional[LettaResponseToolReturnMessage], FieldMetadata(alias="ToolReturnMessage")
    ] = pydantic.Field(default=None)
    """
    A message representing the return value of a tool call (generated by Letta executing the requested tool).
    
    Attributes:
    tool_return (str): The return value of the tool
    status (Literal["success", "error"]): The status of the tool call
    id (str): The ID of the message
    date (datetime): The date the message was created in ISO format
    tool_call_id (str): A unique identifier for the tool call that generated this message
    stdout (Optional[List(str)]): Captured stdout (e.g. prints, logs) from the tool invocation
    stderr (Optional[List(str)]): Captured stderr from the tool invocation
    """

    user_message: typing_extensions.Annotated[
        typing.Optional[LettaResponseUserMessage], FieldMetadata(alias="UserMessage")
    ] = pydantic.Field(default=None)
    """
    A message sent by the user. Never streamed back on a response, only used for cursor pagination.
    
    Attributes:
    message (str): The message sent by the user
    id (str): The ID of the message
    date (datetime): The date the message was created in ISO format
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
