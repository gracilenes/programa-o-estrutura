"""Escreva um programa que solicite ao usuário um nome e um número inteiro e imprima uma mensagem formatada repetindo o nome o número de vezes especificado. Por exemplo, se o nome for "João" e o número for 3, o programa deve imprimir "JoãoJoãoJoão"."""

def repetir_nome():
    # Solicita ao usuário o nome e o número de repetições
    nome = input("Digite seu nome: ")
    numero = int(input("Digite um número inteiro: "))
    
    # Repete o nome o número de vezes especificado
    resultado = nome * numero
    
    # Exibe a mensagem formatada
    print(f"O nome repetido é: {resultado}")

# Executa o programa
repetir_nome()
