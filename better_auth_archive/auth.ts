import { betterAuth } from "better-auth";
import { jwt } from "better-auth/plugins";

const dbUrl = process.env.DATABASE_URL || "postgresql://neondb_owner:npg_zhJvIP74aTle@ep-long-waterfall-abcwopjg-pooler.eu-west-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require";

// FOOLPROOF BUILD DETECTION
const isBuild =
    process.env.NEXT_PHASE === 'phase-production-build' ||
    process.env.NEXT_IS_BUILDING === 'true' ||
    (process.env.VERCEL === '1' && !process.env.VERCEL_REGION) ||
    (!process.env.DATABASE_URL && process.env.NODE_ENV === 'production');

/**
 * THE ULTIMATE LAZY PROXY
 * This prevents BetterAuth from initializing the database adapter during the Next.js build.
 * It strictly only runs `betterAuth()` during runtime when accessed.
 */
let _auth: any = null;

export const auth = new Proxy({} as any, {
    get(_, prop) {
        if (isBuild) {
            if (prop === 'api' || prop === 'options') return {};
            return () => { throw new Error("Auth accessed during build phase. This should not happen."); };
        }

        if (!_auth) {
            console.log("Initializing BetterAuth for the first time...");
            _auth = betterAuth({
                database: {
                    provider: "postgresql",
                    url: dbUrl,
                },
                secret: process.env.BETTER_AUTH_SECRET || "my_super_secure_hackathon_secret_key_2025",
                baseURL: process.env.BETTER_AUTH_URL || process.env.NEXT_PUBLIC_APP_URL || "https://2nd-hackathon-shafqat.vercel.app",
                trustedOrigins: [
                    "https://2nd-hackathon-shafqat.vercel.app",
                    "https://2nd-hackathon-shafqat-shafqats-projects.vercel.app"
                ],
                emailAndPassword: {
                    enabled: true
                },
                plugins: [
                    jwt({
                        jwt: {
                            issuer: "todo-evolution",
                            expiresIn: "7d"
                        }
                    })
                ]
            });
        }
        return (_auth as any)[prop];
    }
});
