# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .text_content import TextContent
from .image_content import ImageContent

__all__ = ["LettaUserMessageContentUnion"]

LettaUserMessageContentUnion: TypeAlias = Annotated[
    Union[TextContent, ImageContent], PropertyInfo(discriminator="type")
]
