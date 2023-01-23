
'''
leer el numero 5
5x1=5
Hasta el 
5X 10
'''

print("Introduce tu numero")

i=int(input('Dame numero para multiplicar:'))

for tem in range(1,11):
    print("La multi de {}+{}={}".format(tem,i,(tem*i)))
