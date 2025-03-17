import tkinter as tk
from tkinter import messagebox
import json

# Nome do arquivo JSON
nome_arquivo = "agenda.json"

# Função para carregar compromissos do arquivo JSON
def carregar_info():
    try:
        with open(nome_arquivo) as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Função para salvar compromisso no JSON
def salvar_info():
    data = entry_data.get()
    compromisso = entry_compromisso.get()

    if data and compromisso:
        info = carregar_info()
        info[data] = compromisso

        with open(nome_arquivo, "w") as arquivo:
            json.dump(info, arquivo, sort_keys=True, indent=4)

        # Atualiza a lista na interface
        atualizar_lista()
        messagebox.showinfo("Sucesso", f"Compromisso em {data} salvo!")
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos!")

# Função para atualizar a lista de compromissos na interface
def atualizar_lista():
    lista_eventos.delete(0, tk.END)  # Limpa a lista
    info = carregar_info()
    for data, compromisso in info.items():
        lista_eventos.insert(tk.END, f"{data} -> {compromisso}")

# Criando a janela principal
root = tk.Tk()
root.title("Agenda - Tkinter")
root.geometry("400x500")
root.configure(bg="#f8f8f8")

# Título
titulo = tk.Label(root, text="Agenda de Compromissos", font=("Arial", 14, "bold"), bg="#f8f8f8")
titulo.pack(pady=10)

# Lista de compromissos
lista_eventos = tk.Listbox(root, font=("Arial", 12), height=10, bg="#ffebcd")
lista_eventos.pack(pady=10, padx=10, fill="both")

# Campos para entrada de dados
tk.Label(root, text="Data (DD/MM/AAAA):", bg="#f8f8f8").pack()
entry_data = tk.Entry(root, font=("Arial", 12))
entry_data.pack(pady=5)

tk.Label(root, text="Compromisso:", bg="#f8f8f8").pack()
entry_compromisso = tk.Entry(root, font=("Arial", 12))
entry_compromisso.pack(pady=5)

# Botão para salvar compromisso
botao_salvar = tk.Button(root, text="Salvar Compromisso", font=("Arial", 12), bg="#ffcc99", command=salvar_info)
botao_salvar.pack(pady=10)

# Atualiza lista ao iniciar
atualizar_lista()

# Executa a interface gráfica
root.mainloop()