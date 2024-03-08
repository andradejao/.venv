import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout

class JanelaControles(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Clientes")
        self.setGeometry(15, 20, 500, 400)

        # Criar um layout para organizar os componentes 
        layout = QVBoxLayout()

        # Label para o título da janela 
        label_titulo = QLabel("Gerenciar os Clientes")
        label_titulo.setStyleSheet("QLabel{font-size:30pt;color:#15c243;font-weight:bold}")

        # Criar elementos de texto para pedir ao usuário 
        #para entrar com dados do cliente. Criaremos as labels(rótulo)
        label_nome = QLabel("Nome do Cliente:")
        label_nome.setStyleSheet("QLabel{font-size:15pt; font-family: arial; font-weight:bold}")

        label_email = QLabel("Email:")
        label_email.setStyleSheet("QLabel{font-size:15pt; font-family: arial; font-weight:bold}")
        
        label_telefone = QLabel("Telefone:")
        label_telefone.setStyleSheet("QLabel{font-size:15pt; font-family: arial; font-weight:bold}")

        # Criar elementos para que os usuários possam escrever
        #o que as labels pedem
        edit_nome = QLineEdit()
        edit_nome.setStyleSheet("QLineEdit{padding:10px; border-radius: 5px}")
      
        edit_email = QLineEdit()
        edit_email.setStyleSheet("QLineEdit{padding:10px; border-radius: 5px}")
        
        edit_telefone = QLineEdit()
        edit_telefone.setStyleSheet("QLineEdit{padding:10px; border-radius: 5px}")

        # Criar um controle de botão para realizar um cadastro
        botao_cadastro = QPushButton("Cadastrar")

        # Adicionar o título
        layout.addWidget(label_titulo)

        # Adicionar os controles de label e edit ao layout
        layout.addWidget(label_nome)
        layout.addWidget(edit_nome)

        layout.addWidget(label_email)
        layout.addWidget(edit_email)
        
        layout.addWidget(label_telefone)
        layout.addWidget(edit_telefone)

        layout.addWidget(botao_cadastro)

        # Adicionar o layout na janela
        self.setLayout(layout)


app = QApplication(sys.argv)
tela = JanelaControles()
tela.show()
app.exec_()
