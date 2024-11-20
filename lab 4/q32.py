"""Escreva um programa para ler uma frase, imprima esta frase com as palavras ordenadas em ordem crescente de comprimento das strings."""

def ordenar_por_comprimento():
    # Solicita ao usuário uma frase
    frase = input("Digite uma frase: ")
    
    # Divide a frase em palavras
    palavras = frase.split()
    
    # Ordena as palavras pelo comprimento
    palavras_ordenadas = sorted(palavras, key=len)
    
    # Exibe as palavras ordenadas
    print("Palavras ordenadas por comprimento:")
    print(" ".join(palavras_ordenadas))

# Executa o programa
ordenar_por_comprimento()
