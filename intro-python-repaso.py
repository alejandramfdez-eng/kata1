#Comentarios en una sola línea

"""
comentarios en varias lineas
esto si mola
"""

'''
otra forma de comentar
en varias lineas
'''

#salida de información
print("Salida de información")

#entrada de información
nombre = input("Ingresa su nombre: ")
#un input captura el dato ingresado por terminal y siempre lo devuelve en formato str
print("Su nombre es"+nombre+ "es un alumno")

#tipos de variables en python
#str 
#int
#float
#bool
variable = "@asdkjfasldkjrfuoiefjh"
print(type(variable))

#variables sensible a mayusculas y minusculas
variable1 = "Carlos"
vARIable1 = "Ivan"
Variable1 = "Jose"
print(variable1)
print(vARIable1)
print(Variable1)    

nombre = None

def nombrar():
    pass

#las variables de python son flexibles
nombre = "Rolando"
print(nombre)
nombre = True
print(nombre)
nombre = 100
print(nombre)

#reglas de nombres de variables 
#nombres de variables y funciones van en minusculas
#nombres de clases con la primera letra en mayusculas
#nombres de variables de tipo constante VALOR_PI=3.1434554
#DECLARACION DE VARIABLES
#NO SE PUEDE
#Numero antes de una letra en nombre de variable
#10valor="Ana"
#espacios entre nombre de variable
#cuenta bancaria =546546546546

nombre10 = "Maria"
#snake case o camel case
cuenta_bancaria_conjunta =546546546546
cuentaCorrienteCerrado = 4545748787

#casting o casteo
numero1 = "100"
numero2 = 50
suma = int(numero1) + numero2
print("la suma es",suma)
#se puede hacer el casting o conversacion de tipos de todas las variables
#str (aqui el valor), bool(aqui el valor), float(aqui el valor)
