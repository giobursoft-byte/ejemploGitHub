# - Escriba un algoritmo que muestre la tabla de multiplicar del 3, del 1 al 10
# print()
# print("-"*5, "Tabla de multiplicar del 3", "-"*5)
# x = 1
# while x<=10:
#     print(f" 3 x {x:<2} = {3*x}")
#     x = x + 1
# print("-"*5, "FIN", "-"*5)
# print()


# Una tabla de multiplicar preguntando al usuario de que numero quiere la tabla
print()
# print("-"*5, "Tabla de multiplicar" , "-"*5)
print("Tabla de multiplicar".center(46,"-"))
t = int(input("Ingrese el numero de tabla que desea saber: "))
x = 1
while x<=10:
    print(f" {t} x {x:<2} = {t*x}")
    x = x + 1
# print("-"*5, "FIN", "-"*5)
print("FIN".center(46,"-"))
print()