# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentExportParams"]


class AgentExportParams(TypedDict, total=False):
    max_steps: int

    use_legacy_format: bool
    """If true, exports using the legacy single-agent format (v1).

    If false, exports using the new multi-entity format (v2).
    """
