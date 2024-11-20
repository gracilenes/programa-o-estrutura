"""Escreva um programa que solicite ao usuário para digitar uma frase e substitua todas as ocorrências da letra "a" por "@"."""

def substituir_a_por_arroba():
    # Solicita ao usuário uma frase
    frase = input("Digite uma frase: ")
    
    # Substitui todas as ocorrências da letra "a" por "@"
    frase_modificada = frase.replace('a', '@')
    
    # Exibe a frase modificada
    print(f"Frase modificada: {frase_modificada}")

# Executa o programa
substituir_a_por_arroba()
