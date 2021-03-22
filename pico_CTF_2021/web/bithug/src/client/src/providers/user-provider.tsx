import * as React from "react";

import { TheGreatLie } from "react-pwn";

import { Api } from "../client";

type User = { user: string; repos: { name: string, readme?: string }[] }

export const UserContext = React.createContext<{ data: User | undefined, refresh: () => Promise<void> }>(TheGreatLie());

export const UserProvider = (props: { children: React.ReactNode }) => {
    const [data, setData] = React.useState<User | undefined>();
    const refresh = () => Api.Web.self().then((self) => setData(self));

    React.useEffect(() => {
        refresh();
    }, []);

    return (
        <UserContext.Provider value={{ data, refresh }}>
            { props.children }
        </UserContext.Provider>
    );
};
