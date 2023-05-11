
from Funciones_stark00 import *
from Funciones_stark01 import *
from funciones_stark02 import *
from data_stark import lista_personajes
import os



bandera = True
bandera_dos = True
maxima = None
minima = None

mas_alto_masculino = None
mas_alto_femenino = None
mas_bajo_masculino = None
mas_bajo_femenino = None
bandera_uno = False
bandera_dos = False
bandera_tres = False
bandera_cuatro = False

bandera_cinco = False

lista = []


while True:
    
    os.system("cls")
    
    match(mostrar_menu_opciones()):

        case "1":
            nombre_personas(lista_personajes,"nombre")
        case "2":
            nombre_altura(lista_personajes)
        case "3":
            maxima = maximo(lista_personajes,"altura")
            print("Se determino el personaje mas alto")
            bandera = False
        case "4":
            minima = minimo(lista_personajes,"altura")
            print("Se determino el personaje mas bajo")
            bandera_dos = False
        case "5":
            promedio_alturas(lista_personajes)
        case "6":
            if bandera == False and bandera_dos == False:
                print(f"""
                El personaje mas alto es: {maxima}
                El personaje mas bajo es: {minima}
                """)
            else:
                print("Primero debes ingresar a la opcion 3 y 4")
                
        case "7":
            mas_pesado = maximo(lista_personajes,"peso")
            menos_pesado = minimo(lista_personajes,"peso")
            print(f"""
            El personaje mas pesado es: {mas_pesado}
            El personaje menos pesado es: {menos_pesado}
            """)
        case "8":                  
            while True:

                os.system("cls")

                match(sub_menu_uno()):
                    case "1": 
                        nombre_genero(lista_personajes,"M","nombre")
                    case "2":
                        nombre_genero(lista_personajes,"F")
                    case "3":
                        print(super_heroe_mas_alto(lista_personajes,"M"))
                        bandera_uno = True
                    case "4":
                        print(super_heroe_mas_alto(lista_personajes,"F"))
                        bandera_dos = True
                    case "5":
                        print(super_heroe_mas_bajo(lista_personajes,"M"))
                        bandera_tres = True
                    case "6":
                        print(super_heroe_mas_bajo(lista_personajes,"F"))
                        bandera_cuatro = True
                    case "7":
                        promedio_altura(lista_personajes,"M")
                    case "8":
                        promedio_altura(lista_personajes,"F")  
                    case "9":
                        if bandera_uno and bandera_dos and bandera_tres and bandera_cuatro:
                            informe_nombres(lista_personajes)
                        else:
                            print("Debe ingresar a las opciones 3-6")
                    case "10":
                        cargar_lista_y_contar(lista_personajes,"color_ojos")
                    case "11":
                        cargar_lista_y_contar(lista_personajes,"color_pelo")
                    case "12":
                        cargar_lista_y_contar(lista_personajes,"inteligencia")
                    case "13":
                        mostrar_por_tipo(lista_personajes,"color_ojos")
                    case "14":
                        mostrar_por_tipo(lista_personajes,"color_pelo")
                    case "15":
                        mostrar_por_tipo(lista_personajes,"inteligencia")
                    case "16":
                        break
                    case _:
                        print("Ingreso una opcion incorrecta")

                os.system("pause")
        case "10":
            if salir():
                break
        case _:
            print("Ingreso una opcion incorrecta")
            
    os.system("pause")
        
    

