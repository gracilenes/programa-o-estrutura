"""Escreva um programa que solicite ao usuário uma frase e substitua todas as vogais por asteriscos (*). Em seguida, imprima a frase formatada."""

def substituir_vogais():
    frase = input("Digite uma frase: ")
    vogais = "aeiouAEIOU"
    
    # Substituir as vogais por asteriscos
    frase_formatada = ''.join('*' if char in vogais else char for char in frase)
    
    # Exibir a frase formatada
    print(f"Frase formatada: {frase_formatada}")

# Executa o programa
substituir_vogais()
