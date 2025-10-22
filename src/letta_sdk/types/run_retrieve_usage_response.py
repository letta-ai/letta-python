# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["RunRetrieveUsageResponse", "CompletionTokensDetails", "PromptTokensDetails"]


class CompletionTokensDetails(BaseModel):
    reasoning_tokens: Optional[int] = None


class PromptTokensDetails(BaseModel):
    cached_tokens: Optional[int] = None


class RunRetrieveUsageResponse(BaseModel):
    completion_tokens: Optional[int] = None

    completion_tokens_details: Optional[CompletionTokensDetails] = None

    prompt_tokens: Optional[int] = None

    prompt_tokens_details: Optional[PromptTokensDetails] = None

    total_tokens: Optional[int] = None
