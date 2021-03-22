import * as React from "react";
import { useParams } from "react-router";
import { RepoProvider } from "../../providers/repo-provider";

import { unreachable, Tabs } from "react-pwn";
import { Nav } from "../nav";
import { RepoContent } from "./repo-content";
import { RepoNoContent } from "./repo-no-content";
import { RepoSettings } from "./repo-settings";
import { RepoUsers } from "./repo-users";

import "./index.scss";

const _Repo = () => {
    const [tab, setTab] = React.useState<"Code" | "Settings" | "Users">("Code");
    return (
        <div className="bh-repo-container">
            <Tabs currentTab={tab} onChange={setTab} options={["Code", "Settings", "Users"]}/>
            {
                tab === "Code" ? <RepoContent/> :
                tab === "Settings" ? <RepoSettings/> :
                tab === "Users" ? <RepoUsers/> :
                unreachable(tab)
            }
        </div>
    )
}

export const Repo = () => {
    const { user, name, 0: path } = useParams<{ user: string; name: string, 0?: string }>();
    const repo = `${user}/${name}`;
    return (
        <>
            <Nav/>
            <RepoProvider
                repo={repo}
                initialPath={path?.split("/")}
                noCommits={<RepoNoContent repo={repo}/>}
            >
                <_Repo/>
            </RepoProvider>
        </>
    );
}