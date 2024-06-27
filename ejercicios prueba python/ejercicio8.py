num1=int(input("ingrese un numero entero "))
num2=int(input("ingrese un segundo numero entero "))
num3=int(input("ingrese un tercer numero entero "))
if num1==num2 and num1==num3 and num2==num3:
    print("los 3 numeros ingresados son iguales")
elif num1==num2 or num1==num3 or num2==num3:
    print("2 numeros son iguales")  
else:
    print("todos los numeros son distintos")       