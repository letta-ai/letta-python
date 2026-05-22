# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from .text_content import TextContent

from .image_content import ImageContent

from ..._utils import PropertyInfo

from typing_extensions import Annotated, TypeAliasType, TypeAlias

__all__ = ["LettaUserMessageContentUnion"]

LettaUserMessageContentUnion: TypeAlias = Annotated[Union[TextContent, ImageContent], PropertyInfo(discriminator="type")]