# Módulo de Administración de Usuarios

class UserManager:
    def __init__(self):
        self.users = {"admin": "password", "user": "pass"}  # Usuarios simulados
        self.current_user = None
        self.permissions = {"admin": ["read", "write", "delete"], "user": ["read"]}

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            self.current_user = username
            return True
        return False

    def logout(self):
        self.current_user = None

    def has_permission(self, action):
        if self.current_user:
            return action in self.permissions.get(self.current_user, [])
        return False

    def get_current_user(self):
        return self.current_user