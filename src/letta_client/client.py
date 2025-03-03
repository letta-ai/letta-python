import inspect
import typing
from pydantic import BaseModel, Field, model_validator
from textwrap import dedent
from abc import abstractmethod

from .base_client import AsyncLettaBase, LettaBase
from .core.request_options import RequestOptions
from .tools.client import ToolsClient as ToolsClientBase
from .types.tool import Tool

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


class BaseTool(Tool):
    name: str = Field(..., description="The name of the function.")
    args_schema: typing.Optional[typing.Type[BaseModel]] = Field(default=None, description="The schema for validating the tool's arguments.")

    @abstractmethod
    def run(self, *args, **kwargs) -> typing.Any:
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


class ToolsClient(ToolsClientBase):

    def create_from_function(
        self,
        *,
        func: typing.Callable,
        args_schema: typing.Optional[typing.Type[BaseModel]] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        source_type: typing.Optional[str] = OMIT,
        json_schema: typing.Optional[
            typing.Dict[str, typing.Optional[typing.Any]]
        ] = OMIT,
        return_char_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tool:
        """
        Create a new tool from a callable

        Parameters
        ----------
        func : typing.Callable
            The callable to create the tool from.
        
        args_schema : typing.Optional[typing.Type[BaseModel]]
            The arguments schema of the function, as a Pydantic model.

        description : typing.Optional[str]
            The description of the tool.

        tags : typing.Optional[typing.Sequence[str]]
            Metadata tags.

        source_type : typing.Optional[str]
            The source type of the function.

        json_schema : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The JSON schema of the function (auto-generated from source_code if not provided)

        return_char_limit : typing.Optional[int]
            The maximum number of characters in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tool
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        
        def add_two_numbers(a: int, b: int) -> int:
            return a + b
        
        client.tools.create_from_function(
            func=add_two_numbers,
        )

        class InventoryEntryData(BaseModel):
            data: InventoryEntry
            quantity_change: int

        def manage_inventory(data: InventoryEntry, quantity_change: int) -> bool:
            pass
        
        client.tools.create_from_function(
            func=manage_inventory,
            args_schema=InventoryEntryData,
        )
        """
        source_code = dedent(inspect.getsource(func))
        args_json_schema = args_schema.model_json_schema() if args_schema and args_schema != OMIT else None
        return self.create(
            source_code=source_code,
            args_json_schema=args_json_schema,
            description=description,
            tags=tags,
            source_type=source_type,
            json_schema=json_schema,
            return_char_limit=return_char_limit,
            request_options=request_options,
        )


    def upsert_from_function(
        self,
        *,
        func: typing.Callable,
        args_schema: typing.Optional[typing.Type[BaseModel]] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        source_type: typing.Optional[str] = OMIT,
        json_schema: typing.Optional[
            typing.Dict[str, typing.Optional[typing.Any]]
        ] = OMIT,
        return_char_limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tool:
        """
        Create or update a tool from a callable

        Parameters
        ----------
        func : typing.Callable
            The callable to create or update the tool from.
        
        args_schema : typing.Optional[typing.Type[BaseModel]]
            The arguments schema of the function, as a Pydantic model.

        description : typing.Optional[str]
            The description of the tool.

        tags : typing.Optional[typing.Sequence[str]]
            Metadata tags.

        source_type : typing.Optional[str]
            The source type of the function.

        json_schema : typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
            The JSON schema of the function (auto-generated from source_code if not provided)

        return_char_limit : typing.Optional[int]
            The maximum number of characters in the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tool
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )

        def add_two_numbers(a: int, b: int) -> int:
            return a + b
        
        client.tools.upsert_from_function(
            func=add_two_numbers,
        )

        class InventoryEntryData(BaseModel):
            data: InventoryEntry
            quantity_change: int

        def manage_inventory(data: InventoryEntry, quantity_change: int) -> bool:
            pass
        
        client.tools.upsert_from_function(
            func=manage_inventory,
            args_schema=InventoryEntryData,
        )
        """
        source_code = dedent(inspect.getsource(func))
        args_json_schema = args_schema.model_json_schema() if args_schema and args_schema != OMIT else None
        return self.upsert(
            source_code=source_code,
            args_json_schema=args_json_schema,
            description=description,
            tags=tags,
            source_type=source_type,
            json_schema=json_schema,
            return_char_limit=return_char_limit,
            request_options=request_options,
        )
    
    def add(
        self,
        *,
        tool: BaseTool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Tool:
        """
        Add a tool to Letta from a custom Tool class

        Parameters
        ----------
        tool : BaseTool
            The tool object to be added.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Tool
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )

        class InventoryItem(BaseModel):
            sku: str  # Unique product identifier
            name: str  # Product name
            price: float  # Current price
            category: str  # Product category (e.g., "Electronics", "Clothing")

        class InventoryEntry(BaseModel):
            timestamp: int  # Unix timestamp of the transaction
            item: InventoryItem  # The product being updated
            transaction_id: str  # Unique identifier for this inventory update

        class InventoryEntryData(BaseModel):
            data: InventoryEntry
            quantity_change: int  # Change in quantity (positive for additions, negative for removals)

        class ManageInventoryTool(BaseTool):
            name: str = "manage_inventory"
            args_schema: Type[BaseModel] = InventoryEntryData
            description: str = "Update inventory catalogue with a new data entry"
            tags: List[str] = ["inventory", "shop"]

            def run(self, data: InventoryEntry, quantity_change: int) -> bool:
                '''
                Implementation of the manage_inventory tool
                '''
                print(f"Updated inventory for {data.item.name} with a quantity change of {quantity_change}")
                return True
                
        client.tools.add(
            tool=ManageInventoryTool()
        )
        """
        source_code = tool.get_source_code()
        args_json_schema = tool.args_schema.model_json_schema() if tool.args_schema else None
        return self.upsert(
            source_code=source_code,
            args_json_schema=args_json_schema or OMIT,
            description=tool.description or OMIT,
            tags=tool.tags or OMIT,
            source_type=tool.source_type or OMIT,
            json_schema=tool.json_schema or OMIT,
            return_char_limit=tool.return_char_limit or OMIT,
            request_options=request_options,
        )
