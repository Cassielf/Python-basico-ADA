# metodos de listas
lista = [1, 3, 12, 8, 2]
print("antes do append", lista)

# append - adiciona itens no final da lista
lista.append(14)
print("depois do append", lista)

#insert - adiciona itens escolhendo a posicao do indice (n1 - indice, n2 valor)
lista.insert(2,10)
print("usando o insert", lista)

#extend - traz os valores de uma outra lista inserindo-os no final
lista2 = [20,14,94]
lista.extend(lista2)
print(lista)

#pop - remove itens da lista, caso nao seja indicado o indice será removido o ultimo item
lista.pop()
print("removendo com o pop vazio",lista)

lista.pop(0)
print("removendo com o pop com indice", lista)

#remove - serve para realizar a delecao de um item baseado no primeiro valor que ele encontra
#lista.remove(14)
#print("usando o remove",lista)

#count - usado para contar a quantidade vezes que um item aparece numa lista
print("quantidade de vezes que o 14 aparece",lista.count(14))

#index - informa qual é o indice que determinado valor está

print("indice do elemento 8 ",lista.index(8))

#sort - é usado para ordenar de maneira crescente ou decrescente os itens da lista
lista.sort()
print("lista crescente",lista)

lista.sort(reverse=True)
print("lista decrescente",lista)

#len - para saber a quantidade de itens que existe na lista
print("quantidade de itens na lista",len(lista))

#sum - soma todos os elementos da lista
print("valor total da lista",sum(lista))

#min - menor valor da lista
print("menor valor da lista", min(lista))

#max - maior valor da lista
print("maior valor da lista", max(lista))