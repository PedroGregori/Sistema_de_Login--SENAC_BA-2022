from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

FILE_UI = 'main_window.ui'

class MainWindow(QMainWindow):
    loginAdm = 'adm'
    senhaAdm = '1234'
    
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(FILE_UI, self)
        
        # Atribui um evento(função) para um botão
        self.button.clicked.connect(self.logar)
        
    def logar(self):
        """Função a ser chamada quando o botão for pressionado"""
        login = self.loginLineEdit.text()
        senha = self.senhaLineEdit.text()
        if login == '' or senha == '':
            self.aviso.setText('Preencha todos os campos!!')
        else:
            if login == self.loginAdm:
                # verificar a senha
                if senha == self.senhaAdm:
                    self.aviso.setText('Login Realizado com Sucesso')
                    # Apaga os campos de login e senha 
                    self.loginLineEdit.clear()
                    self.senhaLineEdit.clear()
                else:
                    self.aviso.setText('Senha inválida, tente novamente!')
            else:
                self.aviso.setText('Login inválido, tente novamente!')