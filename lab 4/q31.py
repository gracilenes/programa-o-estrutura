"""Escreva um código que capitalize a primeira letra de cada palavra em uma frase. Exemplo: "python é incrível" deve se tornar "Python É Incrível"."""

def capitalizar_primeira_letra():
    # Solicita ao usuário uma frase
    frase = input("Digite uma frase: ")
    
    # Capitaliza a primeira letra de cada palavra na frase
    frase_capitalizada = frase.title()
    
    # Exibe a frase com a primeira letra de cada palavra em maiúscula
    print(f"Frase capitalizada: {frase_capitalizada}")

# Executa o programa
capitalizar_primeira_letra()
