# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buildstream/v2/buildstream.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from buildstream._protos.build.bazel.remote.execution.v2 import remote_execution_pb2 as build_dot_bazel_dot_remote_dot_execution_dot_v2_dot_remote__execution__pb2
from buildstream._protos.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='buildstream/v2/buildstream.proto',
  package='buildstream.v2',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n buildstream/v2/buildstream.proto\x12\x0e\x62uildstream.v2\x1a\x36\x62uild/bazel/remote/execution/v2/remote_execution.proto\x1a\x1cgoogle/api/annotations.proto\"9\n\x13GetReferenceRequest\x12\x15\n\rinstance_name\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"O\n\x14GetReferenceResponse\x12\x37\n\x06\x64igest\x18\x01 \x01(\x0b\x32\'.build.bazel.remote.execution.v2.Digest\"v\n\x16UpdateReferenceRequest\x12\x15\n\rinstance_name\x18\x01 \x01(\t\x12\x0c\n\x04keys\x18\x02 \x03(\t\x12\x37\n\x06\x64igest\x18\x03 \x01(\x0b\x32\'.build.bazel.remote.execution.v2.Digest\"\x19\n\x17UpdateReferenceResponse\"&\n\rStatusRequest\x12\x15\n\rinstance_name\x18\x01 \x01(\t\"\'\n\x0eStatusResponse\x12\x15\n\rallow_updates\x18\x01 \x01(\x08\"/\n\x16GetCapabilitiesRequest\x12\x15\n\rinstance_name\x18\x01 \x01(\t\"-\n\x14\x41rtifactCapabilities\x12\x15\n\rallow_updates\x18\x01 \x01(\x08\"Y\n\x12ServerCapabilities\x12\x43\n\x15\x61rtifact_capabilities\x18\x01 \x01(\x0b\x32$.buildstream.v2.ArtifactCapabilities2\xca\x03\n\x10ReferenceStorage\x12\x90\x01\n\x0cGetReference\x12#.buildstream.v2.GetReferenceRequest\x1a$.buildstream.v2.GetReferenceResponse\"5\x82\xd3\xe4\x93\x02/\x12-/v2/{instance_name=**}/buildstream/refs/{key}\x12\xa1\x01\n\x0fUpdateReference\x12&.buildstream.v2.UpdateReferenceRequest\x1a\'.buildstream.v2.UpdateReferenceResponse\"=\x82\xd3\xe4\x93\x02\x37\x1a-/v2/{instance_name=**}/buildstream/refs/{key}:\x06\x64igest\x12\x7f\n\x06Status\x12\x1d.buildstream.v2.StatusRequest\x1a\x1e.buildstream.v2.StatusResponse\"6\x82\xd3\xe4\x93\x02\x30\x1a./v2/{instance_name=**}/buildstream/refs:status2\x9b\x01\n\x0c\x43\x61pabilities\x12\x8a\x01\n\x0fGetCapabilities\x12&.buildstream.v2.GetCapabilitiesRequest\x1a\".buildstream.v2.ServerCapabilities\"+\x82\xd3\xe4\x93\x02%\x12#/v2/{instance_name=**}/capabilitiesb\x06proto3')
  ,
  dependencies=[build_dot_bazel_dot_remote_dot_execution_dot_v2_dot_remote__execution__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETREFERENCEREQUEST = _descriptor.Descriptor(
  name='GetReferenceRequest',
  full_name='buildstream.v2.GetReferenceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='buildstream.v2.GetReferenceRequest.instance_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='buildstream.v2.GetReferenceRequest.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=195,
)


_GETREFERENCERESPONSE = _descriptor.Descriptor(
  name='GetReferenceResponse',
  full_name='buildstream.v2.GetReferenceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='digest', full_name='buildstream.v2.GetReferenceResponse.digest', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=276,
)


_UPDATEREFERENCEREQUEST = _descriptor.Descriptor(
  name='UpdateReferenceRequest',
  full_name='buildstream.v2.UpdateReferenceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='buildstream.v2.UpdateReferenceRequest.instance_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keys', full_name='buildstream.v2.UpdateReferenceRequest.keys', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='digest', full_name='buildstream.v2.UpdateReferenceRequest.digest', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=396,
)


_UPDATEREFERENCERESPONSE = _descriptor.Descriptor(
  name='UpdateReferenceResponse',
  full_name='buildstream.v2.UpdateReferenceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=398,
  serialized_end=423,
)


_STATUSREQUEST = _descriptor.Descriptor(
  name='StatusRequest',
  full_name='buildstream.v2.StatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='buildstream.v2.StatusRequest.instance_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=425,
  serialized_end=463,
)


_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='buildstream.v2.StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='allow_updates', full_name='buildstream.v2.StatusResponse.allow_updates', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=504,
)


_GETCAPABILITIESREQUEST = _descriptor.Descriptor(
  name='GetCapabilitiesRequest',
  full_name='buildstream.v2.GetCapabilitiesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_name', full_name='buildstream.v2.GetCapabilitiesRequest.instance_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=506,
  serialized_end=553,
)


_ARTIFACTCAPABILITIES = _descriptor.Descriptor(
  name='ArtifactCapabilities',
  full_name='buildstream.v2.ArtifactCapabilities',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='allow_updates', full_name='buildstream.v2.ArtifactCapabilities.allow_updates', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=555,
  serialized_end=600,
)


_SERVERCAPABILITIES = _descriptor.Descriptor(
  name='ServerCapabilities',
  full_name='buildstream.v2.ServerCapabilities',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='artifact_capabilities', full_name='buildstream.v2.ServerCapabilities.artifact_capabilities', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=602,
  serialized_end=691,
)

_GETREFERENCERESPONSE.fields_by_name['digest'].message_type = build_dot_bazel_dot_remote_dot_execution_dot_v2_dot_remote__execution__pb2._DIGEST
_UPDATEREFERENCEREQUEST.fields_by_name['digest'].message_type = build_dot_bazel_dot_remote_dot_execution_dot_v2_dot_remote__execution__pb2._DIGEST
_SERVERCAPABILITIES.fields_by_name['artifact_capabilities'].message_type = _ARTIFACTCAPABILITIES
DESCRIPTOR.message_types_by_name['GetReferenceRequest'] = _GETREFERENCEREQUEST
DESCRIPTOR.message_types_by_name['GetReferenceResponse'] = _GETREFERENCERESPONSE
DESCRIPTOR.message_types_by_name['UpdateReferenceRequest'] = _UPDATEREFERENCEREQUEST
DESCRIPTOR.message_types_by_name['UpdateReferenceResponse'] = _UPDATEREFERENCERESPONSE
DESCRIPTOR.message_types_by_name['StatusRequest'] = _STATUSREQUEST
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
DESCRIPTOR.message_types_by_name['GetCapabilitiesRequest'] = _GETCAPABILITIESREQUEST
DESCRIPTOR.message_types_by_name['ArtifactCapabilities'] = _ARTIFACTCAPABILITIES
DESCRIPTOR.message_types_by_name['ServerCapabilities'] = _SERVERCAPABILITIES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetReferenceRequest = _reflection.GeneratedProtocolMessageType('GetReferenceRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREFERENCEREQUEST,
  __module__ = 'buildstream.v2.buildstream_pb2'
  # @@protoc_insertion_point(class_scope:buildstream.v2.GetReferenceRequest)
  ))
_sym_db.RegisterMessage(GetReferenceRequest)

GetReferenceResponse = _reflection.GeneratedProtocolMessageType('GetReferenceResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETREFERENCERESPONSE,
  __module__ = 'buildstream.v2.buildstream_pb2'
  # @@protoc_insertion_point(class_scope:buildstream.v2.GetReferenceResponse)
  ))
_sym_db.RegisterMessage(GetReferenceResponse)

UpdateReferenceRequest = _reflection.GeneratedProtocolMessageType('UpdateReferenceRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEREFERENCEREQUEST,
  __module__ = 'buildstream.v2.buildstream_pb2'
  # @@protoc_insertion_point(class_scope:buildstream.v2.UpdateReferenceRequest)
  ))
_sym_db.RegisterMessage(UpdateReferenceRequest)

UpdateReferenceResponse = _reflection.GeneratedProtocolMessageType('UpdateReferenceResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEREFERENCERESPONSE,
  __module__ = 'buildstream.v2.buildstream_pb2'
  # @@protoc_insertion_point(class_scope:buildstream.v2.UpdateReferenceResponse)
  ))
_sym_db.RegisterMessage(UpdateReferenceResponse)

StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _STATUSREQUEST,
  __module__ = 'buildstream.v2.buildstream_pb2'
  # @@protoc_insertion_point(class_scope:buildstream.v2.StatusRequest)
  ))
_sym_db.RegisterMessage(StatusRequest)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _STATUSRESPONSE,
  __module__ = 'buildstream.v2.buildstream_pb2'
  # @@protoc_insertion_point(class_scope:buildstream.v2.StatusResponse)
  ))
_sym_db.RegisterMessage(StatusResponse)

GetCapabilitiesRequest = _reflection.GeneratedProtocolMessageType('GetCapabilitiesRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCAPABILITIESREQUEST,
  __module__ = 'buildstream.v2.buildstream_pb2'
  # @@protoc_insertion_point(class_scope:buildstream.v2.GetCapabilitiesRequest)
  ))
_sym_db.RegisterMessage(GetCapabilitiesRequest)

ArtifactCapabilities = _reflection.GeneratedProtocolMessageType('ArtifactCapabilities', (_message.Message,), dict(
  DESCRIPTOR = _ARTIFACTCAPABILITIES,
  __module__ = 'buildstream.v2.buildstream_pb2'
  # @@protoc_insertion_point(class_scope:buildstream.v2.ArtifactCapabilities)
  ))
_sym_db.RegisterMessage(ArtifactCapabilities)

ServerCapabilities = _reflection.GeneratedProtocolMessageType('ServerCapabilities', (_message.Message,), dict(
  DESCRIPTOR = _SERVERCAPABILITIES,
  __module__ = 'buildstream.v2.buildstream_pb2'
  # @@protoc_insertion_point(class_scope:buildstream.v2.ServerCapabilities)
  ))
_sym_db.RegisterMessage(ServerCapabilities)



_REFERENCESTORAGE = _descriptor.ServiceDescriptor(
  name='ReferenceStorage',
  full_name='buildstream.v2.ReferenceStorage',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=694,
  serialized_end=1152,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetReference',
    full_name='buildstream.v2.ReferenceStorage.GetReference',
    index=0,
    containing_service=None,
    input_type=_GETREFERENCEREQUEST,
    output_type=_GETREFERENCERESPONSE,
    serialized_options=_b('\202\323\344\223\002/\022-/v2/{instance_name=**}/buildstream/refs/{key}'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateReference',
    full_name='buildstream.v2.ReferenceStorage.UpdateReference',
    index=1,
    containing_service=None,
    input_type=_UPDATEREFERENCEREQUEST,
    output_type=_UPDATEREFERENCERESPONSE,
    serialized_options=_b('\202\323\344\223\0027\032-/v2/{instance_name=**}/buildstream/refs/{key}:\006digest'),
  ),
  _descriptor.MethodDescriptor(
    name='Status',
    full_name='buildstream.v2.ReferenceStorage.Status',
    index=2,
    containing_service=None,
    input_type=_STATUSREQUEST,
    output_type=_STATUSRESPONSE,
    serialized_options=_b('\202\323\344\223\0020\032./v2/{instance_name=**}/buildstream/refs:status'),
  ),
])
_sym_db.RegisterServiceDescriptor(_REFERENCESTORAGE)

DESCRIPTOR.services_by_name['ReferenceStorage'] = _REFERENCESTORAGE


_CAPABILITIES = _descriptor.ServiceDescriptor(
  name='Capabilities',
  full_name='buildstream.v2.Capabilities',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=1155,
  serialized_end=1310,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCapabilities',
    full_name='buildstream.v2.Capabilities.GetCapabilities',
    index=0,
    containing_service=None,
    input_type=_GETCAPABILITIESREQUEST,
    output_type=_SERVERCAPABILITIES,
    serialized_options=_b('\202\323\344\223\002%\022#/v2/{instance_name=**}/capabilities'),
  ),
])
_sym_db.RegisterServiceDescriptor(_CAPABILITIES)

DESCRIPTOR.services_by_name['Capabilities'] = _CAPABILITIES

# @@protoc_insertion_point(module_scope)
