#range tem a mesma função que o contador, isto é, será executado a quantidade de vezes definida dentro do parenteses

'''for i in range(10):
    print (i)

#o range pode ter até 3 parâmetros
for i in range(1, 10): # nesse exemplo, ele define o inicio do contador e vai até a quantidade de vezes informada -1, que no caso foi o 9
    print (i)

for i in range(1, 12, 3): #nesse exemplo foi definido o inicio do contador, e o limite até onde o contador deve ir, e quantos steps ou passos que no caso foi de 3 em 3
    print (i) '''

# um programa simples para receber notas e calcular media

soma = 0

for i in range(1,4):
    nota = float(input(f"Informe sua nota [1]: "))
    
    soma = soma+nota

media = soma/i

print("sua média é: ", media)