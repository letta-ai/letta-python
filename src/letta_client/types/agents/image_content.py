# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["ImageContent", "Source", "SourceURLImage", "SourceBase64Image", "SourceLettaImage"]


class SourceURLImage(BaseModel):
    url: str
    """The URL of the image."""

    type: Optional[Literal["url"]] = None
    """The source type for the image."""


class SourceBase64Image(BaseModel):
    data: str
    """The base64 encoded image data."""

    media_type: str
    """The media type for the image."""

    detail: Optional[str] = None
    """
    What level of detail to use when processing and understanding the image (low,
    high, or auto to let the model decide)
    """

    type: Optional[Literal["base64"]] = None
    """The source type for the image."""


class SourceLettaImage(BaseModel):
    file_id: str
    """The unique identifier of the image file persisted in storage."""

    data: Optional[str] = None
    """The base64 encoded image data."""

    detail: Optional[str] = None
    """
    What level of detail to use when processing and understanding the image (low,
    high, or auto to let the model decide)
    """

    media_type: Optional[str] = None
    """The media type for the image."""

    type: Optional[Literal["letta"]] = None
    """The source type for the image."""


Source: TypeAlias = Annotated[
    Union[SourceURLImage, SourceBase64Image, SourceLettaImage], PropertyInfo(discriminator="type")
]


class ImageContent(BaseModel):
    source: Source
    """The source of the image."""

    type: Optional[Literal["image"]] = None
    """The type of the message."""
