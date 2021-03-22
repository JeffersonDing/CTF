import express, { NextFunction, Response, Request } from "express";
import cookieParser from "cookie-parser";
import "express-async-errors";

import gitRouter from "./git-api";
import authRouter from "./auth-api";
import webRouter from "./web-api";
import staticRouter from "./static-api";
import { GitManager } from "./git";
import { User } from "./auth";

declare global {
    export namespace Express {
        export interface Request {
            git: GitManager;
            hash: string;
            user: User;
        }
    }
}

const main = async () => {
    const app = express();

    app.use(cookieParser());
    app.use("/", authRouter);
    app.use("/", (req, res, next) => {
        console.log(req.user, req.method, req.url, req.query);
        next();
    });

    app.use("/", webRouter);
    app.use("/", gitRouter);
    app.use("/", staticRouter);

    app.use(((err: any, req: Request, res: Response, next: NextFunction) => {
        console.error("Error", err)
        res.status(500);
        if (err instanceof Error) {
            res.send({ error: err.message });
        } else {
            res.send({ error: "Something went wrong..."});
        }
    }) as any) // express's types are wrong :'(
    app.listen(1823);
}

process.on("unhandledRejection", (rejection) => {
    console.error("Unhandled promise rejection", rejection);
});

process.on("uncaughtException", (error) => {
    console.error("Uncaught exception", error);
})

main()