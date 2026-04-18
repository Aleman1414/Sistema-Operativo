# Sistema Operativo Simulado - Versión Mejorada
# Proyecto para clase de Sistemas Operativos

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, scrolledtext
import resource_manager
import file_manager
import task_manager
import user_manager
import scheduler
import advanced_file_manager
import memory_manager
import terminal_simulator
import system_logger
import system_stats

# Configurar tema personalizado
def setup_theme(root):
    """Configura el tema visual de la aplicación"""
    style = ttk.Style()
    style.theme_use('clam')
    
    # Colores
    bg_color = "#1e1e2e"
    fg_color = "#ffffff"
    accent_color = "#7c3aed"
    success_color = "#10b981"
    warning_color = "#f59e0b"
    error_color = "#ef4444"
    
    # Configurar colores del tema
    style.configure('TFrame', background=bg_color)
    style.configure('TLabel', background=bg_color, foreground=fg_color)
    style.configure('TButton', background=accent_color, foreground=fg_color)
    style.map('TButton', background=[('active', '#6d28d9')])
    style.configure('TNotebook', background=bg_color)
    style.configure('TNotebook.Tab', padding=[20, 10])
    style.configure('Accent.TLabel', background=bg_color, foreground=accent_color, font=('Helvetica', 10, 'bold'))
    style.configure('Success.TLabel', background=bg_color, foreground=success_color)
    style.configure('Warning.TLabel', background=bg_color, foreground=warning_color)
    style.configure('Error.TLabel', background=bg_color, foreground=error_color)
    
    root.configure(bg=bg_color)

class SimulatedOS:
    def __init__(self, root):
        self.root = root
        self.root.title("🖥️  Sistema Operativo Simulado - Versión Educativa")
        self.root.geometry("1000x700")
        
        setup_theme(root)
        
        # Crear notebook para pestañas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Inicializar managers
        self.resource_mgr = resource_manager.ResourceManager()
        self.file_mgr = file_manager.FileManager()
        self.task_mgr = task_manager.TaskManager()
        self.user_mgr = user_manager.UserManager()
        self.scheduler = scheduler.Scheduler()
        self.adv_file_mgr = advanced_file_manager.AdvancedFileManager(self.user_mgr)
        self.memory_mgr = memory_manager.MemoryManager()
        self.terminal = terminal_simulator.TerminalSimulator()
        self.logger = system_logger.SystemLogger()
        self.stats = system_stats.SystemStats()
        
        # Crear pestañas
        self.create_dashboard_tab()
        self.create_resource_tab()
        self.create_file_tab()
        self.create_task_tab()
        self.create_user_tab()
        self.create_terminal_tab()
        self.create_scheduler_tab()
        self.create_adv_file_tab()
        self.create_memory_tab()
        self.create_logs_tab()
        self.create_stats_tab()
        
        # Registrar evento inicial
        self.logger.success("Sistema operativo iniciado correctamente")
        self.stats.increment_stat("processes_created")
    
    def create_dashboard_tab(self):
        """Pestaña de panel de control"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="📊 Panel Control")
        
        # Marco superior con información del sistema
        info_frame = ttk.LabelFrame(tab, text="Estado del Sistema", padding=10)
        info_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Información del sistema
        sys_info = [
            ("Usuario:", "admin"),
            ("Estado:", "En ejecución ✓"),
            ("Procesos activos:", "0"),
            ("Memoria total:", "4 GB"),
            ("Almacenamiento:", "100 GB")
        ]
        
        for i, (label, value) in enumerate(sys_info):
            ttk.Label(info_frame, text=label, style='Accent.TLabel').grid(row=i, column=0, sticky=tk.W, padx=5, pady=3)
            ttk.Label(info_frame, text=value).grid(row=i, column=1, sticky=tk.W, padx=5, pady=3)
        
        # Marco de accesos rápidos
        quick_frame = ttk.LabelFrame(tab, text="Accesos Rápidos", padding=10)
        quick_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        quick_buttons = [
            ("📁 Administrador de Archivos", 1),
            ("⚙️  Administrador de Recursos", 2),
            ("📋 Administrador de Tareas", 3),
            ("👤 Administración de Usuarios", 4),
            ("🖥️  Terminal Simulada", 6),
            ("📊 Estadísticas", 11)
        ]
        
        for i, (text, tab_idx) in enumerate(quick_buttons):
            btn = ttk.Button(quick_frame, text=text, 
                           command=lambda idx=tab_idx: self.notebook.select(idx))
            btn.grid(row=i//2, column=i%2, padx=5, pady=5, sticky=tk.EW)

    def create_resource_tab(self):
        """Pestaña Administración de Recursos"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="⚙️  Recursos")
        
        # Marco de monitoreo
        monitor_frame = ttk.LabelFrame(tab, text="Monitoreo de Recursos", padding=10)
        monitor_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # CPU
        ttk.Label(monitor_frame, text="📊 CPU:", style='Accent.TLabel').grid(row=0, column=0, sticky=tk.W, pady=5)
        self.cpu_label = ttk.Label(monitor_frame, text="0%")
        self.cpu_label.grid(row=0, column=1, sticky=tk.EW, padx=10)
        cpu_btn = ttk.Button(monitor_frame, text="Actualizar", command=self.update_cpu)
        cpu_btn.grid(row=0, column=2, padx=5)
        
        # Memoria
        ttk.Label(monitor_frame, text="💾 Memoria:", style='Accent.TLabel').grid(row=1, column=0, sticky=tk.W, pady=5)
        self.mem_label = ttk.Label(monitor_frame, text="0 MB / 0 MB")
        self.mem_label.grid(row=1, column=1, sticky=tk.EW, padx=10)
        mem_btn = ttk.Button(monitor_frame, text="Actualizar", command=self.update_memory)
        mem_btn.grid(row=1, column=2, padx=5)
        
        # Almacenamiento
        ttk.Label(monitor_frame, text="💿 Almacenamiento:", style='Accent.TLabel').grid(row=2, column=0, sticky=tk.W, pady=5)
        self.storage_label = ttk.Label(monitor_frame, text="0 GB / 0 GB")
        self.storage_label.grid(row=2, column=1, sticky=tk.EW, padx=10)
        storage_btn = ttk.Button(monitor_frame, text="Actualizar", command=self.update_storage)
        storage_btn.grid(row=2, column=2, padx=5)
        
        # Periféricos
        ttk.Label(monitor_frame, text="🖱️  Periféricos:", style='Accent.TLabel').grid(row=3, column=0, sticky=tk.W, pady=5)
        self.peripherals_list = tk.Listbox(monitor_frame, height=5, bg="#2e2e3e", fg="#ffffff")
        self.peripherals_list.grid(row=3, column=1, columnspan=2, sticky=tk.EW, padx=10, pady=5)
        periph_btn = ttk.Button(monitor_frame, text="Listar", command=self.list_peripherals)
        periph_btn.grid(row=4, column=1, padx=5, pady=5, sticky=tk.EW)
        
        monitor_frame.columnconfigure(1, weight=1)

    def update_cpu(self):
        usage = self.resource_mgr.get_cpu_usage()
        self.cpu_label.config(text=f"{usage}%")
        self.logger.info(f"CPU verificada: {usage}%")
        self.stats.add_cpu_sample()
    
    def update_memory(self):
        used, total = self.resource_mgr.get_memory_usage()
        self.mem_label.config(text=f"{used} MB / {total} MB")
        self.logger.info(f"Memoria verificada: {used}/{total} MB")
        self.stats.add_memory_sample()
    
    def update_storage(self):
        used, total = self.resource_mgr.get_storage_usage()
        self.storage_label.config(text=f"{used} GB / {total} GB")
        self.logger.info(f"Almacenamiento verificado: {used}/{total} GB")
    
    def list_peripherals(self):
        peripherals = self.resource_mgr.get_peripherals()
        self.peripherals_list.delete(0, tk.END)
        for p in peripherals:
            self.peripherals_list.insert(tk.END, f"🔌 {p}")
        self.logger.info("Periféricos listados")

    def create_file_tab(self):
        """Pestaña Administración de Archivos"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="📁 Archivos")
        
        # Marco de herramientas
        tool_frame = ttk.Frame(tab)
        tool_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(tool_frame, text="➕ Crear", command=self.create_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(tool_frame, text="🗑️  Borrar", command=self.delete_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(tool_frame, text="📋 Copiar", command=self.copy_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(tool_frame, text="📌 Pegar", command=self.paste_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(tool_frame, text="🔄 Actualizar", command=self.list_files).pack(side=tk.LEFT, padx=2)
        
        # Lista de archivos
        self.file_list = tk.Listbox(tab, bg="#2e2e3e", fg="#ffffff")
        self.file_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.clipboard = None

    def create_file(self):
        name = simpledialog.askstring("Crear Archivo", "Nombre del archivo:")
        if not name:
            messagebox.showerror("Error", "Nombre requerido")
            return
        try:
            self.file_mgr.create_file(name)
            self.stats.increment_stat("files_created")
            self.logger.success(f"Archivo creado: {name}")
            self.list_files()
        except Exception as e:
            self.logger.error(f"Error al crear archivo: {str(e)}")
            messagebox.showerror("Error", str(e))

    def delete_file(self):
        selected = self.file_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Selecciona un archivo")
            return
        name = self.file_list.get(selected[0])
        try:
            self.file_mgr.delete_file(name)
            self.stats.increment_stat("files_deleted")
            self.logger.success(f"Archivo eliminado: {name}")
            self.list_files()
        except Exception as e:
            self.logger.error(f"Error al eliminar archivo: {str(e)}")
            messagebox.showerror("Error", str(e))

    def copy_file(self):
        selected = self.file_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Selecciona un archivo")
            return
        self.clipboard = self.file_list.get(selected[0])
        self.logger.info(f"Archivo copiado: {self.clipboard}")
        messagebox.showinfo("Éxito", f"Archivo '{self.clipboard}' copiado")

    def paste_file(self):
        if not self.clipboard:
            messagebox.showerror("Error", "No hay archivo copiado")
            return
        name = simpledialog.askstring("Pegar Archivo", "Nuevo nombre:")
        if not name:
            return
        try:
            self.file_mgr.copy_file(self.clipboard, name)
            self.logger.success(f"Archivo pegado: {name}")
            self.list_files()
        except Exception as e:
            self.logger.error(f"Error al pegar archivo: {str(e)}")
            messagebox.showerror("Error", str(e))

    def list_files(self):
        try:
            files = self.file_mgr.list_files()
            self.file_list.delete(0, tk.END)
            for f in files:
                self.file_list.insert(tk.END, f"📄 {f}")
            self.logger.info(f"Archivos listados: {len(files)} encontrados")
        except Exception as e:
            self.logger.error(f"Error al listar archivos: {str(e)}")
            messagebox.showerror("Error", str(e))

    def create_task_tab(self):
        """Pestaña Administración de Tareas"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="📋 Tareas")
        
        # Marco de herramientas
        tool_frame = ttk.Frame(tab)
        tool_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(tool_frame, text="🔄 Listar Procesos", command=self.list_processes).pack(side=tk.LEFT, padx=5)
        ttk.Button(tool_frame, text="🛑 Matar Proceso", command=self.kill_process).pack(side=tk.LEFT, padx=5)
        
        # Lista de procesos
        self.process_list = tk.Listbox(tab, bg="#2e2e3e", fg="#ffffff")
        self.process_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def list_processes(self):
        try:
            processes = self.task_mgr.list_processes()
            self.process_list.delete(0, tk.END)
            for p in processes:
                self.process_list.insert(tk.END, f"⚙️  PID {p['pid']}: {p['name']}")
            self.logger.info(f"Procesos listados: {len(processes)}")
        except Exception as e:
            self.logger.error(f"Error al listar procesos: {str(e)}")
            messagebox.showerror("Error", str(e))

    def kill_process(self):
        selected = self.process_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Selecciona un proceso")
            return
        item = self.process_list.get(selected[0])
        try:
            pid = int(item.split()[1])
            self.task_mgr.kill_process(pid)
            self.logger.success(f"Proceso terminado: PID {pid}")
            self.list_processes()
        except Exception as e:
            self.logger.error(f"Error al matar proceso: {str(e)}")
            messagebox.showerror("Error", str(e))

    def create_user_tab(self):
        """Pestaña Administración de Usuarios"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="👤 Usuarios")
        
        # Marco de login
        login_frame = ttk.LabelFrame(tab, text="Autenticación", padding=15)
        login_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(login_frame, text="Usuario:", style='Accent.TLabel').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.username_entry = ttk.Entry(login_frame, width=30)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(login_frame, text="Contraseña:", style='Accent.TLabel').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.password_entry = ttk.Entry(login_frame, show="*", width=30)
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)
        
        button_frame = ttk.Frame(login_frame)
        button_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
        ttk.Button(button_frame, text="🔓 Login", command=self.login).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="🔒 Logout", command=self.logout).pack(side=tk.LEFT, padx=5)
        
        # Estado de usuario
        status_frame = ttk.LabelFrame(tab, text="Estado", padding=15)
        status_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(status_frame, text="Usuario actual:", style='Accent.TLabel').grid(row=0, column=0, sticky=tk.W, padx=5)
        self.current_user_label = ttk.Label(status_frame, text="Ninguno", style='Warning.TLabel')
        self.current_user_label.grid(row=0, column=1, sticky=tk.W, padx=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.stats.increment_stat("login_attempts")
        
        if not username or not password:
            self.logger.error("Intento de login sin credenciales")
            messagebox.showerror("Error", "Usuario y contraseña requeridos")
            return
        
        if self.user_mgr.login(username, password):
            self.current_user_label.config(text=username, style='Success.TLabel')
            self.stats.increment_stat("successful_logins")
            self.logger.success(f"Usuario '{username}' autenticado")
            messagebox.showinfo("Éxito", f"¡Bienvenido, {username}!")
        else:
            self.stats.increment_stat("failed_logins")
            self.logger.warning(f"Intento de login fallido para '{username}'")
            messagebox.showerror("Error", "Credenciales incorrectas")

    def logout(self):
        self.user_mgr.logout()
        self.current_user_label.config(text="Ninguno", style='Warning.TLabel')
        self.logger.success("Usuario desconectado")
        messagebox.showinfo("Éxito", "Sesión cerrada")

    def create_terminal_tab(self):
        """Pestaña Terminal Simulada"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="🖥️  Terminal")
        
        # Marco de entrada
        input_frame = ttk.Frame(tab)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(input_frame, text="$", style='Accent.TLabel').pack(side=tk.LEFT, padx=5)
        self.terminal_input = ttk.Entry(input_frame)
        self.terminal_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.terminal_input.bind('<Return>', lambda e: self.execute_terminal_command())
        ttk.Button(input_frame, text="Ejecutar", command=self.execute_terminal_command).pack(side=tk.LEFT, padx=5)
        ttk.Button(input_frame, text="Limpiar", command=self.clear_terminal).pack(side=tk.LEFT, padx=5)
        
        # Salida de terminal
        self.terminal_output = scrolledtext.ScrolledText(tab, height=15, bg="#1a1a2e", fg="#00ff00", font=("Courier", 9))
        self.terminal_output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.terminal_output.config(state=tk.DISABLED)
    
    def execute_terminal_command(self):
        command = self.terminal_input.get()
        if not command.strip():
            return
        
        output = self.terminal.execute(command)
        self.terminal_input.delete(0, tk.END)
        
        self.terminal_output.config(state=tk.NORMAL)
        self.terminal_output.insert(tk.END, f"$ {command}\n")
        self.terminal_output.insert(tk.END, f"{output}\n\n")
        self.terminal_output.config(state=tk.DISABLED)
        self.terminal_output.see(tk.END)
        
        self.logger.info(f"Comando ejecutado: {command}")
    
    def clear_terminal(self):
        self.terminal_output.config(state=tk.NORMAL)
        self.terminal_output.delete(1.0, tk.END)
        self.terminal_output.config(state=tk.DISABLED)
        self.logger.info("Terminal limpiada")
    
    def create_scheduler_tab(self):
        """Pestaña Scheduling"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="⏱️  Scheduling")
        
        # Marco de entrada
        input_frame = ttk.LabelFrame(tab, text="Agregar Proceso", padding=10)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(input_frame, text="PID:", style='Accent.TLabel').grid(row=0, column=0, sticky=tk.W, padx=5)
        self.pid_entry = ttk.Entry(input_frame)
        self.pid_entry.grid(row=0, column=1, padx=5)
        
        ttk.Label(input_frame, text="Tiempo de Burst:", style='Accent.TLabel').grid(row=1, column=0, sticky=tk.W, padx=5)
        self.burst_entry = ttk.Entry(input_frame)
        self.burst_entry.grid(row=1, column=1, padx=5)
        
        ttk.Button(input_frame, text="➕ Agregar", command=self.add_process).grid(row=2, column=0, padx=5, pady=10)
        ttk.Button(input_frame, text="▶️  Ejecutar RR", command=self.run_scheduler).grid(row=2, column=1, padx=5, pady=10)
        
        # Log de scheduling
        self.sched_log = scrolledtext.ScrolledText(tab, height=15, bg="#2e2e3e", fg="#ffffff")
        self.sched_log.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def add_process(self):
        try:
            pid = int(self.pid_entry.get())
            burst = int(self.burst_entry.get())
            if pid <= 0 or burst <= 0:
                raise ValueError("Los valores deben ser positivos")
            self.scheduler.add_process(pid, burst)
            self.logger.success(f"Proceso {pid} agregado al scheduler")
            messagebox.showinfo("Éxito", f"Proceso {pid} agregado")
        except ValueError as e:
            self.logger.error(f"Error al agregar proceso: {str(e)}")
            messagebox.showerror("Error", f"Error: {str(e)}")
    
    def run_scheduler(self):
        log = self.scheduler.run_round_robin()
        self.sched_log.delete(1.0, tk.END)
        for entry in log:
            self.sched_log.insert(tk.END, entry + "\n")
        self.logger.success("Scheduling Round Robin ejecutado")

    def create_adv_file_tab(self):
        """Pestaña Archivos Avanzados"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="📂 Archivos Avanzados")
        
        # Marco de información
        info_frame = ttk.Frame(tab)
        info_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(info_frame, text="📂 Directorio:", style='Accent.TLabel').pack(side=tk.LEFT, padx=5)
        self.current_dir_label = ttk.Label(info_frame, text="root")
        self.current_dir_label.pack(side=tk.LEFT, padx=5)
        
        # Marco de herramientas
        tool_frame = ttk.Frame(tab)
        tool_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(tool_frame, text="📁 Nueva Carpeta", command=self.create_dir).pack(side=tk.LEFT, padx=2)
        ttk.Button(tool_frame, text="🔙 Cambiar Dir", command=self.change_dir).pack(side=tk.LEFT, padx=2)
        ttk.Button(tool_frame, text="📄 Crear Archivo", command=self.create_file_adv).pack(side=tk.LEFT, padx=2)
        ttk.Button(tool_frame, text="🗑️  Borrar", command=self.delete_file_adv).pack(side=tk.LEFT, padx=2)
        ttk.Button(tool_frame, text="🔄 Actualizar", command=self.list_dir).pack(side=tk.LEFT, padx=2)
        
        # Lista
        self.adv_file_list = tk.Listbox(tab, bg="#2e2e3e", fg="#ffffff")
        self.adv_file_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def create_dir(self):
        name = simpledialog.askstring("Crear Directorio", "Nombre:")
        if not name:
            return
        try:
            self.adv_file_mgr.create_directory(name)
            self.logger.success(f"Directorio creado: {name}")
            self.list_dir()
        except Exception as e:
            self.logger.error(f"Error al crear directorio: {str(e)}")
            messagebox.showerror("Error", str(e))

    def change_dir(self):
        selected = self.adv_file_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Selecciona un directorio")
            return
        name = self.adv_file_list.get(selected[0]).replace("📁 ", "")
        try:
            self.adv_file_mgr.change_directory(name)
            self.current_dir_label.config(text=self.adv_file_mgr.current_dir)
            self.logger.success(f"Directorio cambiado a: {name}")
            self.list_dir()
        except Exception as e:
            self.logger.error(f"Error al cambiar directorio: {str(e)}")
            messagebox.showerror("Error", str(e))

    def create_file_adv(self):
        name = simpledialog.askstring("Crear Archivo", "Nombre:")
        if not name:
            return
        try:
            self.adv_file_mgr.create_file(name)
            self.logger.success(f"Archivo creado: {name}")
            self.list_dir()
        except Exception as e:
            self.logger.error(f"Error al crear archivo: {str(e)}")
            messagebox.showerror("Error", str(e))

    def delete_file_adv(self):
        selected = self.adv_file_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Selecciona un archivo")
            return
        name = self.adv_file_list.get(selected[0]).replace("📁 ", "").replace("📄 ", "")
        try:
            self.adv_file_mgr.delete_file(name)
            self.logger.success(f"Archivo eliminado: {name}")
            self.list_dir()
        except Exception as e:
            self.logger.error(f"Error al eliminar archivo: {str(e)}")
            messagebox.showerror("Error", str(e))

    def list_dir(self):
        try:
            files = self.adv_file_mgr.list_directory()
            self.adv_file_list.delete(0, tk.END)
            for f in files:
                icon = "📁 " if f.endswith("/") else "📄 "
                self.adv_file_list.insert(tk.END, icon + f)
            self.logger.info(f"Directorio listado: {len(files)} elementos")
        except Exception as e:
            self.logger.error(f"Error al listar directorio: {str(e)}")
            messagebox.showerror("Error", str(e))

    def create_memory_tab(self):
        """Pestaña Gestión de Memoria"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="💾 Memoria")
        
        # Marco de estado
        state_frame = ttk.LabelFrame(tab, text="Estado de Memoria", padding=10)
        state_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(state_frame, text="Memoria Usada:", style='Accent.TLabel').grid(row=0, column=0, sticky=tk.W, padx=5)
        self.mem_used_label = ttk.Label(state_frame, text="0 MB")
        self.mem_used_label.grid(row=0, column=1, sticky=tk.W, padx=5)
        
        ttk.Label(state_frame, text="Memoria Libre:", style='Accent.TLabel').grid(row=1, column=0, sticky=tk.W, padx=5)
        self.mem_free_label = ttk.Label(state_frame, text="1024 MB")
        self.mem_free_label.grid(row=1, column=1, sticky=tk.W, padx=5)
        
        ttk.Button(state_frame, text="🔄 Actualizar", command=self.update_memory_status).grid(row=2, column=0, padx=5, pady=10)
        
        # Marco de asignación
        alloc_frame = ttk.LabelFrame(tab, text="Asignar/Desasignar Memoria", padding=10)
        alloc_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(alloc_frame, text="PID:", style='Accent.TLabel').grid(row=0, column=0, sticky=tk.W, padx=5)
        self.mem_pid_entry = ttk.Entry(alloc_frame)
        self.mem_pid_entry.grid(row=0, column=1, padx=5)
        
        ttk.Label(alloc_frame, text="Tamaño (MB):", style='Accent.TLabel').grid(row=1, column=0, sticky=tk.W, padx=5)
        self.mem_size_entry = ttk.Entry(alloc_frame)
        self.mem_size_entry.grid(row=1, column=1, padx=5)
        
        ttk.Button(alloc_frame, text="✅ Asignar", command=self.allocate_memory).grid(row=2, column=0, padx=5, pady=10)
        ttk.Button(alloc_frame, text="❌ Desasignar", command=self.deallocate_memory).grid(row=2, column=1, padx=5, pady=10)

    def update_memory_status(self):
        try:
            used, free, total = self.memory_mgr.get_memory_status()
            self.mem_used_label.config(text=f"{used} MB")
            self.mem_free_label.config(text=f"{free} MB")
            self.logger.info(f"Memoria verificada: {used}/{total} MB")
        except Exception as e:
            self.logger.error(f"Error al verificar memoria: {str(e)}")

    def allocate_memory(self):
        try:
            pid = int(self.mem_pid_entry.get())
            size = int(self.mem_size_entry.get())
            if pid <= 0 or size <= 0:
                raise ValueError("Los valores deben ser positivos")
            if self.memory_mgr.allocate(pid, size):
                self.stats.increment_stat("memory_allocations")
                self.logger.success(f"Memoria asignada: {size} MB al PID {pid}")
                messagebox.showinfo("Éxito", f"Memoria asignada a PID {pid}")
                self.update_memory_status()
            else:
                self.logger.warning("No hay suficiente memoria disponible")
                messagebox.showerror("Error", "No hay suficiente memoria")
        except ValueError as e:
            self.logger.error(f"Error de entrada: {str(e)}")
            messagebox.showerror("Error", f"Error: {str(e)}")

    def deallocate_memory(self):
        try:
            pid = int(self.mem_pid_entry.get())
            self.memory_mgr.deallocate(pid)
            self.stats.increment_stat("memory_deallocations")
            self.logger.success(f"Memoria liberada del PID {pid}")
            messagebox.showinfo("Éxito", f"Memoria liberada de PID {pid}")
            self.update_memory_status()
        except ValueError as e:
            self.logger.error(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Error: {str(e)}")

    def create_logs_tab(self):
        """Pestaña de Logs del Sistema"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="📜 Logs")
        
        # Marco de filtros
        filter_frame = ttk.Frame(tab)
        filter_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(filter_frame, text="📋 Todos", command=lambda: self.refresh_logs()).pack(side=tk.LEFT, padx=2)
        ttk.Button(filter_frame, text="✓ Éxito", command=lambda: self.filter_logs("SUCCESS")).pack(side=tk.LEFT, padx=2)
        ttk.Button(filter_frame, text="⚠️  Advertencia", command=lambda: self.filter_logs("WARNING")).pack(side=tk.LEFT, padx=2)
        ttk.Button(filter_frame, text="❌ Error", command=lambda: self.filter_logs("ERROR")).pack(side=tk.LEFT, padx=2)
        ttk.Button(filter_frame, text="🗑️  Limpiar Logs", command=self.clear_logs).pack(side=tk.LEFT, padx=2)
        ttk.Button(filter_frame, text="💾 Exportar", command=self.export_logs).pack(side=tk.LEFT, padx=2)
        
        # Área de logs
        self.logs_display = scrolledtext.ScrolledText(tab, height=20, bg="#1a1a2e", fg="#00ff00", font=("Courier", 8))
        self.logs_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.current_filter = None
    
    def refresh_logs(self):
        self.current_filter = None
        logs = self.logger.get_logs()
        self.display_logs(logs)
    
    def filter_logs(self, level):
        self.current_filter = level
        logs = self.logger.get_logs(level=level)
        self.display_logs(logs)
    
    def display_logs(self, logs):
        self.logs_display.config(state=tk.NORMAL)
        self.logs_display.delete(1.0, tk.END)
        for log in logs:
            line = f"[{log['timestamp']}] {log['icon']} {log['level']}: {log['message']}\n"
            self.logs_display.insert(tk.END, line)
        self.logs_display.config(state=tk.DISABLED)
        self.logs_display.see(tk.END)
    
    def clear_logs(self):
        if messagebox.askyesno("Confirmar", "¿Limpiar todos los logs?"):
            self.logger.clear()
            self.logs_display.config(state=tk.NORMAL)
            self.logs_display.delete(1.0, tk.END)
            self.logs_display.config(state=tk.DISABLED)
    
    def export_logs(self):
        from tkinter import filedialog
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            with open(filename, 'w') as f:
                f.write(self.logger.export_logs())
            messagebox.showinfo("Éxito", "Logs exportados correctamente")
            self.logger.success(f"Logs exportados a: {filename}")
    
    def create_stats_tab(self):
        """Pestaña de Estadísticas"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="📊 Estadísticas")
        
        # Marco de botones
        btn_frame = ttk.Frame(tab)
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(btn_frame, text="🔄 Actualizar", command=self.refresh_stats).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="📥 Descargar", command=self.download_stats).pack(side=tk.LEFT, padx=5)
        
        # Área de estadísticas
        self.stats_display = scrolledtext.ScrolledText(tab, height=25, bg="#1a1a2e", fg="#00ff00", font=("Courier", 9))
        self.stats_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.stats_display.config(state=tk.DISABLED)
    
    def refresh_stats(self):
        summary = self.stats.get_summary()
        self.stats_display.config(state=tk.NORMAL)
        self.stats_display.delete(1.0, tk.END)
        self.stats_display.insert(tk.END, summary)
        self.stats_display.config(state=tk.DISABLED)
    
    def download_stats(self):
        from tkinter import filedialog
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            with open(filename, 'w') as f:
                f.write(self.stats.get_summary())
            messagebox.showinfo("Éxito", "Estadísticas descargadas")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulatedOS(root)
    root.mainloop()