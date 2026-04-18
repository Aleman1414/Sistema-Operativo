# Módulo de Administración de Recursos

import psutil
import os
import threading
import time

class ResourceManager:
    def __init__(self):
        self.cpu_cores = psutil.cpu_count()
        self.memory_total = psutil.virtual_memory().total // (1024**2)  # MB
        self.storage_total = psutil.disk_usage('/').total // (1024**3)  # GB
        self.peripherals = ["Teclado", "Mouse", "Pantalla", "Disco Duro"]  # Simulados

    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        mem = psutil.virtual_memory()
        return mem.used // (1024**2), mem.total // (1024**2)

    def get_storage_usage(self):
        disk = psutil.disk_usage('/')
        return disk.used // (1024**3), disk.total // (1024**3)

    def get_peripherals(self):
        return self.peripherals