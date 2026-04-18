"""
Módulo de Terminal Simulada
Simula una terminal del sistema operativo con comandos básicos
"""

class TerminalSimulator:
    def __init__(self):
        self.history = []
        self.current_dir = "/"
        self.commands = {
            "help": self.cmd_help,
            "cd": self.cmd_cd,
            "pwd": self.cmd_pwd,
            "ls": self.cmd_ls,
            "whoami": self.cmd_whoami,
            "echo": self.cmd_echo,
            "date": self.cmd_date,
            "clear": self.cmd_clear,
        }
        self.current_user = "admin"
    
    def execute(self, command):
        """Ejecuta un comando en la terminal simulada"""
        self.history.append(command)
        
        if not command.strip():
            return ""
        
        parts = command.strip().split()
        cmd = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        if cmd in self.commands:
            return self.commands[cmd](args)
        else:
            return f"Comando no encontrado: {cmd}"
    
    def cmd_help(self, args):
        """Muestra ayuda"""
        help_text = """
Comandos disponibles:
  help          - Muestra esta ayuda
  cd <dir>      - Cambia de directorio
  pwd           - Muestra directorio actual
  ls            - Lista archivos
  whoami        - Muestra usuario actual
  echo <texto>  - Imprime texto
  date          - Muestra fecha y hora actual
  clear         - Limpia el historial
        """
        return help_text
    
    def cmd_cd(self, args):
        """Cambia de directorio"""
        if not args:
            self.current_dir = "/"
            return f"Cambiado a directorio raíz"
        self.current_dir = args[0]
        return f"Cambiado a {self.current_dir}"
    
    def cmd_pwd(self, args):
        """Muestra directorio actual"""
        return f"Directorio actual: {self.current_dir}"
    
    def cmd_ls(self, args):
        """Lista archivos del directorio"""
        return f"Archivos en {self.current_dir}:\n  [dir1]\n  archivo1.txt\n  archivo2.py"
    
    def cmd_whoami(self, args):
        """Muestra usuario actual"""
        return f"Usuario: {self.current_user}"
    
    def cmd_echo(self, args):
        """Imprime texto"""
        return " ".join(args) if args else ""
    
    def cmd_date(self, args):
        """Muestra fecha y hora"""
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    def cmd_clear(self, args):
        """Limpia el historial"""
        self.history = []
        return "Historial limpiado"
    
    def get_history(self):
        """Retorna el historial de comandos"""
        return self.history
