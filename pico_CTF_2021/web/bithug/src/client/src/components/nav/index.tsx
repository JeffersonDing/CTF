import * as React from "react";

import { Api } from "../../client";
import { UserContext } from "../../providers/user-provider";
import { navigate } from "../history";

import "./index.scss";

export const Nav = () => {
    const { data, refresh } = React.useContext(UserContext);

    const logout = () => Api.Web.logout().then(() => refresh()).then(() => navigate("/user/login"));

    return (
        <div className={"bh-nav"}>
            <div className="logo">BitHug</div>
            <div className="bh-nav-item" onClick={() => navigate("/")}>Repos</div>
            <div className="spacer"/>
            {
                data ? <div className="bh-nav-item" onClick={logout}>Logout</div> : undefined
            }
        </div>
    )
}