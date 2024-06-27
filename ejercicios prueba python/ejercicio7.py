num1=int(input("ingrese un numero entero "))
num2=int(input("ingrese un segundo numero entero "))
if num1>0 and num2>0:
    if num1%num2==0:
       print("el numero ",num1, "es multiplo de ",num2)
else:
    print("debe ingresar numeros mayores a 0 ")       