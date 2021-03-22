import { Router } from "express";

import { authManager } from "./auth";

const router = Router();

router.use("/", async (req, res, next) => {
    const token = req.cookies["user-token"];
    if (typeof token === "string") {
        const user = await authManager.userFromToken(token);
        if (user) {
            req.user = { kind: "user", user };
            return next();
        }
    }

    const authHeader = req.header("authorization");
    if (authHeader && authHeader.toLowerCase().startsWith("basic")) {
        const [user, password] = Buffer.from(authHeader.slice(6), "base64").toString().split(":");
        if (await authManager.login(user, password)) {
            req.user = { kind: "user", user };
            return next();
        }
    }

    const sourceIp = req.socket.remoteAddress;
    if (sourceIp === "127.0.0.1" || sourceIp === "::1" || sourceIp === "::ffff:127.0.0.1") {
        req.user = { kind: "admin" };
        return next();
    }

    req.user = { kind: "none" };
    return next();
});

export default router;