import { useRef, useEffect } from "react";
import useChat from "../hooks/useChat";
import MessageBubble from "./MessageBubble";
import InputBar from "./InputBar";
import TypingIndicator from "./TypingIndicator";

export default function ChatWidget() {
  const { messages, sendMessage, isConnected, isLoading } = useChat();
  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <div className="chat-widget">
      <div className="chat-header">
        <div className="chat-header-title">
          <span className="chat-logo">VM</span>
          <span>Spør om Vetle</span>
        </div>
        <div className="chat-header-right">
          <span className={`status-dot ${isConnected ? "connected" : ""}`} />
          <button
            className="chat-close-btn"
            onClick={() => window.parent.postMessage({ type: "close-chat" }, "*")}
            aria-label="Lukk chat"
          >
            ✕
          </button>
        </div>
      </div>

      <div className="chat-messages">
        {messages.length === 0 && (
          <div className="chat-welcome">
            <p>Hei! 👋 Jeg er Vetle sin personlige assistent.</p>
            <p>Spør meg om erfaring, prosjekter, ferdigheter eller kontaktinfo.</p>
          </div>
        )}
        {messages.map((msg, i) => (
          <MessageBubble key={i} role={msg.role} content={msg.content} />
        ))}
        {isLoading && messages[messages.length - 1]?.content === "" && (
          <TypingIndicator />
        )}
        <div ref={messagesEndRef} />
      </div>

      <InputBar onSend={sendMessage} disabled={!isConnected || isLoading} />
    </div>
  );
}
