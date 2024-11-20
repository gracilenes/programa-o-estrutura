"""Maior de Três Números: Escreva um programa que solicita três números ao usuário e retorna o maior dentre eles."""

numero1 = int(input("Digite o número 1: "))
numero2 = int(input("Digite o número 2: "))
numero3 = int(input("Digite o número 3: "))

if numero1 > numero2 and numero1 > numero3:
    print("O maior número é: {numero1}")
if numero2 > numero1 and numero2 > numero3:
    print("O maior número é: {numero2:}")
if numero3 > numero2 and numero3 > numero1:
    print("O maior número é: {numero3:}")