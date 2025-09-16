# 🦾 Offline AI Assistant

This is a lightweight, offline AI assistant for Linux desktops. It can engage in natural conversation, launch applications, run scripts, and is fully customizable. It uses the **Mistral 7B Q5 model** locally and runs entirely on CPU. ⚡

---

## 🌟 Features

* 🤖 Friendly conversational AI powered by **Mistral 7B**.
* 🖥️ Launch Linux applications using keywords.
* 🛠️ Run scripts like cache clearing, file operations, etc.
* 📂 Customizable app/script launcher with JSON configuration.
* 🔒 Fully offline, CPU-based operation.
* 🌐 Simple web interface built with **Flask, HTML, CSS, and JS**.

---

## 📁 Repository Structure

```
offline-ai-assistant/
├── programs/
│   └── linux_apps/
│       ├── launcher.py
│       └── apps.json
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── templates/
│   └── index.html
├── models/
│   └── model-mistral  # placeholder, download the model here
├── app.py
├── requirements.txt
├── environment.yml
├── packages.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/gauthamdv/offline-ai-assistant.git
cd offline-ai-assistant
```

### 2️⃣ Set up Conda environment (recommended)

```bash
conda env create -f environment.yml
conda activate assistant
```

Alternatively, install with pip:

```bash
pip install -r requirements.txt
```

### 3️⃣ Install system packages (Linux)

```bash
xargs sudo apt install -y < packages.txt
```

---

## 🧠 Model Setup

1. Navigate to the `models` folder:

```bash
cd models
```

2. Download the **Mistral 7B Q5 model**:

```bash
wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q5_K_M.gguf
```

3. Replace the placeholder file (`model-mistral`) with the downloaded model:

```bash
mv mistral-7b-instruct-v0.2.Q5_K_M.gguf model-mistral
```

> Make sure `app.py` points to the correct model path in the `Llama()` constructor. 🗂️

---

## 🚀 Running the Assistant

1. Activate the conda environment:

```bash
conda activate assistant
```

2. Start the Flask server:

```bash
python app.py
```

3. Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 💬 Usage

* **Chat**: Type your messages and get responses from the AI.
* **Launch Apps**: Use keywords like `launch browser` or `launch text-editor`.
* **Run Scripts**: Use keywords like `run clean cache` or `run <script-name>` defined in `apps.json`.
* **Reset Conversation**: Click the "Reset" button to clear conversation history.

### 📝 apps.json Example

```json
{
    "text-editor": {
        "aliases": ["notepad", "editor", "text editor"],
        "command": "./programs/linux_apps/launch-text-editor.sh"
    },
    "browser": {
        "aliases": ["firefox", "web", "internet"],
        "command": "./programs/linux_apps/launch-browser.sh"
    },
    "clean-cache": {
        "aliases": ["clean cache", "clear cache"],
        "command": "./programs/clean-cache.sh"
    }
}
```

---

## ⚠️ Notes

* 🔒 **Offline Only**: Runs entirely offline; no API keys needed.
* 🖥️ **CPU Usage**: The model runs on CPU; your Ryzen 9 5900HX should handle normal conversation well.
* 🌱 **Future Enhancements**:

  * ⏱ Timer, calculator, and additional scripts.
  * 🧩 Better intent detection using the LLM.
  * ➕ More apps/scripts in `apps.json`.

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add some feature"`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📬 Contact

Created by **Gautham DV**. ✨

---

## 🗂 Flowchart

```text
User Input
   │
   ├── "launch <app>" → Launcher module → Run app → Response: "<app> launched successfully!"
   │
   ├── "run <script>" → Launcher module → Run script → Response: "<script> executed successfully!"
   │
   └── Else → LLM Response → Generate conversational AI reply → Display in chat
```
