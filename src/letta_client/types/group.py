# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .manager_type import ManagerType

__all__ = ["Group"]


class Group(BaseModel):
    id: str
    """The id of the group. Assigned by the database."""

    agent_ids: List[str]

    description: str

    manager_type: ManagerType

    base_template_id: Optional[str] = None
    """The base template id."""

    deployment_id: Optional[str] = None
    """The id of the deployment."""

    hidden: Optional[bool] = None
    """If set to True, the group will be hidden."""

    last_processed_message_id: Optional[str] = None

    manager_agent_id: Optional[str] = None

    max_message_buffer_length: Optional[int] = None
    """The desired maximum length of messages in the context window of the convo agent.

    This is a best effort, and may be off slightly due to user/assistant
    interleaving.
    """

    max_turns: Optional[int] = None

    min_message_buffer_length: Optional[int] = None
    """The desired minimum length of messages in the context window of the convo agent.

    This is a best effort, and may be off-by-one due to user/assistant interleaving.
    """

    project_id: Optional[str] = None
    """The associated project id."""

    shared_block_ids: Optional[List[str]] = None

    sleeptime_agent_frequency: Optional[int] = None

    template_id: Optional[str] = None
    """The id of the template."""

    termination_token: Optional[str] = None

    turns_counter: Optional[int] = None
