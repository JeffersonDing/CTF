import * as React from "react";

import { Button, Input, A } from "react-pwn";

import { Api } from "../../client";
import { Logo } from "../logo";
import { navigate } from "../history";
import { UserContext } from "../../providers/user-provider";

import "./index.scss";

export const Register = () => {
    const [username, setUsername] = React.useState("");
    const [password, setPassword] = React.useState("");
    const { refresh } = React.useContext(UserContext);

    const submit = async () => {
        const success = await Api.Web.register(username, password);
        if (success) {
            await refresh();
            navigate("/");
        }
    }

    return (
        <div className="bh-register">
            <Logo/>
            <div className="box">
                <div className="box-header">Register with BitHug</div>
                <Input value={username} onChange={setUsername} placeholder="Username" onEnter={submit}/>
                <Input type="password" value={password} onChange={setPassword} placeholder="Password" onEnter={submit}/>
                <Button label="Register" onClick={submit}/>
                <div className="switch">Already have an account? <A href="/user/login">Log In</A></div>
            </div>
        </div>
    )
}