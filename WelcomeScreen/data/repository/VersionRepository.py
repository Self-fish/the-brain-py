from WelcomeScreen.domain.exception.NoVersionException import NoVersionException


def get_version_code():
    try:
        return "1.8"
    except:
        raise NoVersionException
