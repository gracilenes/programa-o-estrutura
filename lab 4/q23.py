"""Escreva um programa que solicite ao usuário para digitar uma frase e verifique se todas as palavras estão em letras maiúsculas"""

def verificar_maiusculas():
    # Solicita ao usuário uma frase
    frase = input("Digite uma frase: ")
    
    # Divide a frase em palavras
    palavras = frase.split()
    
    # Verifica se todas as palavras estão em maiúsculas
    if all(palavra.isupper() for palavra in palavras):
        print("Todas as palavras estão em letras maiúsculas.")
    else:
        print("Nem todas as palavras estão em letras maiúsculas.")

# Executa o programa
verificar_maiusculas()
