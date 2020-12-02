import sys

from WelcomeScreen.Containers import Container
from WelcomeScreen.domain import WelcomeScreenUseCase

if __name__ == '__main__':
    container = Container()
    container.wire(modules=[sys.modules[__name__]])
    WelcomeScreenUseCase.show_screen()

