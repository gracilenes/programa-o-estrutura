"""Escreva um programa que solicite ao usuário para digitar seu nome e, em seguida, imprima as iniciais do nome em letras maiúsculas."""

def exibir_iniciais():
    # Solicita ao usuário seu nome completo
    nome = input("Digite seu nome completo: ")
    
    # Divide o nome completo em palavras
    palavras = nome.split()
    
    # Cria uma lista com as iniciais em maiúsculas
    iniciais = [palavra[0].upper() for palavra in palavras]
    
    # Exibe as iniciais
    print("Iniciais:", '.'.join(iniciais) + '.')

# Executa o programa
exibir_iniciais()
