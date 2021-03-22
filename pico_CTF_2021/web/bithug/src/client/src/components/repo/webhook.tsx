import * as React from "react";

import { Icon } from "../icon";

export interface Props {
    url: string;
    uid: string;
    onDelete: () => void;
}

export const Webhook = (props: Props) => {
    return (
        <div className="bh-webhook">
            <div className="url">{ props.url }</div>
            <Icon className="delete" onClick={props.onDelete}>delete</Icon>
        </div>
    )
}