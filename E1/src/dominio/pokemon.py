"""
Módulo Pokemon - Clase base para los Pokémon
"""

from src.dominio.equipo import EquipoPokemon
from src.dominio.evoluciones import CADENA_PICHU
from src.excepciones import ItemNoEncontradoError
from src.tads.cola import Cola
from src.tads.lista_enlazada import ListaEnlazada
from src.tads.pila import Pila


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
        self.pokemon_list = ListaEnlazada()
        self.equipo = EquipoPokemon(limite=6)
        self.historial = Pila()
        self.turnos = Cola()
    
    def cargar_datos_demo(self):
        """Carga datos de demostración para pruebas."""
        # Datos de ejemplo: Pokémon de la Gen 1
        pokemon_demo = (
            Pokemon(172, "Pichu", "Eléctrico", 20, 40, 15, 60, 2),
            Pokemon(1, "Bulbasaur", "Planta/Veneno", 45, 49, 49, 45, 1),
            Pokemon(4, "Charmander", "Fuego", 39, 52, 43, 65, 1),
            Pokemon(7, "Squirtle", "Agua", 44, 48, 65, 43, 1),
            Pokemon(25, "Pikachu", "Eléctrico", 35, 55, 40, 90, 1),
            Pokemon(26, "Raichu", "Eléctrico", 60, 90, 55, 110, 1),
            Pokemon(39, "Jigglypuff", "Normal/Hada", 115, 40, 20, 20, 1),
        )
        for pokemon in pokemon_demo:
            self.pokemon_list.insertar_al_final(pokemon)
        print(f"✓ Pokédex cargada con {len(pokemon_demo)} Pokémon de demostración")
    
    def listar_catalogo(self):
        """Lista todos los Pokémon en el catálogo."""
        if self.pokemon_list.esta_vacia():
            print("La Pokédex está vacía.")
            return
        
        print("\n--- CATÁLOGO DE POKÉMON ---")
        print(f"{'ID':<5} {'Nombre':<15} {'Tipo':<20} {'Gen':<4}")
        print("-" * 50)
        for pokemon in self.pokemon_list:
            print(f"{pokemon.id:<5} {pokemon.nombre:<15} {pokemon.tipo:<20} {pokemon.numero_gen:<4}")
        print(f"\nTotal: {self.pokemon_list.tamanio()} Pokémon")
    
    def ver_detalle(self, id_pokemon_str):
        """Muestra el detalle de un Pokémon específico."""
        try:
            id_pokemon = int(id_pokemon_str)
        except ValueError:
            print("ERROR: ID inválido. Debe ser un número.")
            return
        
        try:
            self.obtener_pokemon(id_pokemon).mostrar_detalle()
        except ItemNoEncontradoError as error:
            print(f"ERROR: {error}")

    def obtener_pokemon(self, id_pokemon):
        """Busca un Pokémon por ID o lanza ItemNoEncontradoError."""
        for pokemon in self.pokemon_list:
            if pokemon.id == id_pokemon:
                return pokemon
        raise ItemNoEncontradoError(f"Pokémon con ID {id_pokemon} no encontrado.")
    
    def buscar(self, termino):
        """Busca Pokémon por nombre o tipo."""
        termino_lower = termino.lower()
        cantidad = 0
        for pokemon in self.pokemon_list:
            if (termino_lower in pokemon.nombre.lower() or 
                termino_lower in pokemon.tipo.lower()):
                if cantidad == 0:
                    print(f"\n--- RESULTADOS DE BÚSQUEDA: '{termino}' ---")
                    print(f"{'ID':<5} {'Nombre':<15} {'Tipo':<20}")
                    print("-" * 45)
                print(f"{pokemon.id:<5} {pokemon.nombre:<15} {pokemon.tipo:<20}")
                cantidad += 1

        if cantidad == 0:
            print(f"No se encontraron Pokémon que coincidan con '{termino}'.")
            return
        print(f"\nTotal: {cantidad} resultado(s)")

    def mostrar_evoluciones(self, nombre="Pichu"):
        """Muestra la cadena de evoluciones desde el Pokémon indicado."""
        cadena = CADENA_PICHU.recorrer(nombre)
        print(f"\n--- CADENA DE EVOLUCIONES ---")
        print(" -> ".join(cadena))
        return cadena

    def agregar_al_equipo(self, id_pokemon):
        pokemon = self.obtener_pokemon(id_pokemon)
        self.equipo.agregar(pokemon)
        self.historial.apilar(("agregar", pokemon))
        return pokemon

    def quitar_del_equipo(self, id_pokemon):
        pokemon = self.obtener_pokemon(id_pokemon)
        eliminado = self.equipo.quitar(pokemon)
        self.historial.apilar(("quitar", eliminado))
        return eliminado

    def deshacer_ultima_accion(self):
        accion, pokemon = self.historial.desapilar()
        if accion == "agregar":
            self.equipo.quitar(pokemon)
        else:
            self.equipo.agregar(pokemon)
        return accion, pokemon

    def listar_equipo(self):
        if self.equipo.esta_vacia():
            print("El equipo está vacío.")
            return
        print("\n--- EQUIPO ---")
        for pokemon in self.equipo:
            print(pokemon)
        print(f"Total: {self.equipo.tamanio()}/{self.equipo.limite()}")

    def agregar_turno(self, id_pokemon):
        pokemon = self.obtener_pokemon(id_pokemon)
        self.turnos.encolar(pokemon)
        return pokemon

    def procesar_siguiente_turno(self):
        return self.turnos.desencolar()

    def ver_siguiente_turno(self):
        return self.turnos.ver_frente()
