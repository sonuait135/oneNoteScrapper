# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
import typing_extensions
from ..core.unchecked_base_model import UnionMetadata


class TextAssistantMessageContentItem(UncheckedBaseModel):
    type: typing.Literal["text"] = "text"
    text: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AssistantMessageContentItem = typing_extensions.Annotated[
    TextAssistantMessageContentItem, UnionMetadata(discriminant="type")
]
