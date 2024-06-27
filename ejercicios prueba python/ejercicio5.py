aa=int(input("ingrese el año actual "))
aq=int(input("ingrese un año cualquiera "))
if aa>aq:
    res=aa-aq
    if res==1:
      print("faltan ",res," año para llegar al año actual")
    else:
      print("faltan ",res," años para llegar al año actual")  
elif aa<aq:
    res=aq-aa
    if res==1:   
        print("faltan ",res," año para llegar al año ingresado desde el actual")
    else:
        print("faltan ",res," año para llegar al año ingresado desde el actual") 