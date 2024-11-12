'''
El centro de estudiantes de la UTN FRA realiza unas elecciones para definir a su próximo
presidente/a
Para ello requieren un sistema que logre contar los votos positivos de cada uno de los
alumnos.
Cada partido político va a guardar lo siguiente (Estructurar la matriz como crean
conveniente):
-Nro de lista (número positivo 3 cifras)
-Cantidad de votos (Turno mañana)
-Cantidad de votos (Turno tarde)
-Cantidad de votos (Turno noche)

De las 5 listas que se postularon se requiere lo siguiente:

1. Cargar Votos: Se realiza una carga secuencial de todos los votos de cada una de las
cinco listas.
NOTA: Validar todos los ingresos de datos, evitar votos negativos o nro de lista que no sean
números de tres cifras.
2. Mostrar Votos: Muestra en un lindo formato los siguientes datos:
Nro Lista, Votos Turno Mañana,Votos Turno Tarde,Votos Turno Noche,Porcentaje Voto:
EJEMPLO (El formato lo eligen ustedes, mientras se vea lindo) :
3. Ordenar votos turno mañana: Ordena la matriz de mayor a menor por la cantidad de
votos que tuvieron en el turno mañana.
4. No te votó nadie: Encontrar y mostrar a las listas que tengan menos del 5% de todos
los votos.
5. Turno que más fue a votar: Mostrar cuál fue el turno o los turnos al que más alumnos
fueron a votar.
6. Ballotage:Verifica si hay segunda vuelta o no, según las reglas estudiantiles la única
forma de evitar la segunda vuelta es que una lista tenga más del 50% de los votos.
7. Realizar segunda vuelta:Se encarga de realizar la segunda vuelta electoral con los
dos candidatos más votados. Se le pide al usuario la cantidad de alumnos que fueron
a votar en cada turno en la segunda vuelta y de manera random se calculan los votos
del primer y segundo candidato en cada turno. Al final de ello se calcula el porcentaje
final de cada lista y se muestra al ganador de las elecciones.
NOTA: Solo se accede si hay la opción 6 verificó que hay segunda vuelta, sino indicar
que no hubo segunda vuelta.
La cantidad de votos por cada turno debe ser la misma que hubo en la primer vuelta.
'''
from funciones import *


def ejecutar_menu():
    listas = inicializar_matriz(5,4) 

    while(True):
        print("CENTRO DE ESTUDIANTES\n1. Cargar votos\n2. Mostrar votos\n3. Ordenar votos\n4. No te voto nadie\n5. Turno que mas fue a votar\n6. Ballotage\n7. Realizar segunda vuelta\n8. Salir")

        opcion = pedir_numero("Su opcion: ","Opcion invalida ingrese números entre 1-8\nSu opcion:",1,8)

        if opcion == 1:
            listas = cargar_votos(listas)
        elif opcion == 2:
            listas = mostrar_matriz(listas)
        elif opcion == 3:
            listas = ordenar_votos_mañana(listas)
            listas = mostrar_matriz(listas)
        elif opcion == 4:
            listas = mostrar_porcentaje_menor(listas)
        elif opcion == 5:
            listas = mostrar_mayoria_votos(listas)
        elif opcion == 6:
            listas = verificar_segunda_vuelta(listas)
        elif opcion == 7:
            listas = realizar_segunda_vuelta(listas)
        elif opcion == 8:
            print("Saliendo...")
            break
        limpiar_consola()

ejecutar_menu()
