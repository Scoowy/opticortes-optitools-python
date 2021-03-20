from PyQt5.QtCore import QObject, pyqtSlot

from model.M_MainModel import MainModel
from view.V_MainView import MainView
from view.dialogs.V_DialogAbout import DialogAbout
from view.tabs.V_HalfPlank import HalfPlankView
from view.tabs.V_PriceM2 import PriceM2View


class MainController(QObject):
    def __init__(self) -> None:
        super().__init__()

        self._model = MainModel()
        self._view = MainView(self)

    def show(self):
        self._view.show()

    def setVersion(self, version: str):
        self._model.version = version

    def setAuthor(self, author: str):
        self._model.author = author

    @pyqtSlot()
    def openPriceM2Tab(self):
        print("Open Tab: Price m2")
        priceM2Tab = PriceM2View()
        self._view.addTab(priceM2Tab, "Precio por m2")

    @pyqtSlot()
    def openHalfPlankTab(self):
        print("Open Tab: Half plank")
        halfPlank = HalfPlankView()
        self._view.addTab(halfPlank, "Media plancha")

    @pyqtSlot()
    def openAboutDialog(self):
        print("Open Dialog: About")
        aboutDialog = DialogAbout()
