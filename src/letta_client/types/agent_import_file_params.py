# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["AgentImportFileParams"]


class AgentImportFileParams(TypedDict, total=False):
    file: Required[FileTypes]

    append_copy_suffix: bool
    """If set to True, appends "\\__copy" to the end of the agent name."""

    embedding: Optional[str]
    """Embedding handle to override with."""

    env_vars_json: Optional[str]
    """Environment variables as a JSON string to pass to the agent for tool execution.

    Use 'secrets' instead.
    """

    model: Optional[str]
    """Model handle to override the agent's default model.

    This allows the imported agent to use a different model while keeping other
    defaults (e.g., context size) from the original configuration.
    """

    name: Optional[str]
    """If provided, overrides the agent name with this value."""

    override_embedding_handle: Optional[str]
    """Override import with specific embedding handle. Use 'embedding' instead."""

    override_existing_tools: bool
    """
    If set to True, existing tools can get their source code overwritten by the
    uploaded tool definitions. Note that Letta core tools can never be updated
    externally.
    """

    override_model_handle: Optional[str]
    """Model handle to override the agent's default model. Use 'model' instead."""

    override_name: Optional[str]
    """If provided, overrides the agent name with this value. Use 'name' instead."""

    project_id: Optional[str]
    """The project ID to associate the uploaded agent with.

    This is now passed via headers.
    """

    secrets: Optional[str]
    """Secrets as a JSON string to pass to the agent for tool execution."""

    strip_messages: bool
    """If set to True, strips all messages from the agent before importing."""

    x_override_embedding_model: Annotated[str, PropertyInfo(alias="x-override-embedding-model")]
