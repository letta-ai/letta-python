# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DeleteAssistantFileResponse(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The unique identifier of the file.
    """

    object: typing.Optional[str] = None
    deleted: bool = pydantic.Field()
    """
    Whether the file was deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow