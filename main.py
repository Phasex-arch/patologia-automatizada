import sys
import time
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
                             QGridLayout, QTextEdit, QComboBox, QDateEdit,
                             QProgressBar, QMessageBox, QGroupBox, QScrollArea,
                             QFrame, QSpacerItem, QSizePolicy)
from PyQt5.QtCore import Qt, QDate, QTimer
from PyQt5.QtGui import QFont, QPixmap, QIcon, QFontDatabase

class AnimatedButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.PointingHandCursor)
        
    def enterEvent(self, event):
        self.setStyleSheet(self.styleSheet().replace("background-color: #023e8a;", "background-color: #003566;"))
        super().enterEvent(event)
        
    def leaveEvent(self, event):
        self.setStyleSheet(self.styleSheet().replace("background-color: #003566;", "background-color: #023e8a;"))
        super().leaveEvent(event)

class LoginWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()
        
    def initUI(self):
        # Layout principal
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(50, 50, 50, 50)
        
        # Painel esquerdo (imagem/decoração)
        left_panel = QFrame()
        left_panel.setStyleSheet("background-color: #023e8a; border-radius: 15px;")
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(20, 20, 20, 20)
        
        # Logo ou ícone
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
        
        # Painel direito (formulário)
        right_panel = QFrame()
        right_panel.setStyleSheet("background-color: #ffffff; border-radius: 15px;")
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(30, 30, 30, 30)
        
        # Título do formulário
        login_title = QLabel("Faça seu login")
        login_title.setFont(QFont("Arial", 18, QFont.Bold))
        login_title.setAlignment(Qt.AlignCenter)
        login_title.setStyleSheet("color: #023e8a; margin-bottom: 40px;")
        right_layout.addWidget(login_title)
        
        # Formulário de login
        form_layout = QVBoxLayout()
        form_layout.setSpacing(20)
        
        # Campo usuário
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
        
        # Campo senha
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
        
        # Espaçamento antes do botão
        right_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        # Botão de login (mais para baixo)
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
        
        # Mais espaçamento
        right_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        # Rodapé
        footer = QLabel("Sistema de Patologia v1.0 • Desenvolvido para profissionais de saúde")
        footer.setFont(QFont("Arial", 8))
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color: #666666; margin-top: 20px;")
        right_layout.addWidget(footer)
        
        right_panel.setLayout(right_layout)
        
        # Adicionar painéis ao layout principal
        main_layout.addWidget(left_panel)
        main_layout.addWidget(right_panel)
        
        self.setLayout(main_layout)
    
    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        # Verificação simples de credenciais
        if username and password:
            self.main_window.logged_in_user = username
            self.main_window.show_patient_info_screen()
        else:
            QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos.")

class PatientInfoWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()
        
    def initUI(self):
        # Layout principal com fundo
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Cabeçalho
        header = QFrame()
        header.setStyleSheet("background-color: #023e8a; border-radius: 10px; padding: 15px;")
        header_layout = QHBoxLayout()
        
        user_info = QLabel(f"Dr. {self.main_window.logged_in_user}")
        user_info.setFont(QFont("Arial", 12, QFont.Bold))
        user_info.setStyleSheet("color: white;")
        
        title = QLabel("Informações do Paciente")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: white;")
        
        logout_btn = QPushButton("Sair")
        logout_btn.setFont(QFont("Arial", 10))
        logout_btn.setStyleSheet("""
            QPushButton {
                background-color: #ffffff;
                color: #023e8a;
                padding: 8px 15px;
                border-radius: 5px;
                border: none;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)
        logout_btn.clicked.connect(self.main_window.show_login_screen)
        
        header_layout.addWidget(user_info)
        header_layout.addWidget(title)
        header_layout.addWidget(logout_btn)
        header.setLayout(header_layout)
        
        main_layout.addWidget(header)
        
        # Área de conteúdo com rolagem
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 10px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background: #023e8a;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)
        
        content = QWidget()
        content.setStyleSheet("background-color: white; border-radius: 10px;")
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Informações do paciente
        patient_group = QGroupBox("Identificação do Paciente")
        patient_group.setFont(QFont("Arial", 12, QFont.Bold))
        patient_group.setStyleSheet("""
            QGroupBox {
                color: #023e8a;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 15px;
                background-color: #fafafa;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        patient_layout = QGridLayout()
        patient_layout.setVerticalSpacing(15)
        patient_layout.setHorizontalSpacing(20)
        
        # Linha 1
        patient_layout.addWidget(QLabel("Nome completo:"), 0, 0)
        self.patient_name = QLineEdit()
        self.patient_name.setFont(QFont("Arial", 10))
        self.patient_name.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        patient_layout.addWidget(self.patient_name, 0, 1)
        
        patient_layout.addWidget(QLabel("Data de nascimento:"), 0, 2)
        self.birth_date = QDateEdit()
        self.birth_date.setCalendarPopup(True)
        self.birth_date.setDate(QDate.currentDate().addYears(-30))
        self.birth_date.setFont(QFont("Arial", 10))
        self.birth_date.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        patient_layout.addWidget(self.birth_date, 0, 3)
        
        # Linha 2
        patient_layout.addWidget(QLabel("Sexo:"), 1, 0)
        self.gender = QComboBox()
        self.gender.addItems(["Masculino", "Feminino", "Outro"])
        self.gender.setFont(QFont("Arial", 10))
        self.gender.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        patient_layout.addWidget(self.gender, 1, 1)
        
        patient_layout.addWidget(QLabel("Nº de prontuário:"), 1, 2)
        self.record_number = QLineEdit()
        self.record_number.setFont(QFont("Arial", 10))
        self.record_number.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        patient_layout.addWidget(self.record_number, 1, 3)
        
        # Linha 3
        patient_layout.addWidget(QLabel("Código da amostra:"), 2, 0)
        self.sample_code = QLineEdit()
        self.sample_code.setFont(QFont("Arial", 10))
        self.sample_code.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        patient_layout.addWidget(self.sample_code, 2, 1)
        
        patient_group.setLayout(patient_layout)
        layout.addWidget(patient_group)
        
        # Informações clínicas
        clinical_group = QGroupBox("Informações Clínicas")
        clinical_group.setFont(QFont("Arial", 12, QFont.Bold))
        clinical_group.setStyleSheet("""
            QGroupBox {
                color: #023e8a;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                margin-top: 20px;
                padding-top: 15px;
                background-color: #fafafa;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        clinical_layout = QVBoxLayout()
        clinical_layout.setSpacing(10)
        
        clinical_layout.addWidget(QLabel("Suspeita clínica / Hipótese diagnóstica:"))
        self.clinical_suspicion = QTextEdit()
        self.clinical_suspicion.setFont(QFont("Arial", 10))
        self.clinical_suspicion.setMaximumHeight(80)
        self.clinical_suspicion.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        clinical_layout.addWidget(self.clinical_suspicion)
        
        clinical_layout.addWidget(QLabel("Local anatômico da coleta:"))
        self.collection_site = QLineEdit()
        self.collection_site.setFont(QFont("Arial", 10))
        self.collection_site.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        clinical_layout.addWidget(self.collection_site)
        
        clinical_layout.addWidget(QLabel("Tipo de procedimento:"))
        self.procedure_type = QComboBox()
        self.procedure_type.addItems(["Biópsia", "Punção", "Ressecção cirúrgica", "Outro"])
        self.procedure_type.setFont(QFont("Arial", 10))
        self.procedure_type.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        clinical_layout.addWidget(self.procedure_type)
        
        clinical_layout.addWidget(QLabel("História clínica relevante:"))
        self.clinical_history = QTextEdit()
        self.clinical_history.setFont(QFont("Arial", 10))
        self.clinical_history.setMaximumHeight(100)
        self.clinical_history.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        clinical_layout.addWidget(self.clinical_history)
        
        clinical_group.setLayout(clinical_layout)
        layout.addWidget(clinical_group)
        
        # Dados da amostra
        sample_group = QGroupBox("Dados da Amostra")
        sample_group.setFont(QFont("Arial", 12, QFont.Bold))
        sample_group.setStyleSheet("""
            QGroupBox {
                color: #023e8a;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                margin-top: 20px;
                padding-top: 15px;
                background-color: #fafafa;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        sample_layout = QGridLayout()
        sample_layout.setVerticalSpacing(15)
        sample_layout.setHorizontalSpacing(20)
        
        sample_layout.addWidget(QLabel("Tipo de material:"), 0, 0)
        self.material_type = QComboBox()
        self.material_type.addItems(["Tecido", "Citologia", "Líquido", "Outro"])
        self.material_type.setFont(QFont("Arial", 10))
        self.material_type.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        sample_layout.addWidget(self.material_type, 0, 1)
        
        sample_layout.addWidget(QLabel("Quantidade e integridade:"), 0, 2)
        self.sample_quantity = QLineEdit()
        self.sample_quantity.setFont(QFont("Arial", 10))
        self.sample_quantity.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        sample_layout.addWidget(self.sample_quantity, 0, 3)
        
        sample_layout.addWidget(QLabel("Meio de conservação:"), 1, 0)
        self.preservation_medium = QComboBox()
        self.preservation_medium.addItems(["Formol", "Fresco", "Fixador especial"])
        self.preservation_medium.setFont(QFont("Arial", 10))
        self.preservation_medium.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        sample_layout.addWidget(self.preservation_medium, 1, 1)
        
        sample_layout.addWidget(QLabel("Data e hora de coleta:"), 1, 2)
        self.collection_datetime = QLineEdit()
        self.collection_datetime.setText(time.strftime("%d/%m/%Y %H:%M"))
        self.collection_datetime.setFont(QFont("Arial", 10))
        self.collection_datetime.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        sample_layout.addWidget(self.collection_datetime, 1, 3)
        
        sample_group.setLayout(sample_layout)
        layout.addWidget(sample_group)
        
        # Tipo/Nome do tecido
        tissue_group = QGroupBox("Informações do Tecido")
        tissue_group.setFont(QFont("Arial", 12, QFont.Bold))
        tissue_group.setStyleSheet("""
            QGroupBox {
                color: #023e8a;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                margin-top: 20px;
                padding-top: 15px;
                background-color: #fafafa;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        tissue_layout = QVBoxLayout()
        
        tissue_layout.addWidget(QLabel("Tipo/Nome do tecido:"))
        self.tissue_type = QLineEdit()
        self.tissue_type.setFont(QFont("Arial", 10))
        self.tissue_type.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        tissue_layout.addWidget(self.tissue_type)
        
        tissue_group.setLayout(tissue_layout)
        layout.addWidget(tissue_group)
        
        # Botões
        button_layout = QHBoxLayout()
        back_btn = QPushButton("Voltar")
        back_btn.setFont(QFont("Arial", 11))
        back_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                padding: 12px 20px;
                border-radius: 8px;
                border: none;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        back_btn.clicked.connect(self.main_window.show_login_screen)
        button_layout.addWidget(back_btn)
        
        button_layout.addStretch()
        
        analyze_btn = AnimatedButton("Analisar Amostra")
        analyze_btn.setFont(QFont("Arial", 11, QFont.Bold))
        analyze_btn.setStyleSheet("""
            QPushButton {
                background-color: #023e8a;
                color: white;
                padding: 12px 25px;
                border-radius: 8px;
                border: none;
            }
            QPushButton:hover {
                background-color: #003566;
            }
        """)
        analyze_btn.clicked.connect(self.analyze_sample)
        button_layout.addWidget(analyze_btn)
        
        layout.addLayout(button_layout)
        
        content.setLayout(layout)
        scroll.setWidget(content)
        main_layout.addWidget(scroll)
        
        self.setLayout(main_layout)
    
    def analyze_sample(self):
        # Validar campos obrigatórios
        if not all([self.patient_name.text(), self.record_number.text(), 
                   self.sample_code.text(), self.tissue_type.text()]):
            QMessageBox.warning(self, "Campos obrigatórios", 
                               "Por favor, preencha todos os campos obrigatórios.")
            return
        
        # Salvar dados
        self.main_window.patient_data = {
            "patient_name": self.patient_name.text(),
            "birth_date": self.birth_date.date().toString("dd/MM/yyyy"),
            "gender": self.gender.currentText(),
            "record_number": self.record_number.text(),
            "sample_code": self.sample_code.text(),
            "clinical_suspicion": self.clinical_suspicion.toPlainText(),
            "collection_site": self.collection_site.text(),
            "procedure_type": self.procedure_type.currentText(),
            "clinical_history": self.clinical_history.toPlainText(),
            "material_type": self.material_type.currentText(),
            "sample_quantity": self.sample_quantity.text(),
            "preservation_medium": self.preservation_medium.currentText(),
            "collection_datetime": self.collection_datetime.text(),
            "t tissue_type": self.tissue_type.text(),
            "tissue_measurement": "2.5 x 1.8 x 0.5 cm",  # Simulado
            "tissue_weight": "0.8 g"  # Simulado
        }
        
        self.main_window.show_loading_screen()

class LoadingWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        # Título
        title = QLabel("Analisando Amostra")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #023e8a; margin-bottom: 30px;")
        layout.addWidget(title)
        
        # Ícone de carregamento
        icon_label = QLabel()
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setText("🔬")
        icon_label.setStyleSheet("font-size: 60px; background-color: transparent;")
        layout.addWidget(icon_label)
        
        # Texto de carregamento
        loading_text = QLabel("Processando amostra de tecido...")
        loading_text.setFont(QFont("Arial", 12))
        loading_text.setAlignment(Qt.AlignCenter)
        loading_text.setStyleSheet("color: #003566; margin: 20px 0;")
        layout.addWidget(loading_text)
        
        # Barra de progresso
        self.progress = QProgressBar()
        self.progress.setFont(QFont("Arial", 10))
        self.progress.setStyleSheet("""
            QProgressBar {
                border: 2px solid #023e8a;
                border-radius: 10px;
                text-align: center;
                background-color: white;
                height: 20px;
            }
            QProgressBar::chunk {
                background-color: #023e8a;
                border-radius: 8px;
            }
        """)
        self.progress.setFixedWidth(400)
        layout.addWidget(self.progress)
        
        # Texto de status
        self.status_label = QLabel("Inicializando sistema...")
        self.status_label.setFont(QFont("Arial", 10))
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #666666; margin-top: 15px;")
        layout.addWidget(self.status_label)
        
        self.setLayout(layout)
        
        # Simular processo de análise
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0
        self.status_messages = [
            "Preparando amostra...",
            "Analisando estrutura celular...",
            "Processando imagens microscópicas...",
            "Gerando relatório preliminar...",
            "Finalizando análise..."
        ]
        self.current_status = 0
        self.timer.start(100)  # Atualizar a cada 100ms
    
    def update_progress(self):
        self.progress_value += 2
        self.progress.setValue(self.progress_value)
        
        # Atualizar mensagem de status a cada 20%
        if self.progress_value // 20 > self.current_status and self.current_status < len(self.status_messages):
            self.current_status = self.progress_value // 20
            self.status_label.setText(self.status_messages[self.current_status - 1])
        
        if self.progress_value >= 100:
            self.timer.stop()
            self.main_window.show_results_screen()

class ResultsWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()
        
    def initUI(self):
        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Cabeçalho
        header = QFrame()
        header.setStyleSheet("background-color: #023e8a; border-radius: 10px; padding: 15px;")
        header_layout = QHBoxLayout()
        
        user_info = QLabel(f"Dr. {self.main_window.logged_in_user}")
        user_info.setFont(QFont("Arial", 12, QFont.Bold))
        user_info.setStyleSheet("color: white;")
        
        title = QLabel("Laudo Anatomopatológico")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: white;")
        
        date_label = QLabel(time.strftime("%d/%m/%Y %H:%M"))
        date_label.setFont(QFont("Arial", 10))
        date_label.setStyleSheet("color: white;")
        
        header_layout.addWidget(user_info)
        header_layout.addWidget(title)
        header_layout.addWidget(date_label)
        header.setLayout(header_layout)
        
        main_layout.addWidget(header)
        
        # Área de conteúdo com rolagem
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background: #f0f0f0;
                width: 10px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background: #023e8a;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)
        
        content = QWidget()
        content.setStyleSheet("background-color: white; border-radius: 10px; padding: 20px;")
        layout = QVBoxLayout()
        layout.setSpacing(20)
        
        # Verificar se existem dados do paciente
        if not hasattr(self.main_window, 'patient_data') or not self.main_window.patient_data:
            error_label = QLabel("Nenhum dado de paciente disponível. Por favor, preencha o formulário primeiro.")
            error_label.setFont(QFont("Arial", 12))
            error_label.setStyleSheet("color: #d9534f; padding: 20px;")
            error_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(error_label)
            
            back_btn = QPushButton("Voltar ao Formulário")
            back_btn.setFont(QFont("Arial", 11))
            back_btn.setStyleSheet("""
                QPushButton {
                    background-color: #023e8a;
                    color: white;
                    padding: 12px 25px;
                    border-radius: 8px;
                    border: none;
                }
                QPushButton:hover {
                    background-color: #003566;
                }
            """)
            back_btn.clicked.connect(self.main_window.show_patient_info_screen)
            layout.addWidget(back_btn, alignment=Qt.AlignCenter)
            
            content.setLayout(layout)
            scroll.setWidget(content)
            main_layout.addWidget(scroll)
            self.setLayout(main_layout)
            return
        
        # Informações do paciente
        patient_data = self.main_window.patient_data
        
        patient_group = QGroupBox("Identificação do Paciente")
        patient_group.setFont(QFont("Arial", 12, QFont.Bold))
        patient_group.setStyleSheet("""
            QGroupBox {
                color: #023e8a;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 15px;
                background-color: #fafafa;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        patient_layout = QGridLayout()
        patient_layout.setVerticalSpacing(10)
        patient_layout.setHorizontalSpacing(20)
        
        def add_patient_info(label, value, row):
            label_widget = QLabel(label)
            label_widget.setFont(QFont("Arial", 10, QFont.Bold))
            label_widget.setStyleSheet("color: #003566;")
            patient_layout.addWidget(label_widget, row, 0)
            
            value_widget = QLabel(value)
            value_widget.setFont(QFont("Arial", 10))
            value_widget.setStyleSheet("color: #000000;")
            patient_layout.addWidget(value_widget, row, 1)
        
        add_patient_info("Nome:", patient_data.get("patient_name", "N/A"), 0)
        add_patient_info("Data de nascimento:", patient_data.get("birth_date", "N/A"), 1)
        add_patient_info("Sexo:", patient_data.get("gender", "N/A"), 2)
        add_patient_info("Nº de prontuário:", patient_data.get("record_number", "N/A"), 3)
        add_patient_info("Código da amostra:", patient_data.get("sample_code", "N/A"), 4)
        
        patient_group.setLayout(patient_layout)
        layout.addWidget(patient_group)
        
        # Informações da amostra
        sample_group = QGroupBox("Informações da Amostra")
        sample_group.setFont(QFont("Arial", 12, QFont.Bold))
        sample_group.setStyleSheet("""
            QGroupBox {
                color: #023e8a;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 15px;
                background-color: #fafafa;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        sample_layout = QGridLayout()
        sample_layout.setVerticalSpacing(10)
        sample_layout.setHorizontalSpacing(20)
        
        def add_sample_info(label, value, row):
            label_widget = QLabel(label)
            label_widget.setFont(QFont("Arial", 10, QFont.Bold))
            label_widget.setStyleSheet("color: #003566;")
            sample_layout.addWidget(label_widget, row, 0)
            
            value_widget = QLabel(value)
            value_widget.setFont(QFont("Arial", 10))
            value_widget.setStyleSheet("color: #000000;")
            sample_layout.addWidget(value_widget, row, 1)
        
        add_sample_info("Material recebido:", patient_data.get("material_type", "N/A"), 0)
        add_sample_info("Local da coleta:", patient_data.get("collection_site", "N/A"), 1)
        add_sample_info("Tipo de procedimento:", patient_data.get("procedure_type", "N/A"), 2)
        add_sample_info("Tipo de tecido:", patient_data.get("tissue_type", "N/A"), 3)
        add_sample_info("Medidas do tecido:", patient_data.get("tissue_measurement", "N/A"), 4)
        add_sample_info("Peso do tecido:", patient_data.get("tissue_weight", "N/A"), 5)
        add_sample_info("Meio de conservação:", patient_data.get("preservation_medium", "N/A"), 6)
        add_sample_info("Data/hora coleta:", patient_data.get("collection_datetime", "N/A"), 7)
        
        sample_group.setLayout(sample_layout)
        layout.addWidget(sample_group)
        
        # Macroscopia
        macro_group = QGroupBox("Macroscopia")
        macro_group.setFont(QFont("Arial", 12, QFont.Bold))
        macro_group.setStyleSheet("""
            QGroupBox {
                color: #023e8a;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 15px;
                background-color: #fafafa;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        macro_layout = QVBoxLayout()
        macro_text = QTextEdit()
        macro_text.setFont(QFont("Arial", 10))
        macro_text.setText(f"Amostra recebida em {patient_data.get('preservation_medium', 'N/A').lower()}, "
                          f"consistindo de fragmento(s) de tecido {patient_data.get('tissue_type', 'N/A').lower()} "
                          f"medindo {patient_data.get('tissue_measurement', 'N/A')} e pesando {patient_data.get('tissue_weight', 'N/A')}. "
                          "Superfície externa irregular. Corte com aspecto homogêneo, cor esbranquiçada.")
        macro_text.setReadOnly(True)
        macro_text.setStyleSheet("border: 1px solid #ddd; border-radius: 5px; padding: 10px; background-color: white;")
        macro_layout.addWidget(macro_text)
        macro_group.setLayout(macro_layout)
        layout.addWidget(macro_group)
        
        # Microscopia
        micro_group = QGroupBox("Microscopia")
        micro_group.setFont(QFont("Arial", 12, QFont.Bold))
        micro_group.setStyleSheet("""
            QGroupBox {
                color: #023e8a;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 15px;
                background-color: #fafafa;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        micro_layout = QVBoxLayout()
        micro_text = QTextEdit()
        micro_text.setFont(QFont("Arial", 10))
        micro_text.setText("Os cortes histológicos corados pela hematoxilina-eosina mostram fragmentos de tecido "
                          "com arquitetura preservada. Observa-se presença de células com núcleos hipercromáticos "
                          "e moderado pleomorfismo. Mitoses são raras. Não há evidência de invasão vascular ou "
                          "perineural. Margens cirúrgicas livres de comprometimento neoplásico.")
        micro_text.setReadOnly(True)
        micro_text.setStyleSheet("border: 1px solid #ddd; border-radius: 5px; padding: 10px; background-color: white;")
        micro_layout.addWidget(micro_text)
        micro_group.setLayout(micro_layout)
        layout.addWidget(micro_group)
        
        # Diagnóstico
        diagnosis_group = QGroupBox("Conclusão Diagnóstica")
        diagnosis_group.setFont(QFont("Arial", 12, QFont.Bold))
        diagnosis_group.setStyleSheet("""
            QGroupBox {
                color: #023e8a;
                border: 2px solid #e0e0e0;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 15px;
                background-color: #fafafa;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        diagnosis_layout = QVBoxLayout()
        diagnosis_text = QTextEdit()
        diagnosis_text.setFont(QFont("Arial", 10, QFont.Bold))
        diagnosis_text.setText("Fragmentos de tecido compatíveis com lesão benigna.\n"
                              "Sugere-se acompanhamento clínico conforme orientação médica.")
        diagnosis_text.setReadOnly(True)
        diagnosis_text.setStyleSheet("border: 1px solid #ddd; border-radius: 5px; padding: 10px; color: #023e8a; background-color: white;")
        diagnosis_layout.addWidget(diagnosis_text)
        diagnosis_group.setLayout(diagnosis_layout)
        layout.addWidget(diagnosis_group)
        
        # Botões
        button_layout = QHBoxLayout()
        back_btn = QPushButton("Nova Análise")
        back_btn.setFont(QFont("Arial", 11))
        back_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                padding: 12px 20px;
                border-radius: 8px;
                border: none;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        back_btn.clicked.connect(self.main_window.show_patient_info_screen)
        button_layout.addWidget(back_btn)
        
        button_layout.addStretch()
        
        save_btn = AnimatedButton("Salvar Laudo")
        save_btn.setFont(QFont("Arial", 11, QFont.Bold))
        save_btn.setStyleSheet("""
            QPushButton {
                background-color: #023e8a;
                color: white;
                padding: 12px 25px;
                border-radius: 8px;
                border: none;
            }
            QPushButton:hover {
                background-color: #003566;
            }
        """)
        save_btn.clicked.connect(self.save_report)
        button_layout.addWidget(save_btn)
        
        print_btn = QPushButton("Imprimir Laudo")
        print_btn.setFont(QFont("Arial", 11))
        print_btn.setStyleSheet("""
            QPushButton {
                background-color: #48cae4;
                color: white;
                padding: 12px 25px;
                border-radius: 8px;
                border: none;
            }
            QPushButton:hover {
                background-color: #0096c7;
            }
        """)
        print_btn.clicked.connect(self.print_report)
        button_layout.addWidget(print_btn)
        
        layout.addLayout(button_layout)
        
        content.setLayout(layout)
        scroll.setWidget(content)
        main_layout.addWidget(scroll)
        
        self.setLayout(main_layout)
    
    def save_report(self):
        QMessageBox.information(self, "Sucesso", "Laudo salvo com sucesso no sistema!")
    
    def print_report(self):
        QMessageBox.information(self, "Impressão", "Laudo enviado para impressão!")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logged_in_user = ""
        self.patient_data = {}
        self.initUI()
        
    def initUI(self):
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
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        # Inicializar as telas apenas quando necessário
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())