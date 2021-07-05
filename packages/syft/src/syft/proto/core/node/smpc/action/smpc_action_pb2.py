# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/node/smpc/action/smpc_action.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.core.common import common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2
from syft.proto.core.pointer import pointer_pb2 as proto_dot_core_dot_pointer_dot_pointer__pb2
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/core/node/smpc/action/smpc_action.proto',
  package='syft.core.node.common.action',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-proto/core/node/smpc/action/smpc_action.proto\x12\x1csyft.core.node.common.action\x1a%proto/core/common/common_object.proto\x1a proto/core/pointer/pointer.proto\x1a\x1bproto/core/io/address.proto\"\x96\x03\n\nSMPCAction\x12\x13\n\x0bname_action\x18\x01 \x01(\t\x12\'\n\x08_self_id\x18\x02 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61rgs_id\x18\x03 \x03(\x0b\x32\x15.syft.core.common.UID\x12I\n\tkwargs_id\x18\x04 \x03(\x0b\x32\x36.syft.core.node.common.action.SMPCAction.KwargsIdEntry\x12\x0c\n\x04rank\x18\x05 \x01(\r\x12-\n\x0eid_at_location\x18\x06 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x07 \x01(\x0b\x32\x15.syft.core.io.Address\x12%\n\x06msg_id\x18\x08 \x01(\x0b\x32\x15.syft.core.common.UID\x1aK\n\rKwargsIdEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.syft.core.pointer.Pointer:\x02\x38\x01\x62\x06proto3'
  ,
  dependencies=[proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,proto_dot_core_dot_pointer_dot_pointer__pb2.DESCRIPTOR,proto_dot_core_dot_io_dot_address__pb2.DESCRIPTOR,])




_SMPCACTION_KWARGSIDENTRY = _descriptor.Descriptor(
  name='KwargsIdEntry',
  full_name='syft.core.node.common.action.SMPCAction.KwargsIdEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='syft.core.node.common.action.SMPCAction.KwargsIdEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='syft.core.node.common.action.SMPCAction.KwargsIdEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=513,
  serialized_end=588,
)

_SMPCACTION = _descriptor.Descriptor(
  name='SMPCAction',
  full_name='syft.core.node.common.action.SMPCAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name_action', full_name='syft.core.node.common.action.SMPCAction.name_action', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='_self_id', full_name='syft.core.node.common.action.SMPCAction._self_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='args_id', full_name='syft.core.node.common.action.SMPCAction.args_id', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kwargs_id', full_name='syft.core.node.common.action.SMPCAction.kwargs_id', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rank', full_name='syft.core.node.common.action.SMPCAction.rank', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id_at_location', full_name='syft.core.node.common.action.SMPCAction.id_at_location', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='syft.core.node.common.action.SMPCAction.address', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='syft.core.node.common.action.SMPCAction.msg_id', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SMPCACTION_KWARGSIDENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=588,
)

_SMPCACTION_KWARGSIDENTRY.fields_by_name['value'].message_type = proto_dot_core_dot_pointer_dot_pointer__pb2._POINTER
_SMPCACTION_KWARGSIDENTRY.containing_type = _SMPCACTION
_SMPCACTION.fields_by_name['_self_id'].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_SMPCACTION.fields_by_name['args_id'].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_SMPCACTION.fields_by_name['kwargs_id'].message_type = _SMPCACTION_KWARGSIDENTRY
_SMPCACTION.fields_by_name['id_at_location'].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_SMPCACTION.fields_by_name['address'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_SMPCACTION.fields_by_name['msg_id'].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
DESCRIPTOR.message_types_by_name['SMPCAction'] = _SMPCACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SMPCAction = _reflection.GeneratedProtocolMessageType('SMPCAction', (_message.Message,), {

  'KwargsIdEntry' : _reflection.GeneratedProtocolMessageType('KwargsIdEntry', (_message.Message,), {
    'DESCRIPTOR' : _SMPCACTION_KWARGSIDENTRY,
    '__module__' : 'proto.core.node.smpc.action.smpc_action_pb2'
    # @@protoc_insertion_point(class_scope:syft.core.node.common.action.SMPCAction.KwargsIdEntry)
    })
  ,
  'DESCRIPTOR' : _SMPCACTION,
  '__module__' : 'proto.core.node.smpc.action.smpc_action_pb2'
  # @@protoc_insertion_point(class_scope:syft.core.node.common.action.SMPCAction)
  })
_sym_db.RegisterMessage(SMPCAction)
_sym_db.RegisterMessage(SMPCAction.KwargsIdEntry)


_SMPCACTION_KWARGSIDENTRY._options = None
# @@protoc_insertion_point(module_scope)
