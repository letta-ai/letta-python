# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["TemplateUpdateParams"]


class TemplateUpdateParams(TypedDict, total=False):
    agent_file_json: Required[Dict[str, Optional[object]]]
    """The agent file to update the current template version from"""

    save_existing_changes: bool
    """
    If true, Letta will automatically save any changes as a version before updating
    the template
    """

    update_existing_tools: bool
    """
    If true, update existing custom tools source_code and json_schema (source_type
    cannot be changed)
    """
