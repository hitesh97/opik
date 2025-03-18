/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as OpikApi from "../index";

export interface Status {
    unknownFields?: OpikApi.UnknownFieldSet;
    message?: string;
    defaultInstanceForType?: OpikApi.Status;
    messageBytes?: OpikApi.ByteString;
    serializedSize?: number;
    parserForType?: OpikApi.ParserStatus;
    codeValue?: number;
    code?: OpikApi.StatusCode;
    initialized?: boolean;
    initializationErrorString?: string;
    descriptorForType?: OpikApi.Descriptor;
    allFields?: Record<string, Record<string, unknown>>;
    memoizedSerializedSize?: number;
}
