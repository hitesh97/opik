/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as OpikApi from "../index";

export interface FieldDescriptorProto {
    unknownFields?: OpikApi.UnknownFieldSet;
    name?: string;
    typeName?: string;
    type?: OpikApi.FieldDescriptorProtoType;
    defaultValue?: string;
    number?: number;
    label?: OpikApi.FieldDescriptorProtoLabel;
    defaultInstanceForType?: OpikApi.FieldDescriptorProto;
    optionsOrBuilder?: OpikApi.FieldOptionsOrBuilder;
    proto3Optional?: boolean;
    typeNameBytes?: OpikApi.ByteString;
    extendeeBytes?: OpikApi.ByteString;
    defaultValueBytes?: OpikApi.ByteString;
    jsonNameBytes?: OpikApi.ByteString;
    serializedSize?: number;
    parserForType?: OpikApi.ParserFieldDescriptorProto;
    jsonName?: string;
    oneofIndex?: number;
    extendee?: string;
    nameBytes?: OpikApi.ByteString;
    initialized?: boolean;
    options?: OpikApi.FieldOptions;
    initializationErrorString?: string;
    descriptorForType?: OpikApi.Descriptor;
    allFields?: Record<string, Record<string, unknown>>;
    memoizedSerializedSize?: number;
}
