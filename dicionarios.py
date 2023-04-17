#para criar um dicionario

dicionario = {}
dicionario1 = dict()

#dicionario com valores

dicionario = {'nome': 'Byanca', 'idade': 25, 'quantos gatos' : 5}

#adicionando novas chaves
dicionario['programadora'] = True

#sobrescrevendo conteudo
dicionario['idade'] = 26

print(dicionario)
print(dicionario['nome'])

# percorrendo as chaves - propriedades
for chave in dicionario:
    print(chave)

# percorrendo as chaves - propriedades com valor
for chave in dicionario:
    print(chave, dicionario[chave])

#testar se uma chave existe
print('peso' in dicionario)
print('nome' in dicionario)
