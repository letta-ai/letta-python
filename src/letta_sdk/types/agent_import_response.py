# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["AgentImportResponse"]


class AgentImportResponse(BaseModel):
    agent_ids: List[str]
    """List of IDs of the imported agents"""
