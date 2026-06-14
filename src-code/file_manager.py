# file_manager.py

import os

BASE_DIR = "/app/data"

def read_user_file(filename):
    # VULNERABILITY: path traversal
    file_path = os.path.join(BASE_DIR, filename)

    print(f"Opening file: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def save_log(user_input):
    # unsafe file writing
    with open("/tmp/log.txt", "a") as f:
        f.write(user_input + "\n")