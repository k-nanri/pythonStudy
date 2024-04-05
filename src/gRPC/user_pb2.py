# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\"\xa1\x01\n\x04User\x12\n\n\x02id\x18\x01 \x01(\r\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\x14\n\x0cmail_address\x18\x03 \x01(\t\x12!\n\tuser_type\x18\x04 \x01(\x0e\x32\x0e.User.UserType\"B\n\x08UserType\x12\n\n\x06NORMAL\x10\x00\x12\x11\n\rADMINISTRATOR\x10\x01\x12\t\n\x05GUEST\x10\x02\x12\x0c\n\x08\x44ISABLED\x10\x03\"\x87\x01\n\x0bUserRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12(\n\tuser_type\x18\x02 \x01(\x0e\x32\x15.UserRequest.UserType\"B\n\x08UserType\x12\n\n\x06NORMAL\x10\x00\x12\x11\n\rADMINISTRATOR\x10\x01\x12\t\n\x05GUEST\x10\x02\x12\x0c\n\x08\x44ISABLED\x10\x03\"C\n\x0cUserResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x13\n\x04user\x18\x03 \x01(\x0b\x32\x05.User2e\n\x0bUserManager\x12\"\n\x03get\x12\x0c.UserRequest\x1a\r.UserResponse\x12\x32\n\x11get_server_stream\x12\x0c.UserRequest\x1a\r.UserResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USER']._serialized_start=15
  _globals['_USER']._serialized_end=176
  _globals['_USER_USERTYPE']._serialized_start=110
  _globals['_USER_USERTYPE']._serialized_end=176
  _globals['_USERREQUEST']._serialized_start=179
  _globals['_USERREQUEST']._serialized_end=314
  _globals['_USERREQUEST_USERTYPE']._serialized_start=110
  _globals['_USERREQUEST_USERTYPE']._serialized_end=176
  _globals['_USERRESPONSE']._serialized_start=316
  _globals['_USERRESPONSE']._serialized_end=383
  _globals['_USERMANAGER']._serialized_start=385
  _globals['_USERMANAGER']._serialized_end=486
# @@protoc_insertion_point(module_scope)
