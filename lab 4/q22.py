"""Escreva um programa que solicite ao usuário para digitar uma frase e conte quantas vezes uma determinada letra aparece na frase."""

def contar_letra():
    # Solicita ao usuário uma frase e a letra a ser contada
    frase = input("Digite uma frase: ")
    letra = input("Digite a letra que deseja contar: ")

    # Conta quantas vezes a letra aparece na frase
    quantidade = frase.count(letra)

    # Exibe o resultado
    print(f"A letra '{letra}' aparece {quantidade} vez(es) na frase.")

# Executa o programa
contar_letra()
