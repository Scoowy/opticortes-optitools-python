from PyQt5.QtCore import QObject

from model.tabs.M_HalfPlankController import HalfPlankModel


class HalfPlankController(QObject):
    def __init__(self, model: HalfPlankModel) -> None:
        super().__init__()

        self._model = model

    def calculateCostReal(self, cost: float, discount: float):
        self._model.calculateCostReal(cost, discount)

    def calculatePvp(self, costReal: float):
        self._model.calculatePVP(costReal)
