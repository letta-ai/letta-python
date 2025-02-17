# This file was auto-generated by Fern from our API Definition.

from ...core.unchecked_base_model import UncheckedBaseModel
import typing
from .templates_create_agents_from_template_response_agents_item_memory_blocks_item_limit import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemLimit,
)
from .templates_create_agents_from_template_response_agents_item_memory_blocks_item_name import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemName,
)
from .templates_create_agents_from_template_response_agents_item_memory_blocks_item_is_template import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemIsTemplate,
)
from .templates_create_agents_from_template_response_agents_item_memory_blocks_item_label import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemLabel,
)
from .templates_create_agents_from_template_response_agents_item_memory_blocks_item_description import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemDescription,
)
from .templates_create_agents_from_template_response_agents_item_memory_blocks_item_metadata import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemMetadata,
)
from .templates_create_agents_from_template_response_agents_item_memory_blocks_item_id import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemId,
)
from .templates_create_agents_from_template_response_agents_item_memory_blocks_item_organization_id import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemOrganizationId,
)
from .templates_create_agents_from_template_response_agents_item_memory_blocks_item_created_by_id import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemCreatedById,
)
from .templates_create_agents_from_template_response_agents_item_memory_blocks_item_last_updated_by_id import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemLastUpdatedById,
)
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItem(UncheckedBaseModel):
    value: str
    limit: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemLimit] = None
    name: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemName] = None
    is_template: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemIsTemplate] = None
    label: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemLabel] = None
    description: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemDescription] = None
    metadata: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemMetadata] = None
    id: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemId] = None
    organization_id: typing.Optional[
        TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemOrganizationId
    ] = None
    created_by_id: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemCreatedById] = (
        None
    )
    last_updated_by_id: typing.Optional[
        TemplatesCreateAgentsFromTemplateResponseAgentsItemMemoryBlocksItemLastUpdatedById
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
