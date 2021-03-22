import * as path from "path";

import { Router } from "express";
import { fs } from "mz";

const router = Router();

router.get("/main.js", async (req, res) => {
    const file = await fs.readFile(path.join(__dirname, "../../client/dist/main.js"));
    res.contentType("application/javascript");
    res.send(file);
});

router.use("/", async (req, res) => {
    const file = await fs.readFile(path.join(__dirname, "../../client/dist/index.html"));
    res.contentType("text/html");
    res.send(file);
});

export default router;