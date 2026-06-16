import subprocess

def run_diagnostics(target_host):
    print(f"Running diagnostics on {target_host}")

    # FIX: no shell injection
    result = subprocess.run(
        ["ping", "-c", "3", target_host],
        capture_output=True,
        text=True
    )

    return result.stdout


def backup_system(path):
    # FIX: safe subprocess usage
    result = subprocess.run(
        ["tar", "-czf", "backup.tar.gz", path],
        capture_output=True,
        text=True
    )

    return result.returncode