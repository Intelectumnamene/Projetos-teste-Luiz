import random


print("Gerador de Dados")
nome = input("Qual seu nome?")
print("Olá {} ! Seja bem vindo ao gerador de dados.".format(nome))

def gerar_nome():
    nomes = ["Ana", "João", "Maria", "Pedro", "Laura"]
    return random.choice(nomes)

def gerar_email():
    emails = ["ana@email.com", "joao@email.com", "maria@email.com", "pedro@email.com", "laura@email.com"]
    return random.choice(emails)

def gerar_telefone():
    telefones = ["123456789", "987654321", "555555555", "888877776", "333333333"]
    return random.choice(telefones)

def gerar_cidade():
    cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Recife", "Porto Alegre"]
    return random.choice(cidades)

def gerar_estado():
    estados = ["SP", "RJ", "MG", "PE", "RS"]
    return random.choice(estados)

def salvar_dados(dados):
    with open("dados_gerados.txt", "a") as arquivo:
        arquivo.write("\n" + " ".join(map(str, dados)))

def apresentar_opcoes():
    print("Escolha uma ou mais opções abaixo:")
    print("1. Gerar Nome")
    print("2. Gerar E-mail")
    print("3. Gerar Telefone")
    print("4. Gerar Cidade")
    print("5. Gerar Estado")
    print("6. Salvar Dados em um Arquivo")
    print("Digite 'parar' para encerrar o programa")

opcoes = {
    1: gerar_nome,
    2: gerar_email,
    3: gerar_telefone,
    4: gerar_cidade,
    5: gerar_estado
}

dados_gerados = []

while True:
    apresentar_opcoes()
    escolhas = input("Digite o número da(s) opção(ões) desejada(s), separadas por espaço ou vírgula: ")

    if escolhas.lower() == 'parar':
        break

    escolhas = [int(opcao) for opcao in escolhas.replace(',', ' ').split() if opcao.isdigit() and 1 <= int(opcao) <= 6]

    for escolha in escolhas:
        if escolha in opcoes:
            resultado = opcoes[escolha]()
            dados_gerados.append(resultado)
            print(f"Resultado gerado para a opção {escolha}: {resultado}")
        elif escolha == 6:
            salvar_dados(dados_gerados)
            print("Dados salvos no arquivo.")
        else:
            print(f"Opção {escolha} não reconhecida. Tente novamente.")

print("Programa encerrado.")
