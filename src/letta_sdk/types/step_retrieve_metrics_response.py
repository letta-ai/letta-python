# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["StepRetrieveMetricsResponse"]


class StepRetrieveMetricsResponse(BaseModel):
    id: str
    """The id of the step this metric belongs to (matches steps.id)."""

    agent_id: Optional[str] = None
    """The unique identifier of the agent."""

    base_template_id: Optional[str] = None
    """The base template ID that the step belongs to (cloud only)."""

    job_id: Optional[str] = None
    """The unique identifier of the job."""

    llm_request_ns: Optional[int] = None
    """Time spent on LLM requests in nanoseconds."""

    llm_request_start_ns: Optional[int] = None
    """The timestamp of the start of the llm request in nanoseconds."""

    project_id: Optional[str] = None
    """The project that the step belongs to (cloud only)."""

    provider_id: Optional[str] = None
    """The unique identifier of the provider."""

    step_ns: Optional[int] = None
    """Total time for the step in nanoseconds."""

    step_start_ns: Optional[int] = None
    """The timestamp of the start of the step in nanoseconds."""

    template_id: Optional[str] = None
    """The template ID that the step belongs to (cloud only)."""

    tool_execution_ns: Optional[int] = None
    """Time spent on tool execution in nanoseconds."""
