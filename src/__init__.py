"""Acceso al paquete de la aplicación alojado en E1/src."""

from pathlib import Path

RUTA_SRC_PROYECTO = Path(__file__).resolve().parent.parent / "E1" / "src"
if str(RUTA_SRC_PROYECTO) not in __path__:
    __path__.append(str(RUTA_SRC_PROYECTO))
