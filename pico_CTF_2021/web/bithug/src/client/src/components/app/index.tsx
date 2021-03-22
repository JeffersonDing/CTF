import * as React from "react";
import { Router, Route, Switch } from "react-router-dom";
import { ToastContainer } from "react-toastify";

import { history, navigate } from "../history";
import { Register, Login } from "../auth";
import { UserContext, UserProvider } from "../../providers/user-provider";
import { Home } from "../home";
import { NewRepo } from "../new-repo";

import 'react-toastify/dist/ReactToastify.css';
import { Repo } from "../repo";
import { NavigationProvider, PaletteProvider, Palettes } from "react-pwn";

const _App = () => {
    const { data } = React.useContext(UserContext);

    return (
        <Router history={history}>
            <Switch>
                <Route exact path="/user/register">
                    <Register/>
                </Route>
                <Route exact path="/user/login">
                    <Login/>
                </Route>
                {
                    data === undefined
                        ? <Route path="/"><Login/></Route>
                        : (
                            <Switch>
                                <Route exact path="/create">
                                    <NewRepo/>
                                </Route>
                                <Route exact path="/:user/:name">
                                    <Repo/>
                                </Route>
                                <Route exact path="/:user/:name/*">
                                    <Repo/>
                                </Route>
                                <Route exact path="/">
                                    <Home/>
                                </Route>
                            </Switch>
                        )
                }
            </Switch>
        </Router>
    )
}

export const App = () => {
    return (
        <NavigationProvider navigate={navigate}>
            <PaletteProvider palette={Palettes.GreenOrange}>
                <ToastContainer/>
                <UserProvider>
                    <_App/>
                </UserProvider>
            </PaletteProvider>
        </NavigationProvider>
    );
}