"""Escreva um programa que solicite ao usuário seu nome completo e imprima as iniciais de cada palavra em letras maiúsculas. Por exemplo, se o nome for "Fulano de Tal", o programa deve imprimir "F.D.T."""

def imprimir_iniciais():
    nome_completo = input("Digite seu nome completo: ")
    
    # Divide o nome completo em palavras e pega a inicial de cada palavra
    iniciais = '.'.join(palavra[0].upper() for palavra in nome_completo.split())
    
    # Adiciona um ponto final no final
    iniciais_formatadas = iniciais + '.'
    
    print(f"Iniciais: {iniciais_formatadas}")

# Executa o programa
imprimir_iniciais()
