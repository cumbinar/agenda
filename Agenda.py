import json


#LIMPIAR PANTALLA
def crear_linea():
    print("="*65)


#VALIDAR VALOR NUMÉRICO
# Realizar la pregunta requerida
# Devolver número si el dato es numérico
# o volver a preguntar si el dato no es numérico
def preguntar_numero(pregunta):
    while (True):
        dato = input(pregunta)
        if (dato.isnumeric()):
            return int(dato)
        else:
            print("*** ERROR. Por favor ingrese un dato numérico. ***")


#CREAR UN CONTACTO
# Preguntar por nombres, apellidos, edad...
# Hacer un ciclo para preguntar por los números de teléfono
# Retornar una estrcutura de tipo DICC
def crear_contacto():
    contacto = {}
    contacto["documento"] = preguntar_numero("Ingrese número de documento: ")
    contacto["nombres"] = input("Ingrese nombres: ")
    contacto["apellidos"] = input("Ingrese apellidos: ")
    while ( True ):
        genero = input("Ingrese género (M/F): ").upper()
        if (genero != "M" and genero != "F"):
            print("*** ERROR. Por favor ingrese género válido. ***")
        else:
            contacto["genero"] = genero
            break
    contacto["edad"] = preguntar_numero("Ingrese edad: ")
    contacto["lugarnacimiento"] = input("Ingrese lugar de nacimiento: ")
    contacto["listatelefonos"] = []
    while ( True ):
        tel = preguntar_numero("Ingrese número de teléfono o 0 para salir: ")
        if (tel == 0):
            break
        else:
            contacto["listatelefonos"].append(tel)
    return contacto


#INGRESAR UN CONTACTO
# Crear un contacto
# Añadirlo a una lista
def ingresar_contacto(lista_contactos):
    print("--------------------- CREANDO NUEVO CONTACTO ---------------------")
    contacto = crear_contacto()
    lista_contactos.append(contacto)
    print("\nContacto creado. Presione Enter para continuar")
    input()
    return lista_contactos


#MOSTRAR TODOS LOS CONTACTOS
# Presentar un número [posición], nombre y apellido
def mostrar_contactos(lista_contactos):
    print("--------------------- LISTA DE CONTACTOS -------------------------")
    print("POS NOMBRES                        APELLIDOS")
    print("-"*3+" "+"-"*30+" "+"-"*30)
    for pos, contacto in enumerate(lista_contactos):
        print(str(pos).rjust(3)+" "+contacto["nombres"].ljust(30)+" "+contacto["apellidos"].ljust(30))
    print("\n"+str(len(lista_contactos))+" contactos encontrados.\n")

    
#MOSTRAR UN CONTACTO
# Preguntar por la posición
# Mostrar todos los datos del contacto
# Si no hay contactos inicialmente, sacarlo inmediatamente de la función
def mostrar_contacto(lista_contactos):
    mostrar_contactos(lista_contactos)
    if len(lista_contactos) == 0:
        return
    pos = preguntar_numero("Ingrese posición de contacto a mostrar: ")
    if (pos < 0 or pos >= len(lista_contactos)):
        print("No se puede mostrar contacto")
    else:
        print("------------------- INFORMACIÓN DE CONTACTO -------------------")
        print("Documento:        "+str(lista_contactos[pos]["documento"]))
        print("Nombres:          "+lista_contactos[pos]["nombres"])
        print("Apellidos:        "+lista_contactos[pos]["apellidos"])
        print("Edad:             "+str(lista_contactos[pos]["edad"]))
        print("Género:           "+lista_contactos[pos]["genero"])
        print("Lugar nacimiento: "+lista_contactos[pos]["lugarnacimiento"])
        for i in lista_contactos[pos]["listatelefonos"]:
            print("Telefono:          "+str(i))
        print("\nPresione Enter para continuar")
        input()        

    
#EDITAR UN CONTACTO
# Preguntar por la posición
# Preguntar por nombres, apellidos, edad...
# Hacer un ciclo para preguntar por los números de teléfono
def editar_contacto(lista_contactos):
    mostrar_contactos(lista_contactos)
    pos = preguntar_numero("Ingrese posición de contacto a editar: ")
    if (pos < 0 or pos >= len(lista_contactos)):
        print("*** ERROR. Posición no válida. ***")
    else:
        print("--------------------- EDITANDO CONTACTO ---------------------")
        contacto = crear_contacto()
        lista_contactos[pos] = contacto
        print("\nContacto editado. Presione Enter para continuar")
        input()
    return lista_contactos
        

#BUSCAR UN CONTACTO
# Preguntar la subcadena a buscar en los nombres
# Si encuentra uno, imprimir con la posición
def buscar_contacto(lista_contactos):
    print("------------ BUSCANDO CONTACTO POR NOMBRE O APELLIDO ------------")
    subcadena = input("Ingrese parte del nombre o apellido a buscar: ")
    subcadena = subcadena.lower()
    cant_encontrados = 0
    print("\n------------ CONTACTOS ENCONTRADOS CON *"+subcadena.upper()+"* -------------")
    print("POS NOMBRES                        APELLIDOS")
    for pos, contacto in enumerate(lista_contactos):
        if (contacto["nombres"].lower().count(subcadena)>0 or contacto["apellidos"].lower().count(subcadena)>0):
            print(str(pos).rjust(3)+" "+contacto["nombres"].ljust(30)+" "+contacto["apellidos"].ljust(30))
            cant_encontrados+=1
    print("\n"+str(cant_encontrados)+" contactos encontrados. Presione Enter para continuar")
    input()

    
#BORRAR UN CONTACTO
# Preguntar por la posición
# Borrar
def borrar_contacto(lista_contactos):
    mostrar_contactos(lista_contactos)
    pos = int(input("Ingrese posición de contacto a borrar: "))
    if (pos < 0 or pos >= len(lista_contactos)):
        print("*** ERROR. Posición no válida. ***")
    else:
        contacto = lista_contactos.pop(pos)
        print("\nContacto "+contacto["nombres"]+" "+contacto["apellidos"]+" borrado. Presione Enter para continuar")
        input()
    return lista_contactos


#GUARDAR ARCHIVO
# Guarda la información en el archivo
def guardar_contactos(lista_contactos):
    with open('listacontactos.json', 'w') as f:
        json.dump(lista_contactos, f, indent=4)
    print("\nArchivo actualizado. Presione Enter para continuar")
    input()
    

#CARGAR ARCHIVO
# Carga la información del archivo directamente como estructura de datos Python
# Si no encuentra archivo, crea la estructura en blanco
def cargar_archivo():
    try:
        with open('listacontactos.json', 'r') as f:
            estructura = json.load(f)
    except:
        print("\nArchivo no encontrado. Se inicia con información en blanco.")
        estructura = []
    return estructura


#PRESENTAR MENU
# Presenta menú con opciones de funcionalidad
# Repite hasta que seleccione opción de salida
# Previene si el archivo requiere guardarse antes de salir si hay datos cambiados
def presentar_menu():
    listaregistros = cargar_archivo()
    datos_cambiados = False
    while (True):
        crear_linea()
        print("MENU DE CONTACTOS")
        print("1. Ingresar contacto")
        print("2. Mostrar lista de contactos")
        print("3. Mostrar un contacto")
        print("4. Editar un contacto")
        print("5. Buscar un contacto")
        print("6. Borrar un contacto")
        print("7. Guardar contactos en archivo")
        print("9. Salir")
        opc = preguntar_numero("Seleccione opción: ")
        crear_linea()
        match (opc):
            case 1:
                listaregistros = ingresar_contacto(listaregistros)
                datos_cambiados = True
            case 2:
                mostrar_contactos(listaregistros)
                print("\nPresione Enter para continuar")
                input()
            case 3:
                mostrar_contacto(listaregistros)
            case 4:
                listaregistros = editar_contacto(listaregistros)
                datos_cambiados = True
            case 5:
                buscar_contacto(listaregistros)
            case 6:
                listaregistros = borrar_contacto(listaregistros)
                datos_cambiados = True
            case 7:
                guardar_contactos(listaregistros)
                datos_cambiados = False
            case 9:
                if (datos_cambiados == True):
                    guardar = input("Desea guardar cambios antes de salir S/N?").upper()
                    if (guardar=="S"):
                        guardar_contactos(listaregistros)
                print("Programa finalizado")
                break
            case _:
                print("*** ERROR. Opción no válida. ***")

presentar_menu()
