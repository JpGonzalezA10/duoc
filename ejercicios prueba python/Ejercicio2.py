num1=int(input("ingrese un numero entero "))
num2=int(input("ingrese un segundo numero entero "))

if num1>0 and num2>0:
    res=num1/num2
    if num1%num2==0:
      print(f"el resultado de la division es {res} y la division es exacta") 
    
    else:
     print(f"el resultadode la divisio es {res}")
else:
    print("no se puede dividir por 0 ")    