##solicitar al usuario una frase. añadir cada palabra de esa frase a un documento de texto
with open("leer1.txt","a") as arc:
 palabra=input("ingrese una frase: ")
 x= palabra.split(" ")
 arc.write(palabra)
 arc.write("\n")
 print(x)