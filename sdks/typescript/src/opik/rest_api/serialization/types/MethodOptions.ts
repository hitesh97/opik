/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";
import { MethodOptionsIdempotencyLevel } from "./MethodOptionsIdempotencyLevel";
import { ParserMethodOptions } from "./ParserMethodOptions";

export const MethodOptions: core.serialization.ObjectSchema<serializers.MethodOptions.Raw, OpikApi.MethodOptions> =
    core.serialization.object({
        unknownFields: core.serialization.lazyObject(() => serializers.UnknownFieldSet).optional(),
        defaultInstanceForType: core.serialization.lazyObject(() => serializers.MethodOptions).optional(),
        uninterpretedOptionCount: core.serialization.number().optional(),
        uninterpretedOptionList: core.serialization
            .list(core.serialization.lazyObject(() => serializers.UninterpretedOption))
            .optional(),
        uninterpretedOptionOrBuilderList: core.serialization
            .list(core.serialization.lazyObject(() => serializers.UninterpretedOptionOrBuilder))
            .optional(),
        featuresOrBuilder: core.serialization.lazyObject(() => serializers.FeatureSetOrBuilder).optional(),
        idempotencyLevel: MethodOptionsIdempotencyLevel.optional(),
        serializedSize: core.serialization.number().optional(),
        parserForType: ParserMethodOptions.optional(),
        features: core.serialization.lazyObject(() => serializers.FeatureSet).optional(),
        initialized: core.serialization.boolean().optional(),
        deprecated: core.serialization.boolean().optional(),
        allFieldsRaw: core.serialization
            .record(
                core.serialization.string(),
                core.serialization.record(core.serialization.string(), core.serialization.unknown()),
            )
            .optional(),
        allFields: core.serialization
            .record(
                core.serialization.string(),
                core.serialization.record(core.serialization.string(), core.serialization.unknown()),
            )
            .optional(),
        initializationErrorString: core.serialization.string().optional(),
        descriptorForType: core.serialization.lazyObject(() => serializers.Descriptor).optional(),
        memoizedSerializedSize: core.serialization.number().optional(),
    });

export declare namespace MethodOptions {
    export interface Raw {
        unknownFields?: serializers.UnknownFieldSet.Raw | null;
        defaultInstanceForType?: serializers.MethodOptions.Raw | null;
        uninterpretedOptionCount?: number | null;
        uninterpretedOptionList?: serializers.UninterpretedOption.Raw[] | null;
        uninterpretedOptionOrBuilderList?: serializers.UninterpretedOptionOrBuilder.Raw[] | null;
        featuresOrBuilder?: serializers.FeatureSetOrBuilder.Raw | null;
        idempotencyLevel?: MethodOptionsIdempotencyLevel.Raw | null;
        serializedSize?: number | null;
        parserForType?: ParserMethodOptions.Raw | null;
        features?: serializers.FeatureSet.Raw | null;
        initialized?: boolean | null;
        deprecated?: boolean | null;
        allFieldsRaw?: Record<string, Record<string, unknown>> | null;
        allFields?: Record<string, Record<string, unknown>> | null;
        initializationErrorString?: string | null;
        descriptorForType?: serializers.Descriptor.Raw | null;
        memoizedSerializedSize?: number | null;
    }
}
