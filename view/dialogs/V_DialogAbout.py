from PyQt5.QtWidgets import QDialog

from view.dialogs.UI_DialogAbout import Ui_DialogAbout


class DialogAbout(QDialog):
    def __init__(self):
        super().__init__()

        self._ui = Ui_DialogAbout()
        self._ui.setupUi(self)
        # self.exec_()

    def setInfo(self, version: str, author: str):
        versionStr = self._ui.lblVersion.text() + version
        createdByStr = self._ui.lblCreatedBy.text() + author
        self._ui.lblVersion.setText(versionStr)
        self._ui.lblCreatedBy.setText(createdByStr)
