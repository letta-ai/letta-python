# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .agents.text_content_param import TextContentParam
from .agents.image_content_param import ImageContentParam
from .agents.reasoning_content_param import ReasoningContentParam
from .agents.tool_call_content_param import ToolCallContentParam
from .agents.tool_return_content_param import ToolReturnContentParam
from .agents.omitted_reasoning_content_param import OmittedReasoningContentParam
from .agents.redacted_reasoning_content_param import RedactedReasoningContentParam

__all__ = ["LettaMessageContentUnionParam"]

LettaMessageContentUnionParam: TypeAlias = Union[
    TextContentParam,
    ImageContentParam,
    ToolCallContentParam,
    ToolReturnContentParam,
    ReasoningContentParam,
    RedactedReasoningContentParam,
    OmittedReasoningContentParam,
]
