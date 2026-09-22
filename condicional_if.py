a = 10
b = 5

print(a > b) # True
print(a < b) # False
print(a != b) # True
print(a == b) # False   
#condicional, es una estructura la cual ingresa al bloque de código 
#mientras su condición sea verdadera
if a > b:
    print("'a' es mayor a 'b'")
#sino else ingresa si no es verdadera la primera condición if
if a > b:
    print("'a' es mayor a 'b'")
else:
    print("'a' es menor o igual a 'b'")

dia = "viernes"
if dia == "martes":
    print("es martes")
elif dia == "miércoles":
    print("es miércoles")
elif dia == "jueves":
    print("es jueves")
elif dia == "viernes":
    print("es viernes")
else:
    print("no se sabe que día")

usuario = None
password = None

#rolando@gmail.com y rolando12345 credenciales correctas
#operadores de union or and y not
if usuario == "rolando@gmail.com" and password == "rolando12345":
    print("Bienvenido al sistema")
else:
    print("Credenciales no válidas")