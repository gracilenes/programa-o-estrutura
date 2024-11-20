"""Escreva um programa que solicite ao usuário para digitar seu nome em letras minúsculas e, em seguida, imprima o nome com a primeira letra em maiúscula."""

def formatar_nome():
    # Solicita ao usuário o nome em letras minúsculas
    nome = input("Digite seu nome em letras minúsculas: ")
    
    # Formata o nome com a primeira letra maiúscula
    nome_formatado = nome.capitalize()
    
    # Exibe o nome formatado
    print(f"Nome formatado: {nome_formatado}")

# Executa o programa
formatar_nome()
