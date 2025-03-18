/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";

export const MessageOptionsOrBuilder: core.serialization.ObjectSchema<
    serializers.MessageOptionsOrBuilder.Raw,
    OpikApi.MessageOptionsOrBuilder
> = core.serialization.object({
    messageSetWireFormat: core.serialization.boolean().optional(),
    uninterpretedOptionCount: core.serialization.number().optional(),
    uninterpretedOptionList: core.serialization
        .list(core.serialization.lazyObject(() => serializers.UninterpretedOption))
        .optional(),
    noStandardDescriptorAccessor: core.serialization.boolean().optional(),
    deprecatedLegacyJsonFieldConflicts: core.serialization.boolean().optional(),
    uninterpretedOptionOrBuilderList: core.serialization
        .list(core.serialization.lazyObject(() => serializers.UninterpretedOptionOrBuilder))
        .optional(),
    featuresOrBuilder: core.serialization.lazyObject(() => serializers.FeatureSetOrBuilder).optional(),
    mapEntry: core.serialization.boolean().optional(),
    features: core.serialization.lazyObject(() => serializers.FeatureSet).optional(),
    deprecated: core.serialization.boolean().optional(),
    defaultInstanceForType: core.serialization.lazyObject(() => serializers.Message).optional(),
    initializationErrorString: core.serialization.string().optional(),
    unknownFields: core.serialization.lazyObject(() => serializers.UnknownFieldSet).optional(),
    descriptorForType: core.serialization.lazyObject(() => serializers.Descriptor).optional(),
    allFields: core.serialization
        .record(
            core.serialization.string(),
            core.serialization.record(core.serialization.string(), core.serialization.unknown()),
        )
        .optional(),
    initialized: core.serialization.boolean().optional(),
});

export declare namespace MessageOptionsOrBuilder {
    export interface Raw {
        messageSetWireFormat?: boolean | null;
        uninterpretedOptionCount?: number | null;
        uninterpretedOptionList?: serializers.UninterpretedOption.Raw[] | null;
        noStandardDescriptorAccessor?: boolean | null;
        deprecatedLegacyJsonFieldConflicts?: boolean | null;
        uninterpretedOptionOrBuilderList?: serializers.UninterpretedOptionOrBuilder.Raw[] | null;
        featuresOrBuilder?: serializers.FeatureSetOrBuilder.Raw | null;
        mapEntry?: boolean | null;
        features?: serializers.FeatureSet.Raw | null;
        deprecated?: boolean | null;
        defaultInstanceForType?: serializers.Message.Raw | null;
        initializationErrorString?: string | null;
        unknownFields?: serializers.UnknownFieldSet.Raw | null;
        descriptorForType?: serializers.Descriptor.Raw | null;
        allFields?: Record<string, Record<string, unknown>> | null;
        initialized?: boolean | null;
    }
}
