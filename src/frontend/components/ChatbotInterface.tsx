"use client";

import { useState, useRef, useEffect } from "react";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "http://127.0.0.1:8000";

interface Message {
    id: string;
    text: string;
    sender: "user" | "ai";
    timestamp: Date;
}

interface ChatbotInterfaceProps {
    userId: string;
    token: string;
    title?: string;
}

export default function ChatbotInterface({ userId, token, title = "AI Assistant" }: ChatbotInterfaceProps) {
    const [messages, setMessages] = useState<Message[]>([]);
    const [inputText, setInputText] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const messagesEndRef = useRef<null | HTMLDivElement>(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const handleSendMessage = async () => {
        if (!inputText.trim() || isLoading) return;

        // Add user message
        const userMessage: Message = {
            id: Date.now().toString(),
            text: inputText,
            sender: "user",
            timestamp: new Date(),
        };

        setMessages(prev => [...prev, userMessage]);
        setInputText("");
        setIsLoading(true);

        try {
            // Call the AI chat API
            const response = await fetch(`${BACKEND_URL}/api/ai/chat`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify({
                    user_id: userId,
                    query: inputText,
                }),
            });

            if (response.ok) {
                const data = await response.json();
                const aiMessage: Message = {
                    id: (Date.now() + 1).toString(),
                    text: `AI Response: ${data.action_taken || "Processed your request."}`,
                    sender: "ai",
                    timestamp: new Date(),
                };
                setMessages(prev => [...prev, aiMessage]);
            } else {
                const aiMessage: Message = {
                    id: (Date.now() + 1).toString(),
                    text: "Sorry, I encountered an error processing your request.",
                    sender: "ai",
                    timestamp: new Date(),
                };
                setMessages(prev => [...prev, aiMessage]);
            }
        } catch (error) {
            console.error("Error sending message:", error);
            const aiMessage: Message = {
                id: (Date.now() + 1).toString(),
                text: "Sorry, I'm having trouble connecting to the AI service.",
                sender: "ai",
                timestamp: new Date(),
            };
            setMessages(prev => [...prev, aiMessage]);
        } finally {
            setIsLoading(false);
        }
    };

    const handleClearChat = () => {
        if (confirm("Are you sure you want to clear the chat history?")) {
            setMessages([]);
        }
    };

    const handleKeyDown = (e: React.KeyboardEvent) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSendMessage();
        }
    };

    return (
        <div className="w-full max-w-2xl mx-auto">
            <div className="flex justify-between items-center mb-6">
                <h2 className="text-2xl font-bold text-white flex items-center gap-2">
                    <span className="w-2 h-2 bg-purple-500 rounded-full animate-ping" />
                    {title}
                </h2>
                {messages.length > 0 && (
                    <button
                        onClick={handleClearChat}
                        className="text-xs bg-red-900/50 hover:bg-red-800/50 text-red-300 px-3 py-1 rounded-lg transition-colors"
                        title="Clear Chat"
                    >
                        Clear Chat
                    </button>
                )}
            </div>

            <div className="bg-slate-900/50 border border-slate-800 rounded-3xl p-6 mb-8 shadow-2xl backdrop-blur-sm flex flex-col h-[500px]">
                {/* Messages Container */}
                <div className="flex-1 overflow-y-auto mb-4 space-y-4 pr-2 scrollbar-thin scrollbar-thumb-slate-700 scrollbar-track-slate-900">
                    {messages.length === 0 ? (
                        <div className="text-center py-10 text-slate-600">
                            <p>Start a conversation with the AI assistant...</p>
                            <p className="text-sm mt-2">Try asking: "Add a task to buy groceries"</p>
                        </div>
                    ) : (
                        messages.map((message) => (
                            <div
                                key={message.id}
                                className={`flex ${message.sender === "user" ? "justify-end" : "justify-start"}`}
                            >
                                <div
                                    className={`max-w-[80%] rounded-2xl px-4 py-3 ${
                                        message.sender === "user"
                                            ? "bg-purple-600/30 text-white rounded-br-none"
                                            : "bg-slate-800 text-slate-200 rounded-bl-none"
                                    }`}
                                >
                                    {message.text}
                                </div>
                            </div>
                        ))
                    )}
                    {isLoading && (
                        <div className="flex justify-start">
                            <div className="bg-slate-800 text-slate-200 rounded-2xl rounded-bl-none px-4 py-3 max-w-[80%]">
                                <div className="flex space-x-2">
                                    <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce"></div>
                                    <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce delay-100"></div>
                                    <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce delay-200"></div>
                                </div>
                            </div>
                        </div>
                    )}
                    <div ref={messagesEndRef} />
                </div>

                {/* Input Area */}
                <div className="flex gap-3">
                    <textarea
                        value={inputText}
                        onChange={(e) => setInputText(e.target.value)}
                        onKeyDown={handleKeyDown}
                        placeholder="Type your message to the AI assistant..."
                        className="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-purple-500 transition-all placeholder:text-slate-600 resize-none"
                        rows={2}
                    />
                    <button
                        onClick={handleSendMessage}
                        disabled={isLoading || !inputText.trim()}
                        className={`self-end bg-white text-black font-bold px-5 py-3 rounded-xl transition-colors active:scale-95 ${
                            isLoading || !inputText.trim()
                                ? "opacity-50 cursor-not-allowed"
                                : "hover:bg-neutral-200"
                        }`}
                    >
                        Send
                    </button>
                </div>
            </div>
        </div>
    );
}