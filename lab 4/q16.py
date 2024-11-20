"""Escreva um programa que peça ao usuário para digitar seu nome completo e imprima apenas o primeiro nome."""

def exibir_primeiro_nome():
    # Solicita ao usuário o nome completo
    nome_completo = input("Digite seu nome completo: ")
    
    # Divide o nome completo e pega o primeiro nome
    primeiro_nome = nome_completo.split()[0]
    
    # Exibe o primeiro nome
    print(f"Seu primeiro nome é: {primeiro_nome}")

# Executa o programa
exibir_primeiro_nome()
