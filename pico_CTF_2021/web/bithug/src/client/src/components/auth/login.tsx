import * as React from "react";

import { Button, Input, A } from "react-pwn";

import { Api } from "../../client";
import { Logo } from "../logo";
import { navigate } from "../history";
import { UserContext } from "../../providers/user-provider";

import "./index.scss";

export const Login = () => {
    const [username, setUsername] = React.useState("");
    const [password, setPassword] = React.useState("");
    const { refresh } = React.useContext(UserContext);

    const submit = async () => {
        const success = await Api.Web.login(username, password);
        if (success) {
            await refresh();
            navigate("/");
        }
    }

    return (
        <div className="bh-login">
            <Logo/>
            <div className="box">
                <div className="box-header">Login to BitHug</div>
                <Input value={username} onChange={setUsername} placeholder="Username" onEnter={submit}/>
                <Input type="password" value={password} onChange={setPassword} placeholder="Password" onEnter={submit}/>
                <Button label="Login" onClick={submit}/>
                <div className="switch">Need an account? <A href="/user/register">Register</A></div>
            </div>
        </div>
    )
}