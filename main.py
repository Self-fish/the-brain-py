import sys


from WelcomeScreen.Containers import Container
from WelcomeScreen.domain.WelcomeScreenUseCase import WelcomeScreenUseCase

if __name__ == '__main__':
    container = Container()
    container.wire(modules=[sys.modules[__name__]])
    useCase = WelcomeScreenUseCase()
    useCase.show_screen()

