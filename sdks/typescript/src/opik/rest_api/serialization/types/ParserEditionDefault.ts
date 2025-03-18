/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";

export const ParserEditionDefault: core.serialization.Schema<
    serializers.ParserEditionDefault.Raw,
    OpikApi.ParserEditionDefault
> = core.serialization.record(core.serialization.string(), core.serialization.unknown());

export declare namespace ParserEditionDefault {
    export type Raw = Record<string, unknown>;
}
