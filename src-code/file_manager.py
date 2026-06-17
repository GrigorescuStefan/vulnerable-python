import os

BASE_DIR = "/app/data"

def read_user_file(filename):
    # FIX: prevent path traversal
    safe_path = os.path.normpath(os.path.join(BASE_DIR, filename))

    if not safe_path.startswith(BASE_DIR):
        raise ValueError("Invalid file path")

    with open(safe_path, "r", encoding="utf-8") as f:
        return f.read()


def save_log(user_input):
    with open("/tmp/log.txt", "a", encoding="utf-8") as f:
        f.write(user_input + "\n")