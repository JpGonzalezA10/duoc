archivo = open ("documento1.txt","r")
x=archivo.read()
print(f"el contenido de el archivo es: {x}")
archivo.close()