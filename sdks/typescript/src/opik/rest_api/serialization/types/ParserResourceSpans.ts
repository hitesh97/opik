/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";

export const ParserResourceSpans: core.serialization.Schema<
    serializers.ParserResourceSpans.Raw,
    OpikApi.ParserResourceSpans
> = core.serialization.record(core.serialization.string(), core.serialization.unknown());

export declare namespace ParserResourceSpans {
    export type Raw = Record<string, unknown>;
}
