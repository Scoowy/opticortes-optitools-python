from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from controller.tabs.C_PriceM2Controller import PriceM2Controller
from model.tabs.M_PriceM2Controller import PriceM2Model
from view.tabs.UI_PriceM2View import Ui_tabPriceM2


class PriceM2View(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self._model = PriceM2Model()
        self._controller = PriceM2Controller(self._model)
        self._ui = Ui_tabPriceM2()
        self._ui.setupUi(self)

        self.connectWithController()
        self.connectWithModel()

    def connectWithController(self) -> None:
        self._ui.spnPlankLarge.valueChanged.connect(self.plankDimensionChanged)
        self._ui.spnPlankWidth.valueChanged.connect(self.plankDimensionChanged)
        self._ui.spnPieceLarge.valueChanged.connect(self.pieceDimensionChanged)
        self._ui.spnPieceWidth.valueChanged.connect(self.pieceDimensionChanged)

        self._ui.spnPlankM2.valueChanged.connect(self.plankM2Changed)
        self._ui.spnPlankPvp.valueChanged.connect(self.plankM2Changed)

        self._ui.spnPlankPm2.valueChanged.connect(self.piecePVPChanged)
        self._ui.spnPieceM2.valueChanged.connect(self.piecePVPChanged)

    def connectWithModel(self) -> None:
        self._model.plankM2Changed.connect(self.onPlankM2Changed)
        self._model.pieceM2Changed.connect(self.onPieceM2Changed)
        self._model.plankPm2Changed.connect(self.onPlankPm2Changed)
        self._model.piecePVPChanged.connect(self.onPiecePVPChanged)

    @pyqtSlot()
    def plankDimensionChanged(self):
        large = self._ui.spnPlankLarge.value()
        width = self._ui.spnPlankWidth.value()
        self._controller.calculatePlankM2(large, width)

    @pyqtSlot()
    def pieceDimensionChanged(self):
        large = self._ui.spnPieceLarge.value()
        width = self._ui.spnPieceWidth.value()
        self._controller.calculatePieceM2(large, width)

    @pyqtSlot()
    def plankM2Changed(self):
        m2 = self._ui.spnPlankM2.value()
        pvp = self._ui.spnPlankPvp.value()
        self._controller.calculatePlankPriceM2(m2, pvp)

    @pyqtSlot()
    def piecePVPChanged(self):
        m2 = self._ui.spnPieceM2.value()
        priceM2 = self._ui.spnPlankPm2.value()
        self._controller.calculatePiecePVP(m2, priceM2)

    @pyqtSlot(float)
    def onPlankM2Changed(self, value: float) -> None:
        print(value)
        self._ui.spnPlankM2.setValue(value)

    @pyqtSlot(float)
    def onPieceM2Changed(self, value: float) -> None:
        print(value)
        self._ui.spnPieceM2.setValue(value)

    @pyqtSlot(float)
    def onPlankPm2Changed(self, value: float) -> None:
        print(value)
        self._ui.spnPlankPm2.setValue(value)

    @pyqtSlot(float)
    def onPiecePVPChanged(self, value: float) -> None:
        print(value)
        self._ui.lcdPiecePrice.display("{:.2f}".format(value))
