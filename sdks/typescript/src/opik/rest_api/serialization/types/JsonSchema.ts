/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";
import { JsonObjectSchema } from "./JsonObjectSchema";

export const JsonSchema: core.serialization.ObjectSchema<serializers.JsonSchema.Raw, OpikApi.JsonSchema> =
    core.serialization.object({
        name: core.serialization.string().optional(),
        strict: core.serialization.boolean().optional(),
        schema: JsonObjectSchema.optional(),
    });

export declare namespace JsonSchema {
    export interface Raw {
        name?: string | null;
        strict?: boolean | null;
        schema?: JsonObjectSchema.Raw | null;
    }
}
