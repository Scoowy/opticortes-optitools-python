from PyQt5.QtCore import QObject, pyqtSignal


class HalfPlankModel(QObject):
    costRealChanged = pyqtSignal(float)
    pvpChanged = pyqtSignal(float)

    def __init__(self):
        super().__init__()

        self._cost = 0.0
        self._discount = 0.0
        self._costReal = 0.0
        self._pvp = 0.0

    @property
    def cost(self) -> float:
        return self._cost

    @cost.setter
    def cost(self, value: float):
        self._cost = value

    @property
    def discount(self) -> float:
        return self._discount

    @discount.setter
    def discount(self, value: float):
        self._discount = value

    @property
    def costReal(self) -> float:
        return self._costReal

    @costReal.setter
    def costReal(self, value: float):
        self._costReal = value
        self.costRealChanged.emit(self._costReal)

    @property
    def pvp(self) -> float:
        return self._pvp

    @pvp.setter
    def pvp(self, value: float):
        self._pvp = value
        self.pvpChanged.emit(self._pvp)

    # START Logic
    def calculateCostReal(self, cost: float, discount: float):
        costReal = cost - (cost * (discount / 100))
        self.costReal = costReal

    def calculatePVP(self, costReal: float):
        pvp = costReal / 2
        self.pvp = pvp
    # END Logic
