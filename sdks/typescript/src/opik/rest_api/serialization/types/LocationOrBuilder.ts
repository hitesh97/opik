/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";
import { ByteString } from "./ByteString";

export const LocationOrBuilder: core.serialization.ObjectSchema<
    serializers.LocationOrBuilder.Raw,
    OpikApi.LocationOrBuilder
> = core.serialization.object({
    leadingDetachedCommentsList: core.serialization.list(core.serialization.string()).optional(),
    leadingCommentsBytes: ByteString.optional(),
    trailingCommentsBytes: ByteString.optional(),
    leadingDetachedCommentsCount: core.serialization.number().optional(),
    leadingComments: core.serialization.string().optional(),
    trailingComments: core.serialization.string().optional(),
    spanList: core.serialization.list(core.serialization.number()).optional(),
    pathList: core.serialization.list(core.serialization.number()).optional(),
    pathCount: core.serialization.number().optional(),
    spanCount: core.serialization.number().optional(),
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

export declare namespace LocationOrBuilder {
    export interface Raw {
        leadingDetachedCommentsList?: string[] | null;
        leadingCommentsBytes?: ByteString.Raw | null;
        trailingCommentsBytes?: ByteString.Raw | null;
        leadingDetachedCommentsCount?: number | null;
        leadingComments?: string | null;
        trailingComments?: string | null;
        spanList?: number[] | null;
        pathList?: number[] | null;
        pathCount?: number | null;
        spanCount?: number | null;
        defaultInstanceForType?: serializers.Message.Raw | null;
        initializationErrorString?: string | null;
        unknownFields?: serializers.UnknownFieldSet.Raw | null;
        descriptorForType?: serializers.Descriptor.Raw | null;
        allFields?: Record<string, Record<string, unknown>> | null;
        initialized?: boolean | null;
    }
}
