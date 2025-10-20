# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ImageContentParam", "Source", "SourceURLImage", "SourceBase64Image", "SourceLettaImage"]


class SourceURLImage(TypedDict, total=False):
    url: Required[str]
    """The URL of the image."""

    type: Literal["url"]
    """The source type for the image."""


class SourceBase64Image(TypedDict, total=False):
    data: Required[str]
    """The base64 encoded image data."""

    media_type: Required[str]
    """The media type for the image."""

    detail: Optional[str]
    """
    What level of detail to use when processing and understanding the image (low,
    high, or auto to let the model decide)
    """

    type: Literal["base64"]
    """The source type for the image."""


class SourceLettaImage(TypedDict, total=False):
    file_id: Required[str]
    """The unique identifier of the image file persisted in storage."""

    data: Optional[str]
    """The base64 encoded image data."""

    detail: Optional[str]
    """
    What level of detail to use when processing and understanding the image (low,
    high, or auto to let the model decide)
    """

    media_type: Optional[str]
    """The media type for the image."""

    type: Literal["letta"]
    """The source type for the image."""


Source: TypeAlias = Union[SourceURLImage, SourceBase64Image, SourceLettaImage]


class ImageContentParam(TypedDict, total=False):
    source: Required[Source]
    """The source of the image."""

    type: Literal["image"]
    """The type of the message."""
