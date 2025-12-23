"use client";

import { useState, useEffect } from "react";
import { createAuthClient } from "better-auth/react";
import { useRouter } from "next/navigation";

const authClient = createAuthClient();
const BACKEND_URL = "http://127.0.0.1:8000";

export default function DashboardPage() {
    const [tasks, setTasks] = useState<any[]>([]);
    const [newTitle, setNewTitle] = useState("");
    const [loading, setLoading] = useState(true);
    const router = useRouter();

    // In a real app, session would be managed by a Provider
    const [session, setSession] = useState<any>(null);

    useEffect(() => {
        async function init() {
            const { data } = await authClient.getSession();
            if (!data) {
                router.push("/auth");
                return;
            }
            setSession(data);
            fetchTasks(data.user.id, (data as any).token);
        }
        init();
    }, []);

    const fetchTasks = async (userId: string, token: string) => {
        try {
            const res = await fetch(`${BACKEND_URL}/api/${userId}/tasks`, {
                headers: {
                    Authorization: `Bearer ${token}`,
                    "Content-Type": "application/json"
                }
            });
            if (res.ok) {
                const data = await res.json();
                setTasks(data);
            }
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const addTask = async () => {
        if (!newTitle) return;
        const { data } = await authClient.getSession();
        const token = (data as any)?.token;

        try {
            const res = await fetch(`${BACKEND_URL}/api/${session.user.id}/tasks`, {
                method: "POST",
                headers: {
                    Authorization: `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ title: newTitle })
            });
            if (res.ok) {
                const newTask = await res.json();
                setTasks([...tasks, newTask]);
                setNewTitle("");
            }
        } catch (err) {
            console.error(err);
        }
    };

    const toggleTask = async (id: number) => {
        const { data } = await authClient.getSession();
        const token = (data as any)?.token;

        try {
            const res = await fetch(`${BACKEND_URL}/api/${session.user.id}/tasks/${id}/complete`, {
                method: "PATCH",
                headers: { Authorization: `Bearer ${token}` }
            });
            if (res.ok) {
                const updatedTask = await res.json();
                setTasks(tasks.map(t => t.id === id ? updatedTask : t));
            }
        } catch (err) {
            console.error(err);
        }
    };

    const deleteTask = async (id: number) => {
        const { data } = await authClient.getSession();
        const token = (data as any)?.token;

        try {
            const res = await fetch(`${BACKEND_URL}/api/${session.user.id}/tasks/${id}`, {
                method: "DELETE",
                headers: { Authorization: `Bearer ${token}` }
            });
            if (res.ok) {
                setTasks(tasks.filter(t => t.id !== id));
            }
        } catch (err) {
            console.error(err);
        }
    };

    if (loading) return <div className="min-h-screen bg-black flex items-center justify-center text-white">Loading Evolution...</div>;

    return (
        <div className="min-h-screen bg-slate-950 text-slate-200 font-sans p-8">
            <div className="max-w-4xl mx-auto">
                <header className="flex justify-between items-center mb-12">
                    <div>
                        <h1 className="text-4xl font-black bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
                            Evolution Dashboard
                        </h1>
                        <p className="text-slate-500 mt-1">Architeching tasks with AI Precision</p>
                    </div>
                    <button
                        onClick={() => authClient.signOut().then(() => router.push("/auth"))}
                        className="px-4 py-2 border border-slate-700 rounded-lg hover:bg-slate-900 transition"
                    >
                        Logout ({session?.user?.email})
                    </button>
                </header>

                <section className="bg-slate-900/50 border border-slate-800 rounded-3xl p-8 mb-12 shadow-inner">
                    <div className="flex gap-4">
                        <input
                            type="text"
                            value={newTitle}
                            onChange={(e) => setNewTitle(e.target.value)}
                            placeholder="What is the next step in the evolution?"
                            className="flex-1 bg-slate-950 border border-slate-800 rounded-2xl px-6 py-4 focus:outline-none focus:ring-2 focus:ring-purple-500 transition"
                        />
                        <button
                            onClick={addTask}
                            className="bg-purple-600 hover:bg-purple-500 text-white font-bold px-8 rounded-2xl transition shadow-lg shadow-purple-900/20"
                        >
                            Evolve
                        </button>
                    </div>
                </section>

                <section className="space-y-4">
                    {tasks.length === 0 ? (
                        <div className="text-center py-20 bg-slate-900/30 rounded-3xl border border-dashed border-slate-800">
                            <p className="text-slate-600">No tasks detected in the memory matrix.</p>
                        </div>
                    ) : (
                        tasks.map(task => (
                            <div
                                key={task.id}
                                className={`flex items-center justify-between p-6 bg-slate-900 border border-slate-800 rounded-2xl transition hover:border-slate-700 ${task.completed ? 'opacity-60' : ''}`}
                            >
                                <div className="flex items-center gap-4">
                                    <button
                                        onClick={() => toggleTask(task.id)}
                                        className={`w-6 h-6 rounded-full border-2 flex items-center justify-center transition ${task.completed ? 'bg-green-500 border-green-500' : 'border-slate-700 hover:border-purple-500'}`}
                                    >
                                        {task.completed && <span className="text-xs text-white">✓</span>}
                                    </button>
                                    <span className={`text-lg transition ${task.completed ? 'line-through text-slate-500' : 'text-slate-200'}`}>
                                        {task.title}
                                    </span>
                                </div>
                                <button
                                    onClick={() => deleteTask(task.id)}
                                    className="p-2 text-slate-500 hover:text-red-400 transition"
                                >
                                    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                                        <path fillRule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clipRule="evenodd" />
                                    </svg>
                                </button>
                            </div>
                        ))
                    )}
                </section>
            </div>
        </div>
    );
}
