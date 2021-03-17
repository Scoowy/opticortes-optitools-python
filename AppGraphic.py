import typing
import sys
from PyQt5.Qt import QApplication

from controller.C_MainController import MainController
from model.M_MainModel import MainModel
from view.V_MainView import MainView


class App(QApplication):
    def __init__(self, argv: typing.List[str]) -> None:
        super().__init__(argv)

        self.model = MainModel()
        self.controller = MainController(self.model)
        self.view = MainView(self.model, self.controller)

        self.view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
