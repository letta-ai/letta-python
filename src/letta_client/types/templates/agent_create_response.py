# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AgentCreateResponse"]


class AgentCreateResponse(BaseModel):
    agent_ids: List[str]
    """Array of created agent IDs"""

    deployment_id: str
    """The deployment ID for the created agents"""

    group_id: Optional[str] = None
    """Optional group ID if agents were created in a group"""
