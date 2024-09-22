# This file was auto-generated by Fern from our API Definition.

from .chat_stream_event_type import ChatStreamEventType
import typing
from .chat_content_start_event_delta import ChatContentStartEventDelta
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ChatContentStartEvent(ChatStreamEventType):
    """
    A streamed delta event which signifies that a new content block has started.
    """

    index: typing.Optional[int] = None
    delta: typing.Optional[ChatContentStartEventDelta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
