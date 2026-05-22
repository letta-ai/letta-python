# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UsageRetrieveResponse", "CompletionTokensDetails", "PromptTokensDetails"]


class CompletionTokensDetails(BaseModel):
    reasoning_tokens: Optional[int] = None


class PromptTokensDetails(BaseModel):
    cache_creation_tokens: Optional[int] = None

    cache_read_tokens: Optional[int] = None

    cached_tokens: Optional[int] = None


class UsageRetrieveResponse(BaseModel):
    completion_tokens: Optional[int] = None

    completion_tokens_details: Optional[CompletionTokensDetails] = None

    prompt_tokens: Optional[int] = None

    prompt_tokens_details: Optional[PromptTokensDetails] = None

    total_tokens: Optional[int] = None
