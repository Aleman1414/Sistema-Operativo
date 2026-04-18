"""
Módulo de Logs del Sistema
Registra eventos del sistema operativo
"""

from datetime import datetime

class SystemLogger:
    def __init__(self):
        self.logs = []
        self.log_levels = {
            "INFO": "ℹ️",
            "WARNING": "⚠️",
            "ERROR": "❌",
            "SUCCESS": "✓",
            "DEBUG": "🐛"
        }
    
    def log(self, level, message):
        """Registra un evento en el log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = {
            "timestamp": timestamp,
            "level": level,
            "message": message,
            "icon": self.log_levels.get(level, "•")
        }
        self.logs.append(log_entry)
        return log_entry
    
    def info(self, message):
        """Registra un mensaje de información"""
        return self.log("INFO", message)
    
    def warning(self, message):
        """Registra un aviso"""
        return self.log("WARNING", message)
    
    def error(self, message):
        """Registra un error"""
        return self.log("ERROR", message)
    
    def success(self, message):
        """Registra una acción exitosa"""
        return self.log("SUCCESS", message)
    
    def debug(self, message):
        """Registra información de debug"""
        return self.log("DEBUG", message)
    
    def get_logs(self, level=None, limit=50):
        """Retorna los logs filtrados"""
        filtered = self.logs if not level else [l for l in self.logs if l["level"] == level]
        return filtered[-limit:]
    
    def clear(self):
        """Limpia todos los logs"""
        self.logs = []
    
    def export_logs(self):
        """Exporta los logs como texto"""
        text = ""
        for log in self.logs:
            text += f"[{log['timestamp']}] {log['icon']} {log['level']}: {log['message']}\n"
        return text
