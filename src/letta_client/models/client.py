# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
import typing
from ..core.request_options import RequestOptions
from ..types.llm_config import LlmConfig
from ..core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.embedding_config import EmbeddingConfig
from ..core.client_wrapper import AsyncClientWrapper


class ModelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_llms(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[LlmConfig]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LlmConfig]
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.models.list_llms()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/models/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[LlmConfig],
                    construct_type(
                        type_=typing.List[LlmConfig],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_embedding_models(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EmbeddingConfig]:
        """
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
            token="YOUR_TOKEN",
        )
        client.models.list_embedding_models()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/models/embedding",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[EmbeddingConfig],
                    construct_type(
                        type_=typing.List[EmbeddingConfig],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncModelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_llms(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[LlmConfig]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LlmConfig]
            Successful Response

        Examples
        --------
        import asyncio

        from letta_client import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.models.list_llms()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/models/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[LlmConfig],
                    construct_type(
                        type_=typing.List[LlmConfig],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_embedding_models(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EmbeddingConfig]:
        """
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.models.list_embedding_models()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/models/embedding",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[EmbeddingConfig],
                    construct_type(
                        type_=typing.List[EmbeddingConfig],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
