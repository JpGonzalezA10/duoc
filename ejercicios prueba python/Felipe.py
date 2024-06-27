sumadig=0
while True:
    try:
        print("ingresa una de las siguientes opciones")
        print("-------------------------------------------------------------")
        print("1._ deseas ingresar un numero (+) (-) o neuto")
        print("2._ desdeas ingresar un numero par o impar")
        print("3._imprimir la suma de los pares ingresados hasta el momento")
        print("4._ deseas salir")
        print("-------------------------------------------------------------")
        
        op=int(input("ingrese una opcion   "))
        if op<=4 and op>0:
            if op==1:
                num=int(input("ingrese numero  "))
                if num==0:
                    print(f"el numero {num} es neutro")
                elif num>0:
                    print(f"el numero {num} es positivo")
                else:
                    print(f"el numero {num} es negativo")
            elif op==2:
                num=int(input("ingrese numero    "))
                if num%2==0:
                    sumadig=num+sumadig
                    print(f"el numero {num} es par {sumadig}")
                else:
                    print(f"el numero {num} es impar")
            elif op==3:
                print(f"la suma de los pares es {sumadig}")
            elif op==4:
                print("elegiste SALIR - ADIOS")
                break
        else:
              print("las opciones son elegir entre 1 a 4")  
    except ValueError:   
        print("ingresa solo numeros")