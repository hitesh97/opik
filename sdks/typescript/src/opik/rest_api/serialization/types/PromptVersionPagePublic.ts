/**
 * This file was auto-generated by Fern from our API Definition.
 */

import * as serializers from "../index";
import * as OpikApi from "../../api/index";
import * as core from "../../core";
import { PromptVersionPublic } from "./PromptVersionPublic";

export const PromptVersionPagePublic: core.serialization.ObjectSchema<
    serializers.PromptVersionPagePublic.Raw,
    OpikApi.PromptVersionPagePublic
> = core.serialization.object({
    page: core.serialization.number().optional(),
    size: core.serialization.number().optional(),
    total: core.serialization.number().optional(),
    content: core.serialization.list(PromptVersionPublic).optional(),
});

export declare namespace PromptVersionPagePublic {
    export interface Raw {
        page?: number | null;
        size?: number | null;
        total?: number | null;
        content?: PromptVersionPublic.Raw[] | null;
    }
}
