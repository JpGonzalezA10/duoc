import random
import math

peliculas = {}

def agregar_pelicula():
    try:
        codigo = random.randint(1000, 9999)
        nombre = input("Ingrese el nombre de la película: ")
        anio = int(input("Ingrese el año de la película: "))
        categoria = input("Ingrese la categoría de la película: ")
        actores = input("Ingrese los actores de la película (separados por comas): ").split(',')
        director = input("Ingrese el director de la película: ")
        
        peliculas[codigo] = {
            'nombre': nombre,
            'anio': anio,
            'categoria': categoria,
            'actores': [actor.strip() for actor in actores],
            'director': director
        }
        print(f"Película agregada exitosamente con el código {codigo}!")
    except ValueError:
        print("Error: Ingreso de datos inválidos. Asegúrese de ingresar el año como un número.")

def listar_peliculas():
    if peliculas:
        for codigo, datos in peliculas.items():
            print(f"Código: {codigo}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Año: {datos['anio']}")
            print(f"Categoría: {datos['categoria']}")
            print(f"Actores: {', '.join(datos['actores'])}")
            print(f"Director: {datos['director']}\n")
    else:
        print("No hay películas registradas.")

def buscar_pelicula():
    try:
        codigo_buscar = int(input("Ingrese el código de la película a buscar: "))
        if codigo_buscar in peliculas:
            datos = peliculas[codigo_buscar]
            print(f"Nombre: {datos['nombre']}")
            print(f"Año: {datos['anio']}")
            print(f"Categoría: {datos['categoria']}")
            print(f"Actores: {', '.join(datos['actores'])}")
            print(f"Director: {datos['director']}\n")
        else:
            print("No se encontró ninguna película con ese código.")
    except ValueError:
        print("Error: Ingrese un código válido.")

def guardar_peliculas():
    try:
        with open("peliculas.txt", "w") as archivo:
            for codigo, datos in peliculas.items():
                archivo.write(f"Código: {codigo}\n")
                archivo.write(f"Nombre: {datos['nombre']}\n")
                archivo.write(f"Año: {datos['anio']}\n")
                archivo.write(f"Categoría: {datos['categoria']}\n")
                archivo.write(f"Actores: {', '.join(datos['actores'])}\n")
                archivo.write(f"Director: {datos['director']}\n\n")
        print("Películas guardadas en peliculas.txt")
    except Exception as e:
        print(f"Error al guardar las películas: {e}")

def menu():
    while True:
        print("Menú de Usuario")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Buscar Película")
        print("4. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                agregar_pelicula()
            elif opcion == 2:
                listar_peliculas()
            elif opcion == 3:
                buscar_pelicula()
            elif opcion == 4:
                guardar_peliculas()
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Error: Ingrese un número válido.")

if __name__ == "__main__":
    menu()