#CONVERSÃO DE TIPOS

idade = "26"
numero1 = "10"
numero2 = "55"

print(numero1+numero2)

print (idade, type(idade))

idade_inteira = int(idade)

print (idade_inteira, type(idade_inteira))

"""
funções para conversão de tipos
int()
str()
float()
bool()

por padrão todo input recebe string, por tanto ou vc converte no momento que recebe, ou depois de ter recebido o valor na variavel
"""

altura = float(input ("informe sua altura: "))
print(altura, type(altura))