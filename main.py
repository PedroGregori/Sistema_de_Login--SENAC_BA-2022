from PyQt5.QtWidgets import QApplication
import sys # importa o Sistema
from main_window import MainWindow
app = QApplication(sys.argv) # "argv" Argumentos do sistema
janela = MainWindow()
janela.show()
app.exec() # Executar