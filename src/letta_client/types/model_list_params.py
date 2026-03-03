# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .provider_type import ProviderType
from .provider_category import ProviderCategory

__all__ = ["ModelListParams"]


class ModelListParams(TypedDict, total=False):
    provider_category: Optional[List[ProviderCategory]]

    provider_name: Optional[str]

    provider_type: Optional[ProviderType]

    x_billing_cost_source: Annotated[str, PropertyInfo(alias="x-billing-cost-source")]

    x_billing_customer_id: Annotated[str, PropertyInfo(alias="x-billing-customer-id")]

    x_billing_plan_type: Annotated[str, PropertyInfo(alias="x-billing-plan-type")]
