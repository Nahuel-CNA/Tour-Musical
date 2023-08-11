import json
from models.ubicacion import Ubicacion

class ServicioUbicacion:

    def __init__(self):
        ubicaciones = []
        try:
            with open("data/Ubicacion.json","r") as file:
                ubicaciones_json = json.load(file)
            for data in ubicaciones_json:
                ubicaciones.append(Ubicacion.from_json(data))
        except FileNotFoundError:
            with open("data/Ubicacion.json","w") as file:
                json.dump(ubicaciones, file, indent=4)
        finally:
            self.ubicaciones = ubicaciones
    #CRUD ABM
    def crearUbicacion(self,nombre,direccion,coordenadas = None):
        id = len(self.ubicaciones) + 1 
        ubicacion = Ubicacion(id,nombre,direccion,coordenadas)
        self.ubicaciones.append(ubicacion)
    
    def eliminarUbicacion(self,ubicacion):
        self.ubicaciones.remove(ubicacion)
    
    def buscarUbicacion(self,id_ubicacion):
        for ubicacion in self.ubicaciones:
            if ubicacion.id == id_ubicacion:
                return ubicacion
        return None
    
    def modificar(self,id_ubicacion):
        ubicacion = self.buscarUbicacion(id_ubicacion)
        if not(ubicacion is None):
            nombre = input("Ingrese el nombre : ")
            direccion = input("Ingrese la direccion : ")
            coordenadas = []
            for i in range(2):
                coordenadas.append(float(input("Ingrese la coordenada : ")))
            ubicacion.nombre = nombre
            ubicacion.direccion = direccion
            ubicacion.coordenadas = coordenadas
        else:
            print("que no se encuentra la Ubicacion")
    
    def get_ubicaciones(self):
        return self.ubicaciones

    def finalizar(self):
        with open('data/Ubicacion.json', 'w') as f:
            lista = []
            for ubicacion in self.ubicaciones:
                lista.append(ubicacion.to_json())
            json.dump(lista, f, indent=4)

