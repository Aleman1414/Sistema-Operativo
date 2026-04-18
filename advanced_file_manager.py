# Módulo de Sistema de Archivos Avanzado

import os
import shutil
from file_manager import FileManager

class AdvancedFileManager(FileManager):
    def __init__(self, user_manager):
        super().__init__()
        self.user_manager = user_manager
        self.file_system = {"root": {}}  # Estructura de directorios
        self.current_dir = "root"
        self.file_permissions = {}  # archivo: {"owner": user, "perms": ["read", "write"]}

    def create_directory(self, name):
        if not self.user_manager.has_permission("write"):
            raise PermissionError("No tienes permisos para crear directorios")
        if self.current_dir not in self.file_system:
            self.file_system[self.current_dir] = {}
        self.file_system[self.current_dir][name] = {}
        self.file_permissions[name] = {"owner": self.user_manager.get_current_user(), "perms": ["read", "write"]}

    def change_directory(self, path):
        if path in self.file_system.get(self.current_dir, {}):
            self.current_dir = path
        else:
            raise FileNotFoundError("Directorio no encontrado")

    def list_directory(self):
        return list(self.file_system.get(self.current_dir, {}).keys())

    def create_file(self, name):
        if not self.user_manager.has_permission("write"):
            raise PermissionError("No tienes permisos para crear archivos")
        super().create_file(name)
        self.file_permissions[name] = {"owner": self.user_manager.get_current_user(), "perms": ["read", "write"]}

    def delete_file(self, name):
        if not self.user_manager.has_permission("delete"):
            raise PermissionError("No tienes permisos para borrar archivos")
        super().delete_file(name)
        if name in self.file_permissions:
            del self.file_permissions[name]