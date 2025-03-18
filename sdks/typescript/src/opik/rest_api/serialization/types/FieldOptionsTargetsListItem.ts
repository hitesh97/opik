/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";

export const FieldOptionsTargetsListItem: core.serialization.Schema<
    serializers.FieldOptionsTargetsListItem.Raw,
    OpikApi.FieldOptionsTargetsListItem
> = core.serialization.enum_([
    "TARGET_TYPE_UNKNOWN",
    "TARGET_TYPE_FILE",
    "TARGET_TYPE_EXTENSION_RANGE",
    "TARGET_TYPE_MESSAGE",
    "TARGET_TYPE_FIELD",
    "TARGET_TYPE_ONEOF",
    "TARGET_TYPE_ENUM",
    "TARGET_TYPE_ENUM_ENTRY",
    "TARGET_TYPE_SERVICE",
    "TARGET_TYPE_METHOD",
]);

export declare namespace FieldOptionsTargetsListItem {
    export type Raw =
        | "TARGET_TYPE_UNKNOWN"
        | "TARGET_TYPE_FILE"
        | "TARGET_TYPE_EXTENSION_RANGE"
        | "TARGET_TYPE_MESSAGE"
        | "TARGET_TYPE_FIELD"
        | "TARGET_TYPE_ONEOF"
        | "TARGET_TYPE_ENUM"
        | "TARGET_TYPE_ENUM_ENTRY"
        | "TARGET_TYPE_SERVICE"
        | "TARGET_TYPE_METHOD";
}
