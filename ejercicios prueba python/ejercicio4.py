aa=int(input("ingrese el año actual "))
aq=int(input("ingrese un año cualquiera "))
if aa>aq:
    res=aa-aq
    print("faltan ",res," años para llegar al año actual")
elif aa<aq:
    res=aq-aa    
    print("faltan ",res," años para llegar al año ingresado desde el actual")