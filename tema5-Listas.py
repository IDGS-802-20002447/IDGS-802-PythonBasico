'''
Listas
*una lista es una secuencia de elementos.
*Cuando se asigna a una variable, permite agrupar varios elemento en un solo lugar.
*Se crea con los [] o con la keywoard list
'''


#Se admite cualquier tipo de datos
lista1=["Nadia",33,99.6,True,"Juarez",20,8]
print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[-1])
print(lista1[0:3])
#Imprimira apartir del 3
print(lista1[3:])

lista1.append("Juarez")
print(lista1)

lista1.insert(2,"Vianey")
print(lista1)

lista1.extend(["uno",1.1,False])
print(lista1)

lista1.remove(8)
print(lista1)

lista1.pop
print(lista1)

lista2=["tres","cuatro"]

lista3=lista1+lista2
print(lista3)

print(lista2*4)

lista4=[2,1,5,4,3]
print(lista4)

#ordena la lista
lista4=lista4.sort()
print(lista4)

del lista4[0]
print(lista4)
