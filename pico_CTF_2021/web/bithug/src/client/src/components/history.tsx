import { createBrowserHistory } from "history";

export const history = createBrowserHistory();
history.listen(() => console.log("history changed", history))
export const navigate = (path: string) => history.push(path);
