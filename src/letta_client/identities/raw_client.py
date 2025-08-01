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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.identity import Identity
from ..types.identity_property import IdentityProperty
from ..types.identity_type import IdentityType

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawIdentitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        name: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        identifier_key: typing.Optional[str] = None,
        identity_type: typing.Optional[IdentityType] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Identity]]:
        """
        Get a list of all identities in the database

        Parameters
        ----------
        name : typing.Optional[str]

        project_id : typing.Optional[str]

        identifier_key : typing.Optional[str]

        identity_type : typing.Optional[IdentityType]

        before : typing.Optional[str]

        after : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Identity]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/identities/",
            method="GET",
            params={
                "name": name,
                "project_id": project_id,
                "identifier_key": identifier_key,
                "identity_type": identity_type,
                "before": before,
                "after": after,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Identity],
                    construct_type(
                        type_=typing.List[Identity],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
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
        identifier_key: str,
        name: str,
        identity_type: IdentityType,
        project_id: typing.Optional[str] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Identity]:
        """
        Parameters
        ----------
        identifier_key : str
            External, user-generated identifier key of the identity.

        name : str
            The name of the identity.

        identity_type : IdentityType
            The type of the identity.

        project_id : typing.Optional[str]
            The project id of the identity, if applicable.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Identity]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/identities/",
            method="POST",
            json={
                "identifier_key": identifier_key,
                "name": name,
                "identity_type": identity_type,
                "project_id": project_id,
                "agent_ids": agent_ids,
                "block_ids": block_ids,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=typing.Sequence[IdentityProperty], direction="write"
                ),
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
                    Identity,
                    construct_type(
                        type_=Identity,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def upsert(
        self,
        *,
        identifier_key: str,
        name: str,
        identity_type: IdentityType,
        project_id: typing.Optional[str] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Identity]:
        """
        Parameters
        ----------
        identifier_key : str
            External, user-generated identifier key of the identity.

        name : str
            The name of the identity.

        identity_type : IdentityType
            The type of the identity.

        project_id : typing.Optional[str]
            The project id of the identity, if applicable.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Identity]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/identities/",
            method="PUT",
            json={
                "identifier_key": identifier_key,
                "name": name,
                "identity_type": identity_type,
                "project_id": project_id,
                "agent_ids": agent_ids,
                "block_ids": block_ids,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=typing.Sequence[IdentityProperty], direction="write"
                ),
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
                    Identity,
                    construct_type(
                        type_=Identity,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def count(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[int]:
        """
        Get count of all identities for a user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[int]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/identities/count",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    construct_type(
                        type_=int,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve(
        self, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Identity]:
        """
        Parameters
        ----------
        identity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Identity]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/identities/{jsonable_encoder(identity_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Identity,
                    construct_type(
                        type_=Identity,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.Any]]:
        """
        Delete an identity by its identifier key

        Parameters
        ----------
        identity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.Any]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/identities/{jsonable_encoder(identity_id)}",
            method="DELETE",
            request_options=request_options,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def modify(
        self,
        identity_id: str,
        *,
        identifier_key: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        identity_type: typing.Optional[IdentityType] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Identity]:
        """
        Parameters
        ----------
        identity_id : str

        identifier_key : typing.Optional[str]
            External, user-generated identifier key of the identity.

        name : typing.Optional[str]
            The name of the identity.

        identity_type : typing.Optional[IdentityType]
            The type of the identity.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Identity]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/identities/{jsonable_encoder(identity_id)}",
            method="PATCH",
            json={
                "identifier_key": identifier_key,
                "name": name,
                "identity_type": identity_type,
                "agent_ids": agent_ids,
                "block_ids": block_ids,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=typing.Sequence[IdentityProperty], direction="write"
                ),
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
                    Identity,
                    construct_type(
                        type_=Identity,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawIdentitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        name: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        identifier_key: typing.Optional[str] = None,
        identity_type: typing.Optional[IdentityType] = None,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Identity]]:
        """
        Get a list of all identities in the database

        Parameters
        ----------
        name : typing.Optional[str]

        project_id : typing.Optional[str]

        identifier_key : typing.Optional[str]

        identity_type : typing.Optional[IdentityType]

        before : typing.Optional[str]

        after : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Identity]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/identities/",
            method="GET",
            params={
                "name": name,
                "project_id": project_id,
                "identifier_key": identifier_key,
                "identity_type": identity_type,
                "before": before,
                "after": after,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Identity],
                    construct_type(
                        type_=typing.List[Identity],  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
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
        identifier_key: str,
        name: str,
        identity_type: IdentityType,
        project_id: typing.Optional[str] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Identity]:
        """
        Parameters
        ----------
        identifier_key : str
            External, user-generated identifier key of the identity.

        name : str
            The name of the identity.

        identity_type : IdentityType
            The type of the identity.

        project_id : typing.Optional[str]
            The project id of the identity, if applicable.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Identity]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/identities/",
            method="POST",
            json={
                "identifier_key": identifier_key,
                "name": name,
                "identity_type": identity_type,
                "project_id": project_id,
                "agent_ids": agent_ids,
                "block_ids": block_ids,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=typing.Sequence[IdentityProperty], direction="write"
                ),
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
                    Identity,
                    construct_type(
                        type_=Identity,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def upsert(
        self,
        *,
        identifier_key: str,
        name: str,
        identity_type: IdentityType,
        project_id: typing.Optional[str] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Identity]:
        """
        Parameters
        ----------
        identifier_key : str
            External, user-generated identifier key of the identity.

        name : str
            The name of the identity.

        identity_type : IdentityType
            The type of the identity.

        project_id : typing.Optional[str]
            The project id of the identity, if applicable.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Identity]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/identities/",
            method="PUT",
            json={
                "identifier_key": identifier_key,
                "name": name,
                "identity_type": identity_type,
                "project_id": project_id,
                "agent_ids": agent_ids,
                "block_ids": block_ids,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=typing.Sequence[IdentityProperty], direction="write"
                ),
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
                    Identity,
                    construct_type(
                        type_=Identity,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def count(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[int]:
        """
        Get count of all identities for a user

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[int]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/identities/count",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    construct_type(
                        type_=int,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve(
        self, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Identity]:
        """
        Parameters
        ----------
        identity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Identity]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/identities/{jsonable_encoder(identity_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Identity,
                    construct_type(
                        type_=Identity,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, identity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.Any]]:
        """
        Delete an identity by its identifier key

        Parameters
        ----------
        identity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.Any]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/identities/{jsonable_encoder(identity_id)}",
            method="DELETE",
            request_options=request_options,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def modify(
        self,
        identity_id: str,
        *,
        identifier_key: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        identity_type: typing.Optional[IdentityType] = OMIT,
        agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        block_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        properties: typing.Optional[typing.Sequence[IdentityProperty]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Identity]:
        """
        Parameters
        ----------
        identity_id : str

        identifier_key : typing.Optional[str]
            External, user-generated identifier key of the identity.

        name : typing.Optional[str]
            The name of the identity.

        identity_type : typing.Optional[IdentityType]
            The type of the identity.

        agent_ids : typing.Optional[typing.Sequence[str]]
            The agent ids that are associated with the identity.

        block_ids : typing.Optional[typing.Sequence[str]]
            The IDs of the blocks associated with the identity.

        properties : typing.Optional[typing.Sequence[IdentityProperty]]
            List of properties associated with the identity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Identity]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/identities/{jsonable_encoder(identity_id)}",
            method="PATCH",
            json={
                "identifier_key": identifier_key,
                "name": name,
                "identity_type": identity_type,
                "agent_ids": agent_ids,
                "block_ids": block_ids,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=typing.Sequence[IdentityProperty], direction="write"
                ),
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
                    Identity,
                    construct_type(
                        type_=Identity,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
