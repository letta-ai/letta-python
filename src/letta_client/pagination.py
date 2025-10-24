# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Type, Generic, Mapping, TypeVar, Optional, cast
from typing_extensions import Protocol, override, runtime_checkable

from httpx import Response

from ._utils import is_mapping
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncArrayPage",
    "AsyncArrayPage",
    "SyncObjectPage",
    "AsyncObjectPage",
    "SyncNextFilesPage",
    "AsyncNextFilesPage",
]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)

_T = TypeVar("_T")


@runtime_checkable
class ArrayPageItem(Protocol):
    id: Optional[str]


@runtime_checkable
class ObjectPageItem(Protocol):
    id: Optional[str]


@runtime_checkable
class NextFilesPageItem(Protocol):
    next_cursor: Optional[str]


class SyncArrayPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("before", False)

        items = self.items
        if not items:
            return None

        if is_forwards:
            item = cast(Any, items[-1])
            if not isinstance(item, ArrayPageItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"after": item.id})
        else:
            item = cast(Any, self.items[0])
            if not isinstance(item, ArrayPageItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"before": item.id})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class AsyncArrayPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("before", False)

        items = self.items
        if not items:
            return None

        if is_forwards:
            item = cast(Any, items[-1])
            if not isinstance(item, ArrayPageItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"after": item.id})
        else:
            item = cast(Any, self.items[0])
            if not isinstance(item, ArrayPageItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"before": item.id})

    @classmethod
    def build(cls: Type[_BaseModelT], *, response: Response, data: object) -> _BaseModelT:  # noqa: ARG003
        return cls.construct(
            None,
            **{
                **(cast(Mapping[str, Any], data) if is_mapping(data) else {"items": data}),
            },
        )


class SyncObjectPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    messages: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        messages = self.messages
        if not messages:
            return []
        return messages

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("before", False)

        messages = self.messages
        if not messages:
            return None

        if is_forwards:
            item = cast(Any, messages[-1])
            if not isinstance(item, ObjectPageItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"after": item.id})
        else:
            item = cast(Any, self.messages[0])
            if not isinstance(item, ObjectPageItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"before": item.id})


class AsyncObjectPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    messages: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        messages = self.messages
        if not messages:
            return []
        return messages

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("before", False)

        messages = self.messages
        if not messages:
            return None

        if is_forwards:
            item = cast(Any, messages[-1])
            if not isinstance(item, ObjectPageItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"after": item.id})
        else:
            item = cast(Any, self.messages[0])
            if not isinstance(item, ObjectPageItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"before": item.id})


class SyncNextFilesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    files: List[_T]
    next_cursor: Optional[str] = None
    has_more: Optional[bool] = None

    @override
    def _get_page_items(self) -> List[_T]:
        files = self.files
        if not files:
            return []
        return files

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("before", False)

        files = self.files
        if not files:
            return None

        if is_forwards:
            item = cast(Any, files[-1])
            if not isinstance(item, NextFilesPageItem) or item.next_cursor is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"after": item.next_cursor})
        else:
            item = cast(Any, self.files[0])
            if not isinstance(item, NextFilesPageItem) or item.next_cursor is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"before": item.next_cursor})


class AsyncNextFilesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    files: List[_T]
    next_cursor: Optional[str] = None
    has_more: Optional[bool] = None

    @override
    def _get_page_items(self) -> List[_T]:
        files = self.files
        if not files:
            return []
        return files

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("before", False)

        files = self.files
        if not files:
            return None

        if is_forwards:
            item = cast(Any, files[-1])
            if not isinstance(item, NextFilesPageItem) or item.next_cursor is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"after": item.next_cursor})
        else:
            item = cast(Any, self.files[0])
            if not isinstance(item, NextFilesPageItem) or item.next_cursor is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"before": item.next_cursor})
