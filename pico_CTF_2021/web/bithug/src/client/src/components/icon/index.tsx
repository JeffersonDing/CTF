import * as React from "react";

import { classes } from "react-pwn/";

import "./index.scss";

export interface Props {
    className?: string;
    children: string;
    onClick?: () => void;
}

export const Icon = (props: Props) => (
    <i className={classes("material-icon", props.className)} onClick={props.onClick}>{ props.children }</i>
);
