# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .text_content_param import TextContentParam
from .image_content_param import ImageContentParam

__all__ = ["ToolReturnParam", "ToolReturnUnionMember0"]

ToolReturnUnionMember0: TypeAlias = Union[TextContentParam, ImageContentParam]


class ToolReturnParam(TypedDict, total=False):
    status: Required[Literal["success", "error"]]

    tool_call_id: Required[str]

    tool_return: Required[Union[Iterable[ToolReturnUnionMember0], str]]
    """The tool return value - either a string or list of content parts (text/image)"""

    stderr: Optional[SequenceNotStr[str]]

    stdout: Optional[SequenceNotStr[str]]

    type: Literal["tool"]
    """The message type to be created."""
