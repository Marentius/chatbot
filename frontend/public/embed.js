(function () {
  var CHAT_URL = window.CHAT_URL || "http://localhost:3000";

  // Styles
  var css = document.createElement("style");
  css.textContent =
    "#portfolio-chat-btn{position:fixed;bottom:24px;right:24px;width:56px;height:56px;" +
    "border-radius:16px;background:linear-gradient(135deg,#3b82f6,#8b5cf6);color:#fff;" +
    "border:none;cursor:pointer;box-shadow:0 4px 24px rgba(139,92,246,0.3);" +
    "z-index:2147483647;display:flex;align-items:center;justify-content:center;" +
    "transition:transform .2s,box-shadow .2s;font-size:22px}" +
    "#portfolio-chat-btn:hover{transform:scale(1.08);box-shadow:0 6px 32px rgba(139,92,246,0.45)}" +
    "#portfolio-chat-frame{position:fixed;bottom:96px;right:24px;width:400px;height:560px;" +
    "border:1px solid rgba(255,255,255,0.08);border-radius:16px;" +
    "box-shadow:0 8px 40px rgba(0,0,0,0.4);background:#0a0a0f;" +
    "z-index:2147483646;display:none;overflow:hidden}" +
    "@media(max-width:640px){" +
    "#portfolio-chat-btn{bottom:110px;right:20px}" +
    "#portfolio-chat-frame{bottom:0;right:0;width:100%;height:100%;border-radius:0;border:none}}";
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

  var isOpen = false;
  var isMobile = function () { return window.innerWidth <= 640; };

  btn.addEventListener("click", function () {
    isOpen = !isOpen;
    iframe.style.display = isOpen ? "block" : "none";
    btn.innerHTML = isOpen ? "✕" : "💬";

    if (isOpen && isMobile()) {
      btn.style.top = "16px";
      btn.style.bottom = "auto";
      btn.style.right = "16px";
      btn.style.width = "40px";
      btn.style.height = "40px";
      btn.style.borderRadius = "12px";
      btn.style.fontSize = "16px";
      btn.style.background = "rgba(255,255,255,0.1)";
      btn.style.backdropFilter = "blur(10px)";
      btn.style.boxShadow = "none";
    } else {
      btn.style.top = "";
      btn.style.bottom = "";
      btn.style.right = "";
      btn.style.width = "";
      btn.style.height = "";
      btn.style.borderRadius = "";
      btn.style.fontSize = "";
      btn.style.background = "";
      btn.style.backdropFilter = "";
      btn.style.boxShadow = "";
    }
  });
})();
