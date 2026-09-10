"""
Script de prueba para validar que el código funciona (E1)
"""

from src.dominio.pokemon import Pokemon, Pokedex


def test_pokedex():
    """Prueba básica de la Pokédex."""
    
    print("=" * 60)
    print("TEST: Pokédex E1")
    print("=" * 60)
    
    # Test 1: Crear Pokédex y cargar datos
    print("\n[TEST 1] Crear y cargar Pokédex...")
    pokedex = Pokedex()
    pokedex.cargar_datos_demo()
    
    # Test 2: Listar catálogo
    print("\n[TEST 2] Listar catálogo...")
    assert len(pokedex.pokemon_list) > 0, "ERROR: No hay Pokémon en el catálogo"
    pokedex.listar_catalogo()
    
    # Test 3: Ver detalle
    print("\n[TEST 3] Ver detalle de Pikachu (#25)...")
    pokedex.ver_detalle("25")
    
    # Test 4: Buscar por nombre
    print("\n[TEST 4] Buscar 'char' (Charmander)...")
    pokedex.buscar("char")
    
    # Test 5: Buscar por tipo
    print("\n[TEST 5] Buscar 'agua' (Squirtle)...")
    pokedex.buscar("agua")
    
    # Test 6: Buscar sin resultados
    print("\n[TEST 6] Buscar 'xyz' (sin resultados)...")
    pokedex.buscar("xyz")
    
    print("\n" + "=" * 60)
    print("✓ TODOS LOS TESTS PASARON")
    print("=" * 60)


if __name__ == "__main__":
    test_pokedex()
