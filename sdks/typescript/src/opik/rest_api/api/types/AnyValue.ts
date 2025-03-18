/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as OpikApi from "../index";

export interface AnyValue {
    unknownFields?: OpikApi.UnknownFieldSet;
    defaultInstanceForType?: OpikApi.AnyValue;
    kvlistValueOrBuilder?: OpikApi.KeyValueListOrBuilder;
    stringValueBytes?: OpikApi.ByteString;
    arrayValueOrBuilder?: OpikApi.ArrayValueOrBuilder;
    serializedSize?: number;
    parserForType?: OpikApi.ParserAnyValue;
    intValue?: number;
    valueCase?: OpikApi.AnyValueValueCase;
    boolValue?: boolean;
    arrayValue?: OpikApi.ArrayValue;
    kvlistValue?: OpikApi.KeyValueList;
    bytesValue?: OpikApi.ByteString;
    doubleValue?: number;
    initialized?: boolean;
    stringValue?: string;
    initializationErrorString?: string;
    descriptorForType?: OpikApi.Descriptor;
    allFields?: Record<string, Record<string, unknown>>;
    memoizedSerializedSize?: number;
}
