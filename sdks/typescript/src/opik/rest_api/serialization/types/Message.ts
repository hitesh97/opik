/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";
import { ParserMessage } from "./ParserMessage";

export const Message: core.serialization.ObjectSchema<serializers.Message.Raw, OpikApi.Message> =
    core.serialization.object({
        parserForType: ParserMessage.optional(),
        serializedSize: core.serialization.number().optional(),
        defaultInstanceForType: core.serialization.lazyObject(() => serializers.MessageLite).optional(),
        initialized: core.serialization.boolean().optional(),
        initializationErrorString: core.serialization.string().optional(),
        unknownFields: core.serialization.lazyObject(() => serializers.UnknownFieldSet).optional(),
        descriptorForType: core.serialization.lazyObject(() => serializers.Descriptor).optional(),
        allFields: core.serialization
            .record(
                core.serialization.string(),
                core.serialization.record(core.serialization.string(), core.serialization.unknown()),
            )
            .optional(),
    });

export declare namespace Message {
    export interface Raw {
        parserForType?: ParserMessage.Raw | null;
        serializedSize?: number | null;
        defaultInstanceForType?: serializers.MessageLite.Raw | null;
        initialized?: boolean | null;
        initializationErrorString?: string | null;
        unknownFields?: serializers.UnknownFieldSet.Raw | null;
        descriptorForType?: serializers.Descriptor.Raw | null;
        allFields?: Record<string, Record<string, unknown>> | null;
    }
}
