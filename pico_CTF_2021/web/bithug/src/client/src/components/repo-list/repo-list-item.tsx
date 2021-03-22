import * as React from "react";
import { navigate } from "../history";

export interface Props {
    name: string;
    readme?: string;
    href: string;
}

export const RepoListItem = (props: Props) => {
    return (
        <div className="bh-repo-list-item" onClick={() => navigate(props.href)}>
            <div className="name">{ props.name }</div>
            <div className="description">{ props.readme }</div>
        </div>
    );
}
