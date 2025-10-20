# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ManagerType"]

ManagerType: TypeAlias = Literal["round_robin", "supervisor", "dynamic", "sleeptime", "voice_sleeptime", "swarm"]
