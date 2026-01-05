# Vamos solicitar uma string e um número inteiro como entrada. Depois, retornaremos a string repetida o número de vezes informado.

def repete_string(texto, vezes):
    return (texto + " ") * vezes

# Exemplo de uso
string_entrada = input("Digite uma string: ")
numero_entrada = int(input("Digite um número inteiro: "))
resultado = repete_string(string_entrada, numero_entrada)
print(f"String repetida: {resultado}")
