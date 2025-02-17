# This file was auto-generated by Fern from our API Definition.

from ...core.unchecked_base_model import UncheckedBaseModel
import typing
from .templates_create_agents_from_template_response_agents_item_tools_item_tool_type import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemToolType,
)
from .templates_create_agents_from_template_response_agents_item_tools_item_description import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemDescription,
)
from .templates_create_agents_from_template_response_agents_item_tools_item_source_type import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemSourceType,
)
from .templates_create_agents_from_template_response_agents_item_tools_item_organization_id import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemOrganizationId,
)
from .templates_create_agents_from_template_response_agents_item_tools_item_name import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemName,
)
from .templates_create_agents_from_template_response_agents_item_tools_item_source_code import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemSourceCode,
)
from .templates_create_agents_from_template_response_agents_item_tools_item_json_schema import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemJsonSchema,
)
from .templates_create_agents_from_template_response_agents_item_tools_item_created_by_id import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemCreatedById,
)
from .templates_create_agents_from_template_response_agents_item_tools_item_last_updated_by_id import (
    TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemLastUpdatedById,
)
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItem(UncheckedBaseModel):
    id: typing.Optional[str] = None
    tool_type: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemToolType] = None
    description: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemDescription] = None
    source_type: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemSourceType] = None
    organization_id: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemOrganizationId] = None
    name: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemName] = None
    tags: typing.Optional[typing.List[str]] = None
    source_code: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemSourceCode] = None
    json_schema: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemJsonSchema] = None
    return_char_limit: typing.Optional[float] = None
    created_by_id: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemCreatedById] = None
    last_updated_by_id: typing.Optional[TemplatesCreateAgentsFromTemplateResponseAgentsItemToolsItemLastUpdatedById] = (
        None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
