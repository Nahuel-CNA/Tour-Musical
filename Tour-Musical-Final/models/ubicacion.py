class Ubicacion:

    def __init__(self,id,nombre,direccion,coordenadas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        if coordenadas is None:
            self.coordenadas = []
        else:
            self.coordenadas = coordenadas
    
    def __str__(self):
        return f"{self.nombre} - {self.direccion}"
    
    def to_json(self):
        return {
            "id":self.id,
            "nombre":self.nombre,
            "direccion" : self.direccion,
            "coordenadas":self.coordenadas
        }
        
    @classmethod
    def from_json(cls,data):
        id = data["id"]
        nombre = data["nombre"]
        direccion = data["direccion"]
        coordenadas = data["coordenadas"]
        return Ubicacion(id,nombre,direccion,coordenadas)