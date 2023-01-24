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
     
        self.res=self.num1+self.num2
        print("La suma es: {}".format(self.res))
    
    def resta(self):
        #num1=12
    # num2=10
        self.res=self.num1-self.num2
        print("La resta es: {}".format(self.res))
    
 


def main():
         salida=1
         while salida!=2:
            opcion=int(input("ingrese numeros: 1.Suma 2.Resta 3.Salir")) 
            if opcion==1:  
                    num1=int(input('Dame num1:  '))
                    num2=int(input('Dame num2:  ')) 
                    obj=OperaBas(num1,num2)
                    obj.suma()
                

            if opcion==2:
                    num1=int(input('Dame num1:  '))
                    num2=int(input('Dame num2:  ')) 
                    obj=OperaBas(num1,num2)
                    obj.resta
                    

            if opcion==3:
                    print("Adios")
                    salida=0
                    break

if __name__ == "__main__":
        main()









#Termina la clase y empieza a llamar para poder ejecutarse







