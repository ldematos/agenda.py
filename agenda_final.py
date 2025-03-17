import json

nome_arquivo = "agenda.json"

def carregar_info():
    try:
        with open(nome_arquivo) as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def salvar_info(data, compromisso):
    info = carregar_info()
    info[data] = compromisso
    with open(nome_arquivo, "w") as arquivo:
        json.dump(info, arquivo, sort_keys=True, indent=4)

# Programa principal
print(" Programa de agenda ".center(40, "="))
info = carregar_info()

if info:
    print("Seus compromissos salvos na agenda são:\n")
    for data, compromisso in info.items():
        print(f"{data} -> {compromisso}")
else:
    print("Nenhum compromisso foi salvo ainda!")

while True:
    escolha = input("\nAperte 0 para sair. Aperte qualquer outro botão para salvar um novo compromisso.")

    if escolha == "0":
        break
    else:
        data_agend = input("\nDigite a data do seu compromisso (Dia/Mês/Ano): ")
        compro_agend = input("Digite o seu compromisso: ")
        salvar_info(data_agend, compro_agend)
        print(f"\nCompromisso para o dia {data_agend} foi salvo com sucesso!")

print(" Obrigado por usar o programa! ".center(45, "="))