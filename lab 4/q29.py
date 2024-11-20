"""Escreva um programa que substitua todas as ocorrências de uma determinada palavra em uma frase por outra palavra fornecida pelo usuário."""

def substituir_palavra():
    # Solicita ao usuário a frase, a palavra a ser substituída e a nova palavra
    frase = input("Digite uma frase: ")
    palavra_antiga = input("Digite a palavra que deseja substituir: ")
    palavra_nova = input("Digite a nova palavra: ")
    
    # Substitui todas as ocorrências da palavra antiga pela nova
    frase_modificada = frase.replace(palavra_antiga, palavra_nova)
    
    # Exibe a frase modificada
    print(f"Frase modificada: {frase_modificada}")

# Executa o programa
substituir_palavra()
