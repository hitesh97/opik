/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";

export const ParserFileOptions: core.serialization.Schema<
    serializers.ParserFileOptions.Raw,
    OpikApi.ParserFileOptions
> = core.serialization.record(core.serialization.string(), core.serialization.unknown());

export declare namespace ParserFileOptions {
    export type Raw = Record<string, unknown>;
}
