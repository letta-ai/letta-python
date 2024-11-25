# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["AgentMigrateParams"]


class AgentMigrateParams(TypedDict, total=False):
    preserve_core_memories: Required[bool]

    to_template: Required[str]

    variables: Dict[str, str]
    """
    If you chose to not preserve core memories, you should provide the new variables
    for the core memories
    """
