diccionario = {}

def ingresar_usuario():
    nombre = input("Debe ingresar nombre de usuario: ")
    if nombre in diccionario:
        print("Usuario ya existe. Intente otro")
        return
    
    sexo = input("Ingrese su sexo: ")
    if sexo != "M" and sexo != "F":
        print("Debe ingresar M o F solamente. Intente de nuevo.")
        return
    contraseña = input.str.int("Ingrese contraseña (mínimo 8 caracteres): ")
    if contraseña< 8 or contraseña == "":
        print("Contraseña no valida. Intente otra")
        return
    
    diccionario[nombre] = {"sexo": sexo,"contraseña":contraseña}
    print("Print ingresado correctamente")

def buscar_usuario():
    nombre = input("ingrese el nombre de usuario:")
    if nombre in diccionario:
        datos = diccionario[nombre]
        print(f"Sexo {datos["sexo"]}, contraseña: {datos["contraseña"]}")
    else:
        print("El usuario no se encuentra.")
    
def eliminar_usuario():
    nombre = input("Ingrese usuario a buscar: ")
    if nombre in diccionario:
        diccionario.pop[nombre]
        print("Usuario eliminado con exito!")
    else:
        print("No se pudo encontrar el usuario")

while True:   
    try:
        print("1.- Ingresar usuario.")
        print("2.- Buscar usuario.")
        print("3.- Eliminar usuario.")
        print("4.- Salir.")
        opcion = int(input("Escoja su opción: "))
        match opcion:
            case 1:
                ingresar_usuario()
            case 2:
                buscar_usuario()
            case 3:
                eliminar_usuario()
            case 4:
                print("Ha salido con exito!")
                break
            case _:
                print("Debe ingresar una de las opciones mostradas")
    except ValueError as error:
         print(f"Error: {error}")