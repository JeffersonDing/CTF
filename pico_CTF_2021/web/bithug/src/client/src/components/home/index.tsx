import * as React from "react";

import { UserContext } from "../../providers/user-provider";
import { Nav } from "../nav";
import { RepoList } from "../repo-list";

import "./index.scss";

export const Home = () => {
    const { data } = React.useContext(UserContext);
    if (!data) {
        throw new Error("Should not be able to reach this");
    }

    return (
        <>
            <Nav/>
            <div className="bh-home">
                <RepoList/>
            </div>
        </>
    )
}