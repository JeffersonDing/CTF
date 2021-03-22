import * as React from "react";

import { Code, Frame } from "react-pwn";

import { UserContext } from "../../providers/user-provider";
import { getRepoUri } from "./utils";

export interface Props {
    repo: string;
}

export const RepoNoContent = (props: Props) => {
    const { data } = React.useContext(UserContext);
    const repoName = props.repo.split("/")[1];
    const repoHref = getRepoUri(data?.user ?? "", props.repo);

    return (
        <div className="bh-repo no-content">
            <Frame>
                <div className="title">{ props.repo }</div>
                <div>
                    This repo is still empty, but you can start adding files with just a few commands.
                </div>
                <div className="frame-label">bash</div>
                <Code>
                    {
`git clone ${repoHref}
cd ${repoName}

echo "Hello world" > README.md

git add -A
git commit -m "Initial commit"
git push origin master`
                    }
                </Code>
            </Frame>
        </div>
    )
}