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


def _next_cursor_params(*, params: Mapping[str, Any], first_id: str, last_id: str) -> dict[str, str]:
    """Advance cursors in the same traversal direction regardless of sort order.

    - asc + forward traversal: use `after=<last>`
    - desc + forward traversal: use `before=<first>`
    - backward traversal (`before` explicitly set): keep using `before=<first>`
    """
    if params.get("before", False):
        return {"before": first_id}

    if params.get("order") == "desc":
        return {"before": first_id}

    return {"after": last_id}


@runtime_checkable
class ArrayPageItem(Protocol):
    id: Optional[str]


@runtime_checkable
class ObjectPageItem(Protocol):
    id: Optional[str]


@runtime_checkable
class NextFilesPageItem(Protocol):
    id: Optional[str]


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
        items = self.items
        if not items:
            return None

        first_item = cast(Any, items[0])
        last_item = cast(Any, items[-1])
        if not isinstance(first_item, ArrayPageItem) or first_item.id is None:
            # TODO emit warning log
            return None
        if not isinstance(last_item, ArrayPageItem) or last_item.id is None:
            # TODO emit warning log
            return None

        return PageInfo(
            params=_next_cursor_params(
                params=self._options.params,
                first_id=first_item.id,
                last_id=last_item.id,
            )
        )

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
        items = self.items
        if not items:
            return None

        first_item = cast(Any, items[0])
        last_item = cast(Any, items[-1])
        if not isinstance(first_item, ArrayPageItem) or first_item.id is None:
            # TODO emit warning log
            return None
        if not isinstance(last_item, ArrayPageItem) or last_item.id is None:
            # TODO emit warning log
            return None

        return PageInfo(
            params=_next_cursor_params(
                params=self._options.params,
                first_id=first_item.id,
                last_id=last_item.id,
            )
        )

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
        messages = self.messages
        if not messages:
            return None

        first_item = cast(Any, messages[0])
        last_item = cast(Any, messages[-1])
        if not isinstance(first_item, ObjectPageItem) or first_item.id is None:
            # TODO emit warning log
            return None
        if not isinstance(last_item, ObjectPageItem) or last_item.id is None:
            # TODO emit warning log
            return None

        return PageInfo(
            params=_next_cursor_params(
                params=self._options.params,
                first_id=first_item.id,
                last_id=last_item.id,
            )
        )


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
        messages = self.messages
        if not messages:
            return None

        first_item = cast(Any, messages[0])
        last_item = cast(Any, messages[-1])
        if not isinstance(first_item, ObjectPageItem) or first_item.id is None:
            # TODO emit warning log
            return None
        if not isinstance(last_item, ObjectPageItem) or last_item.id is None:
            # TODO emit warning log
            return None

        return PageInfo(
            params=_next_cursor_params(
                params=self._options.params,
                first_id=first_item.id,
                last_id=last_item.id,
            )
        )


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
        files = self.files
        if not files:
            return None

        first_item = cast(Any, files[0])
        last_item = cast(Any, files[-1])
        if not isinstance(first_item, NextFilesPageItem) or first_item.id is None:
            # TODO emit warning log
            return None
        if not isinstance(last_item, NextFilesPageItem) or last_item.id is None:
            # TODO emit warning log
            return None

        return PageInfo(
            params=_next_cursor_params(
                params=self._options.params,
                first_id=first_item.id,
                last_id=last_item.id,
            )
        )


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
        files = self.files
        if not files:
            return None

        first_item = cast(Any, files[0])
        last_item = cast(Any, files[-1])
        if not isinstance(first_item, NextFilesPageItem) or first_item.id is None:
            # TODO emit warning log
            return None
        if not isinstance(last_item, NextFilesPageItem) or last_item.id is None:
            # TODO emit warning log
            return None

        return PageInfo(
            params=_next_cursor_params(
                params=self._options.params,
                first_id=first_item.id,
                last_id=last_item.id,
            )
        )
