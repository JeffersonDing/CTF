import * as React from "react";

import { Button, Frame, Input, Radio } from "react-pwn";

import { Api } from "../../client";
import { navigate } from "../history";
import { Nav } from "../nav";

import "./index.scss";

export const NewRepo = () => {
    const [name, setName] = React.useState("")
    const [initialize, setInitialize] = React.useState(false);

    const createRepo = async () => {
        const result = await Api.Web.createRepo(name, initialize);
        navigate(`/${result.repo}`);
    }

    return (
        <>
            <Nav/>
            <div className="bh-new-repo">
                <Frame>
                    <div className="title">Create new Repo</div>
                    <Input type="text" placeholder="Repository Name" value={name} onChange={setName}/>
                    <Radio
                        options={[{ value: true, label: "Initialize Readme" }, { value: false, label: "Leave Repository Empty" }]}
                        value={initialize}
                        onChange={setInitialize}
                    />
                    <Button label="Create Repository" onClick={createRepo}/>
                </Frame>
            </div>
        </>
    )
}