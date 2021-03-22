import * as path from "path";

import * as fs from "mz/fs";
import { Response } from "express";
import * as child_process from "child_process";

export interface Commit {
    hash: string;
    parents: string[];
    tree: string;
    author: string;
    message: string;
}

export interface File {
    name: string;
    hash: string;
    type: "tree" | "blob";
    mode: "file" | "dir";
}

export class GitManager {
    public repo;
    public name;
    private dir;

    constructor(repo: string) {
        this.repo = repo;
        this.dir = path.join(__dirname, "../repos", repo);
        this.name = repo.split("/")[1].split(".")[0];
    }

    private git(subcommand: string, args: string[] = [], stdin: string | Buffer | undefined = undefined, cwd: string = this.dir) {
        return new Promise<Buffer>((resolve, reject) => {
            const proc = child_process.spawn("git", [subcommand, ...args], { cwd });
            if (stdin) {
                proc.stdin.write(stdin);
            }

            let result = Buffer.from([]);
            proc.on("error", (err) => reject(err));
            proc.stdout.on("data", (data) => { result = Buffer.concat([result, Buffer.from(data)]) });
            proc.stdout.on("error", (err) => reject(err));
            proc.stdout.on("close", () => resolve(result));
            proc.stderr.on("data", (data) => { process.stderr.write(data); })
        })
    }

    public async exists() {
        try {
            await fs.access(this.dir);
            return true;
        } catch (e) {
            return false;
        }
    }

    public async resolveRef(ref: string) {
        if (ref.match(/^[a-zA-Z0-9]{40}$/)) {
            return ref;
        }

        if (!ref.match(/^[a-zA-Z_\-\/]+$/)) {
           return undefined
        }

        const results = await this.git("show-ref", ["--", ref]);
        for (let line of results.toString().split("\n")) {
            const [commit, foundRef] = line.split(/\s+/);
            if (ref === foundRef) {
                return commit;
            }
        }

        return undefined
    }

    public async assertType(hash: string, type: "commit" | "blob" | "tree") {
        if (!hash.match(/^[a-fA-F0-9]{40}$/)) {
            throw new Error(`Invalid ${type}: ${hash}`);
        }

        const foundType = await this.git("cat-file", ["-t", hash]);
        if (foundType.toString().trim() !== type) {
            throw new Error(`Invalid ${type}: ${hash}`);
        }
    }

    public async getCommit(hash: string): Promise<Commit | undefined> {
        await this.assertType(hash, "commit");

        const results = await this.git("cat-file", ["-p", hash]);
        const [head, message] = results.toString().split("\n\n");
        const headerMap = new Map<string, string[]>();
        for (let line of head.split("\n")) {
            const [attr, ...value] = line.split(" ");
            headerMap.set(attr, (headerMap.get(attr) ?? []).concat(value.join(" ")));
        }

        if (headerMap.get("tree") === undefined) {
            return undefined;
        }

        return {
            hash,
            parents: headerMap.get("parent") ?? [],
            author: headerMap.get("author")?.[0] ?? "No author",
            tree: headerMap.get("tree")![0],
            message,
        }
    }

    public async getTree(hash: string) {
        await this.assertType(hash, "tree");

        const result = await this.git("cat-file", ["-p", hash]);
        const files = [] as File[];
        for (let line of result.toString().split("\n")) {
            const match = /^([0-7]{6})\s+(\w+)\s+(\w{40})\s+(.+)$/.exec(line);
            if (match) {
                const isDirectory = !!(parseInt("040000", 8) & parseInt(match[1], 8));
                files.push({
                    mode: isDirectory ? "dir" : "file",
                    type: match[2] as "blob" | "tree",
                    hash: match[3],
                    name: match[4],
                });
            }
        }

        return files;
    }

    public async getBlob(hash: string) {
        await this.assertType(hash, "blob");

        const result = await this.git("cat-file", ["-p", hash]);
        return result.toString();
    }

    public async create() {
        await fs.mkdir(path.dirname(this.dir), { recursive: true });
        await this.git("init", ["--bare", this.dir], undefined, path.join(__dirname, ".."));
    }

    public async initializeReadme(readme: string) {
        const tmpdir = await fs.mkdtemp("/tmp/bithug");
        const repodir = path.join(tmpdir, "localrepo");
        await this.git("clone", [`http://localhost:1823/${this.repo}`, repodir]);
        await this.git("checkout", ["master"], undefined, repodir);
        await fs.writeFile(path.join(repodir, "README.md"), readme);
        await this.git("add", ["README.md"], undefined, repodir);
        await this.git("commit", ["-m", "Initializing README"], undefined, repodir);
        await this.git("push", ["origin", "master"], undefined, repodir);
        // Apparently modernize doesn't promisify `fs.rm`??? This isn't part of the problem, just a bit silly.
        await new Promise<void>((resolve) => fs.rm(tmpdir, { force: true, recursive: true }, () => { resolve() }));
    }

    public async getReadme(ref: string) {
        const master = await this.resolveRef(ref);
        if (!master) return undefined;
        const commit = await this.getCommit(master);
        if (!commit) return undefined;
        const tree = await this.getTree(commit.tree);
        if (!tree) return undefined;
        const file = tree.find(({ name }) => name === "README.md" || name === "README");
        if (!file) return undefined;
        const blob = await this.getBlob(file.hash);
        return blob;
    }

    public async getAccessConfig() {
        const hash = await this.resolveRef("refs/meta/config");
        if (!hash) return undefined
        const configCommit = await this.getCommit(hash);
        if (!configCommit) return undefined
        const configTree = await this.getTree(configCommit.tree);
        const configFile = configTree?.find(({ name, mode }) => name === "access.conf" && mode === "file");
        if (!configFile) return undefined
        const configBlob = await this.getBlob(configFile.hash);
        return configBlob;
    }

    public async uploadPackGet(res: Response) {
        res.status(200);
        res.header("content-type", "application/x-git-upload-pack-advertisement")
        res.write("001e# service=git-upload-pack\n");
        res.write("0000");
        const results = await this.git("upload-pack", ["--advertise-refs", this.dir]);
        res.write(results);
        res.end();
    }

    public async uploadPackPost(res: Response, data: Buffer) {
        const results = await this.git("upload-pack", ["--stateless-rpc", this.dir], data);
        res.write(results);
        res.end();
    }


    public async receivePackGet(res: Response) {
        res.status(200);
        res.header("content-type", "application/x-git-receive-pack-advertisement")
        res.write("001f# service=git-receive-pack\n");
        res.write("0000");
        const results = await this.git("receive-pack", ["--advertise-refs", this.dir]);
        res.write(results);
        res.end();
    }

    public async receivePackPost(res: Response, data: Buffer) {
        const results = await this.git("receive-pack", ["--stateless-rpc", this.dir], data);
        res.send(results);
        const [refUpdate] = data.toString().split("\0");
        const [_old, _new, ref] = refUpdate.split(" ");
        return ref;
    }

    public writeLine(res: Response, data: string) {
        const length = 4 + data.length + 1;
        const prefix = length.toString(16).padStart(4, "0");
        res.write(prefix + data + "\n");
    }
}