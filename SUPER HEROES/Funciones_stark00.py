


# STARK 00

def mostrar_menu_opciones():
    print("""
    |--------------------------------------|
    |          MENU DE OPCIONES            |
    |--------------------------------------|
    | 1.Nombre de cada SuperHeroe          |
    | 2.Cada SuperHeroe con su altura      |
    | 3.SuperHeroe mas alto                |
    | 4.SuperHeroe mas bajo                |
    | 5.Altura promedio de los SuperHeroes |
    | 6.Nombre SuperHeroe alto y bajo      |
    | 7.SuperHeroe mas y menos pesado      |
    | 8.Submenu Stark 01                   |
    | 9.Submenu Stark 02                   |
    | 10.Salir                             |
    |--------------------------------------|
    """)
    opcion = (input("Ingrese Opcion: "))
    return opcion


# # B
def nombre_personas(lista:list,key:str):
    for personaje in lista:
        print(personaje[key])


# # C
def nombre_altura(lista):
    for personaje in lista:
        print(f"{personaje['nombre']} y su altura es {personaje['altura']}")



# # D

def maximo(lista,item):
    bandera = True
    mas_alto= None

    for personaje in lista:
        if bandera or float(personaje[item]) > mas_alto:
            bandera = False
            mas_alto = float(personaje[item])
            

    for personaje in lista:
        if float(personaje[item]) == mas_alto:
            nombre = personaje["nombre"]
    
    return nombre


# # E

def minimo(lista,item):
    bandera = True
    mas_bajo= None

    for personaje in lista:
        if bandera or float(personaje[item]) < mas_bajo:
            bandera = False
            mas_bajo = float(personaje[item])
            


    for personaje in lista:
        if float(personaje[item]) == mas_bajo:
            nombre = personaje["nombre"]

    return nombre
    



# F

def promedio_alturas(lista):
    suma_alturas = 0

    for personaje in lista:
        suma_alturas = suma_alturas + float(personaje["altura"])

    promedio_altura = suma_alturas / len(lista)

    print(f"El promedio de altura de los super heroes es: {promedio_altura:.2f}")








    






def salir():
    respuesta = input("¿Desea salir? (S/N) ")
    if respuesta.lower() == "s":
        return True
    else:
        return False  




















  