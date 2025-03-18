# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
from .message_lite import MessageLite
from .unknown_field_set import UnknownFieldSet
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ..core.pydantic_utilities import update_forward_refs


class EnumValueOptionsOrBuilder(UniversalBaseModel):
    uninterpreted_option_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="uninterpretedOptionCount")
    ] = None
    uninterpreted_option_list: typing_extensions.Annotated[
        typing.Optional[typing.List["UninterpretedOption"]],
        FieldMetadata(alias="uninterpretedOptionList"),
    ] = None
    feature_support_or_builder: typing_extensions.Annotated[
        typing.Optional["FeatureSupportOrBuilder"],
        FieldMetadata(alias="featureSupportOrBuilder"),
    ] = None
    uninterpreted_option_or_builder_list: typing_extensions.Annotated[
        typing.Optional[typing.List["UninterpretedOptionOrBuilder"]],
        FieldMetadata(alias="uninterpretedOptionOrBuilderList"),
    ] = None
    features_or_builder: typing_extensions.Annotated[
        typing.Optional["FeatureSetOrBuilder"], FieldMetadata(alias="featuresOrBuilder")
    ] = None
    feature_support: typing_extensions.Annotated[
        typing.Optional["FeatureSupport"], FieldMetadata(alias="featureSupport")
    ] = None
    debug_redact: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="debugRedact")
    ] = None
    features: typing.Optional["FeatureSet"] = None
    deprecated: typing.Optional[bool] = None
    default_instance_for_type: typing_extensions.Annotated[
        typing.Optional["Message"], FieldMetadata(alias="defaultInstanceForType")
    ] = None
    initialization_error_string: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="initializationErrorString")
    ] = None
    unknown_fields: typing_extensions.Annotated[
        typing.Optional[UnknownFieldSet], FieldMetadata(alias="unknownFields")
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
    initialized: typing.Optional[bool] = None

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

update_forward_refs(Declaration, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    DeclarationOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(Descriptor, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    DescriptorProto, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    DescriptorProtoOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(EditionDefault, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    EditionDefaultOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(EnumDescriptor, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    EnumDescriptorProto, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    EnumDescriptorProtoOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(EnumOptions, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    EnumOptionsOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    EnumReservedRange, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    EnumReservedRangeOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    EnumValueDescriptor, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    EnumValueDescriptorProto, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    EnumValueDescriptorProtoOrBuilder,
    EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder,
)
update_forward_refs(
    EnumValueOptions, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(ExtensionRange, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    ExtensionRangeOptions, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    ExtensionRangeOptionsOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    ExtensionRangeOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(FeatureSet, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    FeatureSetOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(FeatureSupport, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    FeatureSupportOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    FieldDescriptor, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    FieldDescriptorProto, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    FieldDescriptorProtoOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(FieldOptions, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    FieldOptionsOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(FileDescriptor, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    FileDescriptorProto, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(FileOptions, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    FileOptionsOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(Location, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    LocationOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(Message, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(MessageLite, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(MessageOptions, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    MessageOptionsOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    MethodDescriptor, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    MethodDescriptorProto, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    MethodDescriptorProtoOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(MethodOptions, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    MethodOptionsOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(NamePart, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    NamePartOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    OneofDescriptor, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    OneofDescriptorProto, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    OneofDescriptorProtoOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(OneofOptions, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    OneofOptionsOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(ReservedRange, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    ReservedRangeOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    ServiceDescriptor, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    ServiceDescriptorProto, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    ServiceDescriptorProtoOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(ServiceOptions, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    ServiceOptionsOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(SourceCodeInfo, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder)
update_forward_refs(
    SourceCodeInfoOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    UninterpretedOption, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    UninterpretedOptionOrBuilder, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(
    UnknownFieldSet, EnumValueOptionsOrBuilder=EnumValueOptionsOrBuilder
)
update_forward_refs(EnumValueOptionsOrBuilder)
