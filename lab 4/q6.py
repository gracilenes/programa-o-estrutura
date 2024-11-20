"""Escreva um programa que remova todos os espaços em branco de uma string."""

def remover_espacos(string):
    return string.replace(" ", "")

# Exemplo de uso
entrada = "Esta é uma frase com espaços."
saida = remover_espacos(entrada)
print(f"Entrada: '{entrada}'")
print(f"Saída: '{saida}'")
