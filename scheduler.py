# Módulo de Planificación de Procesos

import threading
import time
import queue

class Scheduler:
    def __init__(self):
        self.process_queue = queue.Queue()
        self.quantum = 2  # Tiempo de quantum para Round Robin
        self.log = []  # Log de ejecución

    def add_process(self, pid, burst_time):
        self.process_queue.put({"pid": pid, "burst": burst_time, "remaining": burst_time})

    def run_round_robin(self):
        self.log = []
        while not self.process_queue.empty():
            proc = self.process_queue.get()
            time_slice = min(self.quantum, proc["remaining"])
            self.log.append(f"Ejecutando proceso {proc['pid']} por {time_slice}s")
            time.sleep(time_slice)  # Simular ejecución
            proc["remaining"] -= time_slice
            if proc["remaining"] > 0:
                self.process_queue.put(proc)
        return self.log

    def get_log(self):
        return self.log