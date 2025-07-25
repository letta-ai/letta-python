# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
from .tool import Tool
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GenerateToolOutput(UncheckedBaseModel):
    tool: Tool = pydantic.Field()
    """
    Generated tool
    """

    sample_args: typing.Dict[str, typing.Optional[typing.Any]] = pydantic.Field()
    """
    Sample arguments for the tool
    """

    response: str = pydantic.Field()
    """
    Response from the assistant
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
