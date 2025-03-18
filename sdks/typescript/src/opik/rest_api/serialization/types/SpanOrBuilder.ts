/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";
import { KeyValueOrBuilder } from "./KeyValueOrBuilder";
import { ByteString } from "./ByteString";
import { EventOrBuilder } from "./EventOrBuilder";
import { LinkOrBuilder } from "./LinkOrBuilder";
import { StatusOrBuilder } from "./StatusOrBuilder";
import { SpanOrBuilderKind } from "./SpanOrBuilderKind";

export const SpanOrBuilder: core.serialization.ObjectSchema<serializers.SpanOrBuilder.Raw, OpikApi.SpanOrBuilder> =
    core.serialization.object({
        name: core.serialization.string().optional(),
        flags: core.serialization.number().optional(),
        droppedAttributesCount: core.serialization.number().optional(),
        attributesOrBuilderList: core.serialization.list(KeyValueOrBuilder).optional(),
        traceStateBytes: ByteString.optional(),
        parentSpanId: ByteString.optional(),
        startTimeUnixNano: core.serialization.number().optional(),
        endTimeUnixNano: core.serialization.number().optional(),
        eventsOrBuilderList: core.serialization.list(EventOrBuilder).optional(),
        droppedEventsCount: core.serialization.number().optional(),
        linksOrBuilderList: core.serialization.list(LinkOrBuilder).optional(),
        droppedLinksCount: core.serialization.number().optional(),
        statusOrBuilder: StatusOrBuilder.optional(),
        attributesList: core.serialization.list(core.serialization.lazyObject(() => serializers.KeyValue)).optional(),
        attributesCount: core.serialization.number().optional(),
        traceId: ByteString.optional(),
        spanId: ByteString.optional(),
        traceState: core.serialization.string().optional(),
        kindValue: core.serialization.number().optional(),
        eventsList: core.serialization.list(core.serialization.lazyObject(() => serializers.Event)).optional(),
        eventsCount: core.serialization.number().optional(),
        linksList: core.serialization.list(core.serialization.lazyObject(() => serializers.Link)).optional(),
        linksCount: core.serialization.number().optional(),
        nameBytes: ByteString.optional(),
        kind: SpanOrBuilderKind.optional(),
        status: core.serialization.lazyObject(() => serializers.Status).optional(),
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

export declare namespace SpanOrBuilder {
    export interface Raw {
        name?: string | null;
        flags?: number | null;
        droppedAttributesCount?: number | null;
        attributesOrBuilderList?: KeyValueOrBuilder.Raw[] | null;
        traceStateBytes?: ByteString.Raw | null;
        parentSpanId?: ByteString.Raw | null;
        startTimeUnixNano?: number | null;
        endTimeUnixNano?: number | null;
        eventsOrBuilderList?: EventOrBuilder.Raw[] | null;
        droppedEventsCount?: number | null;
        linksOrBuilderList?: LinkOrBuilder.Raw[] | null;
        droppedLinksCount?: number | null;
        statusOrBuilder?: StatusOrBuilder.Raw | null;
        attributesList?: serializers.KeyValue.Raw[] | null;
        attributesCount?: number | null;
        traceId?: ByteString.Raw | null;
        spanId?: ByteString.Raw | null;
        traceState?: string | null;
        kindValue?: number | null;
        eventsList?: serializers.Event.Raw[] | null;
        eventsCount?: number | null;
        linksList?: serializers.Link.Raw[] | null;
        linksCount?: number | null;
        nameBytes?: ByteString.Raw | null;
        kind?: SpanOrBuilderKind.Raw | null;
        status?: serializers.Status.Raw | null;
        defaultInstanceForType?: serializers.Message.Raw | null;
        initializationErrorString?: string | null;
        unknownFields?: serializers.UnknownFieldSet.Raw | null;
        descriptorForType?: serializers.Descriptor.Raw | null;
        allFields?: Record<string, Record<string, unknown>> | null;
        initialized?: boolean | null;
    }
}
