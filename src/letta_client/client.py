from textwrap import dedent
import inspect
import typing

from .base_client import LettaBase, AsyncLettaBase
from .core.request_options import RequestOptions
from .tools.client import ToolsClient as ToolsClientBase
from .types.letta_schemas_tool_tool import LettaSchemasToolTool


# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class Letta(LettaBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tools = ToolsClient(client_wrapper=self._client_wrapper)


class AsyncLetta(AsyncLettaBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tools = ToolsClient(client_wrapper=self._client_wrapper)


class ToolsClient(ToolsClientBase):

    def create_from_function(
        self,
        *,
        function: typing.Callable,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        source_type: typing.Optional[str] = OMIT,
        json_schema: typing.Optional[
            typing.Dict[str, typing.Optional[typing.Any]]
        ] = OMIT,
        return_char_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LettaSchemasToolTool:
        source_code = dedent(inspect.getsource(function))
        return self.create(
            source_code=source_code,
            name=name,
            description=description,
            tags=tags,
            source_type=source_type,
            json_schema=json_schema,
            return_char_limit=return_char_limit,
            request_options=request_options,
        )
