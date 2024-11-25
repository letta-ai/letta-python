# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["VersionTemplateCreateResponse"]


class VersionTemplateCreateResponse(BaseModel):
    version: str

    agent_id: Optional[str] = FieldInfo(alias="agentId", default=None)
