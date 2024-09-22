# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: opentelemetry/proto/logs/v1/logs.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from opentelemetry.proto.common.v1 import common_pb2 as opentelemetry_dot_proto_dot_common_dot_v1_dot_common__pb2
from opentelemetry.proto.resource.v1 import resource_pb2 as opentelemetry_dot_proto_dot_resource_dot_v1_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&opentelemetry/proto/logs/v1/logs.proto\x12\x1bopentelemetry.proto.logs.v1\x1a*opentelemetry/proto/common/v1/common.proto\x1a.opentelemetry/proto/resource/v1/resource.proto\"L\n\x08LogsData\x12@\n\rresource_logs\x18\x01 \x03(\x0b\x32).opentelemetry.proto.logs.v1.ResourceLogs\"\xa3\x01\n\x0cResourceLogs\x12;\n\x08resource\x18\x01 \x01(\x0b\x32).opentelemetry.proto.resource.v1.Resource\x12:\n\nscope_logs\x18\x02 \x03(\x0b\x32&.opentelemetry.proto.logs.v1.ScopeLogs\x12\x12\n\nschema_url\x18\x03 \x01(\tJ\x06\x08\xe8\x07\x10\xe9\x07\"\xa0\x01\n\tScopeLogs\x12\x42\n\x05scope\x18\x01 \x01(\x0b\x32\x33.opentelemetry.proto.common.v1.InstrumentationScope\x12;\n\x0blog_records\x18\x02 \x03(\x0b\x32&.opentelemetry.proto.logs.v1.LogRecord\x12\x12\n\nschema_url\x18\x03 \x01(\t\"\xef\x02\n\tLogRecord\x12\x16\n\x0etime_unix_nano\x18\x01 \x01(\x06\x12\x1f\n\x17observed_time_unix_nano\x18\x0b \x01(\x06\x12\x44\n\x0fseverity_number\x18\x02 \x01(\x0e\x32+.opentelemetry.proto.logs.v1.SeverityNumber\x12\x15\n\rseverity_text\x18\x03 \x01(\t\x12\x35\n\x04\x62ody\x18\x05 \x01(\x0b\x32\'.opentelemetry.proto.common.v1.AnyValue\x12;\n\nattributes\x18\x06 \x03(\x0b\x32\'.opentelemetry.proto.common.v1.KeyValue\x12 \n\x18\x64ropped_attributes_count\x18\x07 \x01(\r\x12\r\n\x05\x66lags\x18\x08 \x01(\x07\x12\x10\n\x08trace_id\x18\t \x01(\x0c\x12\x0f\n\x07span_id\x18\n \x01(\x0cJ\x04\x08\x04\x10\x05*\xc3\x05\n\x0eSeverityNumber\x12\x1f\n\x1bSEVERITY_NUMBER_UNSPECIFIED\x10\x00\x12\x19\n\x15SEVERITY_NUMBER_TRACE\x10\x01\x12\x1a\n\x16SEVERITY_NUMBER_TRACE2\x10\x02\x12\x1a\n\x16SEVERITY_NUMBER_TRACE3\x10\x03\x12\x1a\n\x16SEVERITY_NUMBER_TRACE4\x10\x04\x12\x19\n\x15SEVERITY_NUMBER_DEBUG\x10\x05\x12\x1a\n\x16SEVERITY_NUMBER_DEBUG2\x10\x06\x12\x1a\n\x16SEVERITY_NUMBER_DEBUG3\x10\x07\x12\x1a\n\x16SEVERITY_NUMBER_DEBUG4\x10\x08\x12\x18\n\x14SEVERITY_NUMBER_INFO\x10\t\x12\x19\n\x15SEVERITY_NUMBER_INFO2\x10\n\x12\x19\n\x15SEVERITY_NUMBER_INFO3\x10\x0b\x12\x19\n\x15SEVERITY_NUMBER_INFO4\x10\x0c\x12\x18\n\x14SEVERITY_NUMBER_WARN\x10\r\x12\x19\n\x15SEVERITY_NUMBER_WARN2\x10\x0e\x12\x19\n\x15SEVERITY_NUMBER_WARN3\x10\x0f\x12\x19\n\x15SEVERITY_NUMBER_WARN4\x10\x10\x12\x19\n\x15SEVERITY_NUMBER_ERROR\x10\x11\x12\x1a\n\x16SEVERITY_NUMBER_ERROR2\x10\x12\x12\x1a\n\x16SEVERITY_NUMBER_ERROR3\x10\x13\x12\x1a\n\x16SEVERITY_NUMBER_ERROR4\x10\x14\x12\x19\n\x15SEVERITY_NUMBER_FATAL\x10\x15\x12\x1a\n\x16SEVERITY_NUMBER_FATAL2\x10\x16\x12\x1a\n\x16SEVERITY_NUMBER_FATAL3\x10\x17\x12\x1a\n\x16SEVERITY_NUMBER_FATAL4\x10\x18*Y\n\x0eLogRecordFlags\x12\x1f\n\x1bLOG_RECORD_FLAGS_DO_NOT_USE\x10\x00\x12&\n!LOG_RECORD_FLAGS_TRACE_FLAGS_MASK\x10\xff\x01\x42s\n\x1eio.opentelemetry.proto.logs.v1B\tLogsProtoP\x01Z&go.opentelemetry.io/proto/otlp/logs/v1\xaa\x02\x1bOpenTelemetry.Proto.Logs.V1b\x06proto3')

_SEVERITYNUMBER = DESCRIPTOR.enum_types_by_name['SeverityNumber']
SeverityNumber = enum_type_wrapper.EnumTypeWrapper(_SEVERITYNUMBER)
_LOGRECORDFLAGS = DESCRIPTOR.enum_types_by_name['LogRecordFlags']
LogRecordFlags = enum_type_wrapper.EnumTypeWrapper(_LOGRECORDFLAGS)
SEVERITY_NUMBER_UNSPECIFIED = 0
SEVERITY_NUMBER_TRACE = 1
SEVERITY_NUMBER_TRACE2 = 2
SEVERITY_NUMBER_TRACE3 = 3
SEVERITY_NUMBER_TRACE4 = 4
SEVERITY_NUMBER_DEBUG = 5
SEVERITY_NUMBER_DEBUG2 = 6
SEVERITY_NUMBER_DEBUG3 = 7
SEVERITY_NUMBER_DEBUG4 = 8
SEVERITY_NUMBER_INFO = 9
SEVERITY_NUMBER_INFO2 = 10
SEVERITY_NUMBER_INFO3 = 11
SEVERITY_NUMBER_INFO4 = 12
SEVERITY_NUMBER_WARN = 13
SEVERITY_NUMBER_WARN2 = 14
SEVERITY_NUMBER_WARN3 = 15
SEVERITY_NUMBER_WARN4 = 16
SEVERITY_NUMBER_ERROR = 17
SEVERITY_NUMBER_ERROR2 = 18
SEVERITY_NUMBER_ERROR3 = 19
SEVERITY_NUMBER_ERROR4 = 20
SEVERITY_NUMBER_FATAL = 21
SEVERITY_NUMBER_FATAL2 = 22
SEVERITY_NUMBER_FATAL3 = 23
SEVERITY_NUMBER_FATAL4 = 24
LOG_RECORD_FLAGS_DO_NOT_USE = 0
LOG_RECORD_FLAGS_TRACE_FLAGS_MASK = 255


_LOGSDATA = DESCRIPTOR.message_types_by_name['LogsData']
_RESOURCELOGS = DESCRIPTOR.message_types_by_name['ResourceLogs']
_SCOPELOGS = DESCRIPTOR.message_types_by_name['ScopeLogs']
_LOGRECORD = DESCRIPTOR.message_types_by_name['LogRecord']
LogsData = _reflection.GeneratedProtocolMessageType('LogsData', (_message.Message,), {
  'DESCRIPTOR' : _LOGSDATA,
  '__module__' : 'opentelemetry.proto.logs.v1.logs_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.logs.v1.LogsData)
  })
_sym_db.RegisterMessage(LogsData)

ResourceLogs = _reflection.GeneratedProtocolMessageType('ResourceLogs', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCELOGS,
  '__module__' : 'opentelemetry.proto.logs.v1.logs_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.logs.v1.ResourceLogs)
  })
_sym_db.RegisterMessage(ResourceLogs)

ScopeLogs = _reflection.GeneratedProtocolMessageType('ScopeLogs', (_message.Message,), {
  'DESCRIPTOR' : _SCOPELOGS,
  '__module__' : 'opentelemetry.proto.logs.v1.logs_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.logs.v1.ScopeLogs)
  })
_sym_db.RegisterMessage(ScopeLogs)

LogRecord = _reflection.GeneratedProtocolMessageType('LogRecord', (_message.Message,), {
  'DESCRIPTOR' : _LOGRECORD,
  '__module__' : 'opentelemetry.proto.logs.v1.logs_pb2'
  # @@protoc_insertion_point(class_scope:opentelemetry.proto.logs.v1.LogRecord)
  })
_sym_db.RegisterMessage(LogRecord)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036io.opentelemetry.proto.logs.v1B\tLogsProtoP\001Z&go.opentelemetry.io/proto/otlp/logs/v1\252\002\033OpenTelemetry.Proto.Logs.V1'
  _SEVERITYNUMBER._serialized_start=941
  _SEVERITYNUMBER._serialized_end=1648
  _LOGRECORDFLAGS._serialized_start=1650
  _LOGRECORDFLAGS._serialized_end=1739
  _LOGSDATA._serialized_start=163
  _LOGSDATA._serialized_end=239
  _RESOURCELOGS._serialized_start=242
  _RESOURCELOGS._serialized_end=405
  _SCOPELOGS._serialized_start=408
  _SCOPELOGS._serialized_end=568
  _LOGRECORD._serialized_start=571
  _LOGRECORD._serialized_end=938
# @@protoc_insertion_point(module_scope)
