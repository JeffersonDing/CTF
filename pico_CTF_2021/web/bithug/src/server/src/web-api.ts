import * as path from "path";

import { Router } from "express";
import * as bodyParser from "body-parser";
import { fs } from "mz";

import { authManager } from "./auth";
import { GitManager } from "./git";

const router = Router();

router.use("/api/login", bodyParser.json());
router.post("/api/login", async (req, res) => {
    const { user, password } = req.body;
    if (typeof user !== "string" || typeof password !== "string") {
        return res.status(400).send({ error: "Bad username or password" });
    }

    const success = await authManager.login(user, password);
    if (!success) {
        return res.status(401).send({ error: "Bad username or paassword" });
    }

    const token = await authManager.createToken(user);
    res.cookie("user-token", token);
    return res.send({});
});

router.use("/api/register", bodyParser.json());
router.post("/api/register", async (req, res) => {
    const { user, password } = req.body;
    if (typeof user !== "string"
        || !user.match(/^[a-zA-Z0-9-_]{3,}$/)
        || typeof password !== "string"
    ) {
        return res.status(400).send({ error: "Invalid username"});
    }

    await authManager.register(user, password);
    const token = await authManager.createToken(user);
    res.cookie("user-token", token);

    // Every user gets their own target to attack. Please do not try to
    // attack someone else's target.
    const targetRepo = new GitManager(`_/${user}.git`);
    await targetRepo.create();
    await targetRepo.initializeReadme(`
## Super Secret Admin Repo

The flag is \`${process.env.FLAG ?? "picoCTF{this_is_a_test_flag}"}\`
`);
    return res.send({});
});

router.use("/api", (req, res, next) => {
    if (req.user.kind === "none") {
        return res.status(404).send({ error: "Not found" });
    }
    next();
});

router.use("/api/repo/create", bodyParser.json());
router.post("/api/repo/create", async (req, res) => {
    const { name, initializeReadme } = req.body;
    if (req.user.kind !== "user"
        || typeof name !== "string"
        || !name.match(/^[a-zA-Z_-]{3,}$/)
    ) {
        throw new Error("Invalid repository");
    }

    const repo = new GitManager(`${req.user.user}/${name}.git`);
    await repo.create();
    if (initializeReadme) {
        await repo.initializeReadme(`# ${name}\n`);
    }
    res.send({ repo: `${req.user.user}/${name}` });
})

router.get("/api/self", async (req, res) => {
    if (req.user.kind !== "user") {
        throw new Error("Can't get self");
    }

    const user = req.user.user;
    let repos: { name: string, readme?: string }[];
    try {
        const repoPath = await fs.readdir(path.join(__dirname, "../repos", user));
        repos = await Promise.all(repoPath
            .map((repo) => new GitManager((`${user}/${repo}`)))
            .map(async (git) => ({
                name: git.name,
                readme: await git.getReadme("refs/heads/master")
            }))
        );
    } catch (e) {
        repos = [];
    }

    res.send({ user, repos });
});

router.post("/api/logout", async (req, res) => {
    res.clearCookie("user-token");
    res.send({});
});

export default router;