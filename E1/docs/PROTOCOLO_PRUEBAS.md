# PROTOCOLO DE PRUEBAS - TP Integrador AyED C2 2026

## Entrega 2 - Casos de prueba

**Tema:** Pokédex  
**Objetivo:** Validar que el catálogo se carga y las operaciones básicas funcionan

---

## Casos de prueba

### CP1: Listar catálogo
| Paso | Descripción | Resultado esperado |
|------|-------------|-------------------|
| 1 | Ejecutar `python -m src.main` | CLI arranca sin errores |
| 2 | Seleccionar opción "1. Listar catálogo" | Se muestra tabla con todos los Pokémon |
| 3 | Verificar que hay al menos 5 Pokémon | ✓ Pasa |

---

### CP2: Ver detalle
| Paso | Descripción | Resultado esperado |
|------|-------------|-------------------|
| 1 | Seleccionar opción "2. Ver detalle" | Solicita ID del Pokémon |
| 2 | Ingresar "25" (Pikachu) | Muestra: Pikachu, tipo Eléctrico, Gen 1, HP=35, Ataque=55, etc. |
| 3 | Ingresar ID inválido como "999" | Muestra "Pokémon no encontrado" |
| 4 | Ingresar texto en lugar de número | Captura error y solicita nuevamente |

---

### CP3: Buscar por nombre
| Paso | Descripción | Resultado esperado |
|------|-------------|-------------------|
| 1 | Seleccionar opción "3. Buscar" | Solicita término de búsqueda |
| 2 | Ingresar "char" | Encuentra y muestra Charmander |
| 3 | Ingresar "abc" | Muestra "No se encontraron coincidencias" |

---

### CP4: Buscar por tipo
| Paso | Descripción | Resultado esperado |
|------|-------------|-------------------|
| 1 | Seleccionar opción "3. Buscar" | Solicita término de búsqueda |
| 2 | Ingresar "agua" | Encuentra y muestra Squirtle |
| 3 | Ingresar "fuego" | Encuentra y muestra Charmander |

---

### CP5: Entrada vacía
| Paso | Descripción | Resultado esperado |
|------|-------------|-------------------|
| 1 | Presionar Enter sin ingresar nada | Muestra "Opción inválida" |
| 2 | Intentar buscar sin término | Maneja sin crash |

---

## Estado actual (E1)

| Caso | Estado | Notas |
|------|--------|-------|
| CP1 | ✓ Pasa | Datos de demo cargados |
| CP2 | ✓ Pasa | Con manejo de errores |
| CP3 | ✓ Pasa | Búsqueda lineal |
| CP4 | ✓ Pasa | Case-insensitive |
| CP5 | ✓ Pasa | Menú robusto |

---

### CP6: Cadena completa de evoluciones
| Paso | Descripción | Resultado esperado |
|------|-------------|-------------------|
| 1 | Ejecutar la opción "4" | Solicita el Pokémon inicial |
| 2 | Ingresar "Pichu" | Muestra `Pichu -> Pikachu -> Raichu` |
| 3 | Verificar el resultado | Incluye las tres evoluciones y respeta el orden |

### CP7: Caso base de la recursión
| Paso | Descripción | Resultado esperado |
|------|-------------|-------------------|
| 1 | Ejecutar la opción "4" | Solicita el Pokémon inicial |
| 2 | Ingresar "Raichu" | Muestra únicamente `Raichu` |
| 3 | Verificar el resultado | No agrega una evolución inexistente |

### CP8: Carga de Pokémon de la cadena
| Paso | Descripción | Resultado esperado |
|------|-------------|-------------------|
| 1 | Ejecutar la opción "1" | Muestra el catálogo |
| 2 | Revisar los nombres | Aparecen Pichu, Pikachu y Raichu |
| 3 | Verificar el total | El catálogo contiene 7 Pokémon |

## Resultados de E2

| Caso | Prueba | Resultado |
|------|--------|-----------|
| CP6 | Cadena Pichu -> Pikachu -> Raichu | pasa |
| CP7 | Caso base Raichu sin evolución siguiente | pasa |
| CP8 | Catálogo incluye Pichu, Pikachu y Raichu | pasa |

## Próximas entregas

- CP9: Ordenar por ataque
- CP10: Agregar Pokémon al equipo de combate
- CP11: Guardar/cargar CSV
- CP12: Guardar/cargar binario

## Entrega 3 - Casos ejecutados

**Comando:** `python test_e3.py`, ejecutado desde `E1/` el 04-oct-2026.

| Caso | Prueba | Resultado esperado | Resultado |
|------|--------|-------------------|-----------|
| P05 | Insertar al inicio y al final; recorrer con `for`; buscar, eliminar y consultar tamaño. | Orden y tamaño correctos; buscar un ausente lanza `ItemNoEncontradoError`. | pasa |
| P06 | Apilar y desapilar dos acciones; comprobar el historial del equipo y deshacer un alta. | LIFO correcto; pila vacía lanza `PilaVaciaError`; el equipo queda vacío tras deshacer. | pasa |
| P07 | Encolar dos Pokémon, consultar el frente y procesar ambos turnos. | FIFO conserva el orden; cola vacía lanza `ColaVaciaError`. | pasa |
| P08 | Agregar seis Pokémon al equipo e intentar agregar un séptimo desde el menú; quitar uno ausente. | El séptimo lanza `ColeccionLlenaError`, que el menú captura; el ausente lanza `ItemNoEncontradoError`; el equipo conserva seis integrantes. | pasa |

**Resultado de la ejecución:** 4 tests ejecutados, 4 OK. También se ejecutó `python test_e1.py`: todos los tests anteriores pasan.
