# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .stop_reason_type import StopReasonType


class LettaStopReason(UncheckedBaseModel):
    """
    The stop reason from Letta indicating why agent loop stopped execution.
    """

    message_type: typing.Optional[typing.Literal["stop_reason"]] = pydantic.Field(default=None)
    """
    The type of the message.
    """

    stop_reason: StopReasonType = pydantic.Field()
    """
    The reason why execution stopped.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
