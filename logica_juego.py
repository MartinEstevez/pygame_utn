import json
import random 



def leer_json(ruta_archivo:str)->list:
    """
    esta funcion lee el archivo json.
    """
    
    with open(ruta_archivo, "r") as archivo:
        lista_preguntas = json.load(archivo)
    return lista_preguntas

def pregunta_al_azar(lista:list,cant_preguntas:int)-> list:
    lista_indice = []
    if len(lista) > 0: 
        contador = 0
        while True:
            indice_aleatorio = random.randint(0, len(lista)-1)
            if lista_indice.count(indice_aleatorio) == 0:
                lista_indice.append(indice_aleatorio)
                contador += 1
                if contador == cant_preguntas:
                    break
    return lista_indice

def mostrar_preguntas(lista_preguntas: list[dict], lista_indice: list[int], clave: str):
    for i in range(len(lista_indice)):
        pregunta = lista_preguntas[lista_indice[i]]  
        print(f"{i+1}. {pregunta[clave]}")  
        mostrar_respuestas(pregunta)  
        print()


def mostrar_respuestas(diccionario: dict, clave: str = "r_") -> None:
    """
    Muestra las respuestas r_1 a r_4 de un diccionario dado.
    """
    for i in range(1, 5):
        print(diccionario[f"{clave}{i}"], end=" / ")
    print()  
    



ruta = "datos.json"
lista_preguntas = leer_json(ruta)
lista = pregunta_al_azar(lista_preguntas, 10)
mostrar_preguntas(lista_preguntas, lista, "pregunta")

