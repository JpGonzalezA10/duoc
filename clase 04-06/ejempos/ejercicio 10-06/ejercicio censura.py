pal_sucias = ["muerte", "droga", "sexo"]

cap = input("Escribe el capítulo del libro: ")

for pal in pal_sucias:
    cap = cap.replace(pal, '*' * len(pal))

with open('capitulo.txt', 'w') as censu:
    censu.write(cap)

print("Capítulo censurado y guardado en 'capitulo.txt'.")

print(cap)