class Evento:

    def __init__(self,id,nombre,artista,genero,
    id_ubicacion,hora_inicio,descripcion,imagen):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.descripcion = descripcion
        self.imagen = imagen

    def __str__(self):
        return f"{self.nombre} - {self.artista} - {self.genero} - {self.hora_inicio} - {self.descripcion}"

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "artista": self.artista,
            "genero" : self.genero,
            "id_ubicacion" : self.id_ubicacion,
            "hora_inicio" : self.hora_inicio,
            "descripcion" : self.descripcion,
            "imagen": self.imagen
        }

    @classmethod
    def from_json(cls,data):
        id = data["id"]
        nombre = data["nombre"]
        artista = data["artista"]
        genero = data["genero"],
        id_ubicacion = data["id_ubicacion"],
        hora_inicio = data["hora_inicio"],
        descripcion = data["descripcion"],
        imagen = data["imagen"]
        return Evento(id,nombre,artista,genero,id_ubicacion,hora_inicio,descripcion,imagen)