/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";

export const FeatureSetEnumType: core.serialization.Schema<
    serializers.FeatureSetEnumType.Raw,
    OpikApi.FeatureSetEnumType
> = core.serialization.enum_(["ENUM_TYPE_UNKNOWN", "OPEN", "CLOSED"]);

export declare namespace FeatureSetEnumType {
    export type Raw = "ENUM_TYPE_UNKNOWN" | "OPEN" | "CLOSED";
}
