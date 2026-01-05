#Vamos testar se uma palavra é um palíndromo. 

def verifica_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

# Exemplo de uso
palavra_entrada = input("Digite uma palavra: ")
if verifica_palindromo(palavra_entrada):
    print(f"A palavra '{palavra_entrada}' é um palíndromo.")
else:
    print(f"A palavra '{palavra_entrada}' não é um palíndromo.")