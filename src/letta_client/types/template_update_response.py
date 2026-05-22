# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

__all__ = ["TemplateUpdateResponse"]

class TemplateUpdateResponse(BaseModel):
    success: bool

    message: Optional[str] = None