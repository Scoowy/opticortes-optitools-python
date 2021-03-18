from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from controller.tabs.C_HalfPlankController import HalfPlankController
from model.tabs.M_HalfPlankController import HalfPlankModel
from view.tabs.UI_HalfPlankView import Ui_tabHalfPlank


class HalfPlankView(QWidget):
    def __init__(self):
        super().__init__()
        self._model = HalfPlankModel()
        self._controller = HalfPlankController(self._model)
        self._ui = Ui_tabHalfPlank()
        self._ui.setupUi(self)

        self.connectWithController()
        self.connectWithModel()

    def connectWithController(self):
        self._ui.spnCost.valueChanged.connect(self.halfPlankChanged)
        self._ui.spnDisc.valueChanged.connect(self.halfPlankChanged)

        self._ui.spnRealCost.valueChanged.connect(self.costChanged)

    def connectWithModel(self):
        self._model.costRealChanged.connect(self.onCostRealChanged)
        self._model.pvpChanged.connect(self.onPvpChanged)

    @pyqtSlot()
    def halfPlankChanged(self):
        cost = self._ui.spnCost.value()
        discount = self._ui.spnDisc.value()
        self._controller.calculateCostReal(cost, discount)

    @pyqtSlot()
    def costChanged(self):
        costReal = self._ui.spnRealCost.value()
        self._controller.calculatePvp(costReal)

    @pyqtSlot(float)
    def onCostRealChanged(self, value: float) -> None:
        print(value)
        self._ui.spnRealCost.setValue(value)

    @pyqtSlot(float)
    def onPvpChanged(self, value: float) -> None:
        print(value)
        self._ui.lcdPVP.display("{:.2f}".format(value))
