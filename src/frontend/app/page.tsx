import Link from "next/link";

export default function Home() {
    return (
        <main className="min-h-screen bg-neutral-950 flex flex-col items-center justify-center relative overflow-hidden">
            {/* Background Decorative Blobs */}
            <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-purple-600/20 blur-[120px] rounded-full" />
            <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-blue-600/20 blur-[120px] rounded-full" />

            <div className="z-10 text-center px-6">
                <h1 className="text-7xl md:text-9xl font-black text-transparent bg-clip-text bg-gradient-to-b from-white to-neutral-500 mb-6 tracking-tighter">
                    EVOLVE.
                </h1>

                <p className="max-w-xl mx-auto text-lg md:text-xl text-neutral-400 mb-12 font-medium">
                    The next generation of task management. Built with AI core,
                    powered by Next.js & FastAPI.
                </p>

                <div className="flex flex-col md:flex-row gap-6 justify-center items-center">
                    <Link
                        href="/auth"
                        className="group relative px-8 py-4 bg-white text-black font-bold rounded-2xl overflow-hidden active:scale-95 transition-transform"
                    >
                        <span className="relative z-10">Start the Evolution</span>
                        <div className="absolute inset-0 bg-neutral-200 translate-y-full group-hover:translate-y-0 transition-transform duration-300" />
                    </Link>

                    <Link
                        href="/dashboard"
                        className="px-8 py-4 border border-neutral-800 text-neutral-300 font-bold rounded-2xl hover:bg-neutral-900 active:scale-95 transition-all"
                    >
                        Dashboard
                    </Link>
                </div>

                <div className="mt-20 flex gap-8 justify-center opacity-40">
                    <div className="flex flex-col items-center">
                        <span className="text-2xl font-bold text-white">FastAPI</span>
                        <span className="text-xs uppercase tracking-widest mt-1">Backend</span>
                    </div>
                    <div className="flex flex-col items-center">
                        <span className="text-2xl font-bold text-white">Neon</span>
                        <span className="text-xs uppercase tracking-widest mt-1">Database</span>
                    </div>
                    <div className="flex flex-col items-center">
                        <span className="text-2xl font-bold text-white">Auth</span>
                        <span className="text-xs uppercase tracking-widest mt-1">Better Auth</span>
                    </div>
                </div>
            </div>

            {/* Grid Pattern Overlay */}
            <div className="absolute inset-0 z-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-20 pointer-events-none" />
        </main>
    );
}
