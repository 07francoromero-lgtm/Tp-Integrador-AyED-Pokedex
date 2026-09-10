"""
Módulo principal del TP Integrador AyED C2 2026 - Pokédex
Punto de entrada de la aplicación
"""

from src.dominio.pokemon import Pokemon, Pokedex


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
        print("4. Ordenar catálogo")
        print("5. Gestionar equipo")
        print("6. Ver historial")
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
            print("Próximamente...")
        elif opcion == "5":
            print("Próximamente...")
        elif opcion == "6":
            print("Próximamente...")
        elif opcion == "0":
            print("¡Gracias por usar Pokédex! Adiós.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
