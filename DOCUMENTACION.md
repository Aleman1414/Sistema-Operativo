# Sistema Operativo Simulado - Documentación Completa

## 📋 Índice
1. [Descripción General](#descripción-general)
2. [Características](#características)
3. [Instalación](#instalación)
4. [Uso del Sistema](#uso-del-sistema)
5. [Módulos y Componentes](#módulos-y-componentes)
6. [Guía de Usuario](#guía-de-usuario)
7. [Arquitectura del Sistema](#arquitectura-del-sistema)
8. [FAQ y Solución de Problemas](#faq-y-solución-de-problemas)

---

## Descripción General

**Sistema Operativo Simulado** es una aplicación educativa desarrollada en **Python con Tkinter** que simula conceptos fundamentales de sistemas operativos. Está diseñada para estudiantes de Ingeniería en Sistemas y profesionales que deseen comprender mejor el funcionamiento interno de un sistema operativo.

### Objetivos
- 🎓 Demostrar conceptos clave de SO de manera interactiva
- 📊 Monitorear recursos del sistema en tiempo real
- 🔐 Implementar autenticación de usuarios
- 📁 Gestionar archivos y directorios
- ⏱️ Simular scheduling de procesos (Round Robin)
- 💾 Gestionar memoria virtual
- 📜 Registrar eventos del sistema en logs
- 📈 Recopilar estadísticas de uso

---

## Características

### 1. **Panel de Control** 📊
- Vista general del estado del sistema
- Información del usuario actual
- Accesos rápidos a todas las funcionalidades
- Estado del SO

### 2. **Administrador de Recursos** ⚙️
- Monitoreo en tiempo real de CPU
- Verificación de memoria disponible
- Control de almacenamiento
- Gestión de periféricos conectados

### 3. **Administrador de Archivos** 📁
- Crear archivos
- Eliminar archivos
- Copiar y pegar archivos
- Listado de archivos en el sistema

### 4. **Administrador de Tareas** 📋
- Listar procesos activos en el sistema
- Terminar procesos específicos
- Monitoreo de PID y nombre del proceso

### 5. **Gestión de Usuarios** 👤
- Autenticación de usuarios
- Login y Logout
- Manejo de credenciales
- Registro de intentos de autenticación

### 6. **Terminal Simulada** 🖥️
- Interfaz de línea de comandos simulada
- Comandos disponibles:
  - `help` - Muestra ayuda
  - `cd <dir>` - Cambia de directorio
  - `pwd` - Muestra directorio actual
  - `ls` - Lista archivos
  - `whoami` - Muestra usuario actual
  - `echo <texto>` - Imprime texto
  - `date` - Muestra fecha y hora
  - `clear` - Limpia el historial

### 7. **Scheduling de Procesos** ⏱️
- Algoritmo Round Robin
- Agregar procesos a la cola
- Ejecutar scheduling
- Visualización del ciclo de ejecución

### 8. **Administrador de Archivos Avanzado** 📂
- Crear directorios
- Navegar entre directorios
- Crear archivos en directorios específicos
- Eliminar archivos y directorios
- Control de permisos

### 9. **Gestión de Memoria** 💾
- Asignar memoria a procesos
- Desasignar memoria
- Monitoreo de memoria libre y usada
- Simulación de memoria virtual

### 10. **Sistema de Logs** 📜
- Registro de todos los eventos del sistema
- Filtrado por nivel (INFO, WARNING, ERROR, SUCCESS)
- Exportación de logs a archivo
- Visualización en tiempo real

### 11. **Estadísticas del Sistema** 📊
- Tiempo de actividad del sistema
- Contadores de actividades
- Promedios de CPU y memoria
- Descarga de estadísticas

---

## Instalación

### Requisitos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

#### 1. Clonar o descargar el proyecto
```bash
cd /path/to/Sistema-Operativo
```

#### 2. Crear un entorno virtual (recomendado)
```bash
python3 -m venv .venv
source .venv/bin/activate  # En macOS/Linux
# o
.venv\Scripts\activate  # En Windows
```

#### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

#### 4. Ejecutar la aplicación
```bash
python main.py
```

### Dependencias del Proyecto
```
tkinter (incluido con Python)
psutil>=5.9.0
```

---

## Uso del Sistema

### Iniciar la Aplicación
```bash
python main.py
```

### Interfaz Principal
La aplicación se abre con una ventana de 1000x700 píxeles con las siguientes áreas:
- **Barra de pestañas**: Acceso a cada módulo
- **Área de contenido**: Controles específicos de cada pestaña
- **Botones de acción**: Ejecutar operaciones

### Navegación
- Hacer clic en las pestañas para cambiar de módulo
- Usar botones dentro de cada pestaña para ejecutar acciones
- Los mensajes de error/éxito aparecen en cuadros de diálogo

---

## Módulos y Componentes

### 1. **main.py**
**Función**: Archivo principal que integra todos los módulos
**Contiene**:
- Clase `SimulatedOS`: Aplicación GUI principal
- Función `setup_theme()`: Configuración de colores y estilos
- Métodos para cada pestaña

**Estructura**:
```python
class SimulatedOS:
    - __init__(): Inicialización
    - create_dashboard_tab()
    - create_resource_tab()
    - create_file_tab()
    - create_task_tab()
    - create_user_tab()
    - create_terminal_tab()
    - create_scheduler_tab()
    - create_adv_file_tab()
    - create_memory_tab()
    - create_logs_tab()
    - create_stats_tab()
```

### 2. **resource_manager.py**
**Función**: Monitorear recursos del sistema
**Clases**:
- `ResourceManager`

**Métodos principales**:
- `get_cpu_usage()`: Retorna porcentaje de CPU utilizado
- `get_memory_usage()`: Retorna memoria usada y total
- `get_storage_usage()`: Retorna almacenamiento usado y total
- `get_peripherals()`: Lista periféricos del sistema

### 3. **file_manager.py**
**Función**: Gestión básica de archivos
**Clases**:
- `FileManager`

**Métodos principales**:
- `create_file(name)`: Crea un archivo
- `delete_file(name)`: Elimina un archivo
- `copy_file(source, dest)`: Copia un archivo
- `list_files()`: Lista todos los archivos

### 4. **task_manager.py**
**Función**: Gestión de procesos del sistema
**Clases**:
- `TaskManager`

**Métodos principales**:
- `list_processes()`: Lista procesos activos
- `kill_process(pid)`: Termina un proceso por PID
- `get_process_info(pid)`: Obtiene información de un proceso

### 5. **user_manager.py**
**Función**: Autenticación y gestión de usuarios
**Clases**:
- `UserManager`

**Métodos principales**:
- `login(username, password)`: Autentica un usuario
- `logout()`: Cierra sesión del usuario
- `has_permission(action)`: Verifica permisos
- `add_user(username, password)`: Agrega nuevo usuario

### 6. **scheduler.py**
**Función**: Simula scheduling de procesos con Round Robin
**Clases**:
- `Scheduler`

**Métodos principales**:
- `add_process(pid, burst_time)`: Agrega proceso a la cola
- `run_round_robin(quantum=4)`: Ejecuta algoritmo RR
- `get_queue()`: Obtiene cola de procesos

### 7. **advanced_file_manager.py**
**Función**: Sistema de archivos avanzado con directorios y permisos
**Clases**:
- `AdvancedFileManager`

**Métodos principales**:
- `create_directory(name)`: Crea directorio
- `change_directory(name)`: Cambia directorio actual
- `create_file(name)`: Crea archivo en directorio actual
- `delete_file(name)`: Elimina archivo
- `list_directory()`: Lista contenido del directorio

### 8. **memory_manager.py**
**Función**: Simulación de gestión de memoria
**Clases**:
- `MemoryManager`

**Métodos principales**:
- `allocate(pid, size)`: Asigna memoria a proceso
- `deallocate(pid)`: Libera memoria de proceso
- `get_memory_status()`: Estado de memoria
- `get_allocated_memory(pid)`: Obtiene memoria asignada

### 9. **terminal_simulator.py** (NUEVO)
**Función**: Simula terminal de comandos
**Clases**:
- `TerminalSimulator`

**Métodos principales**:
- `execute(command)`: Ejecuta comando
- `get_history()`: Obtiene historial
- `cmd_help()`, `cmd_cd()`, `cmd_pwd()`: Comandos específicos

### 10. **system_logger.py** (NUEVO)
**Función**: Registra eventos del sistema
**Clases**:
- `SystemLogger`

**Métodos principales**:
- `log(level, message)`: Registra evento
- `info()`, `warning()`, `error()`, `success()`: Métodos específicos
- `get_logs(level, limit)`: Obtiene logs filtrados
- `export_logs()`: Exporta logs a texto

### 11. **system_stats.py** (NUEVO)
**Función**: Recopila estadísticas del sistema
**Clases**:
- `SystemStats`

**Métodos principales**:
- `increment_stat(name)`: Incrementa contador
- `get_summary()`: Resumen de estadísticas
- `get_average_cpu()`, `get_average_memory()`: Promedios
- `get_uptime()`: Tiempo de actividad

---

## Guía de Usuario

### Administrador de Recursos
**¿Cómo verificar CPU?**
1. Ir a pestaña "⚙️ Recursos"
2. Hacer clic en botón "Actualizar" junto a CPU
3. Ver resultado en etiqueta de CPU

**¿Cómo ver periféricos?**
1. Ir a pestaña "⚙️ Recursos"
2. Hacer clic en "Listar"
3. Ver lista de periféricos

### Administrador de Archivos
**¿Cómo crear archivo?**
1. Ir a pestaña "📁 Archivos"
2. Hacer clic en "➕ Crear"
3. Ingresar nombre del archivo
4. Hacer clic OK

**¿Cómo copiar y pegar?**
1. Seleccionar archivo
2. Hacer clic en "📋 Copiar"
3. Hacer clic en "📌 Pegar"
4. Ingresar nuevo nombre

### Terminal Simulada
**¿Cómo ejecutar comando?**
1. Ir a pestaña "🖥️ Terminal"
2. Escribir comando en caja de entrada
3. Presionar Enter o hacer clic "Ejecutar"
4. Ver resultado en pantalla

**Comandos disponibles**:
```
help     - Muestra todos los comandos
pwd      - Muestra directorio actual
cd /home - Cambia a /home
ls       - Lista archivos
whoami   - Muestra usuario actual
echo hola - Imprime "hola"
date     - Muestra hora actual
clear    - Limpia terminal
```

### Scheduling
**¿Cómo agregar proceso?**
1. Ir a pestaña "⏱️ Scheduling"
2. Ingresar PID (ej: 1001)
3. Ingresar tiempo de Burst (ej: 10)
4. Hacer clic "➕ Agregar"

**¿Cómo ejecutar Round Robin?**
1. Agregar múltiples procesos
2. Hacer clic "▶️ Ejecutar RR"
3. Ver orden de ejecución en log

### Gestión de Memoria
**¿Cómo asignar memoria?**
1. Ir a pestaña "💾 Memoria"
2. Ingresar PID del proceso
3. Ingresar tamaño en MB
4. Hacer clic "✅ Asignar"

**¿Cómo liberar memoria?**
1. Ingresar PID
2. Hacer clic "❌ Desasignar"

### Logs del Sistema
**¿Cómo ver todos los logs?**
1. Ir a pestaña "📜 Logs"
2. Hacer clic "📋 Todos"
3. Ver lista de eventos

**¿Cómo filtrar logs?**
1. Hacer clic en botón de nivel deseado
2. Ver solo logs de ese nivel

**¿Cómo exportar logs?**
1. Hacer clic "💾 Exportar"
2. Seleccionar ubicación
3. Ingresar nombre de archivo

---

## Arquitectura del Sistema

### Flujo de Datos
```
┌─────────────────────────┐
│   GUI (Tkinter)         │
│   (main.py)             │
└────────────┬────────────┘
             │
    ┌────────┴────────┐
    │                 │
┌───▼──────┐  ┌──────▼──────┐
│ Managers │  │   Utilities   │
└──────────┘  └──────────────┘
    │
    ├─ ResourceManager
    ├─ FileManager
    ├─ TaskManager
    ├─ UserManager
    ├─ Scheduler
    ├─ AdvancedFileManager
    ├─ MemoryManager
    ├─ TerminalSimulator
    ├─ SystemLogger
    └─ SystemStats
```

### Interacción de Módulos

1. **Usuario interactúa con GUI** (main.py)
2. **GUI llama métodos** de managers específicos
3. **Managers procesan** solicitud
4. **SystemLogger registra** evento
5. **SystemStats actualiza** contadores
6. **GUI actualiza** con resultado

---

## FAQ y Solución de Problemas

### P: ¿La aplicación no inicia?
**R**: Asegúrate de tener Python 3.7+ instalado:
```bash
python --version
```
Instala dependencias:
```bash
pip install -r requirements.txt
```

### P: ¿Cómo cambiar el tema de colores?
**R**: Edita la función `setup_theme()` en main.py y cambia los valores HEX de los colores.

### P: ¿Por qué no aparecen los periféricos?
**R**: Algunos sistemas no exponen todos los periféricos. Esto es una limitación de psutil. El sistema mostrará lo disponible.

### P: ¿Cómo agregar más usuarios?
**R**: Edita `user_manager.py` y agrega usuarios en el método `__init__()`:
```python
self.users = {
    "admin": "admin123",
    "nuevo_usuario": "contraseña"
}
```

### P: ¿Puedo agregar más comandos a la terminal?
**R**: Sí, edita `terminal_simulator.py`:
1. Agrega método `cmd_nombre(args)`
2. Agrega comando al diccionario en `__init__()`

### P: ¿Cómo cambiar el quantum del Round Robin?
**R**: En `scheduler.py`, busca y modifica la línea:
```python
self.quantum = 4  # Cambia este valor
```

### P: ¿Los logs persisten después de cerrar?
**R**: Por defecto, no. Para que persistan, agrega código para guardarlos en archivo.

---

## Conceptos de Sistemas Operativos Demostrados

1. **Administración de Recursos**: Monitoreo de CPU, memoria, almacenamiento
2. **Gestión de Procesos**: Listar y terminar procesos
3. **Scheduling**: Algoritmo Round Robin
4. **Administración de Archivos**: Crear, eliminar, copiar archivos
5. **Sistema de Permisos**: Control de acceso a usuarios
6. **Memoria Virtual**: Asignación y liberación de memoria
7. **Terminal**: Interfaz de línea de comandos
8. **Logging**: Registro de eventos del sistema

---

## Contribuciones y Mejoras Futuras

### Ideas para Expansión
- [ ] Agregar más algoritmos de scheduling (FCFS, SJF, Priority)
- [ ] Implementar sistema de archivos con FAT o NTFS simulado
- [ ] Agregar soporte para múltiples usuarios simultáneos
- [ ] Crear módulo de networking simulado
- [ ] Exportar/importar configuraciones
- [ ] Interfaz gráfica mejorada con gráficos de uso
- [ ] Simulación de interrupciones del sistema
- [ ] Cache simulado

---

## Licencia
Este proyecto es educativo y está disponible libremente para fines académicos.

---

## Contacto y Soporte
Para preguntas o sugerencias, contacta al desarrollador o revisa la documentación del código.

---

**Última actualización**: Abril 2026
**Versión**: 2.0 (Mejorada)
**Estado**: Completo y funcional
