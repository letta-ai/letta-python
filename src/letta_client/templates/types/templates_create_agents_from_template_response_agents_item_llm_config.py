# This file was auto-generated by Fern from our API Definition.

from ...core.unchecked_base_model import UncheckedBaseModel
from .templates_create_agents_from_template_response_agents_item_llm_config_model_endpoint_type import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemLlmConfigModelEndpointType,
)
import typing
from .templates_create_agents_from_template_response_agents_item_llm_config_model_endpoint import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemLlmConfigModelEndpoint,
)
from .templates_create_agents_from_template_response_agents_item_llm_config_model_wrapper import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemLlmConfigModelWrapper,
)
from .templates_create_agents_from_template_response_agents_item_llm_config_put_inner_thoughts_in_kwargs import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemLlmConfigPutInnerThoughtsInKwargs,
)
from .templates_create_agents_from_template_response_agents_item_llm_config_handle import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemLlmConfigHandle,
)
from .templates_create_agents_from_template_response_agents_item_llm_config_temperature import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemLlmConfigTemperature,
)
from .templates_create_agents_from_template_response_agents_item_llm_config_max_tokens import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemLlmConfigMaxTokens,
)
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class TemplatesCreateAgentsFromTemplateResponseAgentsItemLlmConfig(UncheckedBaseModel):
    model: str
    model_endpoint_type: TemplatesCreateAgentsFromTemplateResponseAgentsItemLlmConfigModelEndpointType
    model_endpoint: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemLlmConfigModelEndpoint] = None
    model_wrapper: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemLlmConfigModelWrapper] = None
    context_window: float
    put_inner_thoughts_in_kwargs: typing.Optional[
        TemplatesCreateAgentsFromTemplateResponseAgentsItemLlmConfigPutInnerThoughtsInKwargs
    ] = None
    handle: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemLlmConfigHandle] = None
    temperature: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemLlmConfigTemperature] = None
    max_tokens: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemLlmConfigMaxTokens] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
