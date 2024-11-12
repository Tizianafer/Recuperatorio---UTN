import os 
import random

def limpiar_consola():
    input("Ingrese cualquier boton para continuar")
    os.system('cls')

def pedir_numero(mensaje: str, mensaje_error: str, minimo: int, maximo:int) -> int:
    numero = int(input(mensaje))
    while numero < minimo or numero > maximo:
        numero = int(input(mensaje_error))
    return numero

def inicializar_matriz(cantidad_filas: int, cantidad_columnas:int) -> list:
    matriz = []
    for _ in range(cantidad_filas):
        fila = [0] * cantidad_columnas
        matriz += [fila]
    return matriz

def cargar_votos(listas):
    for i in range(5):
        nro_lista = pedir_numero("Ingrese el numero de lista: ", "Error, tiene que ser un numero de 3 cifras\nReintente: ", 99, 999)
        votos_mañana = pedir_numero("Ingrese votos del turno mañana: ", "Error, tiene que ser un numero de 3 cifras\nReintente: ", 0,8000)
        votos_tarde = pedir_numero("Ingrese votos del turno tarde: ", "Error, tiene que ser un numero de 3 cifras\nReintente: ", 0, 8000)
        votos_noche = pedir_numero("Ingrese votos del turno noche: ","Error, tiene que ser un numero de 3 cifras\nReintente: ", 0, 8000 )

        listas [i][0] = nro_lista
        listas [i][1] = votos_mañana
        listas [i][2] = votos_tarde
        listas [i][3] = votos_noche
    return listas

def sumar_votos(fila: list) -> int:
    return fila[1] + fila[2] + fila[3]

def calcular_porcentaje(total_votos_lista: int, total_votos_totales: int) -> float:
    if total_votos_totales == 0:
        porcentaje = 0 
    else:
        porcentaje = (total_votos_lista / total_votos_totales) * 100
    return porcentaje

def mostrar_matriz(matriz:list)->list:
    total_votos = 0
    for fila in matriz:
        total_votos += sumar_votos(fila)
    if total_votos == 0:
        print("Error: No se cargaron los votos, vuelva a intentarlo.")
    else:
        print(f"{'Lista':<8} {'Mañana':<8} {'Tarde':<8} {'Noche':<8} {'Porcentaje':<8}")
        for fila in matriz:
            nro_lista = fila[0]
            votos_mañana = fila[1]
            votos_tarde = fila[2]
            votos_noche = fila[3]
            
            total_lista = sumar_votos(fila)
            porcentaje = 0
            if total_votos > 0:
                porcentaje = calcular_porcentaje(total_lista,total_votos)
            
            print(f"{nro_lista:<8} {votos_mañana:<8} {votos_tarde:<8} {votos_noche:<8} {porcentaje:<8.2f}%")
    return matriz

def ordenar_votos_mañana(matriz: list) -> list:
    for i in range(len(matriz)):
        for j in range(len(matriz) - 1):
            if matriz[j][1] < matriz[j + 1][1]:  
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]  
    return matriz 
    
def mostrar_porcentaje_menor(matriz: list) -> list:
    total_votos_totales = 0
    retorno = True
    for fila in matriz:
        total_votos_totales += sumar_votos(fila)

    if total_votos_totales == 0:
        print("Error: No se cargaron los votos. Imposible calcular porcentajes.")
        retorno = False
    else:
        print("\nListas con menos del 5% de los votos:")
        for fila in matriz:
            total_votos = sumar_votos(fila)
            porcentaje_voto = calcular_porcentaje(total_votos,total_votos_totales)
            if porcentaje_voto < 5:
                print(f"Lista N° {fila[0]}: {porcentaje_voto:.2f}%\n")
                retorno = False
        if retorno:
            print("En estas votaciones no hay porcentaje menor al numero solicitado.\n")
    return matriz

def mostrar_mayoria_votos(matriz: list) -> list:
    votos_turno_mañana = 0
    votos_turno_tarde = 0
    votos_turno_noche = 0

    print("\n¿Cual fue el turno con mas votos?")
    for fila in matriz:
        votos_turno_mañana += fila[1]
        votos_turno_tarde += fila[2]
        votos_turno_noche += fila[3]

    if votos_turno_mañana > votos_turno_tarde and votos_turno_mañana > votos_turno_noche:
        print("El turno con más votos fue el turno Mañana.\n")
    elif votos_turno_tarde > votos_turno_mañana and votos_turno_tarde > votos_turno_noche:
        print("El turno con más votos fue el turno Tarde.\n")
    else:
        print("El turno con más votos fue el turno Noche.\n")
    return matriz

def verificar_segunda_vuelta(matriz:list) -> list:
    total_votos_totales = 0
    retorno = True
    for fila in matriz:
        total_votos_totales += sumar_votos(fila)
    if total_votos_totales == 0:
        print("\nError: No se cargaron los votos. Imposible calcular segunda vuelta.\n")
        retorno = False
    else:
        for fila in matriz:
            total_votos_lista = sumar_votos(fila)
            porcentaje_voto = calcular_porcentaje(total_votos_lista,total_votos_totales)

            print(f"\nLista {fila[0]} tiene {total_votos_lista} votos ({porcentaje_voto:.2f}%)")

            if porcentaje_voto > 50:
                print(f"\nLa lista {fila[0]} tiene más del 50% de los votos y no habrá segunda vuelta.\nHay GANADOR.\n")
                retorno = False
                break  
        if retorno:  
            print("\nHay ballogate: Ninguna lista alcanzó más del 50% de los votos.\n")
    return matriz

def realizar_segunda_vuelta(matriz: list) -> None:
    segunda_vuelta = verificar_segunda_vuelta(matriz)
    if not segunda_vuelta:
        print("No hubo segunda vuelta ya que un candidato tiene más del 50% de los votos en la primera vuelta.\n")
    else:
        candidato_1 = None
        candidato1_votos = 0
        candidato_2 = None
        candidato2_votos = 0

        for fila in matriz:
            total_votos = sumar_votos(fila)
            if total_votos > candidato1_votos:
                candidato_2 = candidato_1
                candidato2_votos = candidato1_votos
                candidato_1 = fila[0]
                candidato1_votos = total_votos
            elif total_votos > candidato2_votos:
                candidato_2 = fila[0]
                candidato2_votos = total_votos

        print(f"\nLos dos candidatos más votados son:")
        print(f"Candidato {candidato_1} con {candidato1_votos} votos.")
        print(f"Candidato {candidato_2} con {candidato2_votos} votos.\n")

        total_votos_primera_vuelta = candidato1_votos + candidato2_votos
        print(f"El total de votos en la primera vuelta fue de {total_votos_primera_vuelta} votos.")
        print(f"Ahora, ingrese la cantidad total de votos en cada turno de la segunda vuelta (debe ser {total_votos_primera_vuelta} votos en total por turno).")

        votos_turno1 = pedir_numero(f"Ingrese la cantidad de votos en el turno 1: ", "Error, ingrese un número válido: ", 0, total_votos_primera_vuelta)
        votos_turno2 = pedir_numero(f"Ingrese la cantidad de votos en el turno 2: ", "Error, ingrese un número válido: ", 0, total_votos_primera_vuelta)

        votos_turno1_candidato1 = random.randint(0, votos_turno1)
        votos_turno1_candidato2 = votos_turno1 - votos_turno1_candidato1 

        votos_turno2_candidato1 = random.randint(0, votos_turno2)
        votos_turno2_candidato2 = votos_turno2 - votos_turno2_candidato1 

        total_votos_candidato1 = votos_turno1_candidato1 + votos_turno2_candidato1
        total_votos_candidato2 = votos_turno1_candidato2 + votos_turno2_candidato2

        porcentaje_candidato1 = (total_votos_candidato1 / total_votos_primera_vuelta) * 100
        porcentaje_candidato2 = (total_votos_candidato2 / total_votos_primera_vuelta) * 100

        print(f"\nResultados de la segunda vuelta:")
        print(f"Candidato {candidato_1}: {total_votos_candidato1} votos ({porcentaje_candidato1:.2f}%)")
        print(f"Candidato {candidato_2}: {total_votos_candidato2} votos ({porcentaje_candidato2:.2f}%)")

        if total_votos_candidato1 > total_votos_candidato2:
            print(f"\nEl ganador de la elección es el candidato {candidato_1}!")
        else:
            print(f"\nEl ganador de la elección es el candidato {candidato_2}!")
    return matriz
