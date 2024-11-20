"""Escreva um programa que solicite ao usuário para digitar seu nome e imprima-o em formato invertido. Por exemplo, se o nome for "João Silva", o programa deve imprimir "avliS oãoJ"."""

def inverter_nome():
    # Solicita ao usuário seu nome
    nome = input("Digite seu nome: ")
    
    # Inverte o nome e exibe o resultado
    nome_invertido = nome[::-1]
    print(f"Nome invertido: {nome_invertido}")

# Executa o programa
inverter_nome()