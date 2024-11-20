"""Escreva um programa que solicite ao usuário para digitar uma frase e verifique se ela contém a palavra "Python"."""

def verificar_python():
    # Solicita ao usuário uma frase
    frase = input("Digite uma frase: ")
    
    # Verifica se a palavra "Python" está na frase
    if "Python" in frase:
        print("A frase contém a palavra 'Python'.")
    else:
        print("A frase NÃO contém a palavra 'Python'.")

# Executa o programa
verificar_python()
