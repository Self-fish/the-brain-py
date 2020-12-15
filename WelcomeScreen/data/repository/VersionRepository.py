from WelcomeScreen.domain.exception.NoVersionException import NoVersionException


def get_version_code():
    try:
        return "1.5"
    except:
        raise NoVersionException
