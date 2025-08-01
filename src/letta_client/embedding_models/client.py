# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.embedding_config import EmbeddingConfig
from .raw_client import AsyncRawEmbeddingModelsClient, RawEmbeddingModelsClient


class EmbeddingModelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEmbeddingModelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEmbeddingModelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEmbeddingModelsClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[EmbeddingConfig]:
        """
        List available embedding models using the asynchronous implementation for improved performance

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EmbeddingConfig]
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )
        client.embedding_models.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data


class AsyncEmbeddingModelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEmbeddingModelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEmbeddingModelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEmbeddingModelsClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[EmbeddingConfig]:
        """
        List available embedding models using the asynchronous implementation for improved performance

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EmbeddingConfig]
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.embedding_models.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data
