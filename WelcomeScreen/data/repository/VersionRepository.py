import subprocess
from WelcomeScreen.domain.exception.NoVersionException import NoVersionException


def get_version_code():
    try:
        return "1.1"
    except:
        raise NoVersionException
