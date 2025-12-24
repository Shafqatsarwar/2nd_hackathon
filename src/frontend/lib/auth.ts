import { betterAuth } from "better-auth";
import { jwt } from "better-auth/plugins";

export const auth = betterAuth({
    database: process.env.DATABASE_URL?.startsWith("postgres")
        ? {
            provider: "postgresql",
            url: process.env.DATABASE_URL,
        }
        : {
            provider: "sqlite",
            url: process.env.DATABASE_URL?.replace("sqlite:///", "") || "auth.db",
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
