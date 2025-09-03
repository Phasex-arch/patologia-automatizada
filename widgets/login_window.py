from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QFrame, QMessageBox,
                             QSpacerItem, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from .animated_button import AnimatedButton

class LoginWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()
        
    def initUI(self):
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(50, 50, 50, 50)
        
        # Painel esquerdo
        left_panel = QFrame()
        left_panel.setStyleSheet("background-color: #023e8a; border-radius: 15px;")
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(20, 20, 20, 20)
        
        logo_label = QLabel()
        logo_label.setAlignment(Qt.AlignCenter)
        logo_label.setText("🔬")
        logo_label.setStyleSheet("font-size: 80px; color: #ffffff; background-color: transparent;")
        
        title = QLabel("Sistema de\nPatologia Digital")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #ffffff; background-color: transparent;")
        
        subtitle = QLabel("Laudos Anatomopatológicos")
        subtitle.setFont(QFont("Arial", 12))
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: #ffffff; background-color: transparent; margin-top: 10px;")
        
        left_layout.addStretch()
        left_layout.addWidget(logo_label)
        left_layout.addWidget(title)
        left_layout.addWidget(subtitle)
        left_layout.addStretch()
        
        left_panel.setLayout(left_layout)
        left_panel.setFixedWidth(300)
        
        # Painel direito
        right_panel = QFrame()
        right_panel.setStyleSheet("background-color: #ffffff; border-radius: 15px;")
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(30, 30, 30, 30)
        
        login_title = QLabel("Faça seu login")
        login_title.setFont(QFont("Arial", 18, QFont.Bold))
        login_title.setAlignment(Qt.AlignCenter)
        login_title.setStyleSheet("color: #023e8a; margin-bottom: 40px;")
        right_layout.addWidget(login_title)
        
        form_layout = QVBoxLayout()
        form_layout.setSpacing(20)
        
        user_label = QLabel("Usuário:")
        user_label.setFont(QFont("Arial", 10, QFont.Bold))
        user_label.setStyleSheet("color: #003566;")
        form_layout.addWidget(user_label)
        
        self.username_input = QLineEdit()
        self.username_input.setFont(QFont("Arial", 10))
        self.username_input.setPlaceholderText("Digite seu nome de usuário")
        self.username_input.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 2px solid #dddddd;
                border-radius: 8px;
                background-color: #f9f9f9;
            }
            QLineEdit:focus {
                border: 2px solid #023e8a;
                background-color: #ffffff;
            }
        """)
        form_layout.addWidget(self.username_input)
        
        password_label = QLabel("Senha:")
        password_label.setFont(QFont("Arial", 10, QFont.Bold))
        password_label.setStyleSheet("color: #003566;")
        form_layout.addWidget(password_label)
        
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFont(QFont("Arial", 10))
        self.password_input.setPlaceholderText("Digite sua senha")
        self.password_input.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                border: 2px solid #dddddd;
                border-radius: 8px;
                background-color: #f9f9f9;
            }
            QLineEdit:focus {
                border: 2px solid #023e8a;
                background-color: #ffffff;
            }
        """)
        form_layout.addWidget(self.password_input)
        
        right_layout.addLayout(form_layout)
        right_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        login_btn = AnimatedButton("Entrar no Sistema")
        login_btn.setFont(QFont("Arial", 12, QFont.Bold))
        login_btn.setStyleSheet("""
            QPushButton {
                background-color: #023e8a;
                color: white;
                padding: 15px;
                border-radius: 8px;
                border: none;
                margin-top: 30px;
            }
            QPushButton:hover {
                background-color: #003566;
            }
            QPushButton:pressed {
                background-color: #00264d;
            }
        """)
        login_btn.clicked.connect(self.login)
        right_layout.addWidget(login_btn)
        
        right_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        footer = QLabel("Sistema de Patologia v1.0 • Desenvolvido para profissionais de saúde")
        footer.setFont(QFont("Arial", 8))
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color: #666666; margin-top: 20px;")
        right_layout.addWidget(footer)
        
        right_panel.setLayout(right_layout)
        
        main_layout.addWidget(left_panel)
        main_layout.addWidget(right_panel)
        self.setLayout(main_layout)
    
    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        if username and password:
            self.main_window.logged_in_user = username
            self.main_window.show_patient_info_screen()
        else:
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos.")