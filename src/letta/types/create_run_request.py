# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from .letta_schemas_openai_openai_tool_call import LettaSchemasOpenaiOpenaiToolCall
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreateRunRequest(UniversalBaseModel):
    assistant_id: str = pydantic.Field()
    """
    The unique identifier of the assistant.
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    The model used by the run.
    """

    instructions: str = pydantic.Field()
    """
    The instructions for the run.
    """

    additional_instructions: typing.Optional[str] = pydantic.Field(default=None)
    """
    Additional instructions for the run.
    """

    tools: typing.Optional[typing.List[LettaSchemasOpenaiOpenaiToolCall]] = pydantic.Field(default=None)
    """
    The tools used by the run (overrides assistant).
    """

    metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Metadata associated with the run.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow