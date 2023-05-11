

# STARK 01

def sub_menu_uno():
    print("""
    |---------------------------------------------------------------------|
    |                        SUBMENU DE OPCIONES                          |   
    |---------------------------------------------------------------------|
    | 1.Nombre de cada SuperHeroe de genero M                             |
    | 2.Nombre de cada SuperHeroe de genero F                             |
    | 3.SuperHeroe mas ALTO de genero M                                   |
    | 4.SuperHeroe mas ALTO de genero F                                   |
    | 5.SuperHeroe mas BAJO de genero M                                   |
    | 6.SuperHeroe mas BAJO de genero F                                   |
    | 7.Altura promedio de los SuperHeroes de genero M                    |
    | 8.Altura promedio de los SuperHeroes de genero F                    |
    | 9.Informar el nombre del SuperHeroe asociado a los demas puntos 3-6 |
    | 10.Cuántos SuperHeroes tienen cada tipo de color de ojos            |
    | 11.Cuántos SuperHeroes tienen cada tipo de color de pelo            |
    | 12.Determinar cuántos SuperHeroes tienen cada tipo de inteligencia  |
    | 13.Listar todos los SuperHeroes agrupados por color de ojos         |
    | 14.Listar todos los SuperHeroes agrupados por color de pelo         |
    | 15.Listar todos los SuperHeroes agrupados por tipo de inteligencia  |
    | 16.Volver al menu anterior                                          |
    |---------------------------------------------------------------------|
    """)

    opcion = input("Ingrese Opcion: ")
    return opcion


# 1 y 2
def nombre_genero(lista:list,genero:str,key:str) -> None:
    for personaje in lista:
        if personaje["genero"] == genero:
            print(personaje[key])




# 3 y 4

def super_heroe_mas_alto(lista,genero):
    
    mas_alto = None
    bandera = True

    mas_altos = []

    genero = genero.upper()

    for personaje in lista:
        if (personaje["genero"] == genero):
            if(bandera or float(personaje["altura"]) > mas_alto):

                bandera = False
                mas_alto = float(personaje["altura"])
                

    for personaje in lista:
        if personaje["genero"] == genero:
            if float(personaje["altura"]) == mas_alto:
                mas_altos.append(personaje)
                
                
                

    return mas_altos
            


# 5 y 6

def super_heroe_mas_bajo(lista,genero):
    
    mas_bajo = None
    bandera = True

    mas_bajos= []

    genero = genero.upper()

    for personaje in lista:
        if (personaje["genero"] == genero):
            if(bandera or float(personaje["altura"]) < mas_bajo):

                bandera = False
                mas_bajo = float(personaje["altura"])
                


    for personaje in lista:
        if personaje["genero"] == genero:
            if float(personaje["altura"]) == mas_bajo:
                mas_bajos.append(personaje)
    



    return mas_bajos



# 7 y 8


def promedio_altura(lista,genero):

    suma = 0

    genero = genero.upper()

    for personaje in lista:
        if personaje["genero"] == genero:
            suma = suma + float(personaje["altura"])

    promedio = suma / len(lista)
    
    print(f"El promedio de altura es: {promedio}")



# 9

def informe_nombres(lista):
    
    for i in super_heroe_mas_alto(lista):
        print(i["nombre"])
    for i in super_heroe_mas_bajo(lista):
        print(i["nombre"])


    









def esta_en_lista(lista,item):
    esta = False

    for elemento in lista:
        if elemento == item:
            esta = True
            break
    return esta


def quitar_repetidos(lista:list) -> list:
    lista_sin_repe = []

    for item in lista:
        if esta_en_lista(lista_sin_repe,item) == False:
            lista_sin_repe.append(item)
    
    return lista_sin_repe


# 10 11 y 12

def mostrar_contador(lista2,lista,item):
    for elemento in lista2:
        contador = 0
        print("\n|------------------------------------------------------------|")
        print(f"| {item}:  {elemento}")
        print("|------------------------------------------------------------|")
        for heroe in lista:
            if heroe[item] == elemento:
                contador += 1
        print(contador)
        print("|------------------------------------------------------------|")




def cargar_lista_y_contar(lista: list, item: str) -> None:

    lista2 = []
    for heroe in lista:

        if item == "inteligencia" and heroe[item] == "":
            heroe["inteligencia"] = heroe["inteligencia"].replace("","No Tiene")

        if item == "color_pelo" and heroe[item] == "":
            heroe["color_pelo"] = heroe["color_pelo"].replace("","No Hair")

        heroe[item] = heroe[item].lower()

        
        lista2.append(heroe[item])

    lista2 = quitar_repetidos(lista2)

    mostrar_contador(lista2,lista,item)






# 13 14 y 15




def mostrar_elemento(lista_origen,key,lista):

    for elemento in lista:
        print("\n|------------------------------------------------------------|")
        print(f"| {key}:  {elemento}")
        print("|------------------------------------------------------------|")
        for heroe in lista_origen:
            if heroe[key] == elemento:
                    print(f"| {heroe['nombre']:30s}                             |")
        print("|------------------------------------------------------------|")





def mostrar_por_tipo(lista,item):
    
    lista_por_tipo = []



    for heroe in lista:

        if item == "inteligencia" and heroe[item] == "":
            heroe[item] = heroe[item].replace("","No Tiene")

        if item == "color_pelo" and heroe[item] == "":
            heroe[item] = heroe[item].replace("","No Hair")

        heroe[item] = heroe[item].lower()


        
        lista_por_tipo.append(heroe[item])

    lista_por_tipo = quitar_repetidos(lista_por_tipo)

    
    print("|------------------------------------------------------------|")
    print(f"           LISTA DE PERSONAJES POR {item:10s}                ")
    print("|------------------------------------------------------------|")
    
    mostrar_elemento(lista,item,lista_por_tipo)




