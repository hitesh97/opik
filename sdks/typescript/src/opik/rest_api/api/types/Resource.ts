/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as OpikApi from "../index";

export interface Resource {
    unknownFields?: OpikApi.UnknownFieldSet;
    defaultInstanceForType?: OpikApi.Resource;
    droppedAttributesCount?: number;
    attributesOrBuilderList?: OpikApi.KeyValueOrBuilder[];
    attributesList?: OpikApi.KeyValue[];
    attributesCount?: number;
    serializedSize?: number;
    parserForType?: OpikApi.ParserResource;
    initialized?: boolean;
    initializationErrorString?: string;
    descriptorForType?: OpikApi.Descriptor;
    allFields?: Record<string, Record<string, unknown>>;
    memoizedSerializedSize?: number;
}
