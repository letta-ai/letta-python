# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .action_parameters_model import ActionParametersModel
from .action_response_model import ActionResponseModel
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ActionModel(UniversalBaseModel):
    """
    Action data model.
    """

    name: str
    display_name: typing.Optional[str] = None
    parameters: ActionParametersModel
    response: ActionResponseModel
    app_name: typing_extensions.Annotated[str, FieldMetadata(alias="appName")]
    app_id: typing_extensions.Annotated[str, FieldMetadata(alias="appId")]
    tags: typing.List[str]
    enabled: typing.Optional[bool] = None
    logo: typing.Optional[str] = None
    description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow