"""
Módulo da tela de carregamento.

Este módulo contém a implementação da tela de progresso durante
a análise simulada da amostra.

Classes:
    LoadingWindow: Tela de carregamento durante a análise.
"""

from PyQt5.QtWidgets import QWidget, QLabel, QProgressBar, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont


class LoadingWindow(QWidget):
    """
    Tela de carregamento durante a análise da amostra.
    
    Simula o processo de análise com uma barra de progresso
    e mensagens de status.
    
    Attributes:
        main_window (MainWindow): Referência à janela principal
        progress (QProgressBar): Barra de progresso da análise
        status_label (QLabel): Label para mensagens de status
        timer (QTimer): Timer para controlar a animação do progresso
    """
    
    def __init__(self, main_window):
        """
        Inicializa a tela de carregamento.
        
        Args:
            main_window (MainWindow): Instância da janela principal
        """
        super().__init__()
        self.main_window = main_window
        self.initUI()
        
    def initUI(self):
        """
        Configura a interface gráfica da tela de carregamento.
        
        Cria elementos visuais para simular o processo de análise:
        - Título
        - Ícone
        - Barra de progresso
        - Mensagens de status
        """
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
        
        # Label para mensagens de status
        self.status_label = QLabel("Inicializando sistema...")
        self.status_label.setFont(QFont("Arial", 10))
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color: #666666; margin-top: 15px;")
        layout.addWidget(self.status_label)
        
        self.setLayout(layout)
        
        # Configurar timer para simular progresso
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
        """
        Atualiza a barra de progresso и mensagens de status.
        
        Este método é chamado periodicamente pelo timer para
        simular o avanço do processo de análise.
        """
        self.progress_value += 2
        self.progress.setValue(self.progress_value)
        
        # Atualizar mensagem de status a cada 20%
        if self.progress_value // 20 > self.current_status and self.current_status < len(self.status_messages):
            self.current_status = self.progress_value // 20
            self.status_label.setText(self.status_messages[self.current_status - 1])
        
        # Quando completar, avançar para tela de resultados
        if self.progress_value >= 100:
            self.timer.stop()
            self.main_window.show_results_screen()