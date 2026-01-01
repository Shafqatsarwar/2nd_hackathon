"use client";

import { useState } from "react";
import { createAuthClient } from "better-auth/react";
import { useRouter } from "next/navigation";

const authClient = createAuthClient();

export default function AuthPage() {
    const [isLogin, setIsLogin] = useState(true);
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError("");

        // Prebuilt Admin Account for Hackathon Demo
        if (email === "khansarwar1@hotmail.com" && password === "Admin") {
            localStorage.setItem("admin_access", "true");
            router.push("/dashboard");
            setLoading(false);
            return;
        }

        try {
            if (isLogin) {
                await authClient.signIn.email({ email, password });
            } else {
                await authClient.signUp.email({ email, password, name: email.split('@')[0] });
            }
            router.push("/dashboard");
        } catch (err: any) {
            setError(err.message || "An error occurred");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-900 via-purple-900 to-black p-4">
            <div className="w-full max-w-md bg-white/10 backdrop-blur-xl border border-white/20 p-8 rounded-3xl shadow-2xl">
                <h2 className="text-3xl font-bold text-center text-white mb-8">
                    {isLogin ? "Welcome Back" : "Join the Evolution"}
                </h2>

                {error && (
                    <div className="bg-red-500/20 border border-red-500 text-red-200 p-3 rounded-lg mb-6 text-sm">
                        {error}
                    </div>
                )}

                <form onSubmit={handleSubmit} className="space-y-6">
                    <div>
                        <label className="block text-white/70 text-sm mb-2">Email Address</label>
                        <input
                            type="email"
                            required
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            className="w-full bg-black/30 border border-white/20 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-purple-500 transition"
                            placeholder="you@example.com"
                        />
                    </div>
                    <div>
                        <label className="block text-white/70 text-sm mb-2">Password</label>
                        <input
                            type="password"
                            required
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className="w-full bg-black/30 border border-white/20 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-purple-500 transition"
                            placeholder="••••••••"
                        />
                    </div>

                    <button
                        type="submit"
                        disabled={loading}
                        className="w-full bg-purple-600 hover:bg-purple-700 disabled:opacity-50 text-white font-bold py-3 rounded-xl shadow-lg transform active:scale-95 transition"
                    >
                        {loading ? "Processing..." : isLogin ? "Sign In" : "Create Account"}
                    </button>
                </form>

                <div className="mt-8 text-center text-white/60">
                    {isLogin ? "New here?" : "Already have an account?"}{" "}
                    <button
                        onClick={() => setIsLogin(!isLogin)}
                        className="text-purple-400 hover:text-purple-300 font-medium transition"
                    >
                        {isLogin ? "Create an account" : "Sign in instead"}
                    </button>
                </div>
            </div>
        </div>
    );
}
