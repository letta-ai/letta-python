# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["AgentType"]

AgentType: TypeAlias = Literal[
    "memgpt_agent",
    "memgpt_v2_agent",
    "letta_v1_agent",
    "react_agent",
    "workflow_agent",
    "split_thread_agent",
    "sleeptime_agent",
    "voice_convo_agent",
    "voice_sleeptime_agent",
]
