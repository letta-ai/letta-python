# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["DeploymentDeleteResponse"]


class DeploymentDeleteResponse(BaseModel):
    message: str

    deleted_agents: Optional[List[str]] = None

    deleted_blocks: Optional[List[str]] = None

    deleted_groups: Optional[List[str]] = None
