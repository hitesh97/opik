# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
from .message_lite import MessageLite
from .unknown_field_set import UnknownFieldSet
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
from .field_options_or_builder_ctype import FieldOptionsOrBuilderCtype
from .field_options_or_builder_jstype import FieldOptionsOrBuilderJstype
from .field_options_or_builder_targets_list_item import (
    FieldOptionsOrBuilderTargetsListItem,
)
from .field_options_or_builder_retention import FieldOptionsOrBuilderRetention
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ..core.pydantic_utilities import update_forward_refs


class FieldOptionsOrBuilder(UniversalBaseModel):
    uninterpreted_option_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="uninterpretedOptionCount")
    ] = None
    uninterpreted_option_list: typing_extensions.Annotated[
        typing.Optional[typing.List["UninterpretedOption"]],
        FieldMetadata(alias="uninterpretedOptionList"),
    ] = None
    edition_defaults_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="editionDefaultsCount")
    ] = None
    feature_support_or_builder: typing_extensions.Annotated[
        typing.Optional["FeatureSupportOrBuilder"],
        FieldMetadata(alias="featureSupportOrBuilder"),
    ] = None
    uninterpreted_option_or_builder_list: typing_extensions.Annotated[
        typing.Optional[typing.List["UninterpretedOptionOrBuilder"]],
        FieldMetadata(alias="uninterpretedOptionOrBuilderList"),
    ] = None
    edition_defaults_or_builder_list: typing_extensions.Annotated[
        typing.Optional[typing.List["EditionDefaultOrBuilder"]],
        FieldMetadata(alias="editionDefaultsOrBuilderList"),
    ] = None
    features_or_builder: typing_extensions.Annotated[
        typing.Optional["FeatureSetOrBuilder"], FieldMetadata(alias="featuresOrBuilder")
    ] = None
    unverified_lazy: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="unverifiedLazy")
    ] = None
    targets_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="targetsCount")
    ] = None
    edition_defaults_list: typing_extensions.Annotated[
        typing.Optional[typing.List["EditionDefault"]],
        FieldMetadata(alias="editionDefaultsList"),
    ] = None
    feature_support: typing_extensions.Annotated[
        typing.Optional["FeatureSupport"], FieldMetadata(alias="featureSupport")
    ] = None
    ctype: typing.Optional[FieldOptionsOrBuilderCtype] = None
    jstype: typing.Optional[FieldOptionsOrBuilderJstype] = None
    lazy: typing.Optional[bool] = None
    weak: typing.Optional[bool] = None
    targets_list: typing_extensions.Annotated[
        typing.Optional[typing.List[FieldOptionsOrBuilderTargetsListItem]],
        FieldMetadata(alias="targetsList"),
    ] = None
    debug_redact: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="debugRedact")
    ] = None
    packed: typing.Optional[bool] = None
    features: typing.Optional["FeatureSet"] = None
    deprecated: typing.Optional[bool] = None
    retention: typing.Optional[FieldOptionsOrBuilderRetention] = None
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

update_forward_refs(Declaration, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(DeclarationOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(Descriptor, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(DescriptorProto, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(
    DescriptorProtoOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(EditionDefault, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(
    EditionDefaultOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(EnumDescriptor, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(EnumDescriptorProto, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(
    EnumDescriptorProtoOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(EnumOptions, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(EnumOptionsOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(EnumReservedRange, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(
    EnumReservedRangeOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(EnumValueDescriptor, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(
    EnumValueDescriptorProto, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(
    EnumValueDescriptorProtoOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(EnumValueOptions, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(
    EnumValueOptionsOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(ExtensionRange, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(ExtensionRangeOptions, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(
    ExtensionRangeOptionsOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(
    ExtensionRangeOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(FeatureSet, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(FeatureSetOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(FeatureSupport, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(
    FeatureSupportOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(FieldDescriptor, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(FieldDescriptorProto, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(
    FieldDescriptorProtoOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(FieldOptions, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(FileDescriptor, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(FileDescriptorProto, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(FileOptions, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(FileOptionsOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(Location, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(LocationOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(Message, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(MessageLite, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(MessageOptions, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(
    MessageOptionsOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(MethodDescriptor, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(MethodDescriptorProto, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(
    MethodDescriptorProtoOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(MethodOptions, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(MethodOptionsOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(NamePart, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(NamePartOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(OneofDescriptor, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(OneofDescriptorProto, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(
    OneofDescriptorProtoOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(OneofOptions, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(OneofOptionsOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(ReservedRange, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(ReservedRangeOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(ServiceDescriptor, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(ServiceDescriptorProto, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(
    ServiceDescriptorProtoOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(ServiceOptions, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(
    ServiceOptionsOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(SourceCodeInfo, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(
    SourceCodeInfoOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(UninterpretedOption, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(
    UninterpretedOptionOrBuilder, FieldOptionsOrBuilder=FieldOptionsOrBuilder
)
update_forward_refs(UnknownFieldSet, FieldOptionsOrBuilder=FieldOptionsOrBuilder)
update_forward_refs(FieldOptionsOrBuilder)
