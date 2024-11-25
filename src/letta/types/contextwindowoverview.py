# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .agents.memory.messageoutput import Messageoutput

__all__ = ["Contextwindowoverview", "FunctionsDefinition", "FunctionsDefinitionFunction"]


class FunctionsDefinitionFunction(BaseModel):
    name: str

    description: Optional[str] = None

    parameters: Optional[object] = None


class FunctionsDefinition(BaseModel):
    function: FunctionsDefinitionFunction

    type: Optional[Literal["function"]] = None


class Contextwindowoverview(BaseModel):
    context_window_size_current: int
    """The current number of tokens in the context window."""

    context_window_size_max: int
    """The maximum amount of tokens the context window can hold."""

    core_memory: str
    """The content of the core memory."""

    functions_definitions: Optional[List[FunctionsDefinition]] = None
    """The content of the functions definitions."""

    messages: List[Messageoutput]
    """The messages in the context window."""

    num_archival_memory: int
    """The number of messages in the archival memory."""

    num_messages: int
    """The number of messages in the context window."""

    num_recall_memory: int
    """The number of messages in the recall memory."""

    num_tokens_core_memory: int
    """The number of tokens in the core memory."""

    num_tokens_external_memory_summary: int
    """
    The number of tokens in the external memory summary (archival + recall
    metadata).
    """

    num_tokens_functions_definitions: int
    """The number of tokens in the functions definitions."""

    num_tokens_messages: int
    """The number of tokens in the messages list."""

    num_tokens_summary_memory: int
    """The number of tokens in the summary memory."""

    num_tokens_system: int
    """The number of tokens in the system prompt."""

    system_prompt: str
    """The content of the system prompt."""

    summary_memory: Optional[str] = None
    """The content of the summary memory."""
