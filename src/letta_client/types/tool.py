# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from abc import abstractmethod
from textwrap import dedent
import inspect
import typing

from pydantic import Field as FieldInfo, Field, model_validator

from .._models import BaseModel
from .tool_type import ToolType
from .npm_requirement import NpmRequirement
from .pip_requirement import PipRequirement

__all__ = ["Tool", "BaseTool"]


class Tool(BaseModel):
    id: Optional[str] = None
    """The human-friendly ID of the Tool"""

    args_json_schema: Optional[Dict[str, object]] = None
    """The args JSON schema of the function."""

    created_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    default_requires_approval: Optional[bool] = None
    """Default value for whether or not executing this tool requires approval."""

    description: Optional[str] = None
    """The description of the tool."""

    enable_parallel_execution: Optional[bool] = None
    """
    If set to True, then this tool will potentially be executed concurrently with
    other tools. Default False.
    """

    json_schema: Optional[Dict[str, object]] = None
    """The JSON schema of the function."""

    last_updated_by_id: Optional[str] = None
    """The id of the user that made this Tool."""

    metadata: Optional[Dict[str, object]] = FieldInfo(alias="metadata_", default=None)
    """A dictionary of additional metadata for the tool."""

    name: Optional[str] = None
    """The name of the function."""

    npm_requirements: Optional[List[NpmRequirement]] = None
    """Optional list of npm packages required by this tool."""

    pip_requirements: Optional[List[PipRequirement]] = None
    """Optional list of pip packages required by this tool."""

    return_char_limit: Optional[int] = None
    """The maximum number of characters in the response."""

    source_code: Optional[str] = None
    """The source code of the function."""

    source_type: Optional[str] = None
    """The type of the source code."""

    tags: Optional[List[str]] = None
    """Metadata tags."""

    tool_type: Optional[ToolType] = None
    """The type of the tool."""


class BaseTool(Tool):
    name: Optional[str] = Field(default=None, description="The name of the function.")
    args_schema: typing.Optional[typing.Type[BaseModel]] = Field(default=None, description="The schema for validating the tool's arguments.")

    @abstractmethod
    def run(self, *args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        """
        Execute the tool with the provided arguments.

        Parameters
        ----------
        self
            The instance of the tool
        *args
            Positional arguments to pass to the tool.
        **kwargs
            Keyword arguments to pass to the tool.

        Returns
        -------
        typing.Any
            The result of executing the tool.
        """
        pass


    @model_validator(mode="after")
    def no_self_in_run_source(self) -> "BaseTool":
        """
        Validate that the provided implementation does not reference `self` in the
        `run` method implementation.

        This check is performed after the model is created, so `self` is guaranteed
        to be set.

        If `self` is found in the source code of the `run` method, a `ValueError` is
        raised with a message pointing to the line and value of the offending code.
        """
        source_code = self.get_source_code()
        if "self." in source_code:
            raise_on_line, line_value = None, None
            for i, line in enumerate(source_code.splitlines()):
                if "self." in line:
                    raise_on_line, line_value = i+1, line
                    break;
            raise ValueError(
                f"Detected reference to 'self' in line {raise_on_line} of implementation, " +
                f"which is not allowed:\n\n{line_value}\n\n" +
                f"Please pass in the arguments directly to run() instead.")
        return self


    def get_source_code(self) -> str:
        """
        Get the source code of the `run` method, which will be executed in an agent step.

        Returns
        -------
        str
            The source code of the tool.
        """
        source_code = dedent(inspect.getsource(self.run))

        # replace tool name
        source_code = source_code.replace("def run", f"def {self.name}")

        # remove self, handling several cases
        source_code_lines = source_code.splitlines()
        if "self" in source_code_lines[0]:
            # def run(self, ...): or def run (self,): or def run(self):
            source_code_lines[0] = source_code_lines[0].replace("self, ", "").replace("self,", "").replace("self", "")
        else:
            maybe_line_to_delete = None
            for i, line in enumerate(source_code_lines):
                if line.strip() == "self" or line.strip() == "self,":
                    # def run(
                    #   self,
                    #   ...
                    # ):
                    maybe_line_to_delete = i
                    break
                elif line.strip().startswith("self"):
                    # def run(
                    #   self, ...
                    # ):
                    source_code_lines[i] = line.replace("self, ", "").replace("self,", "").replace("self", "")
                    break
            if maybe_line_to_delete is not None:
                del source_code_lines[maybe_line_to_delete]
                if maybe_line_to_delete == 1 and source_code_lines[0].strip()[-1] == "(" and source_code_lines[1].strip()[0] == ")":
                    # def run(
                    #   self
                    # ):
                    source_code_lines[0] = source_code_lines[0].strip() + source_code_lines[1].strip()
                    del source_code_lines[1]

        source_code = "\n".join(source_code_lines)
        return source_code
