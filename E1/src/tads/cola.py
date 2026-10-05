"""Cola FIFO implementada sobre ListaEnlazada."""

from src.excepciones import ColaVaciaError
from src.tads.lista_enlazada import ListaEnlazada


class Cola:
    def __init__(self):
        self._elementos = ListaEnlazada()

    def encolar(self, elemento):
        self._elementos.insertar_al_final(elemento)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede desencolar una cola vacía.")
        return self._elementos.eliminar_inicio()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("No hay elemento al frente de una cola vacía.")
        return next(iter(self._elementos))

    def esta_vacia(self):
        return self._elementos.esta_vacia()
