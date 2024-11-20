"""Escreva um programa que peça ao usuário para digitar uma frase e imprima o número de caracteres na frase."""

def contar_caracteres():
    # Solicita ao usuário uma frase
    frase = input("Digite uma frase: ")
    
    # Conta o número de caracteres na frase
    numero_caracteres = len(frase)
    
    # Exibe o número de caracteres
    print(f"A frase possui {numero_caracteres} caracteres.")

# Executa o programa
contar_caracteres()
