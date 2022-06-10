
'''
A continuación se va acrear un programa que permita realizar operaciones
matemáticas. El cuál contendrá clase/objetos, con atributos y métodos,
los cuales van a permitir realizar operaciones como suma, divición, factoriales. etc
para ello se van a definir las siguientes clases:

class calculo:
    def __init__(self, numero) -> None:
        self.numero=numero


'''

#Función que permite utilizar operaciones matemáticas como factorial especificamente.
from math import factorial

#Clase calculo con un solo parametro
class calculo:
    #Atributos
    def __init__(self, numero) -> None:
        self.numero=numero
    #Métodos
    def factorial (self):
        if (self.numero==0):
            return (1)
        else:
            return (self.numero*factorial((self.numero)-1))

    def suma(self):
        Suamtorita=(factorial((self.numero)-1)+self.numero)
        return(print("La sumatoria de los n primeros números es: ",Suamtorita))

    def testprimo(self):
            for n in range(2, self.numero): 
                if self.numero % n == 0:
                    print("No es primo", n, "es divisor") 
                    return False 
            print("Es primo")
            return True 


#Pedir datos al usuario
numero=int(input("Digite un número entero para realizar los calculos correspondientes: --> "))
#Instanciación de objeto
numero1=calculo(numero)
#ejecución de métodos
numero1.factorial()
print("El factorial de: ",str(numero1.numero), ": es: ", str(factorial(numero1.numero)))
numero1.suma()
numero1.testprimo()
