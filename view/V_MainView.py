from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QWidget

from view.UI_MainView import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self, controller) -> None:
        super().__init__()

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self.connectWithControllers(controller)

    def connectWithControllers(self, controller):
        self._ui.btnPriceM2.clicked.connect(controller.openPriceM2Tab)
        self._ui.btnHalfPlank.clicked.connect(controller.openHalfPlankTab)

        # self._ui.mActM2.triggered[QAction].connect(self.openPriceM2View)
        self._ui.mActM2.triggered.connect(controller.openPriceM2Tab)
        self._ui.mActMedia.triggered.connect(controller.openHalfPlankTab)
        self._ui.mActAbout.triggered.connect(controller.openAboutDialog)

        self._ui.tabWidget.tabCloseRequested.connect(self.closeTab)

    @pyqtSlot(int)
    def closeTab(self, tab: int):
        if tab != 0:
            self._ui.tabWidget.removeTab(tab)

    def addTab(self, tab: QWidget, tabName: str):
        self._ui.tabWidget.addTab(tab, tabName)
        tabsCount = self._ui.tabWidget.count()
        self._ui.tabWidget.setCurrentIndex(tabsCount - 1)
