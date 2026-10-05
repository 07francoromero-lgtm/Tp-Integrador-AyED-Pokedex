"""Excepciones propias del TP Integrador."""


class PilaVaciaError(Exception):
    """Se intenta consultar o desapilar una pila vacía."""


class ColaVaciaError(Exception):
    """Se intenta consultar o desencolar una cola vacía."""


class ColeccionLlenaError(Exception):
    """Se intenta agregar un elemento a una colección completa."""


class ItemNoEncontradoError(Exception):
    """El elemento solicitado no está en la estructura."""
