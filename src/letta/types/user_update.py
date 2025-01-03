# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UserUpdate(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The id of the user to update.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new name of the user.
    """

    organization_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new organization id of the user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
