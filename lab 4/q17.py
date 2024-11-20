"""Escreva um programa que solicite ao usuário para digitar uma frase e conte quantas palavras existem na frase."""

def contar_palavras():
    # Solicita ao usuário uma frase
    frase = input("Digite uma frase: ")
    
    # Conta o número de palavras na frase (dividindo por espaços)
    numero_palavras = len(frase.split())
    
    # Exibe a quantidade de palavras
    print(f"A frase contém {numero_palavras} palavras.")

# Executa o programa
contar_palavras()
