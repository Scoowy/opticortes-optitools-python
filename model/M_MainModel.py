from PyQt5.QtCore import QObject


class MainModel(QObject):
    def __init__(self):
        super().__init__()

        self._version = ''
        self._author = ''

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value: str):
        self._version = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value: str):
        self._author = value
