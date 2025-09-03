"""
Módulo da janela principal.

Este módulo contém a implementação da janela principal que
gerencia todas as telas da aplicação.

Classes:
    MainWindow: Janela principal que gerencia todas as telas.
"""

from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QFont
from widgets.login_window import LoginWindow
from widgets.patient_info_window import PatientInfoWindow
from widgets.loading_window import LoadingWindow
from widgets.results_window import ResultsWindow


class MainWindow(QMainWindow):
    """
    Classe principal da aplicação que gerencia todas as janelas.
    
    Attributes:
        logged_in_user (str): Nome do usuário autenticado
        patient_data (dict): Dados do paciente e amostra
        login_screen (LoginWindow): Tela de login
        patient_info_screen (PatientInfoWindow): Tela de informações do paciente
        loading_screen (LoadingWindow): Tela de carregamento
        results_screen (ResultsWindow): Tela de resultados
    """
    
    def __init__(self):
        """Inicializa a janela principal e configura a interface."""
        super().__init__()
        self.logged_in_user = ""
        self.patient_data = {}
        self.initUI()
        
    def initUI(self):
        """Configura a interface gráfica da janela principal."""
        self.setWindowTitle("Sistema de Patologia Digital")
        self.setGeometry(100, 100, 1200, 800)
        
        # Definir estilo geral da aplicação - fundo cinza claro
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: #f5f5f5;
            }}
            QWidget {{
                font-family: Arial;
            }}
        """)
        
        # Widget central e layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        # Inicializar as telas (apenas login inicialmente)
        self.login_screen = LoginWindow(self)
        self.patient_info_screen = None
        self.loading_screen = None
        self.results_screen = None
        
        self.layout.addWidget(self.login_screen)
        
        # Mostrar tela de login inicialmente
        self.show_login_screen()
    
    def show_login_screen(self):
        """Exibe a tela de login e esconde as demais."""
        self.login_screen.show()
        if self.patient_info_screen:
            self.patient_info_screen.hide()
        if self.loading_screen:
            self.loading_screen.hide()
        if self.results_screen:
            self.results_screen.hide()
    
    def show_patient_info_screen(self):
        """Exibe a tela de informações do paciente."""
        self.login_screen.hide()
        if self.loading_screen:
            self.loading_screen.hide()
        if self.results_screen:
            self.results_screen.hide()
            
        # Criar tela se não existir
        if not self.patient_info_screen:
            self.patient_info_screen = PatientInfoWindow(self)
            self.layout.addWidget(self.patient_info_screen)
        
        self.patient_info_screen.show()
    
    def show_loading_screen(self):
        """Exibe a tela de carregamento durante a análise."""
        self.login_screen.hide()
        if self.patient_info_screen:
            self.patient_info_screen.hide()
        if self.results_screen:
            self.results_screen.hide()
            
        # Criar tela se não existir
        if not self.loading_screen:
            self.loading_screen = LoadingWindow(self)
            self.layout.addWidget(self.loading_screen)
        
        self.loading_screen.show()
    
    def show_results_screen(self):
        """Exibe a tela de resultados com o laudo completo."""
        self.login_screen.hide()
        if self.patient_info_screen:
            self.patient_info_screen.hide()
        if self.loading_screen:
            self.loading_screen.hide()
            
        # Criar tela se não existir
        if not self.results_screen:
            self.results_screen = ResultsWindow(self)
            self.layout.addWidget(self.results_screen)
        
        self.results_screen.show()