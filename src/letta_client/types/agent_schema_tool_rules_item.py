# This file was auto-generated by Fern from our API Definition.

import typing

from .base_tool_rule_schema import BaseToolRuleSchema
from .child_tool_rule_schema import ChildToolRuleSchema
from .conditional_tool_rule_schema import ConditionalToolRuleSchema
from .max_count_per_step_tool_rule_schema import MaxCountPerStepToolRuleSchema

AgentSchemaToolRulesItem = typing.Union[
    BaseToolRuleSchema, ChildToolRuleSchema, MaxCountPerStepToolRuleSchema, ConditionalToolRuleSchema
]
