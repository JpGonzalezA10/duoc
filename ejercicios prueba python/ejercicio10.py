print("seleccion la ocpcion que desea")
print("T o t para calcular el area de un triangulo")
print("C o c para calcular el area de un circulo")
sel=input("ingrese su seleccion ")
if sel=="T" or sel=="t":
    b=int(input("ingrese la base del triangulo "))
    a=int(input("ingrese la altura del triangulo "))
    area=(b*a)/2
    print(f"el area del triangulo es {area}")
elif sel=="C" or sel=="c":
    r=float(input("ingrese el radio del ciruclo ")) 
    area=3.141592*(r*r) 
    print(f"el area del circulo es {area}")   
else:
    print("No eligio una opcion valida")       