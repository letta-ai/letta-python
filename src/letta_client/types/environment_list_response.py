# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EnvironmentListResponse", "Connection", "ConnectionMetadata"]


class ConnectionMetadata(BaseModel):
    git_branch: Optional[str] = FieldInfo(alias="gitBranch", default=None)

    letta_code_version: Optional[str] = FieldInfo(alias="lettaCodeVersion", default=None)

    node_version: Optional[str] = FieldInfo(alias="nodeVersion", default=None)

    os: Optional[str] = None

    working_directory: Optional[str] = FieldInfo(alias="workingDirectory", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Connection(BaseModel):
    id: str

    connected_at: Optional[float] = FieldInfo(alias="connectedAt", default=None)

    connection_id: Optional[str] = FieldInfo(alias="connectionId", default=None)

    connection_name: str = FieldInfo(alias="connectionName")

    device_id: str = FieldInfo(alias="deviceId")

    first_seen_at: float = FieldInfo(alias="firstSeenAt")

    last_heartbeat: Optional[float] = FieldInfo(alias="lastHeartbeat", default=None)

    last_seen_at: float = FieldInfo(alias="lastSeenAt")

    organization_id: str = FieldInfo(alias="organizationId")

    pod_id: Optional[str] = FieldInfo(alias="podId", default=None)

    api_key_owner: Optional[str] = FieldInfo(alias="apiKeyOwner", default=None)

    current_mode: Optional[Literal["default", "standard", "acceptEdits", "bypassPermissions", "unrestricted"]] = (
        FieldInfo(alias="currentMode", default=None)
    )

    metadata: Optional[ConnectionMetadata] = None

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)


class EnvironmentListResponse(BaseModel):
    connections: List[Connection]

    has_next_page: bool = FieldInfo(alias="hasNextPage")
