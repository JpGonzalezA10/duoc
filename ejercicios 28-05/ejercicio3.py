user=[]
pas=[]
res=1
clave=0
while res != 4:
   if res >0 and res <5:
        print("Seleccione una opcion")
        print("1. Inicio sesión.")
        print("2. Registrar usuario")
        print("3. Eliminar usuario.")
        print("4. Salir.")
        res=int(input("ingrese su opcion del 1 al 4 "))
        if res==1:
            nus = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            if nus in user:
                indice = user.index(nus)
                if pas[indice] == contraseña:
                    print("Inicio de sesión exitoso.")
                else:
                    print("Contraseña incorrecta.")
            else:
                print("Usuario no encontrado.")
                
                
        elif res==2:
            nus = input("Ingrese un nombre de usuario: ")
            if nus not in user:
                contraseña = input("Ingrese una contraseña: ")
                user.append(nus)
                pas.append(contraseña)
                print("Usuario registrado correctamente.")
            else:
                print("usuario ya ingresado")   
                
                 
        elif res==3:
            nus = input("Ingrese el nombre de usuario que desea eliminar: ")
            clave = input("Ingrese su contraseña para confirmar la eliminación: ")

            if nus in user:
                indice = user.index(nus)
                if pas[indice] == clave:
                    del user[indice]
                    del pas[indice]
                    print("Usuario eliminado correctamente.")
                else:
                    print("Contraseña incorrecta. No se pudo eliminar el usuario.")
            else:
                print("Usuario no encontrado.")    
   else:
        print("debe ingresar de 1 a 4")
        res=int(input("ingrese su opcion del 1 al 4 "))