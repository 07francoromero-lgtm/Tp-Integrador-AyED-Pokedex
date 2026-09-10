"""
Módulo Pokemon - Clase base para los Pokémon
"""


class Pokemon:
    """Representa un Pokémon del catálogo."""
    
    def __init__(self, id_pokemon, nombre, tipo, hp, ataque, defensa, velocidad, numero_gen):
        """
        Inicializa un Pokémon.
        
        Args:
            id_pokemon (int): ID único del Pokémon
            nombre (str): Nombre del Pokémon
            tipo (str): Tipo principal (fuego, agua, planta, etc.)
            hp (int): Puntos de vida
            ataque (int): Poder de ataque
            defensa (int): Poder de defensa
            velocidad (int): Velocidad
            numero_gen (int): Número de generación
        """
        self.id = id_pokemon
        self.nombre = nombre
        self.tipo = tipo
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.numero_gen = numero_gen
    
    def __str__(self):
        """Retorna una representación en string del Pokémon."""
        return f"#{self.id:03d} {self.nombre} ({self.tipo})"
    
    def __repr__(self):
        """Representación técnica del Pokémon."""
        return f"Pokemon({self.id}, '{self.nombre}', '{self.tipo}')"
    
    def mostrar_detalle(self):
        """Imprime el detalle completo del Pokémon."""
        print(f"\n--- DETALLE DEL POKÉMON ---")
        print(f"ID: #{self.id:03d}")
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Generación: {self.numero_gen}")
        print(f"Estadísticas:")
        print(f"  HP:     {self.hp}")
        print(f"  Ataque: {self.ataque}")
        print(f"  Defensa: {self.defensa}")
        print(f"  Velocidad: {self.velocidad}")


class Pokedex:
    """Gestor del catálogo de Pokémon."""
    
    def __init__(self):
        """Inicializa la Pokédex vacía."""
        self.pokemon_list = []  # Será reemplazado por ListaEnlazada en E3
        self.equipo = []  # Equipo de combate (máx 6) - será Pila o Lista
        self.historial = []  # Historial de acciones - será Pila
    
    def cargar_datos_demo(self):
        """Carga datos de demostración para pruebas."""
        # Datos de ejemplo: Pokémon de la Gen 1
        pokemon_demo = [
            Pokemon(1, "Bulbasaur", "Planta/Veneno", 45, 49, 49, 45, 1),
            Pokemon(4, "Charmander", "Fuego", 39, 52, 43, 65, 1),
            Pokemon(7, "Squirtle", "Agua", 44, 48, 65, 43, 1),
            Pokemon(25, "Pikachu", "Eléctrico", 35, 55, 40, 90, 1),
            Pokemon(39, "Jigglypuff", "Normal/Hada", 115, 40, 20, 20, 1),
        ]
        self.pokemon_list = pokemon_demo
        print(f"✓ Pokédex cargada con {len(pokemon_demo)} Pokémon de demostración")
    
    def listar_catalogo(self):
        """Lista todos los Pokémon en el catálogo."""
        if not self.pokemon_list:
            print("La Pokédex está vacía.")
            return
        
        print("\n--- CATÁLOGO DE POKÉMON ---")
        print(f"{'ID':<5} {'Nombre':<15} {'Tipo':<20} {'Gen':<4}")
        print("-" * 50)
        for pokemon in self.pokemon_list:
            print(f"{pokemon.id:<5} {pokemon.nombre:<15} {pokemon.tipo:<20} {pokemon.numero_gen:<4}")
        print(f"\nTotal: {len(self.pokemon_list)} Pokémon")
    
    def ver_detalle(self, id_pokemon_str):
        """Muestra el detalle de un Pokémon específico."""
        try:
            id_pokemon = int(id_pokemon_str)
        except ValueError:
            print("ERROR: ID inválido. Debe ser un número.")
            return
        
        for pokemon in self.pokemon_list:
            if pokemon.id == id_pokemon:
                pokemon.mostrar_detalle()
                return
        
        print(f"ERROR: Pokémon con ID {id_pokemon} no encontrado.")
    
    def buscar(self, termino):
        """Busca Pokémon por nombre o tipo."""
        termino_lower = termino.lower()
        resultados = []
        
        for pokemon in self.pokemon_list:
            if (termino_lower in pokemon.nombre.lower() or 
                termino_lower in pokemon.tipo.lower()):
                resultados.append(pokemon)
        
        if not resultados:
            print(f"No se encontraron Pokémon que coincidan con '{termino}'.")
            return
        
        print(f"\n--- RESULTADOS DE BÚSQUEDA: '{termino}' ---")
        print(f"{'ID':<5} {'Nombre':<15} {'Tipo':<20}")
        print("-" * 45)
        for pokemon in resultados:
            print(f"{pokemon.id:<5} {pokemon.nombre:<15} {pokemon.tipo:<20}")
        print(f"\nTotal: {len(resultados)} resultado(s)")
