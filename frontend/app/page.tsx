export default function Home() {
    return (
        <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500">
            <div className="z-10 max-w-5xl w-full items-center justify-center font-mono text-sm flex">
                <div className="bg-white/10 backdrop-blur-md border border-white/20 p-12 rounded-3xl shadow-2xl text-center">
                    <h1 className="text-6xl font-extrabold text-white mb-6 drop-shadow-lg">
                        Phase II
                    </h1>
                    <p className="text-xl text-white/80 mb-8 max-w-md mx-auto">
                        Welcome to the Evolution of Todo. We are now transitioning to a Full-Stack architecture with Next.js and FastAPI.
                    </p>
                    <div className="flex gap-4 justify-center">
                        <div className="px-6 py-3 bg-white text-purple-600 rounded-full font-bold shadow-lg">
                            Backend Ready
                        </div>
                        <div className="px-6 py-3 bg-purple-600 text-white border border-white/30 rounded-full font-bold shadow-lg">
                            Frontend Scaffolded
                        </div>
                    </div>
                </div>
            </div>
        </main>
    );
}
