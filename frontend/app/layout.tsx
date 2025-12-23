import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
    title: "The Evolution of Todo - Phase II",
    description: "Next.js + FastAPI Todo App",
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en">
            <body>{children}</body>
        </html>
    );
}
