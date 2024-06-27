arc=open("documento1.txt","a")
arc.write("\n")
for i in range(5):
    palabra=input("ingrese una palabra para agregar: ")
    arc.write(palabra)
    arc.write("\n")

arc.close()    