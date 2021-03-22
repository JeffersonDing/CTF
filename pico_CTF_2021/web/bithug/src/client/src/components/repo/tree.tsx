import * as React from "react";

import { File } from "@bithug/server/dist/git"
import { classes } from "react-pwn";

import { Path } from "../../providers/repo-provider";
import { Icon } from "../icon";

export interface Props {
    tree: File[];
    path: Path;
    changeDir: (path: Path, kind: "tree" | "blob") => void;
}

export const Tree = (props: Props) => {
    const sortedTree = props.tree
        .sort((f1, f2) => {
            if (f1.mode === f2.mode) return f1.name.localeCompare(f2.name);
            return f1.mode === "dir" ? -1 : 1;
        });

    return (
        <div className="tree-view">
            <div className="files">
                {
                    sortedTree.map((file) => (
                        <div
                            className={classes("file", `mode-${file.mode}`)}
                            onClick={() =>
                                props.changeDir(
                                    props.path.concat({ name: file.name, hash: file.hash }),
                                    file.type
                                )
                            }
                        >
                            <Icon>{ file.mode === "dir" ? "folder" : "description"}</Icon>
                            <div className="file-name">{ file.name }</div>
                        </div>
                    ))
                }
            </div>
        </div>
    );
};