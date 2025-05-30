# This file was auto-generated by Fern from our API Definition.

from ...core.unchecked_base_model import UncheckedBaseModel
import typing
from .templates_list_response_templates_item import TemplatesListResponseTemplatesItem
import typing_extensions
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class TemplatesListResponse(UncheckedBaseModel):
    templates: typing.List[TemplatesListResponseTemplatesItem]
    has_next_page: typing_extensions.Annotated[bool, FieldMetadata(alias="hasNextPage")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
