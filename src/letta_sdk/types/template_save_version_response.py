# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TemplateSaveVersionResponse"]


class TemplateSaveVersionResponse(BaseModel):
    id: str

    latest_version: str
    """The latest version of the template"""

    name: str
    """The exact name of the template"""

    project_id: str

    project_slug: str

    template_deployment_slug: str
    """The full name of the template, including version and project slug"""

    updated_at: str
    """When the template was last updated"""

    description: Optional[str] = None
