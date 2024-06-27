def saludar():
    print("hola")
    
def saludar_completo(x,y):
    print(f"Bienvenido {x} {y}")
nom=input("ingrese su nombre") 
ape=input("ingrese el apellido")   
saludar() 
saludar_completo(nom, ape)
##saludar_completo("juan","perez")   

def cal_fac(num):
    cont=1
    fac=1
    while cont<=num:
        fac=fac*cont
        cont=cont+1
    print(f"el factorial de {num} es: {fac}")    
    
x=int(input("ingrese un numero para calcular"))    
cal_fac(x)
    