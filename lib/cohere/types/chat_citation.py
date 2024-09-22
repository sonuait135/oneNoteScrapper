# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ChatCitation(UncheckedBaseModel):
    """
    A section of the generated reply which cites external knowledge.
    """

    start: int = pydantic.Field()
    """
    The index of text that the citation starts at, counting from zero. For example, a generation of `Hello, world!` with a citation on `world` would have a start value of `7`. This is because the citation starts at `w`, which is the seventh character.
    """

    end: int = pydantic.Field()
    """
    The index of text that the citation ends after, counting from zero. For example, a generation of `Hello, world!` with a citation on `world` would have an end value of `11`. This is because the citation ends after `d`, which is the eleventh character.
    """

    text: str = pydantic.Field()
    """
    The text of the citation. For example, a generation of `Hello, world!` with a citation of `world` would have a text value of `world`.
    """

    document_ids: typing.List[str] = pydantic.Field()
    """
    Identifiers of documents cited by this section of the generated reply.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
