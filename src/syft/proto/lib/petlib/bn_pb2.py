# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/petlib/bn.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/petlib/bn.proto",
    package="syft.lib.petlib",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x19proto/lib/petlib/bn.proto\x12\x0fsyft.lib.petlib"\x11\n\x02\x42n\x12\x0b\n\x03hex\x18\x02 \x01(\tb\x06proto3',
)


_BN = _descriptor.Descriptor(
    name="Bn",
    full_name="syft.lib.petlib.Bn",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="hex",
            full_name="syft.lib.petlib.Bn.hex",
            index=0,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=46,
    serialized_end=63,
)

DESCRIPTOR.message_types_by_name["Bn"] = _BN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Bn = _reflection.GeneratedProtocolMessageType(
    "Bn",
    (_message.Message,),
    {
        "DESCRIPTOR": _BN,
        "__module__": "proto.lib.petlib.bn_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.petlib.Bn)
    },
)
_sym_db.RegisterMessage(Bn)


# @@protoc_insertion_point(module_scope)
