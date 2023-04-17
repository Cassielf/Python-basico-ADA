numero_escolhido = 27
numero_informado = int(input("informe um número entre 1 e 30: "))

""" dessa maneira será pedido apenas uma vez o número para o usuário
if numero_informado == numero_escolhido:
    print("você acertou")

else:
    print("você errou")
"""
# Ao utilizar o while, o número será solicitado mais de uma vez desde que o usuário não consiga acertar

while numero_informado != numero_escolhido :
    print("você errou o número, tente novamente")
    numero_informado = int(input("informe um número entre 1 e 30: "))

print("parabéns! você acertou")

#é importante que a variável de input definida fora do loop também esteja dentro do while, caso esse valor seja sobrescrito a cada execução

#exemplo com contador

cont = 0

while cont < 10:
    print(cont)
    cont = cont+1