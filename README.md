# 📌 Agenda em Python

Este é um projeto simples de agenda em Python que permite salvar e visualizar compromissos usando um arquivo JSON para armazenar os dados.

## 📖 Sobre o Projeto

O programa permite:
- Exibir os compromissos salvos.
- Adicionar novos compromissos informando a data e a descrição.
- Salvar os compromissos de forma persistente em um arquivo `agenda.json`.

## 🖥️ Interface Gráfica
A aplicação possui um design simples e intuitivo, onde os compromissos são listados e podem ser adicionados facilmente.  

## 🛠 Tecnologias Utilizadas

- **Python 3**
- **Tkinter** (Interface Gráfica)
- **JSON** (Armazenamento de dados)

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/agenda.py.git
cd agenda.py
```

### 2️⃣ Executar o Script
```bash
python agenda_final.py
```

## 📌 Exemplo de Uso
```
================================= Programa de agenda =================================
Seus compromissos salvos na agenda são:

15/03/2025 -> Reunião com equipe
20/03/2025 -> Entrega do projeto

Aperte 0 para sair. Aperte qualquer outro botão para salvar um novo compromisso.
```

📝 Estrutura do Código
agenda_console.py → Versão que roda no terminal.
agenda_gui.py → Versão com interface gráfica.
carregar_info() → Carrega os compromissos do arquivo JSON.
salvar_info() → Salva um novo compromisso no JSON.
atualizar_lista() (apenas na versão GUI) → Atualiza a exibição dos compromissos na interface.

📝Guia das bibliotecas:
json -> https://docs.python.org/3/library/json.html


## 🔗 Contribuição
Sinta-se à vontade para contribuir com melhorias e novas funcionalidades! Faça um **fork** do projeto e envie um **pull request**.

---
Criado por Larissa(https://github.com/ldematos) 😊

