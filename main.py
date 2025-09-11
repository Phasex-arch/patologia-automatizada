#!/usr/bin/env python3
"""
Ponto de entrada principal do Sistema de Patologia Digital.

Este módulo inicializa a aplicação Qt e inicia a janela principal.
É o arquivo que deve ser executado para iniciar o sistema.

Autor: Phase-X
Versão: 1.0
Data: 09/2025
"""

import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == '__main__':
    # Inicializa a aplicação Qt
    app = QApplication(sys.argv)
    
    # Cria e exibe a janela principal
    window = MainWindow()
    window.show()
    
    # Executa o loop de eventos da aplicação
    sys.exit(app.exec_())
