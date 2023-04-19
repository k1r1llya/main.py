
class Cal(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('312456.ui', self)
        [i.clicked.connect(self.alfabet) for i in self.buttonGroup_alfabet.buttons()]
        self.button_clear.clicked.connect(self.clear)
        self.button_clearback.clicked.connect(self.clear_back)
        self.button_probel.clicked.connect(self.probel)
        self.dic = {'а': '._', 'б': '_...', 'в': '.__', 'г': '__.', 'д': '_..', 'е': '.', 'й': '.___', 'ж': '..._',
                    'з': '__..', 'и': '..','к': '_._','л':'._..','м':'__','н':'_.','о':'___','п':".__.",'р':'._.'
                    'с': '_._', 'т': '._..', 'у': '__', 'ф': '_.', 'ц': '___', 'ч': '.__.', 'ш': '____', 'щ': '__._',
                    'ь': '_.._', 'ьтвердыйзнак': '.__._.', 'ы': '.._',
                    'э': '..._...', 'ю': '..__', 'я': '._._'}

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
