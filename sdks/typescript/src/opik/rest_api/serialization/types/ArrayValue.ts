/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";
import { ParserArrayValue } from "./ParserArrayValue";

export const ArrayValue: core.serialization.ObjectSchema<serializers.ArrayValue.Raw, OpikApi.ArrayValue> =
    core.serialization.object({
        unknownFields: core.serialization.lazyObject(() => serializers.UnknownFieldSet).optional(),
        defaultInstanceForType: core.serialization.lazyObject(() => serializers.ArrayValue).optional(),
        valuesOrBuilderList: core.serialization
            .list(core.serialization.lazyObject(() => serializers.AnyValueOrBuilder))
            .optional(),
        serializedSize: core.serialization.number().optional(),
        parserForType: ParserArrayValue.optional(),
        valuesCount: core.serialization.number().optional(),
        initialized: core.serialization.boolean().optional(),
        valuesList: core.serialization.list(core.serialization.lazyObject(() => serializers.AnyValue)).optional(),
        initializationErrorString: core.serialization.string().optional(),
        descriptorForType: core.serialization.lazyObject(() => serializers.Descriptor).optional(),
        allFields: core.serialization
            .record(
                core.serialization.string(),
                core.serialization.record(core.serialization.string(), core.serialization.unknown()),
            )
            .optional(),
        memoizedSerializedSize: core.serialization.number().optional(),
    });

export declare namespace ArrayValue {
    export interface Raw {
        unknownFields?: serializers.UnknownFieldSet.Raw | null;
        defaultInstanceForType?: serializers.ArrayValue.Raw | null;
        valuesOrBuilderList?: serializers.AnyValueOrBuilder.Raw[] | null;
        serializedSize?: number | null;
        parserForType?: ParserArrayValue.Raw | null;
        valuesCount?: number | null;
        initialized?: boolean | null;
        valuesList?: serializers.AnyValue.Raw[] | null;
        initializationErrorString?: string | null;
        descriptorForType?: serializers.Descriptor.Raw | null;
        allFields?: Record<string, Record<string, unknown>> | null;
        memoizedSerializedSize?: number | null;
    }
}
