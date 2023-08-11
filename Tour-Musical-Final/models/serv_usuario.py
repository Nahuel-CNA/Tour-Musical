import json
from models.usuario import Usuario

class ServicioUsuario:

    def __init__(self):
        usuarios = []
        try:
            with open("data/Usuario.json","r") as file:
                usuarios_json = json.load(file)
            for data in usuarios_json:
                usuarios.append(Usuario.from_json(data))
        except Exception as error:
            with open("data/Usuario.json","w") as file:
                json.dump(usuarios, file, indent=4)
        finally:
            self.usuarios = usuarios

    def crearUsuario(self,nombre,apellido,historial_eventos = None):
        id = len(self.eventos) + 1 
        usuario = Usuario(id,nombre,apellido,historial_eventos)
        self.usuarios.append(usuario)
    
    def eliminarUsuario(self,usuario):
        self.usuarios.remove(usuario)
    
    def buscarUsuario(self,id_usuario):
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                return usuario
        return None
    
    def modificar(self,id_usuario,nombre,apellido,historial_eventos = None):
        usuario = self.buscarUsuario(id_usuario)
        if not(usuario is None):
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.historial_eventos = historial_eventos
        else:
            print("que no se encuentra el Evento")

    def get_users(self):
        return self.usuarios
    
    def finalizar(self):
        with open('data/Usuario.json', 'w') as f:
            usuarios = []
            for usuario in self.usuarios:
                usuarios.append(usuario.to_json())
            json.dump(usuarios, f, indent=4)