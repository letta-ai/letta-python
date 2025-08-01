# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.unchecked_base_model import construct_type
from ..errors.bad_request_error import BadRequestError
from .types.client_side_access_tokens_create_request_policy_item import ClientSideAccessTokensCreateRequestPolicyItem
from .types.client_side_access_tokens_create_response import ClientSideAccessTokensCreateResponse
from .types.client_side_access_tokens_list_client_side_access_tokens_response import (
    ClientSideAccessTokensListClientSideAccessTokensResponse,
)

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawClientSideAccessTokensClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def client_side_access_tokens_list_client_side_access_tokens(
        self,
        *,
        agent_id: typing.Optional[str] = None,
        offset: typing.Optional[float] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ClientSideAccessTokensListClientSideAccessTokensResponse]:
        """
        List all client side access tokens for the current account. This is only available for cloud users.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            The agent ID to filter tokens by. If provided, only tokens for this agent will be returned.

        offset : typing.Optional[float]
            The offset for pagination. Defaults to 0.

        limit : typing.Optional[float]
            The number of tokens to return per page. Defaults to 10.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ClientSideAccessTokensListClientSideAccessTokensResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/client-side-access-tokens",
            method="GET",
            params={
                "agentId": agent_id,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClientSideAccessTokensListClientSideAccessTokensResponse,
                    construct_type(
                        type_=ClientSideAccessTokensListClientSideAccessTokensResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self,
        *,
        policy: typing.Sequence[ClientSideAccessTokensCreateRequestPolicyItem],
        hostname: str,
        expires_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ClientSideAccessTokensCreateResponse]:
        """
        Create a new client side access token with the specified configuration.

        Parameters
        ----------
        policy : typing.Sequence[ClientSideAccessTokensCreateRequestPolicyItem]

        hostname : str
            The hostname of the client side application. Please specify the full URL including the protocol (http or https).

        expires_at : typing.Optional[str]
            The expiration date of the token. If not provided, the token will expire in 5 minutes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ClientSideAccessTokensCreateResponse]
            201
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/client-side-access-tokens",
            method="POST",
            json={
                "policy": convert_and_respect_annotation_metadata(
                    object_=policy,
                    annotation=typing.Sequence[ClientSideAccessTokensCreateRequestPolicyItem],
                    direction="write",
                ),
                "hostname": hostname,
                "expires_at": expires_at,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClientSideAccessTokensCreateResponse,
                    construct_type(
                        type_=ClientSideAccessTokensCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self,
        token: str,
        *,
        request: typing.Optional[typing.Any] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Delete a client side access token.

        Parameters
        ----------
        token : str
            The access token to delete

        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            204
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/client-side-access-tokens/{jsonable_encoder(token)}",
            method="DELETE",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    construct_type(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawClientSideAccessTokensClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def client_side_access_tokens_list_client_side_access_tokens(
        self,
        *,
        agent_id: typing.Optional[str] = None,
        offset: typing.Optional[float] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ClientSideAccessTokensListClientSideAccessTokensResponse]:
        """
        List all client side access tokens for the current account. This is only available for cloud users.

        Parameters
        ----------
        agent_id : typing.Optional[str]
            The agent ID to filter tokens by. If provided, only tokens for this agent will be returned.

        offset : typing.Optional[float]
            The offset for pagination. Defaults to 0.

        limit : typing.Optional[float]
            The number of tokens to return per page. Defaults to 10.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ClientSideAccessTokensListClientSideAccessTokensResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/client-side-access-tokens",
            method="GET",
            params={
                "agentId": agent_id,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClientSideAccessTokensListClientSideAccessTokensResponse,
                    construct_type(
                        type_=ClientSideAccessTokensListClientSideAccessTokensResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self,
        *,
        policy: typing.Sequence[ClientSideAccessTokensCreateRequestPolicyItem],
        hostname: str,
        expires_at: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ClientSideAccessTokensCreateResponse]:
        """
        Create a new client side access token with the specified configuration.

        Parameters
        ----------
        policy : typing.Sequence[ClientSideAccessTokensCreateRequestPolicyItem]

        hostname : str
            The hostname of the client side application. Please specify the full URL including the protocol (http or https).

        expires_at : typing.Optional[str]
            The expiration date of the token. If not provided, the token will expire in 5 minutes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ClientSideAccessTokensCreateResponse]
            201
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/client-side-access-tokens",
            method="POST",
            json={
                "policy": convert_and_respect_annotation_metadata(
                    object_=policy,
                    annotation=typing.Sequence[ClientSideAccessTokensCreateRequestPolicyItem],
                    direction="write",
                ),
                "hostname": hostname,
                "expires_at": expires_at,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ClientSideAccessTokensCreateResponse,
                    construct_type(
                        type_=ClientSideAccessTokensCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self,
        token: str,
        *,
        request: typing.Optional[typing.Any] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Delete a client side access token.

        Parameters
        ----------
        token : str
            The access token to delete

        request : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            204
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/client-side-access-tokens/{jsonable_encoder(token)}",
            method="DELETE",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.Any],
                    construct_type(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        construct_type(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
