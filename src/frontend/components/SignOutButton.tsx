"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { createAuthClient } from "better-auth/react";

const authClient = createAuthClient();

export default function SignOutButton() {
    const router = useRouter();
    const [loading, setLoading] = useState(false);

    const handleLogout = async () => {
        setLoading(true);
        // Clean up any local persistent state (like admin toggle)
        localStorage.removeItem("admin_access");

        await authClient.signOut();
        router.push("/auth");
        // refresh to ensuring clean state
        router.refresh();
    };

    return (
        <button
            onClick={handleLogout}
            disabled={loading}
            className="px-5 py-2.5 border border-white/10 rounded-xl hover:bg-white/5 transition text-sm font-medium disabled:opacity-50"
        >
            {loading ? "..." : "Logout"}
        </button>
    );
}
