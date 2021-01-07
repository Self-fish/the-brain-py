from WelcomeScreen.domain.exception.NoVersionException import NoVersionException


def get_version_code():
    try:
        return "1.7"
    except:
        raise NoVersionException
