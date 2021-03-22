import * as React from "react";

import type { File } from "@bithug/server/dist/git"; // TODO(zwade): Make a path alias so this looks less jank
import { TheGreatLie } from "react-pwn";

import { Api } from "../client";
import { navigate } from "../components/history";

export type Path = { name: string; hash: string }[];

export interface BaseRepoState {
    repo: string;
    ref?: string;
    commit: string;
    rootTree: string;
    readme?: string;
}

export type Value =
    | { kind: "tree", tree: File[] }
    | { kind: "blob", blob: string }

export interface FileRepoState {
    currentPath: Path;
    currentValue: Value;
}

export interface WebhookRepoState {
    webhooks: { url: string, uid: string }[];
}

export interface AccessRepoState {
    users?: string[];
}

export interface RepoState extends BaseRepoState, FileRepoState, WebhookRepoState, AccessRepoState {}

export interface Repo {
    state: RepoState;
    changeDir: (path: Path, kind: "blob" | "tree") => void;
    refreshWebhooks: () => void;
    refreshUsers: () => void;
}

export interface Props {
    repo: string;
    ref?: string;
    initialPath?: string[];
    children: React.ReactNode;
    loadingScreen?: React.ReactNode;
    noCommits?: React.ReactNode;
}

export const RepoContext = React.createContext<Repo>(TheGreatLie());

const loadBaseData = async (repo: string, ref: string): Promise<BaseRepoState | undefined> => {
    const commit = await Api.Repo.commit(repo, ref);
    if (!commit) {
        return undefined;
    }
    const readme = await Api.Repo.readme(repo, ref);
    return {
        repo,
        commit: commit.hash,
        rootTree: commit.tree,
        readme,
    };
}

const loadTree = async (repoState: BaseRepoState, path: Path) => {
    if (path.length === 0) {
        throw new Error("Can't load empty path");
    }

    const treeHash = path.slice(-1)[0].hash;
    const tree = await Api.Repo.tree(repoState.repo, treeHash);
    return tree;
}

const stringifyPath = (path?: Path) => path?.slice(1).map(({ name }) => name).join("/") ?? "";

export const RepoProvider = (props: Props) => {
    const [noCommits, setNoCommits] = React.useState<true | undefined>();
    const [baseState, setBaseState] = React.useState<BaseRepoState | undefined>();
    const [fileState, setFileState] = React.useState<FileRepoState | undefined>();
    const [webhookState, setWebhookState] = React.useState<{ url: string, uid: string }[]>([]);
    const [accessState, setAccessState] = React.useState<string[] | undefined>();

    const state = baseState !== undefined && fileState !== undefined
        ? { ...baseState, ...fileState, webhooks: webhookState, users: accessState }
        : undefined;

    const initialPathAsString = props.initialPath?.join("/");
    const currentPathAsString = stringifyPath(state?.currentPath)

    const refreshWebhooks = () =>
        Api.Repo
            .webhooks(props.repo)
            .then((webhooks) => setWebhookState(webhooks.map(({ url, uid }) => ({ url, uid }))));

    React.useEffect(() => {
        refreshWebhooks();
    }, []);

    const refreshUsers = () =>
        Api.Repo
            .access(props.repo)
            .then(setAccessState);

    React.useEffect(() => {
        refreshWebhooks();
        refreshUsers();
    }, []);

    React.useEffect(() => {
        if (currentPathAsString === initialPathAsString && state) {
            return;
        }

        loadBaseData(props.repo, props.ref ?? "refs/heads/master")
            .then(async (state) => {
                if (state === undefined) {
                    setNoCommits(true);
                    return;
                }
                setBaseState(state);
                let path = [{ name: props.repo.split("/")[1], hash: state.rootTree }]
                let value: Value = { kind: "tree", tree: await loadTree(state, path) };
                if (props.initialPath) {
                    for (let component of props.initialPath) {
                        if (value.kind !== "tree") break;
                        const file: File | undefined = value.tree.find(({ name }) => name === component);
                        if (!file) break;
                        path = path.concat({ name: file.name, hash: file.hash });
                        if (file.type === "tree") {
                            value = { kind: "tree", tree: await loadTree(state, path) };
                        } else {
                            value = { kind: "blob", blob: await Api.Repo.blob(state.repo, file.hash) };
                        }
                    }
                }
                setFileState({ currentValue: value, currentPath: path });
            })
    }, [props.repo, props.ref, initialPathAsString])

    const changeDir = async (path: Path, kind: "tree" | "blob") => {
        if (!baseState) return;
        const currentValue: Value =
            kind === "tree"
                ? { kind, tree: await loadTree(baseState, path) }
                : { kind, blob: await Api.Repo.blob(props.repo, path.slice(-1)[0].hash) };

        setFileState({ currentValue, currentPath: path });
        navigate(`/${props.repo}/${stringifyPath(path)}`);
    }

    if (noCommits) {
        return (
            <> { props.noCommits} </>
        );
    } else if (!state) {
        return (
            <> { props.loadingScreen } </>
        );
    } else {
        return (
            <RepoContext.Provider value={{ state, changeDir, refreshWebhooks, refreshUsers }}>
                { props.children }
            </RepoContext.Provider>
        );
    }
}