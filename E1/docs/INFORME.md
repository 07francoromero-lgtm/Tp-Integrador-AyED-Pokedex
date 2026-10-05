# INFORME TÉCNICO - TP Integrador AyED C2 2026

## Entrega 3 - TADs propios e integración con la Pokédex

**Fecha:** 04-oct-2026
**Tema:** Pokédex  
**Integrantes:** Franco Romero

---

## 1. Descripción del sistema

Se implementa un gestor de catálogo Pokédex que permite:
- Listar el catálogo completo de Pokémon
- Ver detalles de un Pokémon específico
- Buscar Pokémon por nombre o tipo
- Mostrar cadenas de evolución mediante recursión
- Gestionar un equipo de combate con capacidad máxima de seis Pokémon
- Deshacer la última modificación del equipo mediante una pila
- Preparar y procesar turnos en orden FIFO mediante una cola

---

## 2. Tipos de datos utilizados

### 2.1 Clases del dominio

- **Pokemon**: Representa un Pokémon individual con atributos inmutables:
  - `id` (int): Identificador único
  - `nombre` (str): Nombre del Pokémon
  - `tipo` (str): Tipo/tipo principal
  - `hp`, `ataque`, `defensa`, `velocidad` (int): Estadísticas
  - `numero_gen` (int): Generación a la que pertenece

- **Pokedex**: Gestor del catálogo (contenedor mutable):
  - `pokemon_list` (`ListaEnlazada`): Almacena todos los Pokémon
  - `equipo` (`EquipoPokemon`): Colección enlazada con límite de seis
  - `historial` (`Pila`): Registra altas y bajas para deshacer
  - `turnos` (`Cola`): Mantiene el orden de preparación de los turnos

### 2.2 Justificación de mutabilidad

- `Pokedex` es **mutable**: necesita agregar/quitar Pokémon, mantener historial
- `Pokemon` es **prácticamente inmutable**: una vez creado, no cambia (sus estadísticas son fijas)

---

## 3. Funcionalidades implementadas

1. ✓ **Listar catálogo**: Recorre el catálogo con formato tabular
2. ✓ **Ver detalle**: Busca por ID y muestra todas las estadísticas
3. ✓ **Buscar**: Búsqueda lineal por nombre o tipo
4. ⏳ **Ordenar**: Pendiente para E4
5. ✓ **Gestionar equipo**: colección con límite y operaciones de alta/baja
6. ✓ **Historial**: pila LIFO con operación para deshacer
7. ⏳ **Guardar/Cargar**: Pendiente para E5
8. ✓ **Recursión del dominio**: recorre cadenas de evolución desde un Pokémon inicial
9. ✓ **TADs propios**: ListaEnlazada, Pila y Cola

---

## 4. Estructura del código

```
src/
├── main.py              # CLI principal - bucle de menú
├── dominio/
│   ├── pokemon.py        # Clases Pokemon y Pokedex
│   ├── equipo.py         # Equipo limitado
│   └── evoluciones.py    # CadenaEvolucion y datos de evolución
├── excepciones.py        # Excepciones propias
├── tads/
│   ├── lista_enlazada.py # Nodo, lista e iterador
│   ├── pila.py           # Pila LIFO
│   └── cola.py           # Cola FIFO
├── algoritmos/          # Búsqueda y ordenamiento (E4)
└── persistencia/        # CSV y binario (E5)
```

---

## 5. Ejecución

```bash
python -m src.main
```

El programa presenta un menú interactivo que permite acceder a las operaciones disponibles.

---

## 6. Recursión del dominio

La clase `CadenaEvolucion` trabaja con un diccionario donde cada Pokémon apunta a su siguiente evolución. El caso base ocurre cuando el Pokémon no tiene una evolución siguiente: se devuelve una lista con ese único nombre. En el caso recursivo se devuelve el Pokémon actual y se continúa con la siguiente evolución.

### Traza: Pichu → Pikachu → Raichu

La llamada `CADENA_PICHU.recorrer("Pichu")` se resuelve así:

1. `recorrer("Pichu")`: encuentra como siguiente a `Pikachu`; conserva `Pichu` y llama a `recorrer("Pikachu")`.
2. `recorrer("Pikachu")`: encuentra como siguiente a `Raichu`; conserva `Pikachu` y llama a `recorrer("Raichu")`.
3. `recorrer("Raichu")`: no encuentra una siguiente evolución; aplica el caso base y devuelve `["Raichu"]`.
4. La segunda llamada concatena `Pikachu` y devuelve `["Pikachu", "Raichu"]`.
5. La primera llamada concatena `Pichu` y devuelve `["Pichu", "Pikachu", "Raichu"]`.

El menú transforma esa lista en el texto `Pichu -> Pikachu -> Raichu`.

## 7. Próximos pasos

- **E4**: Búsqueda binaria, algoritmos de ordenamiento
- **E5**: Persistencia en CSV y binario con `struct`
- **E6**: Integración completa y defensa oral

---

## 8. Excepciones

Los submenús capturan excepciones específicas: `PilaVaciaError`, `ColaVaciaError`, `ColeccionLlenaError` e `ItemNoEncontradoError`. La entrada numérica inválida se maneja por separado.

---

## 9. Complejidad temporal (E1)

| Operación | Complejidad | Justificación |
|-----------|-------------|---------------|
| Listar catálogo | O(n) | Recorre todos los Pokémon |
| Ver detalle | O(n) | Búsqueda lineal por ID |
| Buscar | O(n) | Búsqueda lineal por nombre/tipo |

(*) Será optimizada con búsqueda binaria en E4.

---

## Notas

- No se usa pickle, solo la biblioteca estándar
- Los datos de demostración son Gen 1 de Pokémon
- El interfaz es CLI puro, sin librerías externas

## Entrega 3 - TADs, colecciones y excepciones

### Estructuras implementadas

- `src/tads/lista_enlazada.py`: `Nodo` guarda dato y referencia siguiente. `ListaEnlazada` implementa inserción al inicio/final, búsqueda, eliminación, tamaño, lista vacía e iteración con `yield`.
- `src/tads/pila.py`: pila LIFO construida sobre `ListaEnlazada`; el historial del dominio registra altas y bajas del equipo para deshacer la última acción.
- `src/tads/cola.py`: cola FIFO construida sobre `ListaEnlazada`; la Pokédex la usa para preparar y procesar turnos.
- `src/dominio/equipo.py`: equipo con capacidad máxima de seis, almacenado en `ListaEnlazada`; al exceder el máximo lanza `ColeccionLlenaError`.
- `src/excepciones.py`: define las excepciones específicas de pila, cola, colección llena e ítem no encontrado.

El catálogo también está almacenado en `ListaEnlazada`. El listado, las búsquedas y el equipo se recorren mediante `for`, usando el iterador de la estructura. El menú no accede a nodos ni a atributos internos de los TADs; llama operaciones del dominio, que a su vez delegan en los TADs.

### Ejecución y pruebas

Desde la raíz del repositorio, `python -m src.main` inicia el CLI. El paquete de entrada de la raíz delega en la aplicación ubicada en `E1/src`.

Los casos E3 P05–P08 se ejecutan con `python test_e3.py` desde `E1/`. El resultado de esta ejecución fue **4 tests OK**. También se ejecutó `python test_e1.py` para verificar que el catálogo de E1 sigue funcionando.

### Operaciones con errores

Desapilar o consultar una pila vacía lanza `PilaVaciaError`; desencolar o consultar una cola vacía lanza `ColaVaciaError`; superar los seis integrantes lanza `ColeccionLlenaError`; buscar o quitar un Pokémon inexistente lanza `ItemNoEncontradoError`. Los submenús capturan cada excepción de forma específica y muestran el error sin terminar el programa.
