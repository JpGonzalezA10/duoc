sumpares=0

while True:
    try:
        print("1- Verificar (+) (-) o NEUTRO")
        print("2- Verificar PAR/IMPAR")
        print("3- Suma de los PARES")
        print("4- SALIR")
        op = int(input("Ingrese una opción: "))

        if op == 1:
            num = int(input("Ingrese número: "))
            if num == 0:
                print(f"{num} ingresado NEUTRO")
            else:
                if num > 0:
                    print(f"{num} ingresado POSITIVO")
                else:
                    print(f"{num} ingresado NEGATIVO")
        elif op == 2:
            num = int(input("Ingrese número: "))
            if num%2==0:
                print(f"El {num} es PAR")
                sumpares=sumpares+num
            else:
                print(f"El {num} es IMPAR")
        elif op == 3:
            print(f"La suma de los PARES es: {sumpares}")
        elif op == 4:
            print("Adios... Usted salió del programa!")
            break
        else:
            print("Opción inválida!")
    except ValueError:
        print("Debe ingresar un número entero")

        