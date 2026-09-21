# INFORME TÉCNICO - TP Integrador AyED C2 2026

## Entrega 2 - Módulos y recursión del dominio

**Fecha:** 20-sep-2026  
**Tema:** Pokédex  
**Integrantes:** Franco Romero

---

## 1. Descripción del sistema

Se implementa un gestor de catálogo Pokédex que permite:
- Listar el catálogo completo de Pokémon
- Ver detalles de un Pokémon específico
- Buscar Pokémon por nombre o tipo
- Mostrar cadenas de evolución mediante recursión
- Gestionar un equipo de combate (próximas entregas)
- Mantener historial de acciones (próximas entregas)

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
  - `pokemon_list` (list): Almacena todos los Pokémon
  - `equipo` (list): Equipo de combate (será Pila en E3)
  - `historial` (list): Historial de acciones (será Pila en E3)

### 2.2 Justificación de mutabilidad

- `Pokedex` es **mutable**: necesita agregar/quitar Pokémon, mantener historial
- `Pokemon` es **prácticamente inmutable**: una vez creado, no cambia (sus estadísticas son fijas)

---

## 3. Funcionalidades implementadas (E1)

1. ✓ **Listar catálogo**: Recorre el catálogo con formato tabular
2. ✓ **Ver detalle**: Busca por ID y muestra todas las estadísticas
3. ✓ **Buscar**: Búsqueda lineal por nombre o tipo
4. ⏳ **Ordenar**: Pendiente para E4
5. ⏳ **Gestionar equipo**: Pendiente para E3
6. ⏳ **Historial**: Pendiente para E3
7. ⏳ **Guardar/Cargar**: Pendiente para E5
8. ✓ **Recursión del dominio**: recorre cadenas de evolución desde un Pokémon inicial
9. ⏳ **TADs propios**: Pendiente para E3 (ListaEnlazada, Pila, Cola)

---

## 4. Estructura del código

```
src/
├── main.py              # CLI principal - bucle de menú
├── dominio/
│   ├── pokemon.py       # Clases Pokemon y Pokedex
│   └── evoluciones.py    # CadenaEvolucion y datos de evolución
├── tads/                # TADs (E3)
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

- **E2**: Recursión de cadenas de evolución, modulación de código
- **E3**: Implementar TADs (ListaEnlazada, Pila, Cola), encapsulamiento
- **E4**: Búsqueda binaria, algoritmos de ordenamiento
- **E5**: Persistencia en CSV y binario con `struct`
- **E6**: Integración completa y defensa oral

---

## 8. Excepciones

Actualmente se capturan:
- Entrada inválida del usuario
- Pokémon no encontrado

Se añadirán excepciones propias en E3.

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
