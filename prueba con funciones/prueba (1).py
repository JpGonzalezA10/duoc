from prueba import numero_primo,numero_par
con=0
imp=0
sum=0
while True:
    try:
        print("---------------------------------")
        print("menu para seleccionar")
        print("debe seleccionar una opcion del 1 a 4 ")
        print("1 verificar si su numero es primo")
        print("2 verificar si es par o impar")
        print("3 calcular la suma e los numeros pares ingresados hasta el momento")
        print("4 finalizar programa")
        op=int(input("ingrese su opcion "))
        if op>0 and op<5:
            if op==1:
                num=int(input("ingrese el numero a validar "))
                if num>0:
                    numero_primo(num)
                else:
                        print("debe ingresar un numero mayor a 0") 
            elif op==2:
                num=int(input("ingrese el numero a validar "))
                numero_par(num)  
            elif op==3:
                print(f"la suma de los pares hasta el momento es {sum}")
            elif op==4:
                print("gracias por utilizar el programa") 
                break       
        else:
            print("debe ingresar un numero entre 1 y 4")        
    except ValueError:
        print("debe ingresar solo numeros")
   ## except ZeroDivisionError:
     ##   print("no se puede dividir por 0 ")    
    ##elif op==2:

## python C:\\Users\\PCXX\\desktop\\prueba.py