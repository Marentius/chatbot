(function () {
  var CHAT_URL = window.CHAT_URL || "http://localhost:3000";

  // Styles
  var css = document.createElement("style");
  css.textContent =
    "#portfolio-chat-btn{position:fixed;bottom:88px;right:24px;width:56px;height:56px;" +
    "border-radius:16px;background:linear-gradient(135deg,#3b82f6,#8b5cf6);color:#fff;" +
    "border:none;cursor:pointer;box-shadow:0 4px 24px rgba(139,92,246,0.3);" +
    "z-index:2147483646;display:flex;align-items:center;justify-content:center;" +
    "transition:transform .2s,box-shadow .2s;font-size:22px}" +
    "#portfolio-chat-btn:hover{transform:scale(1.08);box-shadow:0 6px 32px rgba(139,92,246,0.45)}" +
    "#portfolio-chat-frame{position:fixed;bottom:160px;right:24px;width:400px;height:560px;" +
    "border:1px solid rgba(255,255,255,0.08);border-radius:16px;" +
    "box-shadow:0 8px 40px rgba(0,0,0,0.4);background:#0a0a0f;" +
    "z-index:2147483647;display:none;overflow:hidden}" +
    "@media(max-width:480px){" +
    "#portfolio-chat-frame{bottom:0;right:0;width:100%;height:100%;border-radius:0;border:none}" +
    "#portfolio-chat-btn{bottom:88px;right:16px}" +
    "#portfolio-chat-btn.open{top:12px;bottom:auto;right:12px;width:40px;height:40px;" +
    "border-radius:12px;font-size:18px;background:rgba(255,255,255,0.1);" +
    "backdrop-filter:blur(10px);box-shadow:none}}";
  document.head.appendChild(css);

  // Chat iframe
  var iframe = document.createElement("iframe");
  iframe.id = "portfolio-chat-frame";
  iframe.src = CHAT_URL;
  iframe.title = "Chat med Vetle sin assistent";
  document.body.appendChild(iframe);

  // Toggle button
  var btn = document.createElement("button");
  btn.id = "portfolio-chat-btn";
  btn.innerHTML = "💬";
  btn.setAttribute("aria-label", "Åpne chat med Vetle sin assistent");
  document.body.appendChild(btn);

  var open = false;
  btn.addEventListener("click", function () {
    open = !open;
    iframe.style.display = open ? "block" : "none";
    btn.innerHTML = open ? "✕" : "💬";
    if (open) {
      btn.classList.add("open");
    } else {
      btn.classList.remove("open");
    }
  });
})();
