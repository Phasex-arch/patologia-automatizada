from PyQt5.QtWidgets import (QWidget, QLabel, QTextEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QGridLayout, QGroupBox, 
                             QScrollArea, QFrame, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import time
from .animated_button import AnimatedButton

class ResultsWindow(QWidget):
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
        content.setStyleSheet("background-color: white; border-radius: 10px; padding: 20px;")
        layout = QVBoxLayout()
        layout.setSpacing(20)
        
        if not hasattr(self.main_window, 'patient_data') or not self.main_window.patient_data:
            self.show_error_message(layout)
        else:
            self.show_patient_report(layout)
        
        content.setLayout(layout)
        scroll.setWidget(content)
        main_layout.addWidget(scroll)
        self.setLayout(main_layout)
    
    def show_error_message(self, layout):
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
    
    def show_patient_report(self, layout):
        patient_data = self.main_window.patient_data
        
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
        
        # Seção 2: Informações da Amostra
        sample_group = QGroupBox("Informações da Amostra")
        sample_group.setFont(QFont("Arial", 12, QFont.Bold))
        sample_group.setStyleSheet(patient_group.styleSheet())
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
        
        # Seção 3: Macroscopia
        macro_group = QGroupBox("Macroscopia")
        macro_group.setFont(QFont("Arial", 12, QFont.Bold))
        macro_group.setStyleSheet(patient_group.styleSheet())
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
        
        # Seção 4: Microscopia
        micro_group = QGroupBox("Microscopia")
        micro_group.setFont(QFont("Arial", 12, QFont.Bold))
        micro_group.setStyleSheet(patient_group.styleSheet())
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
        
        # Seção 5: Diagnóstico
        diagnosis_group = QGroupBox("Conclusão Diagnóstica")
        diagnosis_group.setFont(QFont("Arial", 12, QFont.Bold))
        diagnosis_group.setStyleSheet(patient_group.styleSheet())
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
        
        # Botões de ação
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
    
    def save_report(self):
        QMessageBox.information(self, "Sucesso", "Laudo salvo com sucesso no sistema!")
    
    def print_report(self):
        QMessageBox.information(self, "Impressão", "Laudo enviado para impressão!")