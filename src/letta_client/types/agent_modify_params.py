# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .llm_config_param import LlmConfigParam
from .init_tool_rule_param import InitToolRuleParam
from .child_tool_rule_param import ChildToolRuleParam
from .embedding_config_param import EmbeddingConfigParam
from .parent_tool_rule_param import ParentToolRuleParam
from .continue_tool_rule_param import ContinueToolRuleParam
from .terminal_tool_rule_param import TerminalToolRuleParam
from .text_response_format_param import TextResponseFormatParam
from .conditional_tool_rule_param import ConditionalToolRuleParam
from .json_object_response_format_param import JsonObjectResponseFormatParam
from .json_schema_response_format_param import JsonSchemaResponseFormatParam
from .requires_approval_tool_rule_param import RequiresApprovalToolRuleParam
from .max_count_per_step_tool_rule_param import MaxCountPerStepToolRuleParam
from .required_before_exit_tool_rule_param import RequiredBeforeExitToolRuleParam

__all__ = [
    "AgentModifyParams",
    "Embedding",
    "EmbeddingEmbeddingModelSettings",
    "Model",
    "ModelOpenAIModel",
    "ModelOpenAIModelReasoning",
    "ModelOpenAIModelResponseFormat",
    "ModelAnthropicModel",
    "ModelAnthropicModelThinking",
    "ModelGoogleAIModel",
    "ModelGoogleAIModelResponseSchema",
    "ModelGoogleAIModelThinkingConfig",
    "ModelGoogleVertexModel",
    "ModelGoogleVertexModelResponseSchema",
    "ModelGoogleVertexModelThinkingConfig",
    "ModelAzureModel",
    "ModelAzureModelResponseFormat",
    "ModelXaiModel",
    "ModelXaiModelResponseFormat",
    "ModelGroqModel",
    "ModelGroqModelResponseFormat",
    "ModelDeepseekModel",
    "ModelDeepseekModelResponseFormat",
    "ModelTogetherModel",
    "ModelTogetherModelResponseFormat",
    "ModelBedrockModel",
    "ModelBedrockModelResponseFormat",
    "ResponseFormat",
    "ToolRule",
]


class AgentModifyParams(TypedDict, total=False):
    base_template_id: Optional[str]
    """The base template id of the agent."""

    block_ids: Optional[SequenceNotStr[str]]
    """The ids of the blocks used by the agent."""

    context_window_limit: Optional[int]
    """The context window limit used by the agent."""

    description: Optional[str]
    """The description of the agent."""

    embedding: Optional[Embedding]
    """
    The embedding configuration handle used by the agent, specified in the format
    provider/model-name.
    """

    embedding_config: Optional[EmbeddingConfigParam]
    """Configuration for embedding model connection and processing parameters."""

    enable_sleeptime: Optional[bool]
    """If set to True, memory management will move to a background agent thread."""

    hidden: Optional[bool]
    """If set to True, the agent will be hidden."""

    identity_ids: Optional[SequenceNotStr[str]]
    """The ids of the identities associated with this agent."""

    last_run_completion: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """The timestamp when the agent last completed a run."""

    last_run_duration_ms: Optional[int]
    """The duration in milliseconds of the agent's last run."""

    llm_config: Optional[LlmConfigParam]
    """Configuration for Language Model (LLM) connection and generation parameters."""

    max_files_open: Optional[int]
    """Maximum number of files that can be open at once for this agent.

    Setting this too high may exceed the context window, which will break the agent.
    """

    max_tokens: Optional[int]
    """Deprecated: Use `model` field to configure max output tokens instead.

    The maximum number of tokens to generate, including reasoning step.
    """

    message_buffer_autoclear: Optional[bool]
    """
    If set to True, the agent will not remember previous messages (though the agent
    will still retain state via core memory blocks and archival/recall memory). Not
    recommended unless you have an advanced use case.
    """

    message_ids: Optional[SequenceNotStr[str]]
    """The ids of the messages in the agent's in-context memory."""

    metadata: Optional[Dict[str, object]]
    """The metadata of the agent."""

    model: Optional[Model]
    """The model used by the agent, specified either by a handle or an object.

    See the model schema for more information.
    """

    name: Optional[str]
    """The name of the agent."""

    parallel_tool_calls: Optional[bool]
    """Deprecated: Use `model` field to configure parallel tool calls instead.

    If set to True, enables parallel tool calling.
    """

    per_file_view_window_char_limit: Optional[int]
    """The per-file view window character limit for this agent.

    Setting this too high may exceed the context window, which will break the agent.
    """

    project_id: Optional[str]
    """The id of the project the agent belongs to."""

    reasoning: Optional[bool]
    """Deprecated: Use `model` field to configure reasoning instead.

    Whether to enable reasoning for this agent.
    """

    response_format: Optional[ResponseFormat]
    """Deprecated: Use `model` field to configure response format instead.

    The response format for the agent.
    """

    secrets: Optional[Dict[str, str]]
    """The environment variables for tool execution specific to this agent."""

    source_ids: Optional[SequenceNotStr[str]]
    """The ids of the sources used by the agent."""

    system: Optional[str]
    """The system prompt used by the agent."""

    tags: Optional[SequenceNotStr[str]]
    """The tags associated with the agent."""

    template_id: Optional[str]
    """The id of the template the agent belongs to."""

    timezone: Optional[str]
    """The timezone of the agent (IANA format)."""

    tool_exec_environment_variables: Optional[Dict[str, str]]
    """Deprecated: use `secrets` field instead"""

    tool_ids: Optional[SequenceNotStr[str]]
    """The ids of the tools used by the agent."""

    tool_rules: Optional[Iterable[ToolRule]]
    """The tool rules governing the agent."""


class EmbeddingEmbeddingModelSettings(TypedDict, total=False):
    model: Required[str]
    """The name of the model."""

    provider: Required[Literal["openai", "ollama"]]
    """The provider of the model."""


Embedding: TypeAlias = Union[str, EmbeddingEmbeddingModelSettings]


class ModelOpenAIModelReasoning(TypedDict, total=False):
    reasoning_effort: Literal["minimal", "low", "medium", "high"]
    """The reasoning effort to use when generating text reasoning models"""


ModelOpenAIModelResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class ModelOpenAIModel(TypedDict, total=False):
    model: Required[str]
    """The name of the model."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    provider: Literal["openai"]
    """The provider of the model."""

    reasoning: ModelOpenAIModelReasoning
    """The reasoning configuration for the model."""

    response_format: Optional[ModelOpenAIModelResponseFormat]
    """The response format for the model."""

    temperature: float
    """The temperature of the model."""


class ModelAnthropicModelThinking(TypedDict, total=False):
    budget_tokens: int
    """The maximum number of tokens the model can use for extended thinking."""

    type: Literal["enabled", "disabled"]
    """The type of thinking to use."""


class ModelAnthropicModel(TypedDict, total=False):
    model: Required[str]
    """The name of the model."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    provider: Literal["anthropic"]
    """The provider of the model."""

    temperature: float
    """The temperature of the model."""

    thinking: ModelAnthropicModelThinking
    """The thinking configuration for the model."""

    verbosity: Optional[Literal["low", "medium", "high"]]
    """Soft control for how verbose model output should be, used for GPT-5 models."""


ModelGoogleAIModelResponseSchema: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class ModelGoogleAIModelThinkingConfig(TypedDict, total=False):
    include_thoughts: bool
    """Whether to include thoughts in the model's response."""

    thinking_budget: int
    """The thinking budget for the model."""


class ModelGoogleAIModel(TypedDict, total=False):
    model: Required[str]
    """The name of the model."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    provider: Literal["google_ai"]
    """The provider of the model."""

    response_schema: Optional[ModelGoogleAIModelResponseSchema]
    """The response schema for the model."""

    temperature: float
    """The temperature of the model."""

    thinking_config: ModelGoogleAIModelThinkingConfig
    """The thinking configuration for the model."""


ModelGoogleVertexModelResponseSchema: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class ModelGoogleVertexModelThinkingConfig(TypedDict, total=False):
    include_thoughts: bool
    """Whether to include thoughts in the model's response."""

    thinking_budget: int
    """The thinking budget for the model."""


class ModelGoogleVertexModel(TypedDict, total=False):
    model: Required[str]
    """The name of the model."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    provider: Literal["google_vertex"]
    """The provider of the model."""

    response_schema: Optional[ModelGoogleVertexModelResponseSchema]
    """The response schema for the model."""

    temperature: float
    """The temperature of the model."""

    thinking_config: ModelGoogleVertexModelThinkingConfig
    """The thinking configuration for the model."""


ModelAzureModelResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class ModelAzureModel(TypedDict, total=False):
    model: Required[str]
    """The name of the model."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    provider: Literal["azure"]
    """The provider of the model."""

    response_format: Optional[ModelAzureModelResponseFormat]
    """The response format for the model."""

    temperature: float
    """The temperature of the model."""


ModelXaiModelResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class ModelXaiModel(TypedDict, total=False):
    model: Required[str]
    """The name of the model."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    provider: Literal["xai"]
    """The provider of the model."""

    response_format: Optional[ModelXaiModelResponseFormat]
    """The response format for the model."""

    temperature: float
    """The temperature of the model."""


ModelGroqModelResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class ModelGroqModel(TypedDict, total=False):
    model: Required[str]
    """The name of the model."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    provider: Literal["groq"]
    """The provider of the model."""

    response_format: Optional[ModelGroqModelResponseFormat]
    """The response format for the model."""

    temperature: float
    """The temperature of the model."""


ModelDeepseekModelResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class ModelDeepseekModel(TypedDict, total=False):
    model: Required[str]
    """The name of the model."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    provider: Literal["deepseek"]
    """The provider of the model."""

    response_format: Optional[ModelDeepseekModelResponseFormat]
    """The response format for the model."""

    temperature: float
    """The temperature of the model."""


ModelTogetherModelResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class ModelTogetherModel(TypedDict, total=False):
    model: Required[str]
    """The name of the model."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    provider: Literal["together"]
    """The provider of the model."""

    response_format: Optional[ModelTogetherModelResponseFormat]
    """The response format for the model."""

    temperature: float
    """The temperature of the model."""


ModelBedrockModelResponseFormat: TypeAlias = Union[
    TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam
]


class ModelBedrockModel(TypedDict, total=False):
    model: Required[str]
    """The name of the model."""

    max_output_tokens: int
    """The maximum number of tokens the model can generate."""

    provider: Literal["bedrock"]
    """The provider of the model."""

    response_format: Optional[ModelBedrockModelResponseFormat]
    """The response format for the model."""

    temperature: float
    """The temperature of the model."""


Model: TypeAlias = Union[
    str,
    ModelOpenAIModel,
    ModelAnthropicModel,
    ModelGoogleAIModel,
    ModelGoogleVertexModel,
    ModelAzureModel,
    ModelXaiModel,
    ModelGroqModel,
    ModelDeepseekModel,
    ModelTogetherModel,
    ModelBedrockModel,
]

ResponseFormat: TypeAlias = Union[TextResponseFormatParam, JsonSchemaResponseFormatParam, JsonObjectResponseFormatParam]

ToolRule: TypeAlias = Union[
    ChildToolRuleParam,
    InitToolRuleParam,
    TerminalToolRuleParam,
    ConditionalToolRuleParam,
    ContinueToolRuleParam,
    RequiredBeforeExitToolRuleParam,
    MaxCountPerStepToolRuleParam,
    ParentToolRuleParam,
    RequiresApprovalToolRuleParam,
]
