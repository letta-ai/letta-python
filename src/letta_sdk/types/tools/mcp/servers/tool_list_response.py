# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["ToolListResponse", "ToolListResponseItem", "ToolListResponseItemAnnotations", "ToolListResponseItemHealth"]


class ToolListResponseItemAnnotations(BaseModel):
    destructive_hint: Optional[bool] = FieldInfo(alias="destructiveHint", default=None)

    idempotent_hint: Optional[bool] = FieldInfo(alias="idempotentHint", default=None)

    open_world_hint: Optional[bool] = FieldInfo(alias="openWorldHint", default=None)

    read_only_hint: Optional[bool] = FieldInfo(alias="readOnlyHint", default=None)

    title: Optional[str] = None

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


class ToolListResponseItemHealth(BaseModel):
    status: str
    """Schema health status: STRICT_COMPLIANT, NON_STRICT_ONLY, or INVALID"""

    reasons: Optional[List[str]] = None
    """List of reasons for the health status"""


class ToolListResponseItem(BaseModel):
    input_schema: Dict[str, object] = FieldInfo(alias="inputSchema")

    name: str

    api_meta: Optional[Dict[str, object]] = FieldInfo(alias="_meta", default=None)

    annotations: Optional[ToolListResponseItemAnnotations] = None
    """Additional properties describing a Tool to clients.

    NOTE: all properties in ToolAnnotations are **hints**. They are not guaranteed
    to provide a faithful description of tool behavior (including descriptive
    properties like `title`).

    Clients should never make tool use decisions based on ToolAnnotations received
    from untrusted servers.
    """

    description: Optional[str] = None

    health: Optional[ToolListResponseItemHealth] = None
    """Health status for an MCP tool's schema."""

    output_schema: Optional[Dict[str, object]] = FieldInfo(alias="outputSchema", default=None)

    title: Optional[str] = None

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


ToolListResponse: TypeAlias = List[ToolListResponseItem]
