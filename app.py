from flask import Flask, request, jsonify, render_template
from llama_cpp import Llama
from programs.linux_apps.launcher import launch_app, apps  # import apps JSON

app = Flask(__name__)
conversation_history = []

llm = Llama(
    model_path="models/mistral-7b-instruct-v0.2.Q5_K_M.gguf",
    n_ctx=2048,
    n_threads=16
)

def is_launch_command(user_prompt):
    lower_prompt = user_prompt.lower()
    trigger_words = ["launch", "open", "run", "start", "execute"]
    for trigger in trigger_words:
        if trigger in lower_prompt:
            trigger_index = lower_prompt.find(trigger)
            for app_info in apps.values():
                for alias in app_info.get("aliases", []):
                    alias_index = lower_prompt.find(alias)
                    if alias_index > trigger_index:
                        return True
    return False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history
    data = request.json
    user_prompt = data.get("prompt", "")
    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    conversation_history.append(f"User: {user_prompt}")

    # Only attempt to launch apps if it looks like a launch command
    if is_launch_command(user_prompt):
        launch_response = launch_app(user_prompt)
        if "launched successfully" in launch_response:
            conversation_history.append(f"Assistant: {launch_response}")
            return jsonify({"response": launch_response})
        # If trigger word present but no matching alias, continue to AI

    # Normal AI response
    system_prompt = (
        "You are a friendly AI assistant. Keep your responses short, casual, "
        "and conversational. Avoid long tutorials unless asked."
    )
    conversation_text = system_prompt + "\n" + "\n".join(conversation_history) + "\nAssistant:"

    output = llm(conversation_text, max_tokens=300, stop=["\nUser:", "</s>"])
    response = output["choices"][0]["text"].strip()
    response = response.replace("\nUser:", "").replace("\nAssistant:", "").strip()

    conversation_history.append(f"Assistant: {response}")
    return jsonify({"response": response})

@app.route("/reset", methods=["POST"])
def reset():
    global conversation_history
    conversation_history = []
    return jsonify({"status": "Conversation reset"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

