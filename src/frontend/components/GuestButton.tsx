"use client";

import { useState } from "react";
import TaskInterface from "./TaskInterface";

export default function GuestButton() {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <div className="fixed bottom-4 right-4 z-50">
            {/* Ultra-Compact 'G' Badge with Purple-Blue Gradient */}
            <button
                onClick={() => setIsOpen(!isOpen)}
                className={`w-8 h-8 rounded-full bg-gradient-to-br from-purple-600 to-blue-600 text-white font-black flex items-center justify-center shadow-lg transition-all duration-300 hover:scale-110 active:scale-90 ${isOpen ? "rotate-45 !from-red-500 !to-red-600" : ""
                    }`}
                title="Guest Mode"
            >
                {isOpen ? (
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                ) : (
                    <span className="text-xs">G</span>
                )}
            </button>

            {/* The Guest Terminal/Modal */}
            <div className={`absolute bottom-16 right-0 w-[90vw] md:w-[450px] transition-all duration-500 origin-bottom-right ${isOpen ? "opacity-100 scale-100 translate-y-0" : "opacity-0 scale-90 translate-y-10 pointer-events-none"
                }`}>
                <div className="bg-neutral-900 border border-white/10 rounded-[32px] p-8 shadow-2xl backdrop-blur-3xl overflow-hidden relative">
                    {/* Decorative flare */}
                    <div className="absolute top-0 right-0 w-32 h-32 bg-purple-500/10 blur-3xl -z-10" />

                    <div className="flex justify-between items-start mb-6">
                        <div>
                            <h3 className="text-xl font-bold text-white">Guest Matrix</h3>
                            <p className="text-xs text-slate-500 uppercase tracking-widest mt-0.5">Ephemeral Interaction</p>
                        </div>
                        <div className="flex items-center gap-3">
                            <div className="h-2 w-2 bg-green-500 rounded-full animate-pulse" />
                            <button
                                onClick={() => setIsOpen(false)}
                                className="p-1 hover:bg-white/10 rounded-full transition-colors group"
                            >
                                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-slate-500 group-hover:text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                                </svg>
                            </button>
                        </div>
                    </div>

                    <TaskInterface userId="guest_user" token="guest_token" title="" />

                    <p className="mt-8 text-[10px] text-slate-600 text-center uppercase tracking-widest leading-relaxed">
                        Data is shared globally in this demo environment.
                        Sign in for a private vault.
                    </p>
                </div>
            </div>
        </div>
    );
}
