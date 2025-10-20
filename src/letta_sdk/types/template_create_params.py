# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["TemplateCreateParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    agent_id: Required[str]
    """The ID of the agent to use as a template, can be from any project"""

    type: Required[Literal["agent"]]

    name: str
    """Optional custom name for the template.

    If not provided, a random name will be generated.
    """


class Variant1(TypedDict, total=False):
    agent_file: Required[Dict[str, Optional[object]]]
    """
    The agent file to use as a template, this should be a JSON file exported from
    the platform
    """

    type: Required[Literal["agent_file"]]

    name: str
    """Optional custom name for the template.

    If not provided, a random name will be generated.
    """


TemplateCreateParams: TypeAlias = Union[Variant0, Variant1]
