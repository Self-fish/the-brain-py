import subprocess


def get_version_code():
    version = 0
    try:
        version = subprocess.check_output(["git", "describe"]).strip()
    except subprocess.CalledProcessError:
        pass

    return version
