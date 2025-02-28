import inspect
import typing
from pydantic import BaseModel, Field
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

    @staticmethod
    @abstractmethod
    def run(**kwargs) -> typing.Any:
        """
        Execute the tool with the provided arguments.

        Parameters
        ----------
        **kwargs
            Keyword arguments to pass to the tool.

        Returns
        -------
        typing.Any
            The result of executing the tool.
        """
        pass


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
        args_json_schema = args_schema.model_json_schema() if args_schema else None
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
        args_json_schema = args_schema.model_json_schema() if args_schema else None
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

            def run(data: InventoryEntry, quantity_change: int) -> bool:
                '''
                Implementation of the manage_inventory tool
                '''
                # implementation

                print(f"Updated inventory for {data.item.name} with a quantity change of {quantity_change}")
                return True
                
        client.tools.add(
            tool=ManageInventoryTool
        )
        """
        run_source = dedent(inspect.getsource(tool.run))
        source_code = run_source.replace("def run", f"def {tool.name}")
        args_json_schema = tool.args_schema.model_json_schema() if tool.args_schema else tool.args_json_schema
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
