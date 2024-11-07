# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["Health"]


class Health(BaseModel):
    status: str

    version: str
