import subprocess


def get_version_code():
    return subprocess.check_output(["git", "describe"]).strip()
