# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .batch_job import BatchJob

__all__ = ["BatchListResponse"]

BatchListResponse: TypeAlias = List[BatchJob]
