# 🖥️ Sistema Operativo Simulado - Versión 2.0

<div align="center">

![Python Version](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-Educativo-green.svg)
![Status](https://img.shields.io/badge/Status-Completo-success.svg)

**Una aplicación educativa interactiva que simula los conceptos fundamentales de Sistemas Operativos**

[Características](#características) • [Instalación](#instalación) • [Uso](#uso) • [Módulos](#módulos) • [Documentación](#documentación-completa)

</div>

---

## ✨ Características Principales

### 📊 Panel de Control
- Vista general del estado del sistema
- Accesos rápidos a todas las funcionalidades
- Información del usuario conectado

### ⚙️ Administrador de Recursos
- Monitoreo en tiempo real de CPU, memoria y almacenamiento
- Gestión de periféricos conectados
- Estadísticas en tiempo real

### 📁 Administrador de Archivos
- Crear, eliminar, copiar y pegar archivos
- Operaciones intuitivas de sistema de archivos
- Clipboard virtual

### 📋 Administrador de Tareas
- Listar procesos activos del sistema
- Terminar procesos específicos
- Monitoreo de PID

### 👤 Gestión de Usuarios
- Autenticación segura
- Login/Logout
- Registro de intentos de autenticación

### 🖥️ Terminal Simulada
- Interfaz de línea de comandos
- Comandos: `help`, `pwd`, `cd`, `ls`, `whoami`, `echo`, `date`, `clear`
- Historial de comandos

### ⏱️ Scheduling de Procesos
- Algoritmo Round Robin
- Simulación de cambio de contexto
- Visualización de ciclos de ejecución

### 📂 Administrador Avanzado de Archivos
- Sistema de directorios jerárquico
- Permisos de usuario
- Navegación entre directorios

### 💾 Gestión de Memoria
- Asignación y liberación de memoria
- Monitoreo de memoria virtual
- Simulación de memoria disponible

### 📜 Sistema de Logs
- Registro de todos los eventos
- Filtrado por niveles (INFO, WARNING, ERROR, SUCCESS)
- Exportación a archivo

### 📊 Estadísticas del Sistema
- Tiempo de actividad
- Contadores de actividades
- Promedios de recursos
- Descarga de estadísticas

---

## 🚀 Instalación Rápida

### Requisitos
- Python 3.7 o superior
- pip (gestor de paquetes)

### Pasos

```bash
# 1. Navega al directorio del proyecto
cd /path/to/Sistema-Operativo

# 2. Crea un entorno virtual (recomendado)
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# o
.venv\Scripts\activate  # Windows

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Ejecuta la aplicación
python main.py
```

---

## 📖 Uso

### Iniciar
```bash
python main.py
```

### Interfaz
La aplicación se abre con una interfaz gráfica con 11 pestañas:

1. **📊 Panel Control** - Inicio y accesos rápidos
2. **⚙️ Recursos** - Monitoreo de CPU, memoria, almacenamiento
3. **📁 Archivos** - Operaciones básicas de archivos
4. **📋 Tareas** - Gestión de procesos
5. **👤 Usuarios** - Autenticación
6. **🖥️ Terminal** - Línea de comandos simulada
7. **⏱️ Scheduling** - Algoritmo Round Robin
8. **📂 Archivos Avanzados** - Sistema jerárquico
9. **💾 Memoria** - Asignación de memoria
10. **📜 Logs** - Registro de eventos
11. **📊 Estadísticas** - Resumen del sistema

### Ejemplos de Uso

**Crear un archivo:**
1. Ir a la pestaña 📁 Archivos
2. Hacer clic en "➕ Crear"
3. Ingresar nombre: `documento.txt`
4. Hacer clic OK

**Ejecutar un comando:**
1. Ir a la pestaña 🖥️ Terminal
2. Escribir: `date`
3. Presionar Enter
4. Ver la fecha/hora actual

**Simular scheduling:**
1. Ir a la pestaña ⏱️ Scheduling
2. Agregar procesos con PID y tiempo de burst
3. Hacer clic "▶️ Ejecutar RR"
4. Ver orden de ejecución

---

## 📁 Estructura del Proyecto

```
Sistema-Operativo/
├── main.py                      # Aplicación principal
├── resource_manager.py          # Gestión de recursos
├── file_manager.py              # Operaciones de archivos
├── task_manager.py              # Gestión de procesos
├── user_manager.py              # Autenticación de usuarios
├── scheduler.py                 # Scheduling Round Robin
├── advanced_file_manager.py     # Sistema de directorios
├── memory_manager.py            # Gestión de memoria
├── terminal_simulator.py        # Terminal de comandos
├── system_logger.py             # Sistema de logs
├── system_stats.py              # Estadísticas del sistema
├── requirements.txt             # Dependencias
├── DOCUMENTACION.md             # Documentación detallada
└── README.md                    # Este archivo
```

---

## 🔧 Módulos

### main.py
Aplicación GUI principal que integra todos los módulos.

### resource_manager.py
Monitorea recursos del sistema usando psutil.

### file_manager.py
Gestión básica de archivos del sistema.

### task_manager.py
Lista y termina procesos activos.

### user_manager.py
Autenticación y gestión de usuarios.

### scheduler.py
Simula scheduling de procesos con Round Robin.

### advanced_file_manager.py
Sistema de archivos con directorios y permisos.

### memory_manager.py
Simula gestión de memoria virtual.

### terminal_simulator.py
Emula terminal de comandos básica.

### system_logger.py
Registra eventos del sistema.

### system_stats.py
Recopila estadísticas de uso.

---

## 🎨 Interfaz y Diseño

### Tema
- **Fondo**: Oscuro (#1e1e2e)
- **Texto**: Blanco (#ffffff)
- **Accento**: Púrpura (#7c3aed)
- **Éxito**: Verde (#10b981)
- **Advertencia**: Naranja (#f59e0b)
- **Error**: Rojo (#ef4444)

### Componentes
- Pestañas navegables
- Cuadros de diálogo para entrada
- Listas con scroll
- Áreas de texto con desplazamiento
- Botones de acción

---

## 📚 Conceptos de SO Demostrados

1. ✅ **Administración de Recursos** - Monitoreo de CPU, memoria, almacenamiento
2. ✅ **Gestión de Procesos** - Listar, terminar procesos
3. ✅ **Scheduling** - Algoritmo Round Robin
4. ✅ **Sistema de Archivos** - Crear, eliminar, copiar archivos
5. ✅ **Permisos y Seguridad** - Autenticación de usuarios
6. ✅ **Memoria Virtual** - Asignación y liberación
7. ✅ **Terminal** - Interfaz de línea de comandos
8. ✅ **Logging** - Registro de eventos

---

## ⚡ Comandos Disponibles en Terminal

```
help      # Muestra ayuda
pwd       # Directorio actual
cd <dir>  # Cambiar directorio
ls        # Listar archivos
whoami    # Usuario actual
echo <txt># Imprimir texto
date      # Fecha y hora
clear     # Limpiar terminal
```

---

## 🔐 Usuarios de Prueba

```
Usuario: admin
Contraseña: admin123

Usuario: user
Contraseña: user123
```

---

## ⚙️ Configuración

### Cambiar Quantum del Scheduler
En `scheduler.py`:
```python
self.quantum = 4  # Cambiar este valor
```

### Agregar Nuevos Usuarios
En `user_manager.py`:
```python
self.users = {
    "admin": "admin123",
    "nuevo_usuario": "contraseña123"
}
```

### Cambiar Colores del Tema
En `main.py`, función `setup_theme()`:
```python
bg_color = "#1e1e2e"        # Color de fondo
fg_color = "#ffffff"        # Color de texto
accent_color = "#7c3aed"    # Color de acento
```

---

## 🐛 Solución de Problemas

### Aplicación no inicia
```bash
# Verifica la versión de Python
python --version

# Instala dependencias
pip install -r requirements.txt
```

### Periféricos no aparecen
- Esto es normal en algunos sistemas
- psutil expone solo los periféricos disponibles

### Cómo exportar logs
1. Ir a 📜 Logs
2. Hacer clic "💾 Exportar"
3. Seleccionar ubicación y nombre

---

## 📈 Mejoras Futuras

- [ ] Más algoritmos de scheduling (FCFS, SJF, Priority)
- [ ] Sistema de archivos simulado (FAT, NTFS)
- [ ] Múltiples usuarios concurrentes
- [ ] Networking simulado
- [ ] Gráficos de uso en tiempo real
- [ ] Simulación de interrupciones
- [ ] Cache simulado

---

## 📝 Documentación Completa

Para documentación detallada, consulta [DOCUMENTACION.md](DOCUMENTACION.md)

---

## 👨‍💼 Autor

**Sistema Operativo Simulado v2.0**
Proyecto educativo para la clase de Sistemas Operativos

---

## 📄 Licencia

Proyecto educativo. Libre para uso académico.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para sugerencias o mejoras:

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

---

<div align="center">

**¡Disfruta aprendiendo Sistemas Operativos!** 🎓

Última actualización: Abril 2026 | v2.0 - Mejorado

</div>
