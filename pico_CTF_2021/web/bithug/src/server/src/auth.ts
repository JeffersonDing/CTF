import { v4 as uuid4 } from "uuid";
import * as sqlite from "sqlite3";

export type User =
    | { kind: "admin" }
    | { kind: "user", user: string }
    | { kind: "none" }
    ;

export class AuthManager {
    private db;

    constructor() {
        this.db = new sqlite.Database("./users.sqlite");
        this.db.run("CREATE TABLE IF NOT EXISTS user_auth (user varchar, password varchar);");
        this.db.run("CREATE TABLE IF NOT EXISTS user_token (token varchar, user varchar);");
    }

    private getUser(user: string) {
        return new Promise<{ user: string, password: string } | undefined>((resolve, reject) => {
            const statement = this.db.prepare("SELECT user, password FROM user_auth WHERE user = ?")
            statement.get(user, (error, row) => {
                resolve(row);
            })
        });
    }

    public async register(user: string, password: string) {
        const foundUser = await this.getUser(user);
        if (foundUser) {
            throw new Error("User already exists");
        }

        return new Promise<void>((resolve, reject) => {
            const statement = this.db.prepare("INSERT INTO user_auth (user, password) VALUES (?, ?)");
            statement.run(user, password, () => {
                resolve();
            })
        });
    }

    public async login(user: string, password: string) {
        const foundUser = await this.getUser(user);
        if (!foundUser) {
            return false;
        }
        return foundUser.password === password;
    }

    public async userFromToken(token: string) {
        return new Promise<string | undefined>((resolve, reject) => {
            const statement = this.db.prepare("SELECT user FROM user_token WHERE token = ?");
            statement.get(token, (err, row) => {
                resolve(row?.user);
            })
        })
    }

    public async createToken(user: string) {
        const token = uuid4();
        return new Promise<string>((resolve, reject) => {
            const statement = this.db.prepare("INSERT INTO user_token (token, user) VALUES (?, ?)");
            statement.run(token, user, () => {
                resolve(token);
            });
        });
    }
}

export const authManager = new AuthManager();