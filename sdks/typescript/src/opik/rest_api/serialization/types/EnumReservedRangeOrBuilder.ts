/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";

export const EnumReservedRangeOrBuilder: core.serialization.ObjectSchema<
    serializers.EnumReservedRangeOrBuilder.Raw,
    OpikApi.EnumReservedRangeOrBuilder
> = core.serialization.object({
    start: core.serialization.number().optional(),
    end: core.serialization.number().optional(),
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

export declare namespace EnumReservedRangeOrBuilder {
    export interface Raw {
        start?: number | null;
        end?: number | null;
        defaultInstanceForType?: serializers.Message.Raw | null;
        initializationErrorString?: string | null;
        unknownFields?: serializers.UnknownFieldSet.Raw | null;
        descriptorForType?: serializers.Descriptor.Raw | null;
        allFields?: Record<string, Record<string, unknown>> | null;
        initialized?: boolean | null;
    }
}
