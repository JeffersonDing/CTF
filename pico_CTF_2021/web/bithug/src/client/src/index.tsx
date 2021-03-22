import * as React from "react";
import * as ReactDOM from "react-dom";

import { App } from "./components/app";

import "./index.scss";

export const Main = () => {
    return (
        <App/>
    );
};

ReactDOM.render(<Main/>, document.getElementById("main"));