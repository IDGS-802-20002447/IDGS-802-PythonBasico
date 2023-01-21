''' 
*Son inmutables, no se pueden cambiar sus valores una vez ya definidas
*NO SE CAMBIAN
'''

tupla=("uno","dos","tres")

print(tupla)

#Se puede ingresar cualquier tipo de valores
tuplasVariosDatos=(12,True,23.6,"Nadia",12+2j)
print(tuplasVariosDatos)

#Se pueden agregar adentro de tuplas varias
tuplasConTuplas=(1,2,3,4,(1,2,3))
print(tuplasConTuplas)

#Posicion de algun valor de la tupla
print(tuplasVariosDatos[3])
print(tuplasVariosDatos[-2])

#Se va a recorrer 
print(tuplasVariosDatos[:2])

#Solo se imprimira una parte de la tupla
print(tuplasVariosDatos[0:2])

a,b,c=tupla

print(a)
print(b)
print(c)

#Operaciones entre TUPLAS
tuplaNew=tupla+tuplasVariosDatos
print(tuplaNew)