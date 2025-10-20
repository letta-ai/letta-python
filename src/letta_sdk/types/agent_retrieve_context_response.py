# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .agents.message import Message

__all__ = ["AgentRetrieveContextResponse", "FunctionsDefinition", "FunctionsDefinitionFunction"]


class FunctionsDefinitionFunction(BaseModel):
    name: str

    description: Optional[str] = None

    parameters: Optional[Dict[str, object]] = None

    strict: Optional[bool] = None

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


class FunctionsDefinition(BaseModel):
    function: FunctionsDefinitionFunction

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


class AgentRetrieveContextResponse(BaseModel):
    context_window_size_current: int
    """The current number of tokens in the context window."""

    context_window_size_max: int
    """The maximum amount of tokens the context window can hold."""

    core_memory: str
    """The content of the core memory."""

    external_memory_summary: str
    """
    The metadata summary of the external memory sources (archival + recall
    metadata).
    """

    functions_definitions: Optional[List[FunctionsDefinition]] = None
    """The content of the functions definitions."""

    messages: List[Message]
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
