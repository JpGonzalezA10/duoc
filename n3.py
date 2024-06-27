nombre=str(input("ingrese nombre "))
canthorasnormales=float(input(f"ingrese horas normales trabajadas "))
canthorasextras=float(input("ingrese horas extras trabajadas "))
valorhoranormal=float(input("ingrese valor hora normal "))
sueldobase=canthorasnormales*valorhoranormal+(canthorasextras*(valorhoranormal*1.65))
bonodeproduccion=sueldobase*0.15
bonoincentivo=sueldobase*0.09
totalimponible=sueldobase+bonodeproduccion+bonoincentivo
descuentoafp=totalimponible*0.126
descuentoisapre=totalimponible*0.072
sueldoliquido=totalimponible-descuentoafp-descuentoisapre
print("bono produccion es ",round(bonodeproduccion,2))
print("bono incentivo es ",round (bonoincentivo,2))
print("imponible es ",round(totalimponible,2))
print("descuento afp es ",round (descuentoafp,2))
print("descuento isapre es ",round(descuentoisapre,2))
print("sueldo liquido es ",round(sueldoliquido,2))
