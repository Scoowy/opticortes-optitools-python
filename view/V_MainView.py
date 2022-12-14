from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from controller.C_MainController import MainController
from model.M_MainModel import MainModel
from view.UI_MainView import Ui_MainWindow
from view.V_DialogAbout import DialogAbout
from view.tabs.V_HalfPlank import HalfPlankView
from view.tabs.V_PriceM2 import PriceM2View


class MainView(QMainWindow):
    def __init__(self, model: MainModel, controller: MainController) -> None:
        super().__init__()

        self._model = model
        self._controller = controller
        self._ui = Ui_MainWindow()
        # self._ui = Ui_MainWindow(self)
        self._ui.setupUi(self)

        self.initializeValues()
        self.connectWithControllers()
        self.connectWithModels()

    def initializeValues(self):
        pass

    def connectWithControllers(self):
        # self._ui.btnPriceM2.clicked.connect(self._controller.openPriceM2Tab)
        self._ui.btnPriceM2.clicked.connect(self.openPriceM2View)
        self._ui.btnHalfPlank.clicked.connect(self.openHalfPlankView)

        # self._ui.mActM2.triggered[QAction].connect(self.openPriceM2View)
        self._ui.mActM2.triggered.connect(self.openPriceM2View)
        self._ui.mActMedia.triggered.connect(self.openHalfPlankView)
        self._ui.mActAbout.triggered.connect(self.openDialogAbout)

        self._ui.tabWidget.tabCloseRequested.connect(self.closeTab)

    def connectWithModels(self):
        pass

    @pyqtSlot()
    def openPriceM2View(self):
        print("Correcto")
        priceM2Tab = PriceM2View()
        self._ui.tabWidget.addTab(priceM2Tab, "Price m2")
        self._ui.tabWidget.setCurrentIndex(self._ui.tabWidget.count() - 1)

    @pyqtSlot()
    def openHalfPlankView(self):
        print("Correcto")
        halfPlank = HalfPlankView()
        self._ui.tabWidget.addTab(halfPlank, "Half plank")
        self._ui.tabWidget.setCurrentIndex(self._ui.tabWidget.count() - 1)

    @pyqtSlot()
    def openDialogAbout(self):
        print("About")
        aboutDialog = DialogAbout()

    @pyqtSlot(int)
    def closeTab(self, tab: int):
        if tab != 0:
            self._ui.tabWidget.removeTab(tab)
