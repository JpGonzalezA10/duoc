dis=float(input("ingrese distancia en centimetros "))
km=dis/100000
mt=dis/100
if km>1:
     print(f"la distancia en km es {km}, en metros es {mt} y en centimetros es {dis}")
elif mt>1:
     print(f"la distancia en metros es {mt} y en centimetros es {dis}")
else:       
    print(f"la distancia en {dis}")