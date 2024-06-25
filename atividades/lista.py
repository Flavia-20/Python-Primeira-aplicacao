listaNum = [1,2,3,4,5,6,7,8,9,10]
print(listaNum)

listaNomes = ["Ana", "Bete","carlo", "Sandra"]
print(listaNomes)

listaAno = [2004, 2024]
print(listaAno)

print("=-=-=-=-=-=-=-=-=-=-=-")

lista=[]
for i in range(0, 10, 1):
    lista.append(i)
print(lista)

for num in lista:
    print(num)

print("=-=-=-=-=-=-=-=-=-=-=-")

listaImpar = []
for i in range(1, 11, 1):
    if i %2 != 0: 
        listaImpar.append(i)
print(sum(listaImpar))

print("=-=-=-=-=-=-=-=-=-=-=-")

lista = [] 
for i in range(1, 11, 1):
    lista.append(i)
    print(lista)
lista.reverse()
print(lista)

print("=-=-=-=-=-=-=-=-=-=-=-")

num = int(input("Digite um número: "))
for i in range(1, 11,1):
    print(f"{i} * {num} = {i*num}")

print("=-=-=-=-=-=-=-=-=-=-=-")



