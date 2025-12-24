"use client";

import { useState, useEffect } from "react";
import { createAuthClient } from "better-auth/react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import TaskInterface from "../../components/TaskInterface";
import SignOutButton from "../../components/SignOutButton";

const authClient = createAuthClient();

export default function DashboardPage() {
    const [session, setSession] = useState<any>(null);
    const [loading, setLoading] = useState(true);
    const router = useRouter();

    useEffect(() => {
        async function init() {
            // Check for special Admin login first
            const isAdmin = localStorage.getItem("admin_access") === "true";
            if (isAdmin) {
                setSession({
                    user: { id: "admin", name: "Khan Sarwar", email: "khansarwar1@hotmail.com" },
                    token: "admin_token"
                });
                setLoading(false);
                return;
            }

            const { data } = await authClient.getSession();
            if (!data) {
                router.push("/auth");
                return;
            }
            setSession(data);
            setLoading(false);
        }
        init();
    }, []);

    const handleLogout = async () => {
        localStorage.removeItem("admin_access");
        await authClient.signOut();
        router.push("/auth");
    };

    if (loading) return (
        <div className="min-h-screen bg-neutral-950 flex items-center justify-center">
            <div className="w-16 h-16 border-4 border-purple-500/20 border-t-purple-500 rounded-full animate-spin" />
        </div>
    );

    const userId = session.user.id;
    const token = (session as any).token;

    return (
        <div className="min-h-screen bg-neutral-950 text-slate-200 font-sans p-4 md:p-12 relative overflow-hidden">
            {/* Background accents */}
            <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-purple-600/10 blur-[150px] -z-10" />
            <div className="absolute bottom-0 left-0 w-[500px] h-[500px] bg-blue-600/10 blur-[150px] -z-10" />

            <div className="max-w-5xl mx-auto z-10 relative">
                <header className="flex flex-col md:flex-row justify-between items-start md:items-center mb-16 gap-6">
                    <div>
                        <div className="flex items-center gap-2 mb-2">
                            <span className="text-xs font-bold uppercase tracking-[0.2em] text-purple-400">Phase II</span>
                            <div className="h-[1px] w-8 bg-purple-500/30" />
                        </div>
                        <h1 className="text-5xl font-black text-white tracking-tight">
                            Private Vault
                        </h1>
                        <p className="text-slate-500 mt-2 text-lg">
                            Welcome back, {session.user.name.split(' ')[0]}. Synchronizing your vault.
                        </p>
                    </div>

                    <div className="flex items-center gap-6">
                        <div className="text-right hidden md:block">
                            <p className="text-sm font-bold text-white">{session.user.name}</p>
                            <p className="text-xs text-slate-500">{session.user.email}</p>
                        </div>
                        <SignOutButton />
                    </div>
                </header>

                <div className="grid grid-cols-1 gap-12">
                    <section className="relative">
                        <TaskInterface
                            userId={userId}
                            token={token}
                            title="Private Objectives"
                        />
                    </section>
                </div>

                <footer className="mt-24 pt-12 border-t border-white/5 text-center">
                    <p className="text-slate-600 text-sm">
                        Evolution of Todo &bull; Designed by Product Architects
                    </p>
                </footer>
            </div>
        </div>
    );
}
