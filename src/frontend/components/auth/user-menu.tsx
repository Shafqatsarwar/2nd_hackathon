"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useEffect } from "react";
import { signOut, useSession } from "@/lib/auth-client";

export function UserMenu() {
  const { data: session, isPending } = useSession();
  const router = useRouter();

  useEffect(() => {
    // You can add any sync logic here if needed
  }, []);

  if (isPending) {
    return <div className="px-4 py-2">Loading...</div>;
  }

  if (!session?.user) {
    return <Link href="/sign-in" className="px-4 py-2 hover:underline">Sign in</Link>;
  }

  const displayName = session.user.name || session.user.email;

  return (
    <div className="flex items-center gap-3 px-4 py-2">
      <div className="text-sm font-medium">{displayName}</div>
      <button
        onClick={async () => {
          await signOut();
          router.refresh();
        }}
        className="text-sm bg-gray-200 hover:bg-gray-300 px-3 py-1 rounded-md transition-colors"
      >
        Sign out
      </button>
    </div>
  );
}