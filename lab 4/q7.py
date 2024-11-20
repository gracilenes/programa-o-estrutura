"""Escreva um programa que solicite ao usuário seu nome e idade e imprima uma mensagem formatada no seguinte formato: "Olá, {nome}! Você tem {idade} anos."""

def saudacao():
    nome = input("Digite seu nome: Gracilene")
    idade = input("Digite sua idade: 21")
    print(f"Olá, {nome}! Você tem {idade} anos.")

# Executa o programa
saudacao()
