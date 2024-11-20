"""Escreva um programa que solicite ao usuário dois números e imprima uma mensagem formatada mostrando a soma, subtração, multiplicação e divisão dos números. Por exemplo: "A soma de {num1} e {num2} é {soma}."""

def operacoes_basicas():
    # Solicita os números ao usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Calcula as operações
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2 if num2 != 0 else "Indefinida (divisão por zero)"

    # Exibe os resultados formatados
    print(f"A soma de {num1} e {num2} é {soma}.")
    print(f"A subtração de {num1} e {num2} é {subtracao}.")
    print(f"A multiplicação de {num1} e {num2} é {multiplicacao}.")
    print(f"A divisão de {num1} por {num2} é {divisao}.")

# Executa o programa
operacoes_basicas()

