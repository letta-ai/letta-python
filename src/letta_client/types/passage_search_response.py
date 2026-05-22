# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from .passage import Passage

from typing import Optional, Dict, List

from typing_extensions import TypeAliasType, TypeAlias

__all__ = ["PassageSearchResponse", "PassageSearchResponseItem"]

class PassageSearchResponseItem(BaseModel):
    """Result from a passage search operation with scoring details."""
    passage: Passage
    """The passage object"""

    score: float
    """Relevance score"""

    metadata: Optional[Dict[str, object]] = None
    """Additional metadata about the search result"""

PassageSearchResponse: TypeAlias = List[PassageSearchResponseItem]