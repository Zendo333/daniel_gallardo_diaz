import json
from pickle import TRUE
from funciones import *

def main():
    archivo_medicamentos = "medicamentos.json"
    archivo_laboratorios = "laboratorios.json"

    cargar_o_crear_archivos(archivo_medicamentos, archivo_laboratorios)

    while True:
        mostrar_menu()
        opcion = input("\nIngrese la opción deseada: ")

        if opcion == "1":
            agregar_medicamento(archivo_medicamentos)
        elif opcion == "2":
            agregar_laboratorio(archivo_laboratorios)
        elif opcion == "3":
            mostrar_info(archivo_medicamentos, archivo_laboratorios)
        elif opcion == "4":
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpcion no valida. Ingrese una opcion valida.\n")

if __name__ == "__main__":
    main()