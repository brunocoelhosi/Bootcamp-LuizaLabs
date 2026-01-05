# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!

def concatena_dados(dado1, dado2):
    return str(dado1) + " " +  str(dado2)

# Exemplo de uso
dado1 = input("Digite o primeiro dado: ")
dado2 = input("Digite o segundo dado: ")
resultado = concatena_dados(dado1, dado2)
print("Dados concatenados:", resultado)


