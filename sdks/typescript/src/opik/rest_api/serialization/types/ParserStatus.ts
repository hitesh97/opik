/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";

export const ParserStatus: core.serialization.Schema<serializers.ParserStatus.Raw, OpikApi.ParserStatus> =
    core.serialization.record(core.serialization.string(), core.serialization.unknown());

export declare namespace ParserStatus {
    export type Raw = Record<string, unknown>;
}
