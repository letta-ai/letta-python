# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["FileProcessingStatus"]

FileProcessingStatus: TypeAlias = Literal["pending", "parsing", "embedding", "completed", "error"]
