/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";

export const ParserOneofDescriptorProto: core.serialization.Schema<
    serializers.ParserOneofDescriptorProto.Raw,
    OpikApi.ParserOneofDescriptorProto
> = core.serialization.record(core.serialization.string(), core.serialization.unknown());

export declare namespace ParserOneofDescriptorProto {
    export type Raw = Record<string, unknown>;
}
