# Módulo de Gestión de Memoria

class MemoryManager:
    def __init__(self, total_memory=1024):  # MB simulados
        self.total_memory = total_memory
        self.allocated = {}  # pid: size
        self.free_blocks = [total_memory]

    def allocate(self, pid, size):
        for i, block in enumerate(self.free_blocks):
            if block >= size:
                self.free_blocks[i] -= size
                self.allocated[pid] = size
                return True
        return False  # No hay espacio

    def deallocate(self, pid):
        if pid in self.allocated:
            size = self.allocated.pop(pid)
            self.free_blocks.append(size)
            self.free_blocks.sort(reverse=True)  # Simplificar compactación
        else:
            raise ValueError("Proceso no encontrado")

    def get_memory_status(self):
        used = sum(self.allocated.values())
        free = sum(self.free_blocks)
        return used, free, self.total_memory