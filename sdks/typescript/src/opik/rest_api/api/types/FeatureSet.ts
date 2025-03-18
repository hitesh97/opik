/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as OpikApi from "../index";

export interface FeatureSet {
    unknownFields?: OpikApi.UnknownFieldSet;
    defaultInstanceForType?: OpikApi.FeatureSet;
    repeatedFieldEncoding?: OpikApi.FeatureSetRepeatedFieldEncoding;
    enforceNamingStyle?: OpikApi.FeatureSetEnforceNamingStyle;
    messageEncoding?: OpikApi.FeatureSetMessageEncoding;
    utf8Validation?: OpikApi.FeatureSetUtf8Validation;
    fieldPresence?: OpikApi.FeatureSetFieldPresence;
    serializedSize?: number;
    parserForType?: OpikApi.ParserFeatureSet;
    jsonFormat?: OpikApi.FeatureSetJsonFormat;
    enumType?: OpikApi.FeatureSetEnumType;
    initialized?: boolean;
    initializationErrorString?: string;
    descriptorForType?: OpikApi.Descriptor;
    allFields?: Record<string, Record<string, unknown>>;
    allFieldsRaw?: Record<string, Record<string, unknown>>;
    memoizedSerializedSize?: number;
}
