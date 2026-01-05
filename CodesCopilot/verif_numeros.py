#Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.  

def verifica_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
    
# Exemplo de uso
numero_entrada = int(input("Digite um número inteiro: "))
resultado = verifica_par_ou_impar(numero_entrada)
print(f"O número {numero_entrada} é {resultado}.")
