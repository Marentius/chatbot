(function () {
  var CHAT_URL = window.CHAT_URL || "http://localhost:3000";

  // Styles
  var css = document.createElement("style");
  css.textContent =
    "#portfolio-chat-btn{position:fixed;bottom:24px;right:24px;width:60px;height:60px;" +
    "border-radius:50%;background:#1a2b4a;color:#fff;border:none;cursor:pointer;" +
    "box-shadow:0 4px 16px rgba(0,0,0,0.2);z-index:9998;display:flex;align-items:center;" +
    "justify-content:center;transition:transform .2s,box-shadow .2s;font-size:24px}" +
    "#portfolio-chat-btn:hover{transform:scale(1.08);box-shadow:0 6px 24px rgba(0,0,0,0.3)}" +
    "#portfolio-chat-frame{position:fixed;bottom:100px;right:24px;width:400px;height:600px;" +
    "border:none;border-radius:16px;box-shadow:0 8px 32px rgba(0,0,0,0.15);" +
    "z-index:9999;display:none;overflow:hidden}" +
    "@media(max-width:480px){#portfolio-chat-frame{bottom:0;right:0;width:100%;height:100%;" +
    "border-radius:0}#portfolio-chat-btn{z-index:10000}}";
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
  });
})();
