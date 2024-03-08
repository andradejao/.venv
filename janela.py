import sys
from PyQt5.QtWidgets import QWidget, QApplication 

class Janela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha Janela")
        self.setGeometry(10, 20, 600, 400)

app = QApplication(sys.argv)
tela = Janela()
tela.show()
app.exec_()
