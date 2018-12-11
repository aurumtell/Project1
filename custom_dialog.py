from PyQt5 import uic
from PyQt5.QtWidgets import (QDialog)


class MyDialog(QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi('dialog.ui', self)

    def get_value(self):
        return self.textEdit.toPlainText(), self.textEdit_2.toPlainText()
