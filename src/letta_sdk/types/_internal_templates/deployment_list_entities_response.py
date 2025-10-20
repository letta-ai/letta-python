# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["DeploymentListEntitiesResponse", "Entity"]


class Entity(BaseModel):
    id: str

    type: str

    description: Optional[str] = None

    entity_id: Optional[str] = None

    name: Optional[str] = None

    project_id: Optional[str] = None


class DeploymentListEntitiesResponse(BaseModel):
    deployment_id: str

    message: str

    total_count: int

    entities: Optional[List[Entity]] = None
