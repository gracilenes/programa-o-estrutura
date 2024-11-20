"""Calculadora Simples: Faça uma calculadora que pede ao usuário dois números e uma operação (+, -, *, /) e retorna o resultado dessa operação."""

#pede ao usuario dois numeros
numero1 = int(input("Digite um numero:"))
numero2 = int(input("Digite um numero:"))
# uma operação (+, -, *, /)
operacao = input("Digite uma operação: (+, -, *, /)")

if operacao == "+":
    soma = numero1 + numero2
    print(f"A soma de {numero1} e {numero2} é: {soma}")
elif operacao == "-":
    subtracao = numero1 - numero2
    print(f"A subtração de {numero1} e {numero2} é: {subtracao}")
elif operacao == "*":
    multiplicação = numero1 * numero2
    print(f"A multiplicação de {numero1} e {numero2} é: {multiplicação}")
else:
    divisão = numero1 / numero2
    print(f"A divisão de {numero1} e {numero2} é: {divisão}")
