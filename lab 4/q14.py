"""Escreva um programa que solicite ao usuário uma palavra e imprima uma mensagem formatada mostrando a palavra em caixa alta e caixa baixa."""

def formatar_palavra():
    # Solicita ao usuário uma palavra
    palavra = input("Digite uma palavra: ")
    
    # Exibe a palavra em caixa alta e caixa baixa
    print(f"A palavra em caixa alta: {palavra.upper()}")
    print(f"A palavra em caixa baixa: {palavra.lower()}")

# Executa o programa
formatar_palavra()
