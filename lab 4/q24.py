"""Escreva um programa que solicite ao usuário para digitar seu endereço de e-mail e extraia o nome de usuário (parte antes do "@") e o domínio (parte depois do "@")."""

def extrair_email():
    # Solicita ao usuário o endereço de e-mail
    email = input("Digite seu endereço de e-mail: ")

    # Verifica se o e-mail contém o caractere "@" para garantir que é válido
    if "@" in email:
        # Divide o e-mail em nome de usuário e domínio
        nome_usuario, dominio = email.split("@")
        
        # Exibe o nome de usuário e o domínio
        print(f"Nome de usuário: {nome_usuario}")
        print(f"Domínio: {dominio}")
    else:
        print("Endereço de e-mail inválido. Por favor, insira um e-mail válido.")

# Executa o programa
extrair_email()
