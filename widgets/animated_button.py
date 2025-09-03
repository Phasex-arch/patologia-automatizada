from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt

class AnimatedButton(QPushButton):
    """
    Botão personalizado com efeitos de animação ao passar o mouse.
    """
    
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.PointingHandCursor)
        
    def enterEvent(self, event):
        self.setStyleSheet(self.styleSheet().replace("background-color: #023e8a;", "background-color: #003566;"))
        super().enterEvent(event)
        
    def leaveEvent(self, event):
        self.setStyleSheet(self.styleSheet().replace("background-color: #003566;", "background-color: #023e8a;"))
        super().leaveEvent(event)