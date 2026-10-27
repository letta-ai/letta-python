# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EnvironmentRetrieveResponse", "Metadata", "MetadataMachine", "MetadataSelfUpdate"]


class MetadataMachine(BaseModel):
    architecture: Optional[str] = None

    cpu: Optional[str] = None

    gpus: Optional[List[str]] = None

    memory_bytes: Optional[float] = FieldInfo(alias="memoryBytes", default=None)

    model: Optional[str] = None

    os_name: Optional[str] = FieldInfo(alias="osName", default=None)

    os_version: Optional[str] = FieldInfo(alias="osVersion", default=None)


class MetadataSelfUpdate(BaseModel):
    supported: bool

    writable: bool

    install_path: Optional[str] = None

    manual_command: Optional[str] = None

    reason: Optional[str] = None


class Metadata(BaseModel):
    git_branch: Optional[str] = FieldInfo(alias="gitBranch", default=None)

    letta_code_version: Optional[str] = FieldInfo(alias="lettaCodeVersion", default=None)

    machine: Optional[MetadataMachine] = None

    node_version: Optional[str] = FieldInfo(alias="nodeVersion", default=None)

    os: Optional[str] = None

    sandbox_size: Optional[Literal["regular", "large", "xlarge"]] = FieldInfo(alias="sandboxSize", default=None)

    self_update: Optional[MetadataSelfUpdate] = None

    supported_commands: Optional[List[str]] = None

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


class EnvironmentRetrieveResponse(BaseModel):
    id: str

    connected_at: Optional[float] = FieldInfo(alias="connectedAt", default=None)

    connection_id: Optional[str] = FieldInfo(alias="connectionId", default=None)

    connection_name: str = FieldInfo(alias="connectionName")

    device_id: str = FieldInfo(alias="deviceId")

    first_seen_at: float = FieldInfo(alias="firstSeenAt")

    is_owner: bool = FieldInfo(alias="isOwner")

    last_heartbeat: Optional[float] = FieldInfo(alias="lastHeartbeat", default=None)

    last_seen_at: float = FieldInfo(alias="lastSeenAt")

    organization_id: str = FieldInfo(alias="organizationId")

    pod_id: Optional[str] = FieldInfo(alias="podId", default=None)

    visibility: Literal["private", "organization"]

    api_key_owner: Optional[str] = FieldInfo(alias="apiKeyOwner", default=None)

    current_mode: Optional[Literal["default", "standard", "acceptEdits", "bypassPermissions", "unrestricted"]] = (
        FieldInfo(alias="currentMode", default=None)
    )

    listener_instance_id: Optional[str] = FieldInfo(alias="listenerInstanceId", default=None)

    metadata: Optional[Metadata] = None

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
