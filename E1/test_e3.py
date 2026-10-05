"""Pruebas ejecutables de la Entrega 3."""

from contextlib import redirect_stdout
import io
import unittest
from unittest.mock import patch

from src.dominio.pokemon import Pokedex
from src.main import gestionar_equipo
from src.excepciones import (
    ColaVaciaError,
    ColeccionLlenaError,
    ItemNoEncontradoError,
    PilaVaciaError,
)
from src.tads.cola import Cola
from src.tads.lista_enlazada import ListaEnlazada
from src.tads.pila import Pila


class PruebasEntrega3(unittest.TestCase):
    def test_p05_lista_enlazada_e_iterador(self):
        lista = ListaEnlazada()
        self.assertTrue(lista.esta_vacia())
        lista.insertar_al_inicio("Pikachu")
        lista.insertar_al_inicio("Pichu")
        lista.insertar_al_final("Raichu")
        self.assertEqual(list(lista), ["Pichu", "Pikachu", "Raichu"])
        self.assertEqual(lista.buscar("Pikachu"), "Pikachu")
        self.assertEqual(lista.tamanio(), 3)
        self.assertEqual(lista.eliminar("Pikachu"), "Pikachu")
        self.assertEqual(list(lista), ["Pichu", "Raichu"])
        with self.assertRaises(ItemNoEncontradoError):
            lista.buscar("Mew")
        self.assertEqual(lista.eliminar("Pichu"), "Pichu")
        self.assertEqual(lista.eliminar("Raichu"), "Raichu")
        self.assertTrue(lista.esta_vacia())

    def test_p06_pila_y_deshacer_historial(self):
        pila = Pila()
        pila.apilar("primero")
        pila.apilar("segundo")
        self.assertEqual(pila.ver_tope(), "segundo")
        self.assertEqual(pila.desapilar(), "segundo")
        self.assertEqual(pila.desapilar(), "primero")
        with self.assertRaises(PilaVaciaError):
            pila.desapilar()

        pokedex = Pokedex()
        pokedex.cargar_datos_demo()
        agregado = pokedex.agregar_al_equipo(25)
        self.assertEqual(agregado.nombre, "Pikachu")
        pokedex.deshacer_ultima_accion()
        self.assertTrue(pokedex.equipo.esta_vacia())

    def test_p07_cola_fifo_y_turnos_del_dominio(self):
        cola = Cola()
        cola.encolar("primero")
        cola.encolar("segundo")
        self.assertEqual(cola.ver_frente(), "primero")
        self.assertEqual(cola.desencolar(), "primero")
        self.assertEqual(cola.desencolar(), "segundo")
        with self.assertRaises(ColaVaciaError):
            cola.desencolar()

        pokedex = Pokedex()
        pokedex.cargar_datos_demo()
        pokedex.agregar_turno(25)
        pokedex.agregar_turno(4)
        self.assertEqual(pokedex.ver_siguiente_turno().nombre, "Pikachu")
        self.assertEqual(pokedex.procesar_siguiente_turno().nombre, "Pikachu")
        self.assertEqual(pokedex.procesar_siguiente_turno().nombre, "Charmander")
        with self.assertRaises(ColaVaciaError):
            pokedex.procesar_siguiente_turno()

    def test_p08_equipo_limitado_y_excepciones(self):
        pokedex = Pokedex()
        pokedex.cargar_datos_demo()
        for id_pokemon in (172, 1, 4, 7, 25, 26):
            pokedex.agregar_al_equipo(id_pokemon)
        with self.assertRaises(ColeccionLlenaError):
            pokedex.agregar_al_equipo(39)
        with self.assertRaises(ItemNoEncontradoError):
            pokedex.quitar_del_equipo(39)
        self.assertEqual(pokedex.equipo.tamanio(), 6)

        pokedex_menu = Pokedex()
        pokedex_menu.cargar_datos_demo()
        entradas = ["1", "172", "1", "1", "1", "4", "1", "7",
                    "1", "25", "1", "26", "1", "39", "0"]
        salida = io.StringIO()
        with patch("builtins.input", side_effect=entradas), redirect_stdout(salida):
            gestionar_equipo(pokedex_menu)
        self.assertIn("ERROR: El equipo ya alcanzó su límite de 6 Pokémon.", salida.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=2)
