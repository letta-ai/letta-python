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

    env_vars_json: Optional[str]
    """Environment variables as a JSON string to pass to the agent for tool execution."""

    override_embedding_handle: Optional[str]
    """Override import with specific embedding handle."""

    override_existing_tools: bool
    """
    If set to True, existing tools can get their source code overwritten by the
    uploaded tool definitions. Note that Letta core tools can never be updated
    externally.
    """

    project_id: Optional[str]
    """The project ID to associate the uploaded agent with."""

    strip_messages: bool
    """If set to True, strips all messages from the agent before importing."""

    x_override_embedding_model: Annotated[str, PropertyInfo(alias="x-override-embedding-model")]
