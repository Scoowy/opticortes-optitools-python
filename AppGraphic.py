__version__ = '1.1.0'
__author__ = 'Juan Gahona - @Scoowy'

import sys

from PyQt5.Qt import QApplication

from controller.C_MainController import MainController


class App(QApplication):
    def __init__(self, argv: list) -> None:
        super().__init__(argv)
        self.controller = MainController()
        self.controller.setVersion(__version__)
        self.controller.setAuthor(__author__)
        self.controller.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
