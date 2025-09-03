from PyQt5.QtWidgets import QWidget, QLabel, QProgressBar, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

class LoadingWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        title = QLabel("Analisando Amostra")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #023e8a; margin-bottom: 30px;")
        layout.addWidget(title)
        
        icon_label = QLabel()
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setText("🔬")
        icon_label.setStyleSheet("font-size: 60px; background-color: transparent;")
        layout.addWidget(icon_label)
        
        loading_text = QLabel("Processando amostra de tecido...")
        loading_text.setFont(QFont("Arial", 12))
        loading_text.setAlignment(Qt.AlignCenter)
        loading_text.setStyleSheet("color: #003566; margin: 20px 0;")
        layout.addWidget(loading_text)
        
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
        
        self.status_label = QLabel("Inicializando sistema...")
        self.status_label.setFont(QFont("Arial", 10))
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #666666; margin-top: 15px;")
        layout.addWidget(self.status_label)
        
        self.setLayout(layout)
        
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
        self.timer.start(100)
    
    def update_progress(self):
        self.progress_value += 2
        self.progress.setValue(self.progress_value)
        
        if self.progress_value // 20 > self.current_status and self.current_status < len(self.status_messages):
            self.current_status = self.progress_value // 20
            self.status_label.setText(self.status_messages[self.current_status - 1])
        
        if self.progress_value >= 100:
            self.timer.stop()
            self.main_window.show_results_screen()