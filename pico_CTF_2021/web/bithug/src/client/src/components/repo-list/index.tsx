import * as React from "react";

import { Frame, Button } from "react-pwn";

import { UserContext } from "../../providers/user-provider";
import { RepoListItem } from "./repo-list-item";
import { navigate } from "../history";

import "./index.scss";

export const RepoList = () => {
    const { data } = React.useContext(UserContext);

    if (!data) {
        throw new Error("Should not be reachable");
    }

    return (
        <Frame className="bh-repo-list">
            <div className="title"><span className="user">{ data.user }</span>'s repos</div>
            { data.repos.map(({ name, readme }) => <RepoListItem name={name} readme={readme} href={`/${data.user}/${name}`}/>) }
            <Button label="Create New Repo" onClick={() => navigate("/create")}/>
        </Frame>
    )
}