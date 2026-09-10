# PROTOCOLO DE PRUEBAS - TP Integrador AyED C2 2026

## Entrega 1 - Casos de prueba

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

## Casos pendientes (futuras entregas)

- CP6: Ordenar por ataque
- CP7: Ordenar por velocidad
- CP8: Agregar Pokémon al equipo
- CP9: Recursión de evoluciones
- CP10: Guardar/cargar CSV
- CP11: Guardar/cargar binario
