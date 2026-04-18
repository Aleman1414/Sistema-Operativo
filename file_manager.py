# Módulo de Administración de Archivos

import os
import shutil

class FileManager:
    def __init__(self, base_dir="./simulated_files"):
        self.base_dir = base_dir
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def create_file(self, name):
        path = os.path.join(self.base_dir, name)
        with open(path, 'w') as f:
            f.write("Contenido simulado")

    def delete_file(self, name):
        path = os.path.join(self.base_dir, name)
        if os.path.exists(path):
            os.remove(path)

    def copy_file(self, src, dst):
        src_path = os.path.join(self.base_dir, src)
        dst_path = os.path.join(self.base_dir, dst)
        if os.path.exists(src_path):
            shutil.copy(src_path, dst_path)

    def list_files(self):
        return os.listdir(self.base_dir)