"use client";

import { useState, useEffect } from "react";
import ChatbotInterface from "../../components/ChatbotInterface";

export default function ChatbotPage() {
    const [session, setSession] = useState<any>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
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

        // Check for regular session
        const sessionData = localStorage.getItem("better-auth-session");
        if (sessionData) {
            try {
                const parsed = JSON.parse(sessionData);
                setSession(parsed);
            } catch (e) {
                console.error("Error parsing session data:", e);
            }
        }

        setLoading(false);
    }, []);

    if (loading) return (
        <div className="min-h-screen bg-neutral-950 flex items-center justify-center">
            <div className="w-16 h-16 border-4 border-purple-500/20 border-t-purple-500 rounded-full animate-spin" />
        </div>
    );

    const userId = session?.user?.id || "guest_user";
    const token = session?.token || "guest_token";

    return (
        <div className="min-h-screen bg-neutral-950 text-slate-200 font-sans p-4 md:p-12 relative overflow-hidden">
            {/* Background accents */}
            <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-purple-600/10 blur-[150px] -z-10" />
            <div className="absolute bottom-0 left-0 w-[500px] h-[500px] bg-blue-600/10 blur-[150px] -z-10" />

            <div className="max-w-5xl mx-auto z-10 relative">
                <header className="flex flex-col md:flex-row justify-between items-start md:items-center mb-16 gap-6">
                    <div>
                        <div className="flex items-center gap-2 mb-2">
                            <span className="text-xs font-bold uppercase tracking-[0.2em] text-purple-400">Phase III</span>
                            <div className="h-[1px] w-8 bg-purple-500/30" />
                        </div>
                        <h1 className="text-5xl font-black text-white tracking-tight">
                            AI Assistant
                        </h1>
                        <p className="text-slate-500 mt-2 text-lg">
                            Your AI-powered task management assistant.
                        </p>
                    </div>
                </header>

                <div className="grid grid-cols-1 gap-12">
                    <section className="relative">
                        <ChatbotInterface
                            userId={userId}
                            token={token}
                            title="AI Chat Interface"
                        />
                    </section>
                </div>

                <footer className="mt-24 pt-12 border-t border-white/5 text-center">
                    <p className="text-slate-600 text-sm">
                        Evolution of Todo &bull; AI-Powered Task Management
                    </p>
                </footer>
            </div>
        </div>
    );
}