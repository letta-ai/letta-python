# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ToolType"]

ToolType: TypeAlias = Literal[
    "custom",
    "letta_core",
    "letta_memory_core",
    "letta_multi_agent_core",
    "letta_sleeptime_core",
    "letta_voice_sleeptime_core",
    "letta_builtin",
    "letta_files_core",
    "external_composio",
    "external_langchain",
    "external_mcp",
]
