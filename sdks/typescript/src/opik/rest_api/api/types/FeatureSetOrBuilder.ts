/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as OpikApi from "../index";

export interface FeatureSetOrBuilder {
    repeatedFieldEncoding?: OpikApi.FeatureSetOrBuilderRepeatedFieldEncoding;
    enforceNamingStyle?: OpikApi.FeatureSetOrBuilderEnforceNamingStyle;
    messageEncoding?: OpikApi.FeatureSetOrBuilderMessageEncoding;
    utf8Validation?: OpikApi.FeatureSetOrBuilderUtf8Validation;
    fieldPresence?: OpikApi.FeatureSetOrBuilderFieldPresence;
    jsonFormat?: OpikApi.FeatureSetOrBuilderJsonFormat;
    enumType?: OpikApi.FeatureSetOrBuilderEnumType;
    defaultInstanceForType?: OpikApi.Message;
    initializationErrorString?: string;
    unknownFields?: OpikApi.UnknownFieldSet;
    descriptorForType?: OpikApi.Descriptor;
    allFields?: Record<string, Record<string, unknown>>;
    initialized?: boolean;
}
