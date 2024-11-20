"""Escreva um programa que solicite ao usuário um número decimal e imprima uma mensagem formatada mostrando o número com duas casas decimais."""

def formatar_decimal():
    # Solicita ao usuário um número decimal
    numero = float(input("Digite um número decimal: "))
    
    # Exibe o número formatado com duas casas decimais
    print(f"O número com duas casas decimais é: {numero:.2f}")

# Executa o programa
formatar_decimal()
