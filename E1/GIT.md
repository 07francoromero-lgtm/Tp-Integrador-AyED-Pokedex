# Git — Guía para el grupo

## Configuración inicial (una sola vez)

Si aún no has configurado git globalmente:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@ejemplo.com"
```

## Clonar el repositorio (si estás en otra máquina)

```bash
git clone https://github.com/07francoromero-lgtm/Tp-Integrador-AyED-Pokedex.git
cd Tp-Integrador-AyED-Pokedex/E1
```

## Flujo típico de trabajo

### 1. Antes de empezar a trabajar

```bash
git pull origin main
```

(Asegúrate de tener los cambios más recientes)

### 2. Hacer cambios locales

```bash
# Edita archivos en tu editor
# Prueba el código: python -m src.main
```

### 3. Guardar cambios locales

```bash
git add .
git status  # Verifica qué archivos van a subir
git commit -m "Descripción clara de lo que hiciste"
```

Ejemplos de mensajes:
- `"E1: CLI básico y clase Pokemon"`
- `"Agregar búsqueda en Pokedex"`
- `"Refactoring de main.py"`

### 4. Enviar al repositorio remoto

```bash
git push origin main
```

## Entregas oficiales (con tags)

### Antes de cada vencimiento

```bash
# Asegúrate de que todos los cambios estén committed
git status

# Crea el tag
git tag entrega-1

# Envía todo
git push origin main
git push origin entrega-1
```

### Si te equivocas antes del vencimiento

```bash
# Elimina el tag local
git tag -d entrega-1

# Elimina el tag remoto
git push origin :refs/tags/entrega-1

# Crea uno nuevo
git tag entrega-1
git push origin entrega-1
```

## Qué NO subir

El `.gitignore` ya excluye:
- `__pycache__/`
- `.venv/`
- `*.bin` (archivos binarios de prueba)

No hagas commit de:
- Archivos de datos modificados localmente
- Tokens o credenciales
- Archivos temporales `.tmp`

## Ver historial

```bash
# Ver últimos commits
git log --oneline

# Ver qué cambió en el último commit
git show

# Ver cambios no committed
git diff
```

## En caso de conflicto

Si dos personas editan el mismo archivo:

```bash
# Antes de push, intenta traer cambios
git pull origin main

# Git te mostrará las líneas en conflicto (entre <<< y >>>)
# Resuelve manualmente en el editor
# Luego:
git add archivo_resuelto.py
git commit -m "Resolver conflicto en archivo_resuelto.py"
git push origin main
```

## Contacto con la cátedra

El repositorio debe estar visible (público o privado con acceso) para:
- diego.ambrossio@unab.edu.ar
- angel.bianco@unab.edu.ar

**Mail de inscripción del grupo:** enviar a ambos antes del 30-ago-2026 con:
- Nombres, emails, usuarios GitHub
- Tema (Pokédex)
- URL del repo
