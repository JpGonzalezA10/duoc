with open("leer2.txt","a") as arc:
 palabra=input("ingrese un correo: ")
 x= palabra.split("@")
 arc.write(x[0])
 arc.write("\n")
 print(x[0])