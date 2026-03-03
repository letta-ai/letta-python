# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .create_sse_mcp_server_param import CreateSseMcpServerParam
from .create_stdio_mcp_server_param import CreateStdioMcpServerParam
from .create_streamable_http_mcp_server_param import CreateStreamableHTTPMcpServerParam

__all__ = ["McpServerCreateParams", "Config"]


class McpServerCreateParams(TypedDict, total=False):
    config: Required[Config]
    """The MCP server configuration (Stdio, SSE, or Streamable HTTP)"""

    server_name: Required[str]
    """The name of the MCP server"""

    x_billing_cost_source: Annotated[str, PropertyInfo(alias="x-billing-cost-source")]

    x_billing_customer_id: Annotated[str, PropertyInfo(alias="x-billing-customer-id")]

    x_billing_plan_type: Annotated[str, PropertyInfo(alias="x-billing-plan-type")]


Config: TypeAlias = Union[CreateStdioMcpServerParam, CreateSseMcpServerParam, CreateStreamableHTTPMcpServerParam]
