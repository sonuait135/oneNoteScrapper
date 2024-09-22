# This file was auto-generated by Fern from our API Definition.

from ....core.unchecked_base_model import UncheckedBaseModel
import typing
from .event import Event
import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class ListEventsResponse(UncheckedBaseModel):
    """
    Response to a request to list events of a fine-tuned model.
    """

    events: typing.Optional[typing.List[Event]] = pydantic.Field(default=None)
    """
    List of events for the fine-tuned model.
    """

    next_page_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Pagination token to retrieve the next page of results. If the value is "",
    it means no further results for the request.
    """

    total_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total count of results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
