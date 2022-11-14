import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QDialog

class Cal(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('312456.ui', self)
        [i.clicked.connect(self.alfabet) for i in self.buttonGroup_alfabet.buttons()]
        self.button_clear.clicked.connect(self.clear)
        self.button_clearback.clicked.connect(self.clear_back)
        self.button_probel.clicked.connect(self.probel)
        self.dic = {'a': '._', 'b': '_...', 'c': '_._.', 'd': '_..', 'e': '.', 'f': '.._.', 'g': '__.', 'h': '....',
                    'i': '..', 'j': '.___',
                    'k': '_._', 'l': '._..', 'm': '__', 'n': '_.', 'o': '___', 'p': '.__.', 'q': '__._', 'r': '._.',
                    's': '...', 't': '_', 'u': '.._',
                    'v': '..._', 'w': '.__', 'x': '_.._', 'y': '_.__', 'z': '__..'}

        self.n = ''

    def alfabet(self):
        self.n += self.dic[str(self.sender().text())]
        self.lineEdit.setText(self.n)

    def clear(self):
        self.n = ''
        self.lineEdit.setText('')

    def clear_back(self):
        self.n = self.n[:-2]
        self.lineEdit.setText(self.n)

    def probel(self):
        self.n += '  '
        self.lineEdit.setText(self.n)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cal()
    ex.show()
    sys.exit(app.exec())