# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .xai_model_settings import XaiModelSettings
from .groq_model_settings import GroqModelSettings
from .azure_model_settings import AzureModelSettings
from .text_response_format import TextResponseFormat
from .openai_model_settings import OpenAIModelSettings
from .bedrock_model_settings import BedrockModelSettings
from .deepseek_model_settings import DeepseekModelSettings
from .together_model_settings import TogetherModelSettings
from .anthropic_model_settings import AnthropicModelSettings
from .google_ai_model_settings import GoogleAIModelSettings
from .json_object_response_format import JsonObjectResponseFormat
from .json_schema_response_format import JsonSchemaResponseFormat
from .google_vertex_model_settings import GoogleVertexModelSettings

__all__ = [
    "Conversation",
    "ModelSettings",
    "ModelSettingsZaiModelSettings",
    "ModelSettingsZaiModelSettingsResponseFormat",
    "ModelSettingsZaiModelSettingsThinking",
    "ModelSettingsOpenRouterModelSettings",
    "ModelSettingsOpenRouterModelSettingsResponseFormat",
    "ModelSettingsChatGptoAuthModelSettings",
    "ModelSettingsChatGptoAuthModelSettingsReasoning",
]

ModelSettingsZaiModelSettingsResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ModelSettingsZaiModelSettingsThinking(BaseModel):
    """The thinking configuration for GLM-4.5+ models."""

    clear_thinking: Optional[bool] = None
    """If False, preserved thinking is used (recommended for agents)."""

    type: Optional[Literal["enabled", "disabled"]] = None
    """Whether thinking is enabled or disabled."""


class ModelSettingsZaiModelSettings(BaseModel):
    """Z.ai (ZhipuAI) model configuration (OpenAI-compatible)."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["zai"]] = None
    """The type of the provider."""

    response_format: Optional[ModelSettingsZaiModelSettingsResponseFormat] = None
    """The response format for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""

    thinking: Optional[ModelSettingsZaiModelSettingsThinking] = None
    """The thinking configuration for GLM-4.5+ models."""


ModelSettingsOpenRouterModelSettingsResponseFormat: TypeAlias = Annotated[
    Union[TextResponseFormat, JsonSchemaResponseFormat, JsonObjectResponseFormat, None],
    PropertyInfo(discriminator="type"),
]


class ModelSettingsOpenRouterModelSettings(BaseModel):
    """OpenRouter model configuration (OpenAI-compatible)."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["openrouter"]] = None
    """The type of the provider."""

    response_format: Optional[ModelSettingsOpenRouterModelSettingsResponseFormat] = None
    """The response format for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""


class ModelSettingsChatGptoAuthModelSettingsReasoning(BaseModel):
    """The reasoning configuration for the model."""

    reasoning_effort: Optional[Literal["none", "low", "medium", "high", "xhigh"]] = None
    """The reasoning effort level for GPT-5.x and o-series models."""


class ModelSettingsChatGptoAuthModelSettings(BaseModel):
    """ChatGPT OAuth model configuration (uses ChatGPT backend API)."""

    max_output_tokens: Optional[int] = None
    """The maximum number of tokens the model can generate."""

    parallel_tool_calls: Optional[bool] = None
    """Whether to enable parallel tool calling."""

    provider_type: Optional[Literal["chatgpt_oauth"]] = None
    """The type of the provider."""

    reasoning: Optional[ModelSettingsChatGptoAuthModelSettingsReasoning] = None
    """The reasoning configuration for the model."""

    temperature: Optional[float] = None
    """The temperature of the model."""


ModelSettings: TypeAlias = Annotated[
    Union[
        OpenAIModelSettings,
        AnthropicModelSettings,
        GoogleAIModelSettings,
        GoogleVertexModelSettings,
        AzureModelSettings,
        XaiModelSettings,
        ModelSettingsZaiModelSettings,
        GroqModelSettings,
        DeepseekModelSettings,
        TogetherModelSettings,
        BedrockModelSettings,
        ModelSettingsOpenRouterModelSettings,
        ModelSettingsChatGptoAuthModelSettings,
        None,
    ],
    PropertyInfo(discriminator="provider_type"),
]


class Conversation(BaseModel):
    """Represents a conversation on an agent for concurrent messaging."""

    id: str
    """The unique identifier of the conversation."""

    agent_id: str
    """The ID of the agent this conversation belongs to."""

    created_at: Optional[datetime] = None
    """The timestamp when the object was created."""

    created_by_id: Optional[str] = None
    """The id of the user that made this object."""

    in_context_message_ids: Optional[List[str]] = None
    """The IDs of in-context messages for the conversation."""

    isolated_block_ids: Optional[List[str]] = None
    """
    IDs of blocks that are isolated (specific to this conversation, overriding agent
    defaults).
    """

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this object."""

    model: Optional[str] = None
    """The model handle for this conversation (overrides agent's model).

    Format: provider/model-name.
    """

    api_model_settings: Optional[ModelSettings] = FieldInfo(alias="model_settings", default=None)
    """The model settings for this conversation (overrides agent's model settings)."""

    summary: Optional[str] = None
    """A summary of the conversation."""

    updated_at: Optional[datetime] = None
    """The timestamp when the object was last updated."""
