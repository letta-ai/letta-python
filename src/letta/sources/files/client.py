# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ... import core
from ...core.request_options import RequestOptions
from ...types.job import Job
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import parse_obj_as
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...types.file_metadata import FileMetadata
from ...core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class FilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def upload(
        self, source_id: str, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> Job:
        """
        Upload a file to a data source.

        Parameters
        ----------
        source_id : str

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            Successful Response

        Examples
        --------
        from letta import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.sources.files.upload(
            source_id="source_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/sources/{jsonable_encoder(source_id)}/upload",
            method="POST",
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Job,
                    parse_obj_as(
                        type_=Job,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(
        self,
        source_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FileMetadata]:
        """
        List paginated files associated with a data source.

        Parameters
        ----------
        source_id : str

        limit : typing.Optional[int]
            Number of files to return

        cursor : typing.Optional[str]
            Pagination cursor to fetch the next set of results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FileMetadata]
            Successful Response

        Examples
        --------
        from letta import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.sources.files.list(
            source_id="source_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/sources/{jsonable_encoder(source_id)}/files",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[FileMetadata],
                    parse_obj_as(
                        type_=typing.List[FileMetadata],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, source_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a data source.

        Parameters
        ----------
        source_id : str

        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from letta import Letta

        client = Letta(
            token="YOUR_TOKEN",
        )
        client.sources.files.delete(
            source_id="source_id",
            file_id="file_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/sources/{jsonable_encoder(source_id)}/{jsonable_encoder(file_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def upload(
        self, source_id: str, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> Job:
        """
        Upload a file to a data source.

        Parameters
        ----------
        source_id : str

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            Successful Response

        Examples
        --------
        import asyncio

        from letta import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sources.files.upload(
                source_id="source_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/sources/{jsonable_encoder(source_id)}/upload",
            method="POST",
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Job,
                    parse_obj_as(
                        type_=Job,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(
        self,
        source_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FileMetadata]:
        """
        List paginated files associated with a data source.

        Parameters
        ----------
        source_id : str

        limit : typing.Optional[int]
            Number of files to return

        cursor : typing.Optional[str]
            Pagination cursor to fetch the next set of results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FileMetadata]
            Successful Response

        Examples
        --------
        import asyncio

        from letta import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sources.files.list(
                source_id="source_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/sources/{jsonable_encoder(source_id)}/files",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[FileMetadata],
                    parse_obj_as(
                        type_=typing.List[FileMetadata],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self, source_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a data source.

        Parameters
        ----------
        source_id : str

        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from letta import AsyncLetta

        client = AsyncLetta(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.sources.files.delete(
                source_id="source_id",
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/sources/{jsonable_encoder(source_id)}/{jsonable_encoder(file_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)