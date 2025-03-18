/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as OpikApi from "../index";

export interface AnyValueOrBuilder {
    kvlistValueOrBuilder?: OpikApi.KeyValueListOrBuilder;
    stringValueBytes?: OpikApi.ByteString;
    arrayValueOrBuilder?: OpikApi.ArrayValueOrBuilder;
    intValue?: number;
    valueCase?: OpikApi.AnyValueOrBuilderValueCase;
    boolValue?: boolean;
    arrayValue?: OpikApi.ArrayValue;
    kvlistValue?: OpikApi.KeyValueList;
    bytesValue?: OpikApi.ByteString;
    doubleValue?: number;
    stringValue?: string;
    defaultInstanceForType?: OpikApi.Message;
    initializationErrorString?: string;
    unknownFields?: OpikApi.UnknownFieldSet;
    descriptorForType?: OpikApi.Descriptor;
    allFields?: Record<string, Record<string, unknown>>;
    initialized?: boolean;
}
