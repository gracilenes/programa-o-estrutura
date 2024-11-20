"""Escreva um programa que solicite ao usuário uma frase e imprima uma mensagem formatada mostrando a quantidade de caracteres, palavras e linhas na frase."""

def analisar_frase():
    frase = input("Digite uma frase: ")

    # Cálculo das métricas
    quantidade_caracteres = len(frase)
    quantidade_palavras = len(frase.split())
    quantidade_linhas = len(frase.splitlines())

    # Exibição dos resultados
    print(f"A frase possui:")
    print(f"- {quantidade_caracteres} caracteres.")
    print(f"- {quantidade_palavras} palavras.")
    print(f"- {quantidade_linhas} linhas.")

# Executa o programa
analisar_frase()
