# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime

from ..._models import BaseModel
from ..agent_type import AgentType
from .core_memory.block import Block

__all__ = ["Memory", "FileBlock"]


class FileBlock(BaseModel):
    file_id: str
    """Unique identifier of the file."""

    is_open: bool
    """True if the agent currently has the file open."""

    source_id: str
    """Unique identifier of the source."""

    value: str
    """Value of the block."""

    id: Optional[str] = None
    """The human-friendly ID of the Block"""

    base_template_id: Optional[str] = None
    """The base template id of the block."""

    created_by_id: Optional[str] = None
    """The id of the user that made this Block."""

    deployment_id: Optional[str] = None
    """The id of the deployment."""

    description: Optional[str] = None
    """Description of the block."""

    entity_id: Optional[str] = None
    """The id of the entity within the template."""

    hidden: Optional[bool] = None
    """If set to True, the block will be hidden."""

    is_template: Optional[bool] = None
    """Whether the block is a template (e.g. saved human/persona options)."""

    label: Optional[str] = None
    """Label of the block (e.g. 'human', 'persona') in the context window."""

    last_accessed_at: Optional[datetime] = None
    """UTC timestamp of the agent’s most recent access to this file.

    Any operations from the open, close, or search tools will update this field.
    """

    last_updated_by_id: Optional[str] = None
    """The id of the user that last updated this Block."""

    limit: Optional[int] = None
    """Character limit of the block."""

    metadata: Optional[Dict[str, object]] = None
    """Metadata of the block."""

    name: Optional[str] = None
    """The id of the template."""

    preserve_on_migration: Optional[bool] = None
    """Preserve the block on template migration."""

    project_id: Optional[str] = None
    """The associated project id."""

    read_only: Optional[bool] = None
    """Whether the agent has read-only access to the block."""


class Memory(BaseModel):
    blocks: List[Block]
    """Memory blocks contained in the agent's in-context memory"""

    agent_type: Union[AgentType, str, None] = None
    """Agent type controlling prompt rendering."""

    file_blocks: Optional[List[FileBlock]] = None
    """Special blocks representing the agent's in-context memory of an attached file"""

    prompt_template: Optional[str] = None
    """Deprecated. Ignored for performance."""
