# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .text_content import TextContent
from .image_content import ImageContent

__all__ = ["ToolReturn", "ToolReturnUnionMember0"]

ToolReturnUnionMember0: TypeAlias = Annotated[Union[TextContent, ImageContent], PropertyInfo(discriminator="type")]


class ToolReturn(BaseModel):
    status: Literal["success", "error"]

    tool_call_id: str

    tool_return: Union[List[ToolReturnUnionMember0], str]
    """The tool return value - either a string or list of content parts (text/image)"""

    stderr: Optional[List[str]] = None

    stdout: Optional[List[str]] = None

    type: Optional[Literal["tool"]] = None
    """The message type to be created."""
