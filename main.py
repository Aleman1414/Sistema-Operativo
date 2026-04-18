# Sistema Operativo Simulado
# Proyecto para clase de Sistemas Operativos

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import resource_manager
import file_manager
import task_manager
import user_manager
import scheduler
import advanced_file_manager
import memory_manager

class SimulatedOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Operativo Simulado")
        self.root.geometry("800x600")

        # Crear notebook para pestañas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Pestaña Administración de Recursos
        self.resource_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.resource_tab, text="Recursos")
        self.setup_resource_tab()

        # Pestaña Administración de Archivos
        self.file_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.file_tab, text="Archivos")
        self.setup_file_tab()

        # Pestaña Administración de Tareas
        self.task_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.task_tab, text="Tareas")
        self.setup_task_tab()

        # Pestaña Usuarios
        self.user_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.user_tab, text="Usuarios")
        self.setup_user_tab()

        # Pestaña Scheduling
        self.sched_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.sched_tab, text="Scheduling")
        self.setup_sched_tab()

        # Pestaña Archivos Avanzados
        self.adv_file_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.adv_file_tab, text="Archivos Avanzados")
        self.setup_adv_file_tab()

        # Pestaña Memoria
        self.memory_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.memory_tab, text="Memoria")
        self.setup_memory_tab()

        # Inicializar managers
        self.resource_mgr = resource_manager.ResourceManager()
        self.file_mgr = file_manager.FileManager()
        self.task_mgr = task_manager.TaskManager()
        self.user_mgr = user_manager.UserManager()
        self.scheduler = scheduler.Scheduler()
        self.adv_file_mgr = advanced_file_manager.AdvancedFileManager(self.user_mgr)
        self.memory_mgr = memory_manager.MemoryManager()

    def setup_resource_tab(self):
        # CPU
        ttk.Label(self.resource_tab, text="CPU:").grid(row=0, column=0, padx=10, pady=5)
        self.cpu_label = ttk.Label(self.resource_tab, text="0%")
        self.cpu_label.grid(row=0, column=1, padx=10, pady=5)
        ttk.Button(self.resource_tab, text="Actualizar CPU", command=self.update_cpu).grid(row=0, column=2, padx=10, pady=5)

        # Memoria
        ttk.Label(self.resource_tab, text="Memoria:").grid(row=1, column=0, padx=10, pady=5)
        self.mem_label = ttk.Label(self.resource_tab, text="0 MB / 0 MB")
        self.mem_label.grid(row=1, column=1, padx=10, pady=5)
        ttk.Button(self.resource_tab, text="Actualizar Memoria", command=self.update_memory).grid(row=1, column=2, padx=10, pady=5)

        # Almacenamiento
        ttk.Label(self.resource_tab, text="Almacenamiento:").grid(row=2, column=0, padx=10, pady=5)
        self.storage_label = ttk.Label(self.resource_tab, text="0 GB / 0 GB")
        self.storage_label.grid(row=2, column=1, padx=10, pady=5)
        ttk.Button(self.resource_tab, text="Actualizar Almacenamiento", command=self.update_storage).grid(row=2, column=2, padx=10, pady=5)

        # Periféricos
        ttk.Label(self.resource_tab, text="Periféricos:").grid(row=3, column=0, padx=10, pady=5)
        self.peripherals_list = tk.Listbox(self.resource_tab, height=5)
        self.peripherals_list.grid(row=3, column=1, padx=10, pady=5)
        ttk.Button(self.resource_tab, text="Listar Periféricos", command=self.list_peripherals).grid(row=3, column=2, padx=10, pady=5)

    def update_cpu(self):
        usage = self.resource_mgr.get_cpu_usage()
        self.cpu_label.config(text=f"{usage}%")

    def update_memory(self):
        used, total = self.resource_mgr.get_memory_usage()
        self.mem_label.config(text=f"{used} MB / {total} MB")

    def update_storage(self):
        used, total = self.resource_mgr.get_storage_usage()
        self.storage_label.config(text=f"{used} GB / {total} GB")

    def list_peripherals(self):
        peripherals = self.resource_mgr.get_peripherals()
        self.peripherals_list.delete(0, tk.END)
        for p in peripherals:
            self.peripherals_list.insert(tk.END, p)

    def setup_file_tab(self):
        # Lista de archivos
        self.file_list = tk.Listbox(self.file_tab, height=10)
        self.file_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Botones
        button_frame = ttk.Frame(self.file_tab)
        button_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Button(button_frame, text="Crear Archivo", command=self.create_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Borrar Archivo", command=self.delete_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Copiar Archivo", command=self.copy_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Pegar Archivo", command=self.paste_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Listar Archivos", command=self.list_files).pack(side=tk.LEFT, padx=5)

        self.clipboard = None

    def create_file(self):
        name = simpledialog.askstring("Crear Archivo", "Nombre del archivo:")
        if not name:
            messagebox.showerror("Error", "Nombre requerido")
            return
        try:
            self.file_mgr.create_file(name)
            self.list_files()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_file(self):
        selected = self.file_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Selecciona un archivo")
            return
        name = self.file_list.get(selected[0])
        try:
            self.file_mgr.delete_file(name)
            self.list_files()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def copy_file(self):
        selected = self.file_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Selecciona un archivo")
            return
        self.clipboard = self.file_list.get(selected[0])

    def paste_file(self):
        if not self.clipboard:
            messagebox.showerror("Error", "No hay archivo copiado")
            return
        name = simpledialog.askstring("Pegar Archivo", "Nuevo nombre:")
        if not name:
            messagebox.showerror("Error", "Nombre requerido")
            return
        try:
            self.file_mgr.copy_file(self.clipboard, name)
            self.list_files()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def list_files(self):
        try:
            files = self.file_mgr.list_files()
            self.file_list.delete(0, tk.END)
            for f in files:
                self.file_list.insert(tk.END, f)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def setup_task_tab(self):
        # Lista de procesos
        self.process_list = tk.Listbox(self.task_tab, height=10)
        self.process_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Botones
        button_frame = ttk.Frame(self.task_tab)
        button_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Button(button_frame, text="Listar Procesos", command=self.list_processes).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Matar Proceso", command=self.kill_process).pack(side=tk.LEFT, padx=5)

    def list_processes(self):
        try:
            processes = self.task_mgr.list_processes()
            self.process_list.delete(0, tk.END)
            for p in processes:
                self.process_list.insert(tk.END, f"{p['pid']}: {p['name']}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def kill_process(self):
        selected = self.process_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Selecciona un proceso")
            return
        item = self.process_list.get(selected[0])
        try:
            pid = int(item.split(':')[0])
            self.task_mgr.kill_process(pid)
            self.list_processes()
        except ValueError:
            messagebox.showerror("Error", "PID inválido")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def setup_user_tab(self):
        # Login
        ttk.Label(self.user_tab, text="Usuario:").grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = ttk.Entry(self.user_tab)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)
        ttk.Label(self.user_tab, text="Contraseña:").grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = ttk.Entry(self.user_tab, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)
        ttk.Button(self.user_tab, text="Login", command=self.login).grid(row=2, column=0, padx=10, pady=5)
        ttk.Button(self.user_tab, text="Logout", command=self.logout).grid(row=2, column=1, padx=10, pady=5)

        # Usuario actual
        ttk.Label(self.user_tab, text="Usuario actual:").grid(row=3, column=0, padx=10, pady=5)
        self.current_user_label = ttk.Label(self.user_tab, text="Ninguno")
        self.current_user_label.grid(row=3, column=1, padx=10, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if not username or not password:
            messagebox.showerror("Error", "Usuario y contraseña requeridos")
            return
        if self.user_mgr.login(username, password):
            self.current_user_label.config(text=username)
            messagebox.showinfo("Éxito", f"Bienvenido, {username}")
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def logout(self):
        self.user_mgr.logout()
        self.current_user_label.config(text="Ninguno")
        messagebox.showinfo("Éxito", "Sesión cerrada")

    def setup_sched_tab(self):
        # Agregar proceso
        ttk.Label(self.sched_tab, text="PID:").grid(row=0, column=0, padx=10, pady=5)
        self.pid_entry = ttk.Entry(self.sched_tab)
        self.pid_entry.grid(row=0, column=1, padx=10, pady=5)
        ttk.Label(self.sched_tab, text="Tiempo de Burst:").grid(row=1, column=0, padx=10, pady=5)
        self.burst_entry = ttk.Entry(self.sched_tab)
        self.burst_entry.grid(row=1, column=1, padx=10, pady=5)
        ttk.Button(self.sched_tab, text="Agregar Proceso", command=self.add_process).grid(row=2, column=0, padx=10, pady=5)
        ttk.Button(self.sched_tab, text="Ejecutar Round Robin", command=self.run_scheduler).grid(row=2, column=1, padx=10, pady=5)

        # Log
        self.sched_log = tk.Text(self.sched_tab, height=10)
        self.sched_log.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def add_process(self):
        try:
            pid = int(self.pid_entry.get())
            burst = int(self.burst_entry.get())
            if pid <= 0 or burst <= 0:
                raise ValueError
            self.scheduler.add_process(pid, burst)
            messagebox.showinfo("Éxito", f"Proceso {pid} agregado")
        except ValueError:
            messagebox.showerror("Error", "PID y burst deben ser números positivos")

    def run_scheduler(self):
        log = self.scheduler.run_round_robin()
        self.sched_log.delete(1.0, tk.END)
        for entry in log:
            self.sched_log.insert(tk.END, entry + "\n")

    def setup_adv_file_tab(self):
        # Directorio actual
        ttk.Label(self.adv_file_tab, text="Directorio actual:").grid(row=0, column=0, padx=10, pady=5)
        self.current_dir_label = ttk.Label(self.adv_file_tab, text="root")
        self.current_dir_label.grid(row=0, column=1, padx=10, pady=5)

        # Lista de archivos/directorios
        self.adv_file_list = tk.Listbox(self.adv_file_tab, height=10)
        self.adv_file_list.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        # Botones
        button_frame = ttk.Frame(self.adv_file_tab)
        button_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        ttk.Button(button_frame, text="Crear Directorio", command=self.create_dir).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Cambiar Dir", command=self.change_dir).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Crear Archivo", command=self.create_file_adv).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Borrar", command=self.delete_file_adv).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Listar", command=self.list_dir).pack(side=tk.LEFT, padx=5)

    def create_dir(self):
        name = simpledialog.askstring("Crear Directorio", "Nombre:")
        if not name:
            messagebox.showerror("Error", "Nombre requerido")
            return
        try:
            self.adv_file_mgr.create_directory(name)
            self.list_dir()
        except PermissionError as e:
            messagebox.showerror("Error", str(e))

    def change_dir(self):
        selected = self.adv_file_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Selecciona un directorio")
            return
        name = self.adv_file_list.get(selected[0])
        try:
            self.adv_file_mgr.change_directory(name)
            self.current_dir_label.config(text=self.adv_file_mgr.current_dir)
            self.list_dir()
        except FileNotFoundError as e:
            messagebox.showerror("Error", str(e))

    def create_file_adv(self):
        name = simpledialog.askstring("Crear Archivo", "Nombre:")
        if not name:
            messagebox.showerror("Error", "Nombre requerido")
            return
        try:
            self.adv_file_mgr.create_file(name)
            self.list_dir()
        except PermissionError as e:
            messagebox.showerror("Error", str(e))

    def delete_file_adv(self):
        selected = self.adv_file_list.curselection()
        if not selected:
            messagebox.showerror("Error", "Selecciona un archivo")
            return
        name = self.adv_file_list.get(selected[0])
        try:
            self.adv_file_mgr.delete_file(name)
            self.list_dir()
        except PermissionError as e:
            messagebox.showerror("Error", str(e))

    def list_dir(self):
        files = self.adv_file_mgr.list_directory()
        self.adv_file_list.delete(0, tk.END)
        for f in files:
            self.adv_file_list.insert(tk.END, f)

    def setup_memory_tab(self):
        # Estado de memoria
        ttk.Label(self.memory_tab, text="Memoria Usada:").grid(row=0, column=0, padx=10, pady=5)
        self.mem_used_label = ttk.Label(self.memory_tab, text="0 MB")
        self.mem_used_label.grid(row=0, column=1, padx=10, pady=5)
        ttk.Label(self.memory_tab, text="Memoria Libre:").grid(row=1, column=0, padx=10, pady=5)
        self.mem_free_label = ttk.Label(self.memory_tab, text="1024 MB")
        self.mem_free_label.grid(row=1, column=1, padx=10, pady=5)
        ttk.Button(self.memory_tab, text="Actualizar Estado", command=self.update_memory_status).grid(row=2, column=0, padx=10, pady=5)

        # Asignar/desasignar
        ttk.Label(self.memory_tab, text="PID:").grid(row=3, column=0, padx=10, pady=5)
        self.mem_pid_entry = ttk.Entry(self.memory_tab)
        self.mem_pid_entry.grid(row=3, column=1, padx=10, pady=5)
        ttk.Label(self.memory_tab, text="Tamaño (MB):").grid(row=4, column=0, padx=10, pady=5)
        self.mem_size_entry = ttk.Entry(self.memory_tab)
        self.mem_size_entry.grid(row=4, column=1, padx=10, pady=5)
        ttk.Button(self.memory_tab, text="Asignar", command=self.allocate_memory).grid(row=5, column=0, padx=10, pady=5)
        ttk.Button(self.memory_tab, text="Desasignar", command=self.deallocate_memory).grid(row=5, column=1, padx=10, pady=5)

    def update_memory_status(self):
        used, free, total = self.memory_mgr.get_memory_status()
        self.mem_used_label.config(text=f"{used} MB")
        self.mem_free_label.config(text=f"{free} MB")

    def allocate_memory(self):
        try:
            pid = int(self.mem_pid_entry.get())
            size = int(self.mem_size_entry.get())
            if pid <= 0 or size <= 0:
                raise ValueError
            if self.memory_mgr.allocate(pid, size):
                messagebox.showinfo("Éxito", f"Memoria asignada a PID {pid}")
                self.update_memory_status()
            else:
                messagebox.showerror("Error", "No hay suficiente memoria")
        except ValueError:
            messagebox.showerror("Error", "PID y tamaño deben ser números positivos")

    def deallocate_memory(self):
        try:
            pid = int(self.mem_pid_entry.get())
            self.memory_mgr.deallocate(pid)
            messagebox.showinfo("Éxito", f"Memoria liberada de PID {pid}")
            self.update_memory_status()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except ValueError:
            messagebox.showerror("Error", "PID debe ser un número positivo")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimulatedOS(root)
    root.mainloop()