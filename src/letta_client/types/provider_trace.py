# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ProviderTrace"]


class ProviderTrace(BaseModel):
    """Letta's internal representation of a provider trace.

    Attributes:
        id (str): The unique identifier of the provider trace.
        request_json (Dict[str, Any]): JSON content of the provider request.
        response_json (Dict[str, Any]): JSON content of the provider response.
        step_id (str): ID of the step that this trace is associated with.
        organization_id (str): The unique identifier of the organization.
        created_at (datetime): The timestamp when the object was created.
    """

    request_json: Dict[str, object]
    """JSON content of the provider request"""

    response_json: Dict[str, object]
    """JSON content of the provider response"""

    id: Optional[str] = None
    """The human-friendly ID of the Provider_trace"""

    created_at: Optional[datetime] = None
    """The timestamp when the object was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this object."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this object."""

    step_id: Optional[str] = None
    """ID of the step that this trace is associated with"""

    updated_at: Optional[datetime] = None
    """The timestamp when the object was last updated."""
