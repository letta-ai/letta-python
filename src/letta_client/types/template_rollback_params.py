# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TemplateRollbackParams"]


class TemplateRollbackParams(TypedDict, total=False):
    version: Required[str]
    """The target version to rollback to (e.g., "1", "2", "latest").

    Cannot be "current" or "dev".
    """
