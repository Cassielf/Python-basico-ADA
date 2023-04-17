#A estrutura de lista permite que sejam armazenados mais de um tipo de variável 

#variaveis separadas
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

#em uma lista
notas = [7.9,9.7,8.2,5.1,2.0]

#lista vazia
lista = []
lista = list() #cria lista vazia, ou converte para o tipo lista

#listas de listas
lista1 = [7, ["Byanca e Fábio"], "tem 5 gatos"]

#acessando itens armazenados nas listas
#os indices sempre começam por 0, cada indice representa a posicao de algum item armazenado
#para acessar de maneira decrescente é so utilizar valores negativos

print (lista1[1], lista1[2])
print (lista1[-1], lista1[-2])

#para imprimir itens utilizando um intervalo de indices
print(lista1[0:3])
print(notas[0:]) #vai ate o final da lista
print(notas[0:5:2]) # imprime todas as notas de dois em dois

#percorrer uma lista item por item

for elemento in notas:
    print("valores armazenados", elemento)

# para saber a quantidade de itens na lista

print ("quantidade de itens: ", len(notas))

#usando o for, fica visivel o indices de cada item armazenado ou cada item

for i in range(len(notas)):
    #print(i)
    print(notas[i])



