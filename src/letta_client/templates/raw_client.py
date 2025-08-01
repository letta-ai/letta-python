# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.request_options import RequestOptions
from ..core.unchecked_base_model import construct_type
from .types.templates_list_response import TemplatesListResponse


class RawTemplatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        offset: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TemplatesListResponse]:
        """
        List all templates

        Parameters
        ----------
        offset : typing.Optional[str]

        limit : typing.Optional[str]

        name : typing.Optional[str]

        project_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TemplatesListResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/templates",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
                "name": name,
                "projectId": project_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TemplatesListResponse,
                    construct_type(
                        type_=TemplatesListResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTemplatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        offset: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TemplatesListResponse]:
        """
        List all templates

        Parameters
        ----------
        offset : typing.Optional[str]

        limit : typing.Optional[str]

        name : typing.Optional[str]

        project_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TemplatesListResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/templates",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
                "name": name,
                "projectId": project_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TemplatesListResponse,
                    construct_type(
                        type_=TemplatesListResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
