window.sendMessage = async function() {
    const input = document.getElementById("prompt");
    const message = input.value.trim();
    if (!message) return;

    const chat = document.getElementById("chat");

    // Display user message
    const userDiv = document.createElement("div");
    userDiv.className = "message user";
    userDiv.innerHTML = "<strong>You:</strong> " + message;
    chat.appendChild(userDiv);
    chat.scrollTop = chat.scrollHeight;

    input.value = "";

    // Display thinking indicator
    const thinkingDiv = document.createElement("div");
    thinkingDiv.className = "message assistant";
    thinkingDiv.innerHTML = "<strong>Assistant:</strong> is typing...";
    chat.appendChild(thinkingDiv);
    chat.scrollTop = chat.scrollHeight;

    // Send to Flask API
    const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: message })
    });
    const data = await res.json();

    // Replace thinking with actual response
    thinkingDiv.innerHTML = "<strong>Assistant:</strong> " + data.response;
    chat.scrollTop = chat.scrollHeight;
}

