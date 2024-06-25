pessoa = {'nome':'Fulano', 'idade':12, 'cidade':'lagarto'}
print(pessoa)

pessoa['idade']= 15
print(pessoa)

pessoa['profissao'] = 'Engenheiro'
print(pessoa)

del pessoa['cidade']
print(pessoa)

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)


pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")


frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)

