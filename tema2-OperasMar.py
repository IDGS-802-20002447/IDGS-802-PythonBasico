num1=20
num2=10

print("Suma",(num1 + num2))
print("Resta",(num1 - num2))
print("Multiplicacion",(num1 * num2))
print("Division",(num1 / num2))
print("Division exacta",(num1 // num2))
print("Potencia",(num1 ** num2))

#Concatenacion en Python
texto1="Hola"
texto2="Mundo"

textoFinal=texto1+" "+texto2
print(textoFinal)
print("El salud es: %s %s" %(texto1,texto2))

saludoFinal="Saludo: {} {}".format(texto1,texto2)
# es la posicion de indice que se coloca en la cadena
saludoFinal2="Saludo 2: {0} {1}".format(texto1,texto2)

print(saludoFinal)
print(saludoFinal2)

#Colocar como un alias con x y Y
saludoFinal3="Saludo 3: {x} {y}".format(x=texto1,y=texto2)