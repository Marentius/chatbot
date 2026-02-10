import { useState, useRef, useCallback, useEffect } from "react";

const WS_URL =
  import.meta.env.VITE_WS_URL?.replace(/^http/, "ws") ||
  `ws://${window.location.hostname}:8080`;

export default function useChat() {
  const [messages, setMessages] = useState([]);
  const [isConnected, setIsConnected] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const wsRef = useRef(null);
  const botBufferRef = useRef("");

  const connect = useCallback(() => {
    if (wsRef.current?.readyState === WebSocket.OPEN) return;

    const ws = new WebSocket(`${WS_URL}/api/ws/chat`);

    ws.onopen = () => setIsConnected(true);

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);

      switch (data.type) {
        case "start":
          setIsLoading(true);
          botBufferRef.current = "";
          setMessages((prev) => [...prev, { role: "bot", content: "" }]);
          break;

        case "token":
          botBufferRef.current += data.content;
          setMessages((prev) => {
            const updated = [...prev];
            updated[updated.length - 1] = {
              role: "bot",
              content: botBufferRef.current,
            };
            return updated;
          });
          break;

        case "done":
          setIsLoading(false);
          break;

        case "error":
          setIsLoading(false);
          setMessages((prev) => [
            ...prev,
            { role: "bot", content: data.content || "En feil oppstod." },
          ]);
          break;
      }
    };

    ws.onclose = () => {
      setIsConnected(false);
      // Reconnect after 2 seconds
      setTimeout(connect, 2000);
    };

    ws.onerror = () => ws.close();

    wsRef.current = ws;
  }, []);

  useEffect(() => {
    connect();
    return () => wsRef.current?.close();
  }, [connect]);

  const sendMessage = useCallback(
    (text) => {
      if (!text.trim() || !wsRef.current || isLoading) return;

      setMessages((prev) => [...prev, { role: "user", content: text }]);
      wsRef.current.send(JSON.stringify({ message: text }));
    },
    [isLoading]
  );

  return { messages, sendMessage, isConnected, isLoading };
}
