# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["BlockListParams"]


class BlockListParams(TypedDict, total=False):
    after: Optional[str]
    """Block ID cursor for pagination.

    Returns blocks that come after this block ID in the specified sort order
    """

    before: Optional[str]
    """Block ID cursor for pagination.

    Returns blocks that come before this block ID in the specified sort order
    """

    connected_to_agents_count_eq: Optional[Iterable[int]]
    """Filter blocks by the exact number of connected agents.

    If provided, returns blocks that have exactly this number of connected agents.
    """

    connected_to_agents_count_gt: Optional[int]
    """Filter blocks by the number of connected agents.

    If provided, returns blocks that have more than this number of connected agents.
    """

    connected_to_agents_count_lt: Optional[int]
    """Filter blocks by the number of connected agents.

    If provided, returns blocks that have less than this number of connected agents.
    """

    description_search: Optional[str]
    """Search blocks by description.

    If provided, returns blocks whose description matches the search query. This is
    a full-text search on block descriptions.
    """

    identifier_keys: Optional[SequenceNotStr[str]]
    """Search agents by identifier keys"""

    identity_id: Optional[str]
    """The ID of the identity in the format 'identity-<uuid4>'"""

    label: Optional[str]
    """Label to include (alphanumeric, hyphens, underscores, forward slashes)"""

    label_search: Optional[str]
    """Search blocks by label.

    If provided, returns blocks whose label matches the search query. This is a
    full-text search on block labels.
    """

    limit: Optional[int]
    """Number of blocks to return"""

    match_all_tags: bool
    """If True, only returns blocks that match ALL given tags.

    Otherwise, return blocks that have ANY of the passed-in tags.
    """

    name: Optional[str]
    """Name filter (alphanumeric, spaces, hyphens, underscores)"""

    order: Literal["asc", "desc"]
    """Sort order for blocks by creation time.

    'asc' for oldest first, 'desc' for newest first
    """

    order_by: Literal["created_at"]
    """Field to sort by"""

    project_id: Optional[str]
    """Search blocks by project id"""

    tags: Optional[SequenceNotStr[str]]
    """List of tags to filter blocks by"""

    templates_only: bool
    """Whether to include only templates"""

    value_search: Optional[str]
    """Search blocks by value.

    If provided, returns blocks whose value matches the search query. This is a
    full-text search on block values.
    """
