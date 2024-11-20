"""Escreva um programa que peça ao usuário para digitar seu nome completo e, em seguida, imprima apenas o sobrenome."""

def exibir_sobrenome():
    # Solicita ao usuário o nome completo
    nome_completo = input("Digite seu nome completo: ")
    
    # Divide o nome completo em partes (palavras)
    partes_nome = nome_completo.split()
    
    # O sobrenome é geralmente a última palavra
    sobrenome = partes_nome[-1]
    
    # Exibe o sobrenome
    print(f"Seu sobrenome é: {sobrenome}")

# Executa o programa
exibir_sobrenome()
