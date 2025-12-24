import { betterAuth } from "better-auth";
import { jwt } from "better-auth/plugins";

export const auth = betterAuth({
    database: process.env.DATABASE_URL
        ? {
            provider: "postgresql",
            url: process.env.DATABASE_URL,
        }
        : {
            provider: "sqlite",
            url: "auth.db",
        },
    emailAndPassword: {
        enabled: true
    },
    plugins: [
        jwt({
            jwt: {
                // This secret must match BETTER_AUTH_SECRET in FastAPI backend
                issuer: "todo-evolution",
                expiresIn: "7d"
            }
        })
    ]
});
