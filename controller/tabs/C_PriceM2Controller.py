from PyQt5.QtCore import QObject, pyqtSlot

from model.tabs.M_PriceM2Controller import PriceM2Model


class PriceM2Controller(QObject):
    def __init__(self, model: PriceM2Model) -> None:
        super().__init__()

        self._model = model

    def calculatePlankM2(self, large: float, width: float):
        self._model.calculatePlankM2(large, width)

    def calculatePieceM2(self, large: float, width: float):
        self._model.calculatePieceM2(large, width)

    def calculatePlankPriceM2(self, m2: float, pvp: float):
        self._model.calculatePlankPriceM2(m2, pvp)

    def calculatePiecePVP(self, m2: float, priceM2: float):
        self._model.calculatePiecePVP(m2, priceM2)
