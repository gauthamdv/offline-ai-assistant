import subprocess
import json
import os

apps_file = os.path.join(os.path.dirname(__file__), "apps.json")
with open(apps_file, "r") as f:
    apps = json.load(f)

TRIGGER_WORDS = ["launch", "open", "run", "start", "execute", "please"]

def launch_app(user_command: str):
    lower_cmd = user_command.lower()

    # Check for trigger word + alias appearing after it
    matched_app = None
    for trigger in TRIGGER_WORDS:
        if trigger in lower_cmd:
            trigger_index = lower_cmd.find(trigger)
            for app_key, app_info in apps.items():
                for alias in app_info.get("aliases", []):
                    alias_index = lower_cmd.find(alias)
                    if alias_index > trigger_index:
                        matched_app = app_key
                        break
                if matched_app:
                    break
        if matched_app:
            break

    if not matched_app:
        return "Sorry, I couldn't identify which app or script to launch."

    command = apps[matched_app]["command"]

    try:
        subprocess.Popen(command, shell=True)  # Run in background
        return f"{matched_app.replace('-', ' ').title()} launched successfully! 🚀"
    except Exception as e:
        return f"Error launching {matched_app}: {e}"

