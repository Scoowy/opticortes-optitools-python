from PyQt5.QtCore import QObject, pyqtSignal

from utils.GeometryUtils import calculateSquareMeter


class PriceM2Model(QObject):
    plankM2Changed = pyqtSignal(float)
    plankPm2Changed = pyqtSignal(float)
    pieceM2Changed = pyqtSignal(float)
    piecePVPChanged = pyqtSignal(float)

    def __init__(self):
        super().__init__()

        self._plankLarge = 0.0
        self._plankWidth = 0.0
        self._plankM2 = 0.0
        self._plankPVP = 0.0
        self._plankPm2 = 0.0

        self._pieceLarge = 0.0
        self._pieceWidth = 0.0
        self._pieceM2 = 0.0
        self._piecePVP = 0.0

    @property
    def plankLarge(self) -> float:
        return self._plankLarge

    @plankLarge.setter
    def plankLarge(self, value: float):
        self._plankLarge = value

    @property
    def plankWidth(self) -> float:
        return self._plankWidth

    @plankWidth.setter
    def plankWidth(self, value: float):
        self._plankWidth = value

    @property
    def plankM2(self) -> float:
        return self._plankM2

    @plankM2.setter
    def plankM2(self, value: float):
        self._plankM2 = value
        self.plankM2Changed.emit(self._plankM2)

    @property
    def plankPVP(self) -> float:
        return self._plankPVP

    @plankPVP.setter
    def plankPVP(self, value: float):
        self._plankPVP = value

    @property
    def plankPm2(self) -> float:
        return self._plankPm2

    @plankPm2.setter
    def plankPm2(self, value: float):
        self._plankPm2 = value
        self.plankPm2Changed.emit(self._plankPm2)

    @property
    def pieceLarge(self) -> float:
        return self._pieceLarge

    @pieceLarge.setter
    def pieceLarge(self, value: float):
        self._pieceLarge = value

    @property
    def pieceWidth(self) -> float:
        return self._pieceWidth

    @pieceWidth.setter
    def pieceWidth(self, value: float):
        self._pieceWidth = value

    @property
    def pieceM2(self) -> float:
        return self._pieceM2

    @pieceM2.setter
    def pieceM2(self, value: float):
        self._pieceM2 = value
        self.pieceM2Changed.emit(self._pieceM2)

    @property
    def piecePVP(self) -> float:
        return self._piecePVP

    @piecePVP.setter
    def piecePVP(self, value: float):
        self._piecePVP = value
        self.piecePVPChanged.emit(self._piecePVP)

    # START Logic
    def calculatePlankM2(self, large: float, width: float):
        squareMeters = calculateSquareMeter(large, width)
        self.plankM2 = squareMeters

    def calculatePieceM2(self, large: float, width: float):
        squareMeters = calculateSquareMeter(large, width)
        self.pieceM2 = squareMeters

    def calculatePlankPriceM2(self, m2: float, pvp: float):
        priceM2 = 0.0
        if m2 != 0:
            priceM2 = pvp / m2
        self.plankPm2 = priceM2

    def calculatePiecePVP(self, m2: float, prieceM2: float):
        piecePVP = m2 * prieceM2
        self.piecePVP = piecePVP
    # END Logic
