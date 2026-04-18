# Módulo de Administración de Tareas

import psutil

class TaskManager:
    def __init__(self):
        pass

    def list_processes(self):
        processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                processes.append({'pid': proc.info['pid'], 'name': proc.info['name']})
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return processes[:10]  # Limitar a 10 para simplicidad

    def kill_process(self, pid):
        try:
            proc = psutil.Process(pid)
            proc.terminate()
        except psutil.NoSuchProcess:
            pass