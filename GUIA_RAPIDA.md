# 🚀 Guía de Inicio Rápido

## Bienvenido al Sistema Operativo Simulado

Esta guía te ayudará a empezar en 5 minutos.

---

## Paso 1: Instalar

```bash
# Abre terminal/cmd en la carpeta del proyecto
cd Sistema-Operativo

# Crea entorno virtual
python3 -m venv .venv

# Activa entorno
source .venv/bin/activate  # macOS/Linux
# o
.venv\Scripts\activate     # Windows

# Instala paquetes
pip install -r requirements.txt
```

---

## Paso 2: Ejecutar

```bash
python main.py
```

Se abrirá una ventana con 11 pestañas. ¡Listo!

---

## Paso 3: Explorar

### 📊 Panel Control (Pestaña 1)
- Ver información general del sistema
- Accesos rápidos a funcionalidades
- Estado actual

### ⚙️ Recursos (Pestaña 2)
- **Actualizar CPU**: Ver uso actual de CPU
- **Actualizar Memoria**: Ver RAM disponible
- **Listar Periféricos**: Ver dispositivos

### 📁 Archivos (Pestaña 3)
**Crear archivo:**
1. Clic en "➕ Crear"
2. Escribir nombre: `miarchivo.txt`
3. OK

**Copiar y pegar:**
1. Seleccionar archivo
2. Clic "📋 Copiar"
3. Clic "📌 Pegar"
4. Ingresar nuevo nombre

### 🖥️ Terminal (Pestaña 6)
Prueba estos comandos:
```
help      # Ver ayuda
pwd       # Ver directorio
date      # Ver fecha/hora
whoami    # Ver usuario
echo hola # Imprimir texto
```

### ⏱️ Scheduling (Pestaña 7)
1. Ingresar PID: `1001`
2. Ingresar Burst: `10`
3. Clic "➕ Agregar" (repetir 2-3 veces)
4. Clic "▶️ Ejecutar RR"
5. Ver orden de ejecución

### 💾 Memoria (Pestaña 9)
1. Ingresar PID: `2001`
2. Ingresar Tamaño: `256` MB
3. Clic "✅ Asignar"
4. Ver confirmación

### 📜 Logs (Pestaña 10)
- Ver todos los eventos
- Filtrar por nivel
- Exportar a archivo

### 📊 Estadísticas (Pestaña 11)
- Ver tiempo de actividad
- Contadores de actividades
- Descargar estadísticas

---

## Usuarios de Prueba

```
Usuario: admin
Contraseña: admin123

Usuario: user
Contraseña: user123
```

Para autenticarte:
1. Ir a pestaña "👤 Usuarios"
2. Ingresa credenciales
3. Clic "🔓 Login"

---

## Errores Comunes

**"ModuleNotFoundError: No module named 'tkinter'"**
- Tkinter viene con Python. Si tienes problema:
- macOS: `brew install python-tk`
- Ubuntu: `sudo apt-get install python3-tk`

**"ModuleNotFoundError: No module named 'psutil'"**
- Instala: `pip install psutil`

**"No aparecen periféricos"**
- Normal en algunos sistemas
- Psutil expone solo lo disponible

---

## Próximos Pasos

1. Explora cada pestaña
2. Lee la [DOCUMENTACION.md](DOCUMENTACION.md) completa
3. Intenta agregar nuevos usuarios
4. Modifica comandos en la terminal
5. Experimenta con el scheduler

---

## Consejos

✨ **Tip 1**: Usa los logs para entender qué está sucediendo
✨ **Tip 2**: Las estadísticas son útiles para ver el historial
✨ **Tip 3**: La terminal simulada es excelente para aprender comandos
✨ **Tip 4**: El scheduler muestra cómo funcionan los cambios de contexto

---

## ¿Necesitas ayuda?

- Lee [DOCUMENTACION.md](DOCUMENTACION.md) para más detalles
- Revisa [README.md](README_NUEVO.md) para características completas
- Explora el código fuente de cada módulo

---

¡Disfruta explorando! 🎓
