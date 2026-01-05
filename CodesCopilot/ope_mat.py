# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def opera_matematica(num1, num2):
    return num1 + num2, num1 - num2, num1 * num2, num1 / num2
# Exemplo de uso
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma, subtracao, multiplicacao, divisao = opera_matematica(numero1, numero2)
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")

