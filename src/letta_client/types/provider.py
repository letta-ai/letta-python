# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .provider_category import ProviderCategory
from .provider_type import ProviderType


class Provider(UncheckedBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the provider, lazily created by the database manager.
    """

    name: str = pydantic.Field()
    """
    The name of the provider
    """

    provider_type: ProviderType = pydantic.Field()
    """
    The type of the provider
    """

    provider_category: ProviderCategory = pydantic.Field()
    """
    The category of the provider (base or byok)
    """

    api_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    API key or secret key used for requests to the provider.
    """

    base_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Base URL for the provider.
    """

    access_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    Access key used for requests to the provider.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    Region used for requests to the provider.
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The last update timestamp of the provider.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
