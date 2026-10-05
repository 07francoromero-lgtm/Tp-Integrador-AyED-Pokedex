"""
Módulo principal del TP Integrador AyED C2 2026 - Pokédex
Punto de entrada de la aplicación
"""

from src.dominio.pokemon import Pokedex
from src.excepciones import (
    ColaVaciaError,
    ColeccionLlenaError,
    ItemNoEncontradoError,
    PilaVaciaError,
)


def gestionar_equipo(pokedex):
    """Menú del equipo; opera únicamente mediante la API del dominio."""
    while True:
        print("\n--- EQUIPO POKÉMON ---")
        print("1. Agregar Pokémon")
        print("2. Quitar Pokémon")
        print("3. Deshacer última acción")
        print("4. Listar equipo")
        print("0. Volver")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            try:
                pokemon = pokedex.agregar_al_equipo(int(input("ID del Pokémon: ").strip()))
                print(f"{pokemon.nombre} agregado al equipo.")
            except ValueError:
                print("ERROR: el ID debe ser un número.")
            except ItemNoEncontradoError as error:
                print(f"ERROR: {error}")
            except ColeccionLlenaError as error:
                print(f"ERROR: {error}")
        elif opcion == "2":
            try:
                pokemon = pokedex.quitar_del_equipo(int(input("ID del Pokémon: ").strip()))
                print(f"{pokemon.nombre} quitado del equipo.")
            except ValueError:
                print("ERROR: el ID debe ser un número.")
            except ItemNoEncontradoError as error:
                print(f"ERROR: {error}")
        elif opcion == "3":
            try:
                accion, pokemon = pokedex.deshacer_ultima_accion()
                print(f"Acción deshecha: {accion} {pokemon.nombre}.")
            except PilaVaciaError as error:
                print(f"ERROR: {error}")
            except ItemNoEncontradoError as error:
                print(f"ERROR: {error}")
            except ColeccionLlenaError as error:
                print(f"ERROR: {error}")
        elif opcion == "4":
            pokedex.listar_equipo()
        elif opcion == "0":
            return
        else:
            print("Opción inválida.")


def gestionar_turnos(pokedex):
    """Menú de preparación y procesamiento FIFO de turnos."""
    while True:
        print("\n--- TURNOS DE COMBATE ---")
        print("1. Encolar Pokémon")
        print("2. Ver próximo turno")
        print("3. Procesar turno")
        print("0. Volver")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            try:
                pokemon = pokedex.agregar_turno(int(input("ID del Pokémon: ").strip()))
                print(f"Turno de {pokemon.nombre} agregado.")
            except ValueError:
                print("ERROR: el ID debe ser un número.")
            except ItemNoEncontradoError as error:
                print(f"ERROR: {error}")
        elif opcion == "2":
            try:
                print(f"Próximo turno: {pokedex.ver_siguiente_turno().nombre}")
            except ColaVaciaError as error:
                print(f"ERROR: {error}")
        elif opcion == "3":
            try:
                print(f"Turno procesado: {pokedex.procesar_siguiente_turno().nombre}")
            except ColaVaciaError as error:
                print(f"ERROR: {error}")
        elif opcion == "0":
            return
        else:
            print("Opción inválida.")


def main():
    """Función principal. Ejecuta el menú CLI."""
    print("=" * 60)
    print("POKÉDEX - TP Integrador AyED C2 2026")
    print("=" * 60)
    print()
    
    # Instancia la Pokédex
    pokedex = Pokedex()
    
    # Carga los datos (por ahora de forma simulada)
    pokedex.cargar_datos_demo()
    
    # Menú principal
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Listar catálogo")
        print("2. Ver detalle de Pokémon")
        print("3. Buscar Pokémon")
        print("4. Ver cadena de evoluciones")
        print("5. Gestionar equipo")
        print("6. Gestionar turnos")
        print("0. Salir")
        print()
        
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            pokedex.listar_catalogo()
        elif opcion == "2":
            pokemon_id = input("Ingresa el ID del Pokémon: ").strip()
            pokedex.ver_detalle(pokemon_id)
        elif opcion == "3":
            busqueda = input("Ingresa el nombre o tipo a buscar: ").strip()
            pokedex.buscar(busqueda)
        elif opcion == "4":
            nombre = input("Ingresa el Pokémon inicial (Enter para Pichu): ").strip()
            pokedex.mostrar_evoluciones(nombre or "Pichu")
        elif opcion == "5":
            gestionar_equipo(pokedex)
        elif opcion == "6":
            gestionar_turnos(pokedex)
        elif opcion == "0":
            print("¡Gracias por usar Pokédex! Adiós.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
