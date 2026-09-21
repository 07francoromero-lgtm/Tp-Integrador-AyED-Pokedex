"""Recorrido recursivo de cadenas de evolución Pokémon."""


class CadenaEvolucion:
    """Representa una cadena lineal de evoluciones y permite recorrerla."""

    def __init__(self, evoluciones):
        """Recibe un diccionario con nombre -> siguiente evolución."""
        self.evoluciones = evoluciones

    def recorrer(self, nombre):
        """Devuelve desde ``nombre`` hasta la última evolución, recursivamente."""
        siguiente = self.evoluciones.get(nombre)
        if siguiente is None:
            return [nombre]
        return [nombre] + self.recorrer(siguiente)

    def como_texto(self, nombre):
        """Devuelve la cadena con el formato usado por la Pokédex."""
        return " -> ".join(self.recorrer(nombre))


CADENA_PICHU = CadenaEvolucion({
    "Pichu": "Pikachu",
    "Pikachu": "Raichu",
})
