#Libreria para limpiar la pantalla
import os


class OperaBas:
    #Declaracion de propiedades
    num1=0
    num2=0
    res=0

    #self=this Para referenciar las propiedades
    #Para mandar variables usamos las comas y sino solo el self
    #Declaracion de constructor

    def __init__(self,a,b):
        self.num1=a
        self.num2=b

    #Declaracionde metodos de clase
    def suma(self):
        #num1=12
    # num2=10
        self.res=self.num1+self.num2
        print("La suma es: {}".format(self.res))

#Termina la clase y empieza a llamar para poder ejecutarse

def main():
        #Mandar llamar la libreria para limpiar
        os.system("cls")
        #Poner los parametros que se usaran
        obj=OperaBas(3,4)
        obj.suma()

if __name__ == "__main__":
        main()






