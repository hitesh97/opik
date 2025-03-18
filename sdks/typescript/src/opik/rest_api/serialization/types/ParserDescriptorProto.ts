/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";

export const ParserDescriptorProto: core.serialization.Schema<
    serializers.ParserDescriptorProto.Raw,
    OpikApi.ParserDescriptorProto
> = core.serialization.record(core.serialization.string(), core.serialization.unknown());

export declare namespace ParserDescriptorProto {
    export type Raw = Record<string, unknown>;
}
