"""Equipo Pokémon de capacidad limitada."""

from src.excepciones import ColeccionLlenaError
from src.tads.lista_enlazada import ListaEnlazada


class EquipoPokemon:
    """Colección principal del equipo, almacenada en una lista enlazada."""

    def __init__(self, limite=6):
        self._integrantes = ListaEnlazada()
        self._limite = limite

    def agregar(self, pokemon):
        if self._integrantes.tamanio() >= self._limite:
            raise ColeccionLlenaError(
                f"El equipo ya alcanzó su límite de {self._limite} Pokémon."
            )
        self._integrantes.insertar_al_final(pokemon)

    def quitar(self, pokemon):
        return self._integrantes.eliminar(pokemon)

    def buscar(self, pokemon):
        return self._integrantes.buscar(pokemon)

    def esta_vacia(self):
        return self._integrantes.esta_vacia()

    def tamanio(self):
        return self._integrantes.tamanio()

    def limite(self):
        return self._limite

    def __iter__(self):
        return iter(self._integrantes)
