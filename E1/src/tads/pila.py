"""Pila LIFO implementada sobre ListaEnlazada."""

from src.excepciones import PilaVaciaError
from src.tads.lista_enlazada import ListaEnlazada


class Pila:
    def __init__(self):
        self._elementos = ListaEnlazada()

    def apilar(self, elemento):
        self._elementos.insertar_al_inicio(elemento)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar una pila vacía.")
        return self._elementos.eliminar_inicio()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("No hay elemento en una pila vacía.")
        return next(iter(self._elementos))

    def esta_vacia(self):
        return self._elementos.esta_vacia()
