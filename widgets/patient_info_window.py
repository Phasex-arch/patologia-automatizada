from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QGridLayout, QTextEdit, 
                             QComboBox, QDateEdit, QGroupBox, QScrollArea,
                             QFrame, QSpacerItem, QSizePolicy, QMessageBox)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
import time
from .animated_button import AnimatedButton

class PatientInfoWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()
        
    def initUI(self):
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
        
        # Área de conteúdo
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
        
        # Seção 1: Identificação do Paciente
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
        
        patient_layout.addWidget(QLabel("Código da amostra:"), 2, 0)
        self.sample_code = QLineEdit()
        self.sample_code.setFont(QFont("Arial", 10))
        self.sample_code.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        patient_layout.addWidget(self.sample_code, 2, 1)
        
        patient_group.setLayout(patient_layout)
        layout.addWidget(patient_group)
        
        # Seção 2: Informações Clínicas
        clinical_group = QGroupBox("Informações Clínicas")
        clinical_group.setFont(QFont("Arial", 12, QFont.Bold))
        clinical_group.setStyleSheet(patient_group.styleSheet())
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
        
        # Seção 3: Dados da Amostra
        sample_group = QGroupBox("Dados da Amostra")
        sample_group.setFont(QFont("Arial", 12, QFont.Bold))
        sample_group.setStyleSheet(patient_group.styleSheet())
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
        
        # Seção 4: Informações do Tecido
        tissue_group = QGroupBox("Informações do Tecido")
        tissue_group.setFont(QFont("Arial", 12, QFont.Bold))
        tissue_group.setStyleSheet(patient_group.styleSheet())
        tissue_layout = QVBoxLayout()
        
        tissue_layout.addWidget(QLabel("Tipo/Nome do tecido:"))
        self.tissue_type = QLineEdit()
        self.tissue_type.setFont(QFont("Arial", 10))
        self.tissue_type.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        tissue_layout.addWidget(self.tissue_type)
        
        tissue_group.setLayout(tissue_layout)
        layout.addWidget(tissue_group)
        
        # Botões de navegação
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
        if not all([self.patient_name.text(), self.record_number.text(), 
                   self.sample_code.text(), self.tissue_type.text()]):
            QMessageBox.warning(self, "Campos obrigatórios", 
                               "Por favor, preencha todos os campos obrigatórios.")
            return
        
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
            "tissue_type": self.tissue_type.text(),
            "tissue_measurement": "2.5 x 1.8 x 0.5 cm",
            "tissue_weight": "0.8 g"
        }
        
        self.main_window.show_loading_screen()