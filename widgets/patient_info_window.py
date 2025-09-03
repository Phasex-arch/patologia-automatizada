"""
Módulo da tela de informações do paciente.

Este módulo contém a implementação do formulário de coleta de
dados do paciente e amostra para geração do laudo.

Classes:
    PatientInfoWindow: Tela de coleta de informações do paciente.
"""

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QGridLayout, QTextEdit, 
                             QComboBox, QDateEdit, QGroupBox, QScrollArea,
                             QFrame, QSpacerItem, QSizePolicy, QMessageBox)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
import time
from .animated_button import AnimatedButton


class PatientInfoWindow(QWidget):
    """
    Tela de coleta de informações do paciente e amostra.
    
    Esta janela contém um formulário abrangente para coletar
    todas as informações necessárias para gerar o laudo.
    
    Attributes:
        main_window (MainWindow): Referência à janela principal
        Vários campos de entrada para dados do paciente e amostra
    """
    
    def __init__(self, main_window):
        """
        Inicializa a tela de informações do paciente.
        
        Args:
            main_window (MainWindow): Instância da janela principal
        """
        super().__init__()
        self.main_window = main_window
        self.initUI()
        
    def initUI(self):
        """
        Configura a interface gráfica do formulário de paciente.
        
        Cira seções organizadas para:
        - Identificação do paciente
        - Informações clínicas
        - Dados da amostra
        - Informações do tecido
        """
        # Layout principal com margens
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # ===== CABEÇALHO =====
        header = QFrame()
        header.setStyleSheet("background-color: #023e8a; border-radius: 10px; padding: 15px;")
        header_layout = QHBoxLayout()
        
        # Informações do usuário logado
        user_info = QLabel(f"Dr. {self.main_window.logged_in_user}")
        user_info.setFont(QFont("Arial", 12, QFont.Bold))
        user_info.setStyleSheet("color: white;")
        
        # Título da página
        title = QLabel("Informações do Paciente")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: white;")
        
        # Botão de logout
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
        
        # Organizar cabeçalho
        header_layout.addWidget(user_info)
        header_layout.addWidget(title)
        header_layout.addWidget(logout_btn)
        header.setLayout(header_layout)
        
        main_layout.addWidget(header)
        
        # ===== ÁREA DE CONTEÚDO COM ROLAGEM =====
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
        
        # Widget de conteúdo
        content = QWidget()
        content.setStyleSheet("background-color: white; border-radius: 10px;")
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Estilo CSS personalizado para comboboxes
        combo_style = """
            QComboBox {
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: white;
                color: #333;
                min-height: 15px;
            }
            QComboBox:hover {
                border: 1px solid #023e8a;
                background-color: #f8f9fa;
            }
            QComboBox:focus {
                border: 2px solid #023e8a;
                background-color: #ffffff;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 30px;
                border-left: 1px solid #ddd;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
                background-color: #f8f9fa;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 6px solid #666;
                margin-right: 10px;
            }
            QComboBox::down-arrow:on {
                border-top: 6px solid #023e8a;
            }
            QComboBox QAbstractItemView {
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: white;
                selection-background-color: #023e8a;
                selection-color: white;
                outline: none;
                margin: 0px;
                padding: 0px;
            }
            QComboBox QAbstractItemView::item {
                padding: 12px 8px;
                border-bottom: 1px solid #f0f0f0;
                margin: 0px;
            }
            QComboBox QAbstractItemView::item:last {
                border-bottom: none;
            }
            QComboBox QAbstractItemView::item:selected {
                background-color: #023e8a;
                color: white;
                font-weight: bold;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #e6f0ff;
                color: #023e8a;
            }
            QComboBox QScrollBar:vertical {
                width: 12px;
                background: #f0f0f0;
            }
            QComboBox QScrollBar::handle:vertical {
                background: #023e8a;
                border-radius: 6px;
                min-height: 20px;
            }
            QComboBox QScrollBar::add-line:vertical, 
            QComboBox QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """
        
        # ===== SEÇÃO 1: IDENTIFICAÇÃO DO PACIENTE =====
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
        
        # Campos de identificação do paciente
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
        self.gender.setStyleSheet(combo_style)
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
        
        # ===== SEÇÃO 2: INFORMAÇÕES CLÍNICAS =====
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
        self.procedure_type.setStyleSheet(combo_style)
        self.procedure_type.currentTextChanged.connect(self.on_procedure_type_changed)
        clinical_layout.addWidget(self.procedure_type)
        
        # Campo dinâmico para "Outro" no procedimento (inicialmente oculto)
        self.other_procedure_layout = QHBoxLayout()
        self.other_procedure_label = QLabel("Especifique o procedimento:")
        self.other_procedure_label.setFont(QFont("Arial", 10))
        self.other_procedure_label.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        self.other_procedure_label.hide()

        self.other_procedure_input = QLineEdit()
        self.other_procedure_input.setFont(QFont("Arial", 10))
        self.other_procedure_input.setPlaceholderText("Digite o tipo de procedimento")
        self.other_procedure_input.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        self.other_procedure_input.hide()

        self.other_procedure_layout.addWidget(self.other_procedure_label)
        self.other_procedure_layout.addWidget(self.other_procedure_input)
        clinical_layout.addLayout(self.other_procedure_layout)
        
        clinical_layout.addWidget(QLabel("História clínica relevante:"))
        self.clinical_history = QTextEdit()
        self.clinical_history.setFont(QFont("Arial", 10))
        self.clinical_history.setMaximumHeight(100)
        self.clinical_history.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        clinical_layout.addWidget(self.clinical_history)
        
        clinical_group.setLayout(clinical_layout)
        layout.addWidget(clinical_group)
        
        # ===== SEÇÃO 3: DADOS DA AMOSTRA =====
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
        self.material_type.setStyleSheet(combo_style)
        self.material_type.currentTextChanged.connect(self.on_material_type_changed)
        sample_layout.addWidget(self.material_type, 0, 1)
        
        # Campo dinâmico para "Outro" no material (inicialmente oculto)
        self.other_material_layout = QHBoxLayout()
        self.other_material_label = QLabel("Especifique o material:")
        self.other_material_label.setFont(QFont("Arial", 10))
        self.other_material_label.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        self.other_material_label.hide()

        self.other_material_input = QLineEdit()
        self.other_material_input.setFont(QFont("Arial", 10))
        self.other_material_input.setPlaceholderText("Digite o tipo de material")
        self.other_material_input.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        self.other_material_input.hide()

        self.other_material_layout.addWidget(self.other_material_label)
        self.other_material_layout.addWidget(self.other_material_input)
        sample_layout.addLayout(self.other_material_layout, 1, 0, 1, 4)  # Ocupa toda a linha
        
        sample_layout.addWidget(QLabel("Quantidade e integridade:"), 2, 0)
        self.sample_quantity = QLineEdit()
        self.sample_quantity.setFont(QFont("Arial", 10))
        self.sample_quantity.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        sample_layout.addWidget(self.sample_quantity, 2, 1)
        
        sample_layout.addWidget(QLabel("Meio de conservação:"), 2, 2)
        self.preservation_medium = QComboBox()
        self.preservation_medium.addItems(["Formol", "Fresco", "Fixador especial"])
        self.preservation_medium.setFont(QFont("Arial", 10))
        self.preservation_medium.setStyleSheet(combo_style)
        sample_layout.addWidget(self.preservation_medium, 2, 3)
        
        sample_layout.addWidget(QLabel("Data e hora de coleta:"), 3, 0)
        self.collection_datetime = QLineEdit()
        self.collection_datetime.setText(time.strftime("%d/%m/%Y %H:%M"))
        self.collection_datetime.setFont(QFont("Arial", 10))
        self.collection_datetime.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 5px; background-color: white;")
        sample_layout.addWidget(self.collection_datetime, 3, 1)
        
        sample_group.setLayout(sample_layout)
        layout.addWidget(sample_group)
        
        # ===== SEÇÃO 4: INFORMAÇÕES DO TECIDO =====
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
        
        # ===== BOTÕES DE NAVEGAÇÃO =====
        button_layout = QHBoxLayout()
        
        # Botão Voltar
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
        
        # Botão Analisar Amostra
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
        
        # Finalizar configuração do conteúdo
        content.setLayout(layout)
        scroll.setWidget(content)
        main_layout.addWidget(scroll)
        
        self.setLayout(main_layout)
    
    def on_procedure_type_changed(self, text):
        """
        Mostra ou oculta o campo de especificação quando 'Outro' é selecionado no procedimento.
        
        Args:
            text (str): Texto selecionado no combobox
        """
        if text == "Outro":
            self.other_procedure_label.show()
            self.other_procedure_input.show()
            self.other_procedure_input.setFocus()
        else:
            self.other_procedure_label.hide()
            self.other_procedure_input.hide()
            self.other_procedure_input.clear()
    
    def on_material_type_changed(self, text):
        """
        Mostra ou oculta o campo de especificação quando 'Outro' é selecionado no material.
        
        Args:
            text (str): Texto selecionado no combobox de material
        """
        if text == "Outro":
            self.other_material_label.show()
            self.other_material_input.show()
            self.other_material_input.setFocus()
        else:
            self.other_material_label.hide()
            self.other_material_input.hide()
            self.other_material_input.clear()
    
    def analyze_sample(self):
        """
        Valida e processa os dados do formulário.
        
        Verifica se os campos obrigatórios foram preenchidos e,
        em case positivo, salva os dados e avança para a tela de carregamento.
        
        Em uma implementação real, aqui seria feita validação
        mais robusta dos dados inseridos.
        """
        # Validar campos obrigatórios
        if not all([self.patient_name.text(), self.record_number.text(), 
                   self.sample_code.text(), self.tissue_type.text()]):
            QMessageBox.warning(self, "Campos obrigatórios", 
                               "Por favor, preencha todos os campos obrigatórios.")
            return
        
        # Validar campo "Outro" do procedimento se necessário
        if self.procedure_type.currentText() == "Outro" and not self.other_procedure_input.text().strip():
            QMessageBox.warning(self, "Campo obrigatório", 
                               "Por favor, especifique o tipo de procedimento.")
            return
        
        # Validar campo "Outro" do material se necessário
        if self.material_type.currentText() == "Outro" and not self.other_material_input.text().strip():
            QMessageBox.warning(self, "Campo obrigatório", 
                               "Por favor, especifique o tipo de material.")
            return
        
        # Obter o tipo de procedimento (tratamento especial para "Outro")
        procedure_type = self.procedure_type.currentText()
        if procedure_type == "Outro":
            procedure_type = self.other_procedure_input.text().strip()
        
        # Obter o tipo de material (tratamento especial para "Outro")
        material_type = self.material_type.currentText()
        if material_type == "Outro":
            material_type = self.other_material_input.text().strip()
        
        # Salvar dados na janela principal
        self.main_window.patient_data = {
            "patient_name": self.patient_name.text(),
            "birth_date": self.birth_date.date().toString("dd/MM/yyyy"),
            "gender": self.gender.currentText(),
            "record_number": self.record_number.text(),
            "sample_code": self.sample_code.text(),
            "clinical_suspicion": self.clinical_suspicion.toPlainText(),
            "collection_site": self.collection_site.text(),
            "procedure_type": procedure_type,  # Usar o valor tratado
            "clinical_history": self.clinical_history.toPlainText(),
            "material_type": material_type,  # Usar o valor tratado
            "sample_quantity": self.sample_quantity.text(),
            "preservation_medium": self.preservation_medium.currentText(),
            "collection_datetime": self.collection_datetime.text(),
            "tissue_type": self.tissue_type.text(),
            "tissue_measurement": "2.5 x 1.8 x 0.5 cm",  # Valor simulado
            "tissue_weight": "0.8 g"  # Valor simulado
        }
        
        # Avançar para tela de carregamento
        self.main_window.show_loading_screen()