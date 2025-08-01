# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .pip_requirement import PipRequirement


class LocalSandboxConfig(UncheckedBaseModel):
    sandbox_dir: typing.Optional[str] = pydantic.Field(default=None)
    """
    Directory for the sandbox environment.
    """

    use_venv: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not to use the venv, or run directly in the same run loop.
    """

    venv_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name for the venv in the sandbox directory. We first search for an existing venv with this name, otherwise, we make it from the requirements.txt.
    """

    pip_requirements: typing.Optional[typing.List[PipRequirement]] = pydantic.Field(default=None)
    """
    List of pip packages to install with mandatory name and optional version following semantic versioning. This only is considered when use_venv is True.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
