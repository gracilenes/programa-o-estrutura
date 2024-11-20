"""Escreva um programa que solicite ao usuário para digitar uma frase e verifique se ela termina com um ponto final."""

def verificar_ponto_final():
    # Solicita ao usuário uma frase
    frase = input("Digite uma frase: ")
    
    # Verifica se a frase termina com um ponto final
    if frase.endswith('.'):
        print("A frase termina com um ponto final.")
    else:
        print("A frase NÃO termina com um ponto final.")

# Executa o programa
verificar_ponto_final()
