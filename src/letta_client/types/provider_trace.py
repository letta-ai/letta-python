# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
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
        agent_id (str): ID of the agent that generated this trace.
        agent_tags (list[str]): Tags associated with the agent for filtering.
        call_type (str): Type of call (agent_step, summarization, etc.).
        run_id (str): ID of the run this trace is associated with.
        source (str): Source service that generated this trace (memgpt-server, lettuce-py).
        organization_id (str): The unique identifier of the organization.
        created_at (datetime): The timestamp when the object was created.
    """

    request_json: Dict[str, object]
    """JSON content of the provider request"""

    response_json: Dict[str, object]
    """JSON content of the provider response"""

    id: Optional[str] = None
    """The human-friendly ID of the Provider_trace"""

    agent_id: Optional[str] = None
    """ID of the agent that generated this trace"""

    agent_tags: Optional[List[str]] = None
    """Tags associated with the agent for filtering"""

    call_type: Optional[str] = None
    """Type of call (agent_step, summarization, etc.)"""

    created_at: Optional[datetime] = None
    """The timestamp when the object was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this object."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this object."""

    run_id: Optional[str] = None
    """ID of the run this trace is associated with"""

    source: Optional[str] = None
    """Source service that generated this trace (memgpt-server, lettuce-py)"""

    step_id: Optional[str] = None
    """ID of the step that this trace is associated with"""

    updated_at: Optional[datetime] = None
    """The timestamp when the object was last updated."""
