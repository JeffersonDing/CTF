import * as sqlite from "sqlite3";
import { v4 } from "uuid";

export interface Webhook {
    uid: string;
    repo: string;
    user: string;
    url: string;
    contentType: string;
    body: Buffer;
}

export type SerializedWebhook = Omit<Webhook, "body"> & { body: string };

export class WebhookManager {
    private db;

    constructor() {
        this.db = new sqlite.Database("./webhooks.sqlite");
        this.db.run("CREATE TABLE IF NOT EXISTS webhooks (uid varchar, repo varchar, user varchar, url varchar, contentType varchar, body varchar);");
    }

    public async getWebhooksForRepo(repo: string) {
        return new Promise<Webhook[]>((resolve, reject) => {
            const statement = this.db.prepare("SELECT * FROM webhooks WHERE repo = ?");
            statement.all(repo, (err, rows) => {
                return resolve(rows.map(({ uid, repo, user, url, body, contentType }) => ({ uid, repo, user, url, body, contentType })));
            });
        });
    }

    public async getWebhooksForUser(repo: string, user: string) {
        return new Promise<Webhook[]>((resolve, reject) => {
            const statement = this.db.prepare("SELECT * FROM webhooks WHERE repo = ? AND user = ?");
            statement.all(repo, user, (err: any, rows: any[]) => {
                return resolve(rows.map(({ uid, repo, user, url, body, contentType }) => ({ uid, repo, user, url, body, contentType })));
            });
        });
    }

    public async addWebhook(repo: string, user: string, url: string, contentType: string, body: Buffer) {
        return new Promise<string>((resolve, reject) => {
            const uid = v4();
            const statement = this.db.prepare("INSERT INTO webhooks (uid, repo, user, url, contentType, body) VALUES (?, ?, ?, ?, ?, ?)");
            statement.run(uid, repo, user, url, contentType, body, () => {
                resolve(uid);
            });
        });
    }

    public async deleteWebhook(repo: string, user: string, uid: string) {
        return new Promise<void>((resolve, reject) => {
            const statement = this.db.prepare("DELETE FROM webhooks WHERE repo = ? AND user = ? AND uid = ?");
            statement.run(repo, user, uid, (err: any, rows: any) => {
                console.log(err, rows);
                if (err) {
                    reject("Webhook not found");
                } else {
                    resolve()
                }
            })
        })
    }
}

export const webhookManager = new WebhookManager();