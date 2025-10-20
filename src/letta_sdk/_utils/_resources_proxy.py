from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `letta_sdk.resources` module.

    This is used so that we can lazily import `letta_sdk.resources` only when
    needed *and* so that users can just import `letta_sdk` and reference `letta_sdk.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("letta_sdk.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
