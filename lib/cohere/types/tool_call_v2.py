# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .tool_call_v2function import ToolCallV2Function
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ToolCallV2(UncheckedBaseModel):
    """
    A array of tool calls to be made.
    """

    id: typing.Optional[str] = None
    type: typing.Optional[typing.Literal["function"]] = None
    function: typing.Optional[ToolCallV2Function] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
