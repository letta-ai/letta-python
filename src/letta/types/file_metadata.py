# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FileMetadata(UniversalBaseModel):
    """
    Representation of a single FileMetadata
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-friendly ID of the File
    """

    organization_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the organization associated with the document.
    """

    source_id: str = pydantic.Field()
    """
    The unique identifier of the source associated with the document.
    """

    file_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the file.
    """

    file_path: typing.Optional[str] = pydantic.Field(default=None)
    """
    The path to the file.
    """

    file_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the file (MIME type).
    """

    file_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The size of the file in bytes.
    """

    file_creation_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The creation date of the file.
    """

    file_last_modified_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last modified date of the file.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The creation date of the file.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The update date of the file.
    """

    is_deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this file is deleted or not.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow