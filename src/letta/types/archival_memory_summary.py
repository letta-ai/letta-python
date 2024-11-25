# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["ArchivalMemorySummary"]


class ArchivalMemorySummary(BaseModel):
    size: int
    """Number of rows in archival memory"""
