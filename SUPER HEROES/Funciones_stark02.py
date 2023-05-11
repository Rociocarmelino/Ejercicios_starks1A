
from data_stark import *
import os



# 0

def stark_normalizar_datos(lista:list):
    

    if len(lista) == 0:
        print("Error.Lista de heroes vacia")

    datos_modificados = False

    for heroe in lista:
        for clave,valor in heroe.items():
                if clave == "fuerza":
                    if str(valor).isdigit():
                        heroe[clave] = int(valor)
                        datos_modificados = True
                elif clave == "altura" or clave == "peso":
                    heroe[clave] = float(valor)
                    datos_modificados = True
                    

    if datos_modificados:
        print("Datos normalizados")

stark_normalizar_datos(lista_personajes)






# 1.1

def obtener_nombre(heroe:dict) -> str:

    nombre = heroe.get("nombre")

    return f"Nombre:  {nombre}"
    




# 1.2

def imprimir_dato(cadena:str) -> None:
    print(cadena)


# 1.3

def stark_imprimir_nombres_heroes(lista:list):  # esta funcion usarla en el punto 1 stark 00

    if not lista:
        return -1
    
    for heroe in lista:
        nombre = obtener_nombre(heroe)
        imprimir_dato(nombre)
    



# 2

def obtener_nombre_y_dato(heroe:dict,key:str):

    nombre = heroe.get("nombre")

    valor_de_key = heroe.get(key)

    return f"nombre: {nombre} | {key}: {valor_de_key}"


# 3

def stark_imprimir_nombres_alturas(lista:list):

    if len(lista) == 0:
        return -1

    for heroe in lista:
        print(obtener_nombre_y_dato(heroe,"altura"))


# 4.1

def calcular_max(lista:list,key:str) -> str:

    bandera = True
    maximo = None

    for heroe in lista:
        if bandera or heroe[key] > maximo:
            maximo = heroe[key]
            bandera = False


    for personaje in lista:
        if personaje[key] == maximo:
            heroe_maximo = personaje
            
    return heroe_maximo
    


# 4.2

def calcular_min(lista:list,key:str) -> str:

    bandera = True
    minimo = None

    for heroe in lista:
        if bandera or heroe[key] < minimo:
            minimo = heroe[key]
            bandera = False


    for personaje in lista:
        if personaje[key] == minimo:
            heroe_minimo = personaje
            
    return heroe_minimo


# 4.3

def calcular_max_min_dato(lista:list,calculo:str,key:str) -> str:

    if calculo == "maximo":
        nombre = calcular_max(lista,key)
    elif calculo == "minimo":
        nombre = calcular_min(lista,key)

    return nombre


# 4.4

def stark_calcular_imprimir_heroe(lista:list,calculo:str,key:str) -> str:

    if len(lista) == 0:
        return -1
    
    if calculo == "maximo":
        heroe = calcular_max_min_dato(lista,calculo,key)
        dato = obtener_nombre_y_dato(heroe,key)
        cadena = "Mayor Altura: " + dato
        imprimir_dato(cadena)
    elif calculo == "minimo":
        heroe = calcular_max_min_dato(lista,calculo,key)
        dato = obtener_nombre_y_dato(heroe,key)
        cadena = "Menor Altura: " + dato
        imprimir_dato(cadena)
    


# 5.1

def sumar_dato_heroe(lista:list,key:str) -> int:

    suma = 0

    for heroe in lista:
        if type(heroe) == dict and len(heroe) > 0:
            dato = heroe.get(key)
            suma += dato
    
    return suma


# 5.2

def dividir(dividendo:int,divisor:int) -> int:

    if divisor == 0:
        return 0    
    else:
        resultado = dividendo / divisor 
        return resultado


# 5.3

def calcular_promedio(lista:list,key:str) -> float:

    contador = len(lista)

    suma = sumar_dato_heroe(lista,key)

    promedio = dividir(suma,contador)

    return promedio


# 5.4

def stark_calcular_imprimir_promedio_altura(lista:list):

    if len(lista) > 0:
        resultado = calcular_promedio(lista,"altura")
        cadena = f"El promedio de Altura es: {resultado}"
        imprimir_dato(cadena)
    else:
        return -1
    


# 6.1

def imprimir_menu() -> str:
    menu = """
    
    |----------------------------------------------------|
    |              SUBMENU OPCIONES 02                   |
    |----------------------------------------------------|
    | 1.Normalizar datos                                 |
    | 2.Imprimir nombre de los heroes                    |
    | 3.Imprimir nombre y altura de los heroes           |
    | 4.Calcular maximo/minimo                           |
    | 10.Salir                                           |
    |----------------------------------------------------|


    """
    imprimir_dato(menu)

# 6.2

def validar_entero(numero:str) -> bool:
    
    es_digito = False

    if numero.isdigit():
        es_digito = True

    return es_digito


# 6.3

def stark_menu_principal() -> int:
    
    imprimir_menu()

    opcion = input("Ingrese opcion: ")

    if validar_entero(opcion):
        opcion = int(opcion)
        return opcion
    else:
        return -1
    

# 7

def stark_marvel_app(lista:list):

    while True:
        os.system("cls")
        match(stark_menu_principal()):
            case 1:
                print("hola")
            case _:
                print("Opcion incorrecta")
        os.system("pause")
            

































