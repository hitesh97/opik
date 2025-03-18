/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as OpikApi from "../index";

export interface KeyValue {
    unknownFields?: OpikApi.UnknownFieldSet;
    value?: OpikApi.AnyValue;
    key?: string;
    defaultInstanceForType?: OpikApi.KeyValue;
    valueOrBuilder?: OpikApi.AnyValueOrBuilder;
    serializedSize?: number;
    parserForType?: OpikApi.ParserKeyValue;
    keyBytes?: OpikApi.ByteString;
    initialized?: boolean;
    initializationErrorString?: string;
    descriptorForType?: OpikApi.Descriptor;
    allFields?: Record<string, Record<string, unknown>>;
    memoizedSerializedSize?: number;
}
