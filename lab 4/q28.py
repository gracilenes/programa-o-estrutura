"""Escreva um programa que solicite ao usuário para digitar uma frase e, em seguida, divida a frase em palavras individuais e as imprima em linhas separadas."""

def dividir_palavras():
    # Solicita ao usuário uma frase
    frase = input("Digite uma frase: ")
    
    # Divide a frase em palavras usando o espaço como separador
    palavras = frase.split()
    
    # Imprime cada palavra em uma linha separada
    for palavra in palavras:
        print(palavra)

# Executa o programa
dividir_palavras()
