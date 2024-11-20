"""Escreva um programa que solicite ao usuário uma quantidade de horas, minutos e segundos, e imprima uma mensagem formatada mostrando o total de segundos. Por exemplo: "O total de segundos é {total_segundos}."""

def calcular_total_segundos():
    # Solicita ao usuário as horas, minutos e segundos
    horas = int(input("Digite a quantidade de horas: "))
    minutos = int(input("Digite a quantidade de minutos: "))
    segundos = int(input("Digite a quantidade de segundos: "))

    # Calcula o total de segundos
    total_segundos = (horas * 3600) + (minutos * 60) + segundos

    # Exibe o total de segundos
    print(f"O total de segundos é {total_segundos}.")

# Executa o programa
calcular_total_segundos()
