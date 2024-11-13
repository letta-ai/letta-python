# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["RecallMemorySummary"]


class RecallMemorySummary(BaseModel):
    size: int
    """Number of rows in recall memory"""
