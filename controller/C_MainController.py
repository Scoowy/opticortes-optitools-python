from PyQt5.QtCore import QObject, pyqtSlot

from model.M_MainModel import MainModel


class MainController(QObject):
    def __init__(self, model: MainModel) -> None:
        super().__init__()

        self._model = model

    @pyqtSlot()
    def openPriceM2Tab(self):
        print("Open Tab: Price m2")
