import subprocess


def get_version_code(self):
    return subprocess.check_output(["git", "describe"]).strip()
