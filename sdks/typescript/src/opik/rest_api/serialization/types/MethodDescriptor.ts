/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";

export const MethodDescriptor: core.serialization.ObjectSchema<
    serializers.MethodDescriptor.Raw,
    OpikApi.MethodDescriptor
> = core.serialization.object({
    index: core.serialization.number().optional(),
    proto: core.serialization.lazyObject(() => serializers.MethodDescriptorProto).optional(),
    options: core.serialization.lazyObject(() => serializers.MethodOptions).optional(),
    fullName: core.serialization.string().optional(),
    file: core.serialization.lazyObject(() => serializers.FileDescriptor).optional(),
    service: core.serialization.lazyObject(() => serializers.ServiceDescriptor).optional(),
    inputType: core.serialization.lazyObject(() => serializers.Descriptor).optional(),
    outputType: core.serialization.lazyObject(() => serializers.Descriptor).optional(),
    name: core.serialization.string().optional(),
    clientStreaming: core.serialization.boolean().optional(),
    serverStreaming: core.serialization.boolean().optional(),
});

export declare namespace MethodDescriptor {
    export interface Raw {
        index?: number | null;
        proto?: serializers.MethodDescriptorProto.Raw | null;
        options?: serializers.MethodOptions.Raw | null;
        fullName?: string | null;
        file?: serializers.FileDescriptor.Raw | null;
        service?: serializers.ServiceDescriptor.Raw | null;
        inputType?: serializers.Descriptor.Raw | null;
        outputType?: serializers.Descriptor.Raw | null;
        name?: string | null;
        clientStreaming?: boolean | null;
        serverStreaming?: boolean | null;
    }
}
