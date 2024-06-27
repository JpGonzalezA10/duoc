def numero_primo(num):
    con=0
    imp=0
    while num>=con:
     con=con+1
     if num%con==0:
         imp=imp+1
    if imp==2:
       print(f"es primo el numero {num}")  
    if imp!= 2:
        print(f"el  {num} no es primo")    
         

def numero_par(num):
    sum=0
    if num%2==0:
        sum=sum+num
        print(f"el numero {num} es par")
    else:
        print(f"El numero {num} es impar")    
        
        
        
def suma_pares(num):
    sum=sum+num