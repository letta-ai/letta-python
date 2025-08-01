# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.step import Step
from .feedback.client import AsyncFeedbackClient, FeedbackClient
from .raw_client import AsyncRawStepsClient, RawStepsClient
from .types.steps_list_request_feedback import StepsListRequestFeedback


class StepsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStepsClient(client_wrapper=client_wrapper)
        self.feedback = FeedbackClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStepsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStepsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        model: typing.Optional[str] = None,
        agent_id: typing.Optional[str] = None,
        trace_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        feedback: typing.Optional[StepsListRequestFeedback] = None,
        has_feedback: typing.Optional[bool] = None,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Step]:
        """
        List steps with optional pagination and date filters.
        Dates should be provided in ISO 8601 format (e.g. 2025-01-29T15:01:19-08:00)

        Parameters
        ----------
        before : typing.Optional[str]
            Return steps before this step ID

        after : typing.Optional[str]
            Return steps after this step ID

        limit : typing.Optional[int]
            Maximum number of steps to return

        order : typing.Optional[str]
            Sort order (asc or desc)

        start_date : typing.Optional[str]
            Return steps after this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")

        end_date : typing.Optional[str]
            Return steps before this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")

        model : typing.Optional[str]
            Filter by the name of the model used for the step

        agent_id : typing.Optional[str]
            Filter by the ID of the agent that performed the step

        trace_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by trace ids returned by the server

        feedback : typing.Optional[StepsListRequestFeedback]
            Filter by feedback

        has_feedback : typing.Optional[bool]
            Filter by whether steps have feedback (true) or not (false)

        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by tags

        project_id : typing.Optional[str]
            Filter by the project ID that is associated with the step (cloud only).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Step]
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )
        client.steps.list()
        """
        _response = self._raw_client.list(
            before=before,
            after=after,
            limit=limit,
            order=order,
            start_date=start_date,
            end_date=end_date,
            model=model,
            agent_id=agent_id,
            trace_ids=trace_ids,
            feedback=feedback,
            has_feedback=has_feedback,
            tags=tags,
            project_id=project_id,
            request_options=request_options,
        )
        return _response.data

    def retrieve(self, step_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Step:
        """
        Get a step by ID.

        Parameters
        ----------
        step_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Step
            Successful Response

        Examples
        --------
        from letta_client import Letta

        client = Letta(
            project="YOUR_PROJECT",
            token="YOUR_TOKEN",
        )
        client.steps.retrieve(
            step_id="step_id",
        )
        """
        _response = self._raw_client.retrieve(step_id, request_options=request_options)
        return _response.data


class AsyncStepsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStepsClient(client_wrapper=client_wrapper)
        self.feedback = AsyncFeedbackClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStepsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStepsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        before: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[str] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        model: typing.Optional[str] = None,
        agent_id: typing.Optional[str] = None,
        trace_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        feedback: typing.Optional[StepsListRequestFeedback] = None,
        has_feedback: typing.Optional[bool] = None,
        tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Step]:
        """
        List steps with optional pagination and date filters.
        Dates should be provided in ISO 8601 format (e.g. 2025-01-29T15:01:19-08:00)

        Parameters
        ----------
        before : typing.Optional[str]
            Return steps before this step ID

        after : typing.Optional[str]
            Return steps after this step ID

        limit : typing.Optional[int]
            Maximum number of steps to return

        order : typing.Optional[str]
            Sort order (asc or desc)

        start_date : typing.Optional[str]
            Return steps after this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")

        end_date : typing.Optional[str]
            Return steps before this ISO datetime (e.g. "2025-01-29T15:01:19-08:00")

        model : typing.Optional[str]
            Filter by the name of the model used for the step

        agent_id : typing.Optional[str]
            Filter by the ID of the agent that performed the step

        trace_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by trace ids returned by the server

        feedback : typing.Optional[StepsListRequestFeedback]
            Filter by feedback

        has_feedback : typing.Optional[bool]
            Filter by whether steps have feedback (true) or not (false)

        tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Filter by tags

        project_id : typing.Optional[str]
            Filter by the project ID that is associated with the step (cloud only).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Step]
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
            await client.steps.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            before=before,
            after=after,
            limit=limit,
            order=order,
            start_date=start_date,
            end_date=end_date,
            model=model,
            agent_id=agent_id,
            trace_ids=trace_ids,
            feedback=feedback,
            has_feedback=has_feedback,
            tags=tags,
            project_id=project_id,
            request_options=request_options,
        )
        return _response.data

    async def retrieve(self, step_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Step:
        """
        Get a step by ID.

        Parameters
        ----------
        step_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Step
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
            await client.steps.retrieve(
                step_id="step_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve(step_id, request_options=request_options)
        return _response.data
