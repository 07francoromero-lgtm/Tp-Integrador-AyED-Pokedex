# INFORME TÉCNICO - TP Integrador AyED C2 2026

## Entrega 1 - Estructura Base y Catálogo

**Fecha:** 09-sep-2026  
**Tema:** Pokédex  
**Integrantes:** Franco Romero, Elias Carvallo

---

## 1. Descripción del sistema

Se implementa un gestor de catálogo Pokédex que permite:
- Listar el catálogo completo de Pokémon
- Ver detalles de un Pokémon específico
- Buscar Pokémon por nombre o tipo
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
8. ⏳ **Recursión del dominio**: Pendiente para E2 (cadenas de evolución)
9. ⏳ **TADs propios**: Pendiente para E3 (ListaEnlazada, Pila, Cola)

---

## 4. Estructura del código

```
src/
├── main.py              # CLI principal - bucle de menú
├── dominio/
│   └── pokemon.py       # Clases Pokemon y Pokedex
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

## 6. Próximos pasos

- **E2**: Recursión de cadenas de evolución, modulación de código
- **E3**: Implementar TADs (ListaEnlazada, Pila, Cola), encapsulamiento
- **E4**: Búsqueda binaria, algoritmos de ordenamiento
- **E5**: Persistencia en CSV y binario con `struct`
- **E6**: Integración completa y defensa oral

---

## 7. Excepciones

Actualmente se capturan:
- Entrada inválida del usuario
- Pokémon no encontrado

Se añadirán excepciones propias en E3.

---

## 8. Complejidad temporal (E1)

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
