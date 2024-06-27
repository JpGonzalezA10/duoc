#hacer un programa que permita ingresar 150 numeros 
#y que imprima la cantidad de pares ingresados y la multiplicacions de los impares
#controlar todos los errores
while True:
    try:    
        con=0
        mi=1
        cp=0
        while con<5:
            num=int(input("ingrese un numero "))
            if num>0:
                if num%2==0:
                    cp=cp+1
                elif num%2==1:
                    mi=mi*num    
                con=con+1
            else:
                print("debe ingresar numero mayor a 0")    
            
        print(f"la cantidad de pares es {cp} y la multiplicacion de los impares es {mi}")
        break        
    except ValueError:
        print("debe ingresar numeros")