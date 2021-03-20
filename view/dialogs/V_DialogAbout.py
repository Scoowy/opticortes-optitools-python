from PyQt5.QtWidgets import QDialog

from view.dialogs.UI_DialogAbout import Ui_DialogAbout


class DialogAbout(QDialog):
    def __init__(self):
        super().__init__()

        self._ui = Ui_DialogAbout()
        self._ui.setupUi(self)
        self.exec_()
