from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from view.tabs.UI_HalfPlankView import Ui_tabHalfPlank


class HalfPlankView(QWidget):
    def __init__(self):
        super().__init__()
        self._model = None
        self._controller = None
        self._ui = Ui_tabHalfPlank()
        self._ui.setupUi(self)

        self.connectWithController()
        self.connectWithModel()

    def connectWithController(self):
        pass

    def connectWithModel(self):
        pass
