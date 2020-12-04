import subprocess
from WelcomeScreen.domain.exception.NoVersionException import NoVersionException


def get_version_code():
    try:
        return "1.0"
    except:
        raise NoVersionException
