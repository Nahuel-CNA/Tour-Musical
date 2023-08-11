import json

from models.evento import Evento
from models.serv_ubicacion import ServicioUbicacion
class ServicioEventos:

    def __init__(self):
        eventos = []
        try:
            with open("data/Eventos.json","r") as file:
                eventos_json = json.load(file)
                
            for data in eventos_json:
                eventos.append(Evento.from_json(data))
        except FileNotFoundError as error:
            with open("data/Eventos.json","w") as file:
                json.dump(eventos, file, indent=4)
        finally:
            self.eventos = eventos

    def crearEvento(self,nombre,artista,genero,
        id_ubicacion,hora_inicio,descripcion,imagen):
        id = len(self.eventos) + 1 
        evento = Evento(id,nombre,artista,genero,
            id_ubicacion,hora_inicio,descripcion,imagen)
        self.eventos.append(evento)
    
    def eliminarEvento(self,evento):
        self.eventos.remove(evento)
    
    def buscarEvento(self,id_evento):
        for evento in self.eventos:
            if evento.id == id_evento:
                return evento
        return None
    
    def modificar(self,id_evento,nombre,artista,genero,
        id_ubicacion,hora_inicio,descripcion,imagen):
        evento = self.buscarEvento(id_evento)
        if not(evento is None):
            evento.nombre = nombre
            evento.artista = artista
            evento.genero = genero
            evento.id_ubicacion = id_ubicacion
            evento.hora_inicio = hora_inicio
            evento.descripcion = descripcion
            evento.imagen = imagen
        else:
            print("que no se encuentra el Evento")
    
    def finalizar(self):
        with open('data/Eventos.json', 'w') as f:
            eventos = []
            for evento in self.eventos:
                eventos.append(evento.to_json())
            json.dump(eventos, f, indent=4)
    
    def get_eventos(self):
        return self.eventos
    
    def get_ubicacion(self,id_ubicacion):
        servicio_ubicacion = ServicioUbicacion()
        return servicio_ubicacion.buscarUbicacion(id_ubicacion)
    #boton desactivado de busqueda
    """def search_event(self):
    search_text = self.filter_input.get()
    if search_text:
        eventos = self.get_values()
        filtered_eventos = [evento for evento in eventos if any(search_text.lower() in str(value).lower() for value in evento)]
        self.table.delete(*self.table.get_children())
        for evento in filtered_eventos:
            self.table.insert("", tk.END, values=evento)"""
    #Boton de editar desactivado
    """def edit_event(self):
    evento_row = self.get_evento_table()
    if evento_row:
        # Implementar la lógica para abrir una ventana de edición
        # Pasar el evento_row a la ventana de edición para que pueda ser editado
        pass
    else:
        print("Selecciona un evento para editar")"""
    #boton eliminar desactivado
    """def delete_event(self):
    evento_row = self.get_evento_table()
    if evento_row:
        confirmation = messagebox.askyesno("Eliminar Evento", "¿Estás seguro de que quieres eliminar este evento?")
        if confirmation:
            # Implementar la lógica para eliminar el evento
            # Actualizar la tabla después de eliminar el evento
            pass
    else:
        print("Selecciona un evento para eliminar")"""""
    
    


