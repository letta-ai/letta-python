# This file was auto-generated by Fern from our API Definition.

import typing
from .agents_search_deployed_agents_request_search_item_zero import AgentsSearchDeployedAgentsRequestSearchItemZero
from .agents_search_deployed_agents_request_search_item_operator import (
    AgentsSearchDeployedAgentsRequestSearchItemOperator,
)
from .agents_search_deployed_agents_request_search_item_direction import (
    AgentsSearchDeployedAgentsRequestSearchItemDirection,
)

AgentsSearchDeployedAgentsRequestSearchItem = typing.Union[
    AgentsSearchDeployedAgentsRequestSearchItemZero,
    AgentsSearchDeployedAgentsRequestSearchItemOperator,
    AgentsSearchDeployedAgentsRequestSearchItemDirection,
]