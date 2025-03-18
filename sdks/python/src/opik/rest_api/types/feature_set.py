# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
from .unknown_field_set import UnknownFieldSet
from .message_lite import MessageLite
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
from .feature_set_repeated_field_encoding import FeatureSetRepeatedFieldEncoding
from .feature_set_enforce_naming_style import FeatureSetEnforceNamingStyle
from .feature_set_message_encoding import FeatureSetMessageEncoding
from .feature_set_utf_8_validation import FeatureSetUtf8Validation
from .feature_set_field_presence import FeatureSetFieldPresence
from .parser_feature_set import ParserFeatureSet
from .feature_set_json_format import FeatureSetJsonFormat
from .feature_set_enum_type import FeatureSetEnumType
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ..core.pydantic_utilities import update_forward_refs


class FeatureSet(UniversalBaseModel):
    unknown_fields: typing_extensions.Annotated[
        typing.Optional[UnknownFieldSet], FieldMetadata(alias="unknownFields")
    ] = None
    default_instance_for_type: typing_extensions.Annotated[
        typing.Optional["FeatureSet"], FieldMetadata(alias="defaultInstanceForType")
    ] = None
    repeated_field_encoding: typing_extensions.Annotated[
        typing.Optional[FeatureSetRepeatedFieldEncoding],
        FieldMetadata(alias="repeatedFieldEncoding"),
    ] = None
    enforce_naming_style: typing_extensions.Annotated[
        typing.Optional[FeatureSetEnforceNamingStyle],
        FieldMetadata(alias="enforceNamingStyle"),
    ] = None
    message_encoding: typing_extensions.Annotated[
        typing.Optional[FeatureSetMessageEncoding],
        FieldMetadata(alias="messageEncoding"),
    ] = None
    utf_8_validation: typing_extensions.Annotated[
        typing.Optional[FeatureSetUtf8Validation], FieldMetadata(alias="utf8Validation")
    ] = None
    field_presence: typing_extensions.Annotated[
        typing.Optional[FeatureSetFieldPresence], FieldMetadata(alias="fieldPresence")
    ] = None
    serialized_size: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="serializedSize")
    ] = None
    parser_for_type: typing_extensions.Annotated[
        typing.Optional[ParserFeatureSet], FieldMetadata(alias="parserForType")
    ] = None
    json_format: typing_extensions.Annotated[
        typing.Optional[FeatureSetJsonFormat], FieldMetadata(alias="jsonFormat")
    ] = None
    enum_type: typing_extensions.Annotated[
        typing.Optional[FeatureSetEnumType], FieldMetadata(alias="enumType")
    ] = None
    initialized: typing.Optional[bool] = None
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
from .message_options import MessageOptions  # noqa: E402
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

update_forward_refs(UnknownFieldSet, FeatureSet=FeatureSet)
update_forward_refs(Declaration, FeatureSet=FeatureSet)
update_forward_refs(DeclarationOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(Descriptor, FeatureSet=FeatureSet)
update_forward_refs(DescriptorProto, FeatureSet=FeatureSet)
update_forward_refs(DescriptorProtoOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(EditionDefault, FeatureSet=FeatureSet)
update_forward_refs(EditionDefaultOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(EnumDescriptor, FeatureSet=FeatureSet)
update_forward_refs(EnumDescriptorProto, FeatureSet=FeatureSet)
update_forward_refs(EnumDescriptorProtoOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(EnumOptions, FeatureSet=FeatureSet)
update_forward_refs(EnumOptionsOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(EnumReservedRange, FeatureSet=FeatureSet)
update_forward_refs(EnumReservedRangeOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(EnumValueDescriptor, FeatureSet=FeatureSet)
update_forward_refs(EnumValueDescriptorProto, FeatureSet=FeatureSet)
update_forward_refs(EnumValueDescriptorProtoOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(EnumValueOptions, FeatureSet=FeatureSet)
update_forward_refs(EnumValueOptionsOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(ExtensionRange, FeatureSet=FeatureSet)
update_forward_refs(ExtensionRangeOptions, FeatureSet=FeatureSet)
update_forward_refs(ExtensionRangeOptionsOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(ExtensionRangeOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(FeatureSetOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(FeatureSupport, FeatureSet=FeatureSet)
update_forward_refs(FeatureSupportOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(FieldDescriptor, FeatureSet=FeatureSet)
update_forward_refs(FieldDescriptorProto, FeatureSet=FeatureSet)
update_forward_refs(FieldDescriptorProtoOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(FieldOptions, FeatureSet=FeatureSet)
update_forward_refs(FieldOptionsOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(FileDescriptor, FeatureSet=FeatureSet)
update_forward_refs(FileDescriptorProto, FeatureSet=FeatureSet)
update_forward_refs(FileOptions, FeatureSet=FeatureSet)
update_forward_refs(FileOptionsOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(Location, FeatureSet=FeatureSet)
update_forward_refs(LocationOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(Message, FeatureSet=FeatureSet)
update_forward_refs(MessageLite, FeatureSet=FeatureSet)
update_forward_refs(MessageOptions, FeatureSet=FeatureSet)
update_forward_refs(MessageOptionsOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(MethodDescriptor, FeatureSet=FeatureSet)
update_forward_refs(MethodDescriptorProto, FeatureSet=FeatureSet)
update_forward_refs(MethodDescriptorProtoOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(MethodOptions, FeatureSet=FeatureSet)
update_forward_refs(MethodOptionsOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(NamePart, FeatureSet=FeatureSet)
update_forward_refs(NamePartOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(OneofDescriptor, FeatureSet=FeatureSet)
update_forward_refs(OneofDescriptorProto, FeatureSet=FeatureSet)
update_forward_refs(OneofDescriptorProtoOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(OneofOptions, FeatureSet=FeatureSet)
update_forward_refs(OneofOptionsOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(ReservedRange, FeatureSet=FeatureSet)
update_forward_refs(ReservedRangeOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(ServiceDescriptor, FeatureSet=FeatureSet)
update_forward_refs(ServiceDescriptorProto, FeatureSet=FeatureSet)
update_forward_refs(ServiceDescriptorProtoOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(ServiceOptions, FeatureSet=FeatureSet)
update_forward_refs(ServiceOptionsOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(SourceCodeInfo, FeatureSet=FeatureSet)
update_forward_refs(SourceCodeInfoOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(UninterpretedOption, FeatureSet=FeatureSet)
update_forward_refs(UninterpretedOptionOrBuilder, FeatureSet=FeatureSet)
update_forward_refs(FeatureSet)
