import subprocess
from WelcomeScreen.domain.exception.NoVersionException import NoVersionException


def get_version_code():
    try:
        return subprocess.check_output(["git", "describe"]).strip()
    except subprocess.CalledProcessError:
        raise NoVersionException
