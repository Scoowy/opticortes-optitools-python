from PyQt5.QtCore import QObject, pyqtSlot

from model.M_MainModel import MainModel
from view.V_MainView import MainView


class MainController(QObject):
    def __init__(self) -> None:
        super().__init__()

        self._model = MainModel()
        self._view = MainView()

    def show(self):
        self._view.show()

    @pyqtSlot()
    def openPriceM2Tab(self):
        print("Open Tab: Price m2")
