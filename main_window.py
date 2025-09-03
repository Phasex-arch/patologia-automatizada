from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QFont
from widgets.login_window import LoginWindow
from widgets.patient_info_window import PatientInfoWindow
from widgets.loading_window import LoadingWindow
from widgets.results_window import ResultsWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logged_in_user = ""
        self.patient_data = {}
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Sistema de Patologia Digital")
        self.setGeometry(100, 100, 1200, 800)
        
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: #f5f5f5;
            }}
            QWidget {{
                font-family: Arial;
            }}
        """)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        self.login_screen = LoginWindow(self)
        self.patient_info_screen = None
        self.loading_screen = None
        self.results_screen = None
        
        self.layout.addWidget(self.login_screen)
        self.show_login_screen()
    
    def show_login_screen(self):
        self.login_screen.show()
        if self.patient_info_screen:
            self.patient_info_screen.hide()
        if self.loading_screen:
            self.loading_screen.hide()
        if self.results_screen:
            self.results_screen.hide()
    
    def show_patient_info_screen(self):
        self.login_screen.hide()
        if self.loading_screen:
            self.loading_screen.hide()
        if self.results_screen:
            self.results_screen.hide()
            
        if not self.patient_info_screen:
            self.patient_info_screen = PatientInfoWindow(self)
            self.layout.addWidget(self.patient_info_screen)
        
        self.patient_info_screen.show()
    
    def show_loading_screen(self):
        self.login_screen.hide()
        if self.patient_info_screen:
            self.patient_info_screen.hide()
        if self.results_screen:
            self.results_screen.hide()
            
        if not self.loading_screen:
            self.loading_screen = LoadingWindow(self)
            self.layout.addWidget(self.loading_screen)
        
        self.loading_screen.show()
    
    def show_results_screen(self):
        self.login_screen.hide()
        if self.patient_info_screen:
            self.patient_info_screen.hide()
        if self.loading_screen:
            self.loading_screen.hide()
            
        if not self.results_screen:
            self.results_screen = ResultsWindow(self)
            self.layout.addWidget(self.results_screen)
        
        self.results_screen.show()