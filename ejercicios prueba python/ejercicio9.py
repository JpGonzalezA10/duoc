
ai=int(input("ingrese un año "))
if ai%4==0 and ai%100!=0:
    print("el año si es bisiesto")
elif ai%4==0 and ai%100==0 and ai%400==0:
     print("el año si es bisiesto")  
else:
    print("el año no es bisiesto")    
