# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
from .unknown_field_set import UnknownFieldSet
from .message_lite import MessageLite
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
from .parser_message_options import ParserMessageOptions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ..core.pydantic_utilities import update_forward_refs


class MessageOptions(UniversalBaseModel):
    unknown_fields: typing_extensions.Annotated[
        typing.Optional[UnknownFieldSet], FieldMetadata(alias="unknownFields")
    ] = None
    default_instance_for_type: typing_extensions.Annotated[
        typing.Optional["MessageOptions"], FieldMetadata(alias="defaultInstanceForType")
    ] = None
    message_set_wire_format: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="messageSetWireFormat")
    ] = None
    uninterpreted_option_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="uninterpretedOptionCount")
    ] = None
    uninterpreted_option_list: typing_extensions.Annotated[
        typing.Optional[typing.List["UninterpretedOption"]],
        FieldMetadata(alias="uninterpretedOptionList"),
    ] = None
    no_standard_descriptor_accessor: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="noStandardDescriptorAccessor")
    ] = None
    deprecated_legacy_json_field_conflicts: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="deprecatedLegacyJsonFieldConflicts")
    ] = None
    uninterpreted_option_or_builder_list: typing_extensions.Annotated[
        typing.Optional[typing.List["UninterpretedOptionOrBuilder"]],
        FieldMetadata(alias="uninterpretedOptionOrBuilderList"),
    ] = None
    features_or_builder: typing_extensions.Annotated[
        typing.Optional["FeatureSetOrBuilder"], FieldMetadata(alias="featuresOrBuilder")
    ] = None
    serialized_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="serializedSize")
    ] = None
    parser_for_type: typing_extensions.Annotated[
        typing.Optional[ParserMessageOptions], FieldMetadata(alias="parserForType")
    ] = None
    map_entry: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="mapEntry")
    ] = None
    features: typing.Optional["FeatureSet"] = None
    initialized: typing.Optional[bool] = None
    deprecated: typing.Optional[bool] = None
    initialization_error_string: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="initializationErrorString")
    ] = None
    descriptor_for_type: typing_extensions.Annotated[
        typing.Optional["Descriptor"], FieldMetadata(alias="descriptorForType")
    ] = None
    all_fields: typing_extensions.Annotated[
        typing.Optional[
            typing.Dict[str, typing.Dict[str, typing.Optional[typing.Any]]]
        ],
        FieldMetadata(alias="allFields"),
    ] = None
    all_fields_raw: typing_extensions.Annotated[
        typing.Optional[
            typing.Dict[str, typing.Dict[str, typing.Optional[typing.Any]]]
        ],
        FieldMetadata(alias="allFieldsRaw"),
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


from .declaration import Declaration  # noqa: E402
from .declaration_or_builder import DeclarationOrBuilder  # noqa: E402
from .descriptor import Descriptor  # noqa: E402
from .descriptor_proto import DescriptorProto  # noqa: E402
from .descriptor_proto_or_builder import DescriptorProtoOrBuilder  # noqa: E402
from .edition_default import EditionDefault  # noqa: E402
from .edition_default_or_builder import EditionDefaultOrBuilder  # noqa: E402
from .enum_descriptor import EnumDescriptor  # noqa: E402
from .enum_descriptor_proto import EnumDescriptorProto  # noqa: E402
from .enum_descriptor_proto_or_builder import EnumDescriptorProtoOrBuilder  # noqa: E402
from .enum_options import EnumOptions  # noqa: E402
from .enum_options_or_builder import EnumOptionsOrBuilder  # noqa: E402
from .enum_reserved_range import EnumReservedRange  # noqa: E402
from .enum_reserved_range_or_builder import EnumReservedRangeOrBuilder  # noqa: E402
from .enum_value_descriptor import EnumValueDescriptor  # noqa: E402
from .enum_value_descriptor_proto import EnumValueDescriptorProto  # noqa: E402
from .enum_value_descriptor_proto_or_builder import EnumValueDescriptorProtoOrBuilder  # noqa: E402
from .enum_value_options import EnumValueOptions  # noqa: E402
from .enum_value_options_or_builder import EnumValueOptionsOrBuilder  # noqa: E402
from .extension_range import ExtensionRange  # noqa: E402
from .extension_range_options import ExtensionRangeOptions  # noqa: E402
from .extension_range_options_or_builder import ExtensionRangeOptionsOrBuilder  # noqa: E402
from .extension_range_or_builder import ExtensionRangeOrBuilder  # noqa: E402
from .feature_set import FeatureSet  # noqa: E402
from .feature_set_or_builder import FeatureSetOrBuilder  # noqa: E402
from .feature_support import FeatureSupport  # noqa: E402
from .feature_support_or_builder import FeatureSupportOrBuilder  # noqa: E402
from .field_descriptor import FieldDescriptor  # noqa: E402
from .field_descriptor_proto import FieldDescriptorProto  # noqa: E402
from .field_descriptor_proto_or_builder import FieldDescriptorProtoOrBuilder  # noqa: E402
from .field_options import FieldOptions  # noqa: E402
from .field_options_or_builder import FieldOptionsOrBuilder  # noqa: E402
from .file_descriptor import FileDescriptor  # noqa: E402
from .file_descriptor_proto import FileDescriptorProto  # noqa: E402
from .file_options import FileOptions  # noqa: E402
from .file_options_or_builder import FileOptionsOrBuilder  # noqa: E402
from .location import Location  # noqa: E402
from .location_or_builder import LocationOrBuilder  # noqa: E402
from .message import Message  # noqa: E402
from .message_options_or_builder import MessageOptionsOrBuilder  # noqa: E402
from .method_descriptor import MethodDescriptor  # noqa: E402
from .method_descriptor_proto import MethodDescriptorProto  # noqa: E402
from .method_descriptor_proto_or_builder import MethodDescriptorProtoOrBuilder  # noqa: E402
from .method_options import MethodOptions  # noqa: E402
from .method_options_or_builder import MethodOptionsOrBuilder  # noqa: E402
from .name_part import NamePart  # noqa: E402
from .name_part_or_builder import NamePartOrBuilder  # noqa: E402
from .oneof_descriptor import OneofDescriptor  # noqa: E402
from .oneof_descriptor_proto import OneofDescriptorProto  # noqa: E402
from .oneof_descriptor_proto_or_builder import OneofDescriptorProtoOrBuilder  # noqa: E402
from .oneof_options import OneofOptions  # noqa: E402
from .oneof_options_or_builder import OneofOptionsOrBuilder  # noqa: E402
from .reserved_range import ReservedRange  # noqa: E402
from .reserved_range_or_builder import ReservedRangeOrBuilder  # noqa: E402
from .service_descriptor import ServiceDescriptor  # noqa: E402
from .service_descriptor_proto import ServiceDescriptorProto  # noqa: E402
from .service_descriptor_proto_or_builder import ServiceDescriptorProtoOrBuilder  # noqa: E402
from .service_options import ServiceOptions  # noqa: E402
from .service_options_or_builder import ServiceOptionsOrBuilder  # noqa: E402
from .source_code_info import SourceCodeInfo  # noqa: E402
from .source_code_info_or_builder import SourceCodeInfoOrBuilder  # noqa: E402
from .uninterpreted_option import UninterpretedOption  # noqa: E402
from .uninterpreted_option_or_builder import UninterpretedOptionOrBuilder  # noqa: E402

update_forward_refs(UnknownFieldSet, MessageOptions=MessageOptions)
update_forward_refs(Declaration, MessageOptions=MessageOptions)
update_forward_refs(DeclarationOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(Descriptor, MessageOptions=MessageOptions)
update_forward_refs(DescriptorProto, MessageOptions=MessageOptions)
update_forward_refs(DescriptorProtoOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(EditionDefault, MessageOptions=MessageOptions)
update_forward_refs(EditionDefaultOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(EnumDescriptor, MessageOptions=MessageOptions)
update_forward_refs(EnumDescriptorProto, MessageOptions=MessageOptions)
update_forward_refs(EnumDescriptorProtoOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(EnumOptions, MessageOptions=MessageOptions)
update_forward_refs(EnumOptionsOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(EnumReservedRange, MessageOptions=MessageOptions)
update_forward_refs(EnumReservedRangeOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(EnumValueDescriptor, MessageOptions=MessageOptions)
update_forward_refs(EnumValueDescriptorProto, MessageOptions=MessageOptions)
update_forward_refs(EnumValueDescriptorProtoOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(EnumValueOptions, MessageOptions=MessageOptions)
update_forward_refs(EnumValueOptionsOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(ExtensionRange, MessageOptions=MessageOptions)
update_forward_refs(ExtensionRangeOptions, MessageOptions=MessageOptions)
update_forward_refs(ExtensionRangeOptionsOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(ExtensionRangeOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(FeatureSet, MessageOptions=MessageOptions)
update_forward_refs(FeatureSetOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(FeatureSupport, MessageOptions=MessageOptions)
update_forward_refs(FeatureSupportOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(FieldDescriptor, MessageOptions=MessageOptions)
update_forward_refs(FieldDescriptorProto, MessageOptions=MessageOptions)
update_forward_refs(FieldDescriptorProtoOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(FieldOptions, MessageOptions=MessageOptions)
update_forward_refs(FieldOptionsOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(FileDescriptor, MessageOptions=MessageOptions)
update_forward_refs(FileDescriptorProto, MessageOptions=MessageOptions)
update_forward_refs(FileOptions, MessageOptions=MessageOptions)
update_forward_refs(FileOptionsOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(Location, MessageOptions=MessageOptions)
update_forward_refs(LocationOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(Message, MessageOptions=MessageOptions)
update_forward_refs(MessageLite, MessageOptions=MessageOptions)
update_forward_refs(MessageOptionsOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(MethodDescriptor, MessageOptions=MessageOptions)
update_forward_refs(MethodDescriptorProto, MessageOptions=MessageOptions)
update_forward_refs(MethodDescriptorProtoOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(MethodOptions, MessageOptions=MessageOptions)
update_forward_refs(MethodOptionsOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(NamePart, MessageOptions=MessageOptions)
update_forward_refs(NamePartOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(OneofDescriptor, MessageOptions=MessageOptions)
update_forward_refs(OneofDescriptorProto, MessageOptions=MessageOptions)
update_forward_refs(OneofDescriptorProtoOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(OneofOptions, MessageOptions=MessageOptions)
update_forward_refs(OneofOptionsOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(ReservedRange, MessageOptions=MessageOptions)
update_forward_refs(ReservedRangeOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(ServiceDescriptor, MessageOptions=MessageOptions)
update_forward_refs(ServiceDescriptorProto, MessageOptions=MessageOptions)
update_forward_refs(ServiceDescriptorProtoOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(ServiceOptions, MessageOptions=MessageOptions)
update_forward_refs(ServiceOptionsOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(SourceCodeInfo, MessageOptions=MessageOptions)
update_forward_refs(SourceCodeInfoOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(UninterpretedOption, MessageOptions=MessageOptions)
update_forward_refs(UninterpretedOptionOrBuilder, MessageOptions=MessageOptions)
update_forward_refs(MessageOptions)
