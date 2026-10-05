"""Implementación propia de una lista simplemente enlazada."""

from src.excepciones import ItemNoEncontradoError


class Nodo:
    """Nodo con un dato y una referencia al nodo siguiente."""

    def __init__(self, dato, siguiente=None):
        self._dato = dato
        self._siguiente = siguiente


class ListaEnlazada:
    """Lista enlazada iterable, sin almacenamiento en listas de Python."""

    def __init__(self):
        self._cabeza = None
        self._tamanio = 0

    def insertar_al_inicio(self, dato):
        self._cabeza = Nodo(dato, self._cabeza)
        self._tamanio += 1

    def insertar_al_final(self, dato):
        nodo_nuevo = Nodo(dato)
        if self.esta_vacia():
            self._cabeza = nodo_nuevo
        else:
            actual = self._cabeza
            while actual._siguiente is not None:
                actual = actual._siguiente
            actual._siguiente = nodo_nuevo
        self._tamanio += 1

    def buscar(self, dato):
        actual = self._cabeza
        while actual is not None:
            if actual._dato == dato:
                return actual._dato
            actual = actual._siguiente
        raise ItemNoEncontradoError(f"No se encontró: {dato}")

    def eliminar(self, dato):
        anterior = None
        actual = self._cabeza
        while actual is not None:
            if actual._dato == dato:
                if anterior is None:
                    self._cabeza = actual._siguiente
                else:
                    anterior._siguiente = actual._siguiente
                self._tamanio -= 1
                return actual._dato
            anterior = actual
            actual = actual._siguiente
        raise ItemNoEncontradoError(f"No se encontró: {dato}")

    def eliminar_inicio(self):
        if self.esta_vacia():
            raise ItemNoEncontradoError("No se puede eliminar de una lista vacía.")
        dato = self._cabeza._dato
        self._cabeza = self._cabeza._siguiente
        self._tamanio -= 1
        return dato

    def tamanio(self):
        return self._tamanio

    def esta_vacia(self):
        return self._cabeza is None

    def __len__(self):
        return self.tamanio()

    def __iter__(self):
        actual = self._cabeza
        while actual is not None:
            yield actual._dato
            actual = actual._siguiente
