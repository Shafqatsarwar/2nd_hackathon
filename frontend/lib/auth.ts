import { betterAuth } from "better-auth";
import { jwt } from "better-auth/plugins";

export const auth = betterAuth({
    database: {
        // For the Hackathon demonstration, we use the same Neon URL 
        // Better Auth will manage its own tables (user, session, account)
        provider: "postgresql",
        url: process.env.DATABASE_URL as string,
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
