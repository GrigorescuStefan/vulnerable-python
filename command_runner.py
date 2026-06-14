# command_runner.py

import os

def run_diagnostics(target_host):
    print(f"Running diagnostics on {target_host}")

    # VULNERABILITY: command injection
    command = "ping -c 3 " + target_host
    result = os.system(command)

    return result


def backup_system(path):
    # VULNERABILITY: unsafe shell usage
    os.system("tar -czf backup.tar.gz " + path)