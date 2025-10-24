# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .text_content_param import TextContentParam
from .image_content_param import ImageContentParam

__all__ = ["LettaUserMessageContentUnionParam"]

LettaUserMessageContentUnionParam: TypeAlias = Union[TextContentParam, ImageContentParam]
