"""
Módulo do botão animado personalizado.

Este módulo contém a implementação de um botão personalizado com
efeitos de animação quando o mouse passa por cima.

Classes:
    AnimatedButton: Botão com efeitos de hover personalizados.
"""

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt


class AnimatedButton(QPushButton):
    """
    Botão personalizado com efeitos de animação ao passar o mouse.
    
    Herda de QPushButton e adiciona efeitos visuais para melhorar
    a experiência do usuário.
    
    Attributes:
        Nenhum atributo adicional além dos herdados de QPushButton.
    """
    
    def __init__(self, text, parent=None):
        """
        Inicializa o botão animado.
        
        Args:
            text (str): Texto a ser exibido no botão
            parent (QWidget, optional): Widget pai. Defaults to None.
        """
        super().__init__(text, parent)
        self.setCursor(Qt.PointingHandCursor)  # Cursor de mão ao passar sobre o botão
        
    def enterEvent(self, event):
        """
        Evento acionado quando o mouse entra na área do botão.
        
        Altera a cor de fundo para um tom mais escuro para dar
        feedback visual ao usuário.
        """
        self.setStyleSheet(self.styleSheet().replace("background-color: #023e8a;", "background-color: #003566;"))
        super().enterEvent(event)
        
    def leaveEvent(self, event):
        """
        Evento acionado quando o mouse sai da área do botão.
        
        Restaura a cor original do botão.
        """
        self.setStyleSheet(self.styleSheet().replace("background-color: #003566;", "background-color: #023e8a;"))
        super().leaveEvent(event)