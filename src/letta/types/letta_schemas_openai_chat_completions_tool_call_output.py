# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .tool_call_function_output import ToolCallFunctionOutput
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class LettaSchemasOpenaiChatCompletionsToolCallOutput(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The ID of the tool call
    """

    type: typing.Optional[str] = None
    function: ToolCallFunctionOutput = pydantic.Field()
    """
    The arguments and name for the function
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow