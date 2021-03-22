import * as React from "react";

import { Code, Frame } from "react-pwn";

import { RepoContext } from "../../providers/repo-provider";


export const RepoUsers = () => {
    const { state } = React.useContext(RepoContext);

    return (
        <div className="bh-repo-users">
            {
                state.users === undefined
                    ? (
                        <Frame>
                            <div className="title">Add Users</div>
                            <div>
                                To add users to your repository, you can edit the file <Code inline>access.conf</Code> on the <Code inline>refs/meta/config</Code> commit of this repo.
                            </div>
                            <div className="frame-label">bash</div>
                            <Code>{
`git checkout --orphan
echo "some-user-here" > access.conf
git add access.conf
git commit -m "Added a user to the repo"
git push origin @:refs/meta/config`
                            }</Code>
                        </Frame>
                    ) : (
                        <Frame>
                            <div className="title">User Access</div>
                            <div>The following users have access to this repository</div>
                            {
                                state.users.map((user) =>
                                    <Code>{ user }</Code>
                                )
                            }
                        </Frame>
                    )
            }
        </div>
    )
}