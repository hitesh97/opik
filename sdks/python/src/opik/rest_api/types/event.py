# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
from .unknown_field_set import UnknownFieldSet
from .any_value import AnyValue
from .any_value_or_builder import AnyValueOrBuilder
from .array_value import ArrayValue
from .array_value_or_builder import ArrayValueOrBuilder
from .declaration import Declaration
from .declaration_or_builder import DeclarationOrBuilder
from .descriptor import Descriptor
from .descriptor_proto import DescriptorProto
from .descriptor_proto_or_builder import DescriptorProtoOrBuilder
from .edition_default import EditionDefault
from .edition_default_or_builder import EditionDefaultOrBuilder
from .enum_descriptor import EnumDescriptor
from .enum_descriptor_proto import EnumDescriptorProto
from .enum_descriptor_proto_or_builder import EnumDescriptorProtoOrBuilder
from .enum_options import EnumOptions
from .enum_options_or_builder import EnumOptionsOrBuilder
from .enum_reserved_range import EnumReservedRange
from .enum_reserved_range_or_builder import EnumReservedRangeOrBuilder
from .enum_value_descriptor import EnumValueDescriptor
from .enum_value_descriptor_proto import EnumValueDescriptorProto
from .enum_value_descriptor_proto_or_builder import EnumValueDescriptorProtoOrBuilder
from .enum_value_options import EnumValueOptions
from .enum_value_options_or_builder import EnumValueOptionsOrBuilder
from .extension_range import ExtensionRange
from .extension_range_options import ExtensionRangeOptions
from .extension_range_options_or_builder import ExtensionRangeOptionsOrBuilder
from .extension_range_or_builder import ExtensionRangeOrBuilder
from .feature_set import FeatureSet
from .feature_set_or_builder import FeatureSetOrBuilder
from .feature_support import FeatureSupport
from .feature_support_or_builder import FeatureSupportOrBuilder
from .field_descriptor import FieldDescriptor
from .field_descriptor_proto import FieldDescriptorProto
from .field_descriptor_proto_or_builder import FieldDescriptorProtoOrBuilder
from .field_options import FieldOptions
from .field_options_or_builder import FieldOptionsOrBuilder
from .file_descriptor import FileDescriptor
from .file_descriptor_proto import FileDescriptorProto
from .file_options import FileOptions
from .file_options_or_builder import FileOptionsOrBuilder
from .key_value import KeyValue
from .key_value_list import KeyValueList
from .key_value_list_or_builder import KeyValueListOrBuilder
from .location import Location
from .location_or_builder import LocationOrBuilder
from .message import Message
from .message_lite import MessageLite
from .message_options import MessageOptions
from .message_options_or_builder import MessageOptionsOrBuilder
from .method_descriptor import MethodDescriptor
from .method_descriptor_proto import MethodDescriptorProto
from .method_descriptor_proto_or_builder import MethodDescriptorProtoOrBuilder
from .method_options import MethodOptions
from .method_options_or_builder import MethodOptionsOrBuilder
from .name_part import NamePart
from .name_part_or_builder import NamePartOrBuilder
from .oneof_descriptor import OneofDescriptor
from .oneof_descriptor_proto import OneofDescriptorProto
from .oneof_descriptor_proto_or_builder import OneofDescriptorProtoOrBuilder
from .oneof_options import OneofOptions
from .oneof_options_or_builder import OneofOptionsOrBuilder
from .reserved_range import ReservedRange
from .reserved_range_or_builder import ReservedRangeOrBuilder
from .service_descriptor import ServiceDescriptor
from .service_descriptor_proto import ServiceDescriptorProto
from .service_descriptor_proto_or_builder import ServiceDescriptorProtoOrBuilder
from .service_options import ServiceOptions
from .service_options_or_builder import ServiceOptionsOrBuilder
from .source_code_info import SourceCodeInfo
from .source_code_info_or_builder import SourceCodeInfoOrBuilder
from .uninterpreted_option import UninterpretedOption
from .uninterpreted_option_or_builder import UninterpretedOptionOrBuilder
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
from .key_value_or_builder import KeyValueOrBuilder
from .parser_event import ParserEvent
from .byte_string import ByteString
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ..core.pydantic_utilities import update_forward_refs


class Event(UniversalBaseModel):
    unknown_fields: typing_extensions.Annotated[
        typing.Optional[UnknownFieldSet], FieldMetadata(alias="unknownFields")
    ] = None
    name: typing.Optional[str] = None
    default_instance_for_type: typing_extensions.Annotated[
        typing.Optional["Event"], FieldMetadata(alias="defaultInstanceForType")
    ] = None
    dropped_attributes_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="droppedAttributesCount")
    ] = None
    attributes_or_builder_list: typing_extensions.Annotated[
        typing.Optional[typing.List[KeyValueOrBuilder]],
        FieldMetadata(alias="attributesOrBuilderList"),
    ] = None
    time_unix_nano: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="timeUnixNano")
    ] = None
    attributes_list: typing_extensions.Annotated[
        typing.Optional[typing.List[KeyValue]], FieldMetadata(alias="attributesList")
    ] = None
    attributes_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="attributesCount")
    ] = None
    serialized_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="serializedSize")
    ] = None
    parser_for_type: typing_extensions.Annotated[
        typing.Optional[ParserEvent], FieldMetadata(alias="parserForType")
    ] = None
    name_bytes: typing_extensions.Annotated[
        typing.Optional[ByteString], FieldMetadata(alias="nameBytes")
    ] = None
    initialized: typing.Optional[bool] = None
    initialization_error_string: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="initializationErrorString")
    ] = None
    descriptor_for_type: typing_extensions.Annotated[
        typing.Optional[Descriptor], FieldMetadata(alias="descriptorForType")
    ] = None
    all_fields: typing_extensions.Annotated[
        typing.Optional[
            typing.Dict[str, typing.Dict[str, typing.Optional[typing.Any]]]
        ],
        FieldMetadata(alias="allFields"),
    ] = None
    memoized_serialized_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="memoizedSerializedSize")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(
            extra="allow", frozen=True
        )  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(UnknownFieldSet, Event=Event)
update_forward_refs(AnyValue, Event=Event)
update_forward_refs(AnyValueOrBuilder, Event=Event)
update_forward_refs(ArrayValue, Event=Event)
update_forward_refs(ArrayValueOrBuilder, Event=Event)
update_forward_refs(Declaration, Event=Event)
update_forward_refs(DeclarationOrBuilder, Event=Event)
update_forward_refs(Descriptor, Event=Event)
update_forward_refs(DescriptorProto, Event=Event)
update_forward_refs(DescriptorProtoOrBuilder, Event=Event)
update_forward_refs(EditionDefault, Event=Event)
update_forward_refs(EditionDefaultOrBuilder, Event=Event)
update_forward_refs(EnumDescriptor, Event=Event)
update_forward_refs(EnumDescriptorProto, Event=Event)
update_forward_refs(EnumDescriptorProtoOrBuilder, Event=Event)
update_forward_refs(EnumOptions, Event=Event)
update_forward_refs(EnumOptionsOrBuilder, Event=Event)
update_forward_refs(EnumReservedRange, Event=Event)
update_forward_refs(EnumReservedRangeOrBuilder, Event=Event)
update_forward_refs(EnumValueDescriptor, Event=Event)
update_forward_refs(EnumValueDescriptorProto, Event=Event)
update_forward_refs(EnumValueDescriptorProtoOrBuilder, Event=Event)
update_forward_refs(EnumValueOptions, Event=Event)
update_forward_refs(EnumValueOptionsOrBuilder, Event=Event)
update_forward_refs(ExtensionRange, Event=Event)
update_forward_refs(ExtensionRangeOptions, Event=Event)
update_forward_refs(ExtensionRangeOptionsOrBuilder, Event=Event)
update_forward_refs(ExtensionRangeOrBuilder, Event=Event)
update_forward_refs(FeatureSet, Event=Event)
update_forward_refs(FeatureSetOrBuilder, Event=Event)
update_forward_refs(FeatureSupport, Event=Event)
update_forward_refs(FeatureSupportOrBuilder, Event=Event)
update_forward_refs(FieldDescriptor, Event=Event)
update_forward_refs(FieldDescriptorProto, Event=Event)
update_forward_refs(FieldDescriptorProtoOrBuilder, Event=Event)
update_forward_refs(FieldOptions, Event=Event)
update_forward_refs(FieldOptionsOrBuilder, Event=Event)
update_forward_refs(FileDescriptor, Event=Event)
update_forward_refs(FileDescriptorProto, Event=Event)
update_forward_refs(FileOptions, Event=Event)
update_forward_refs(FileOptionsOrBuilder, Event=Event)
update_forward_refs(KeyValue, Event=Event)
update_forward_refs(KeyValueList, Event=Event)
update_forward_refs(KeyValueListOrBuilder, Event=Event)
update_forward_refs(Location, Event=Event)
update_forward_refs(LocationOrBuilder, Event=Event)
update_forward_refs(Message, Event=Event)
update_forward_refs(MessageLite, Event=Event)
update_forward_refs(MessageOptions, Event=Event)
update_forward_refs(MessageOptionsOrBuilder, Event=Event)
update_forward_refs(MethodDescriptor, Event=Event)
update_forward_refs(MethodDescriptorProto, Event=Event)
update_forward_refs(MethodDescriptorProtoOrBuilder, Event=Event)
update_forward_refs(MethodOptions, Event=Event)
update_forward_refs(MethodOptionsOrBuilder, Event=Event)
update_forward_refs(NamePart, Event=Event)
update_forward_refs(NamePartOrBuilder, Event=Event)
update_forward_refs(OneofDescriptor, Event=Event)
update_forward_refs(OneofDescriptorProto, Event=Event)
update_forward_refs(OneofDescriptorProtoOrBuilder, Event=Event)
update_forward_refs(OneofOptions, Event=Event)
update_forward_refs(OneofOptionsOrBuilder, Event=Event)
update_forward_refs(ReservedRange, Event=Event)
update_forward_refs(ReservedRangeOrBuilder, Event=Event)
update_forward_refs(ServiceDescriptor, Event=Event)
update_forward_refs(ServiceDescriptorProto, Event=Event)
update_forward_refs(ServiceDescriptorProtoOrBuilder, Event=Event)
update_forward_refs(ServiceOptions, Event=Event)
update_forward_refs(ServiceOptionsOrBuilder, Event=Event)
update_forward_refs(SourceCodeInfo, Event=Event)
update_forward_refs(SourceCodeInfoOrBuilder, Event=Event)
update_forward_refs(UninterpretedOption, Event=Event)
update_forward_refs(UninterpretedOptionOrBuilder, Event=Event)
update_forward_refs(Event)
