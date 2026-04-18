"""
Módulo de Estadísticas del Sistema
Recopila y muestra estadísticas de uso del sistema
"""

import resource_manager
from datetime import datetime

class SystemStats:
    def __init__(self):
        self.resource_mgr = resource_manager.ResourceManager()
        self.stats = {
            "processes_created": 0,
            "files_created": 0,
            "files_deleted": 0,
            "login_attempts": 0,
            "successful_logins": 0,
            "failed_logins": 0,
            "memory_allocations": 0,
            "memory_deallocations": 0,
            "start_time": datetime.now(),
            "cpu_samples": [],
            "memory_samples": []
        }
    
    def increment_stat(self, stat_name):
        """Incrementa una estadística"""
        if stat_name in self.stats:
            if isinstance(self.stats[stat_name], int):
                self.stats[stat_name] += 1
    
    def add_cpu_sample(self):
        """Añade una muestra de CPU"""
        cpu = self.resource_mgr.get_cpu_usage()
        self.stats["cpu_samples"].append(cpu)
        if len(self.stats["cpu_samples"]) > 100:
            self.stats["cpu_samples"].pop(0)
    
    def add_memory_sample(self):
        """Añade una muestra de memoria"""
        used, total = self.resource_mgr.get_memory_usage()
        self.stats["memory_samples"].append((used, total))
        if len(self.stats["memory_samples"]) > 100:
            self.stats["memory_samples"].pop(0)
    
    def get_uptime(self):
        """Retorna el tiempo de actividad del sistema"""
        uptime = datetime.now() - self.stats["start_time"]
        hours, remainder = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours}h {minutes}m {seconds}s"
    
    def get_average_cpu(self):
        """Retorna el promedio de CPU"""
        if not self.stats["cpu_samples"]:
            return 0
        return sum(self.stats["cpu_samples"]) / len(self.stats["cpu_samples"])
    
    def get_average_memory(self):
        """Retorna el promedio de memoria utilizada"""
        if not self.stats["memory_samples"]:
            return 0
        used_samples = [m[0] for m in self.stats["memory_samples"]]
        return sum(used_samples) / len(used_samples)
    
    def get_summary(self):
        """Retorna un resumen de las estadísticas"""
        summary = f"""
╔══════════════════════════════════════════╗
║      ESTADÍSTICAS DEL SISTEMA            ║
╚══════════════════════════════════════════╝

⏱️  Tiempo activo: {self.get_uptime()}

📊 Actividad:
   • Procesos creados: {self.stats['processes_created']}
   • Archivos creados: {self.stats['files_created']}
   • Archivos eliminados: {self.stats['files_deleted']}
   • Asignaciones de memoria: {self.stats['memory_allocations']}
   • Liberaciones de memoria: {self.stats['memory_deallocations']}

👤 Sesiones:
   • Intentos de login: {self.stats['login_attempts']}
   • Logins exitosos: {self.stats['successful_logins']}
   • Logins fallidos: {self.stats['failed_logins']}

💻 Recursos:
   • CPU promedio: {self.get_average_cpu():.1f}%
   • Memoria promedio: {self.get_average_memory():.1f} MB
        """
        return summary
    
    def get_stats_dict(self):
        """Retorna todas las estadísticas"""
        return self.stats.copy()
