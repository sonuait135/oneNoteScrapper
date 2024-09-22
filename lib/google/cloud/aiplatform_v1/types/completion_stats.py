# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1",
    manifest={
        "CompletionStats",
    },
)


class CompletionStats(proto.Message):
    r"""Success and error statistics of processing multiple entities
    (for example, DataItems or structured data rows) in batch.

    Attributes:
        successful_count (int):
            Output only. The number of entities that had
            been processed successfully.
        failed_count (int):
            Output only. The number of entities for which
            any error was encountered.
        incomplete_count (int):
            Output only. In cases when enough errors are
            encountered a job, pipeline, or operation may be
            failed as a whole. Below is the number of
            entities for which the processing had not been
            finished (either in successful or failed state).
            Set to -1 if the number is unknown (for example,
            the operation failed before the total entity
            number could be collected).
        successful_forecast_point_count (int):
            Output only. The number of the successful
            forecast points that are generated by the
            forecasting model. This is ONLY used by the
            forecasting batch prediction.
    """

    successful_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    failed_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    incomplete_count: int = proto.Field(
        proto.INT64,
        number=3,
    )
    successful_forecast_point_count: int = proto.Field(
        proto.INT64,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
