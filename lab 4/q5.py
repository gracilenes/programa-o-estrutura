"""Escreva um programa que verifique se uma palavra é um palíndromo (lê-se igual de trás para frente). Exemplo: "radar"."""

def eh_palindromo(palavra):
    # Remove espaços e converte para minúsculas para garantir a comparação
    palavra = palavra.replace(" ", "").lower()
    # Verifica se a palavra é igual à sua versão invertida
    return palavra == palavra[::-1]

# Exemplo de uso
entrada = "radar"
if eh_palindromo(entrada):
    print(f'"{entrada}" é um palíndromo!')
else:
    print(f'"{entrada}" não é um palíndromo.')
