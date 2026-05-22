# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TemplateUpdateResponse"]


class TemplateUpdateResponse(BaseModel):
    success: bool

    message: Optional[str] = None
