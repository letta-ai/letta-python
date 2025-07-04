# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
import typing
from ..types.provider_category import ProviderCategory
from ..types.provider_type import ProviderType
from ..core.request_options import RequestOptions
from ..types.llm_config import LlmConfig
from ..core.unchecked_base_model import construct_type
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper


class ModelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        provider_category: typing.Optional[typing.Union[ProviderCategory, typing.Sequence[ProviderCategory]]] = None,
        provider_name: typing.Optional[str] = None,
        provider_type: typing.Optional[ProviderType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[LlmConfig]:
        """
        List available LLM models using the asynchronous implementation for improved performance

        Parameters
        ----------
        provider_category : typing.Optional[typing.Union[ProviderCategory, typing.Sequence[ProviderCategory]]]

        provider_name : typing.Optional[str]

        provider_type : typing.Optional[ProviderType]

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
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )
        client.models.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/models/",
            method="GET",
            params={
                "provider_category": provider_category,
                "provider_name": provider_name,
                "provider_type": provider_type,
            },
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncModelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        provider_category: typing.Optional[typing.Union[ProviderCategory, typing.Sequence[ProviderCategory]]] = None,
        provider_name: typing.Optional[str] = None,
        provider_type: typing.Optional[ProviderType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[LlmConfig]:
        """
        List available LLM models using the asynchronous implementation for improved performance

        Parameters
        ----------
        provider_category : typing.Optional[typing.Union[ProviderCategory, typing.Sequence[ProviderCategory]]]

        provider_name : typing.Optional[str]

        provider_type : typing.Optional[ProviderType]

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
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.models.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/models/",
            method="GET",
            params={
                "provider_category": provider_category,
                "provider_name": provider_name,
                "provider_type": provider_type,
            },
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
