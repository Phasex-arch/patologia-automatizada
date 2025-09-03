## 🏥 Sistema de Patologia Digital - Laudos Anatomopatológicos 🏥
![Banner](imgs/banner.jpg)

# Sistema Completo de Automação para Laudos Médicos
Sistema desenvolvido em Python com PyQt5 para automação de laudos anatomopatológicos. Permite que patologistas realizem todo o fluxo de trabalho digitalmente, desde o login até a geração completa do laudo médico.

### Objetivo
Automatizar e digitalizar o processo de criação de laudos anatomopatológicos, substituindo processos manuais por um fluxo digital eficiente, organizado e profissional, aumentando a produtividade e reduzindo erros.

## Funcionalidades

### Sistema de Autenticação
- Tela de login moderna com validação de usuário
- Interface profissional com dois painéis (logo + formulário)
- Feedback visual imediato para o usuário

### Gestão de Pacientes
- Formulário completo de cadastro de pacientes
- Campos organizados por categorias:
    - Identificação do paciente
    - Informações clínicas
    - Dados da amostra biológica
    - Informações do tecido

### Processo de Análise
- Tela de carregamento com barra de progresso animada
- Simulação de análise de amostras em tempo real
- Mensagens de status durante o processamento

### Geração Automática de Laudos
- Laudo completo com todas as seções médicas:
    - Identificação do paciente
    - Informações da amostra
    - Descrição macroscópica
    - Descrição microscópica
    - Diagnóstico final
    - Conclusões

### Operações de Sistema
- Simulação de salvamento de laudos
- Simulação de impressão de documentos
- Navegação entre telas intuitiva

## Tecnologias Utilizadas
- Python 3.8+ - Linguagem de programação principal
- PyQt5 5.15.9 - Framework para interface gráfica desktop
- Qt Designer - Para criação dos layouts (conceitual)
- CSS Integrado - Estilização avançada dos componentes

### Banco de Dados em Memória:
- Os registros são armazenados em um array chamado `database`, que pode conter até 100 registros.

## Arquitetura do Sistema
```bash
sistema_patologia/
├── main.py                    # Ponto de entrada da aplicação
├── README.md                  # Informações sobre o projeto
├── LICENSE                    # Licença do projeto
├── main_window.py             # Controlador principal das janelas
├── requirements.txt           # Dependências do projeto
└── 📁 widgets/               # Componentes personalizados
    ├── 📁 __init__.py        # Inicialização do pacote
    ├── 📁 animated_button.py # Botão com efeitos de animação
    ├── 📁 login_window.py    # Módulo de autenticação
    ├── 📁 patient_info_window.py # Formulário de pacientes
    ├── 📁 loading_window.py  # Tela de processamento
    └── 📁 results_window.py  # Gerador de laudos
```

## Funcionalidades Técnicas
### Fluxo de Trabalho
1. Autenticação → Cadastro → Análise → Laudo
2. Navegação linear entre telas
3. Persistência de dados durante a sessão

### Interface
- Design moderno com paleta de cores profissional (#023e8a)
- Componentes animados e interativos
- Layout responsivo e adaptável
- Scroll areas para conteúdo extenso
- Agrupamento visual por seções

### Performance
- Carregamento rápido das telas
- Animções suaves sem travamentos
- Interface responsiva

## Como Executar
### Pré-requisitos
- Python 3.8 ou superior
- pip install -r requirements.txt

### Instalação Rápida
```bash
# Clone o repositório
git clone https://github.com/Phasex-arch/patologia-automatizada
cd sistema-patologia

# Instale as dependências
pip install -r requirements.txt

# Execute o sistema
python main.py
```

### Instalação Manual
```bash
# Apenas PyQt5 necessário
pip install PyQt5==5.15.9

# Execute o sistema
python main.py
```

## Fluxo de Uso
1. Login no Sistema
- Insira credenciais (qualquer texto é aceito para demo)
- Interface com validação básica

2. Cadastro do Paciente
- Preencha formulário com dados completos
- Campos obrigatórios validados
- Organização por seções médicas

3. Processamento da Amostra
- Visualize barra de progresso animada
- Acompanhe status da análise
- Processamento automático ao finalizar

4. Geração do Laudo
- Visualize laudo completo formatado
- Use botões para ações:
    - Nova análise
    - Salvar laudo
    - Imprimir laudo

## Solução de Problemas
### Erro: PyQt5 não encontrado
```bash
pip install PyQt5
```

### Erro: Módulos não importados
Execute a partir do diretório raiz:
```bash
cd sistema-patologia
python main.py
```

### Interface travando
- Verifique se há processos Python antigos
- Reinicie a aplicação

## Próximas Melhorias
- Leitura automática da ficha
- Persistência em Banco de Dados
- Geração de PDF dos laudos
- Sistema de usuários com perfis
- Histórico de pacientes
- Integração com impressora
- Backup automático
- Modo escuro/claro
- Exportação para Excel
- Integração com Machine Learning

## Para Desenvolvedores
### Estrutura do Código
- Modular: Cada tela em arquivo separado
- Documentado: Docstrings completas
- Manutenível: Código organizado e comentado

### Padrões Utilizados
- MVC implícito na separação de telas
- Componentes reutilizáveis
- Estilização consistente

### ⚠️ Aviso Importante
Sistema de Demonstração - Este é um projeto para fins educacionais e de demonstração. Não deve ser utilizado em ambiente médico real sem as devidas validações, testes de segurança e conformidade com regulamentações de saúde

## Licença
Este projeto está licenciado sob a [All Rights Reserved](LICENSE).