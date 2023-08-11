from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter
import os
from PIL import Image
from datetime import datetime
from models.serv_evento import ServicioEventos
from views.info_evento import EventoInfo

class EventoGui(customtkinter.CTkFrame):

    def __init__(self,root,corner_radius):
        super().__init__(root,corner_radius)
        self.grid_columnconfigure(0, weight=1)
        image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "forms/assets")

        #image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "forms/assets")
        self.evento_large_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "frame_evento.png")), size=(500, 150)) #imagen en el medio de la app
        self.evento_frame_large_image_label = customtkinter.CTkLabel(self, text="", image=self.evento_large_image)
        self.evento_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        
        self.frame_table = customtkinter.CTkFrame(self,corner_radius=0)
        self.frame_table.grid(row=1, column=0, sticky="nsew")
        self.frame_table.grid_columnconfigure(0, weight=1)

        self.frame_filter = customtkinter.CTkFrame(self.frame_table,corner_radius=0)
        self.frame_filter.grid(row=0, column=0, sticky="nsew")
        self.filter_input = customtkinter.CTkEntry(self.frame_filter,width=300,placeholder_text="Buscar")
        self.filter_input.grid(row=0,column=0,padx=10,pady=10)
        self.filter_boton = customtkinter.CTkButton(self.frame_filter,text="BUSCAR")
        self.filter_boton.grid(row=0,column=1,padx=10,pady=10)

        self.boton_editar = customtkinter.CTkButton(self.frame_filter,text="EDITAR",fg_color="#A1A892",hover_color="#60d3f0")
        self.boton_eliminar = customtkinter.CTkButton(self.frame_filter,text="ELIMINAR",fg_color="#A1A892",hover_color="#e84351")
        self.boton_ver = customtkinter.CTkButton(self.frame_filter,text="VER",fg_color="#A1A892",hover_color="#3bed44",command=self.event_info)
        self.boton_editar.grid(row=0,column=2,padx=10,pady=10)
        self.boton_eliminar.grid(row=0,column=3,padx=10,pady=10)
        self.boton_ver.grid(row=0,column=4,padx=10,pady=10)
        
        self.create_table()
        self.table.bind("<Double-Button-1>", self.event_info)

    def get_values(self):
        eventos = ServicioEventos()
        lista_eventos = eventos.get_eventos()
        values = []
        for evento in lista_eventos:
            fila_evento = []
            fila_evento.append(evento.id)
            fila_evento.append(evento.nombre)
            fila_evento.append(evento.artista)
            fila_evento.append(evento.genero[0])
            fila_evento.append(evento.id_ubicacion)
            fila_evento.append(eventos.get_ubicacion(evento.id_ubicacion[0]).nombre)
            fila_evento.append(eventos.get_ubicacion(evento.id_ubicacion[0]).direccion)
            hora_inicio = datetime.fromisoformat(evento.hora_inicio[0]).strftime("%d/%m/%Y %H:%M:%S")
            fila_evento.append(hora_inicio)
            values.append(fila_evento)
            fila_evento.append(evento.descripcion)
            fila_evento.append(evento.imagen)
        return values
    
    def insert_table(self):
        eventos = self.get_values()
        for evento in eventos:
            self.table.insert("", tk.END, values=evento)
        
    def create_table(self):
        self.table = ttk.Treeview(self.frame_table, column=("c1", "c2", "c3","c4","c5","c6","c7","c8","c9","c10"), show='headings',height=25)
        self.table.column("#1", anchor=tk.CENTER,stretch=False, minwidth=0, width=0)
        self.table.heading("#1", text="Id")
        self.table.column("#2", anchor=tk.CENTER)
        self.table.heading("#2", text="Nombre")
        self.table.column("#3", anchor=tk.CENTER)
        self.table.heading("#3", text="Artista")
        self.table.column("#4", anchor=tk.CENTER)
        self.table.heading("#4", text="Genero")
        self.table.column("#5",anchor=tk.CENTER,stretch=False, minwidth=0, width=0)
        self.table.heading("#5", text="Id_ubicacion")
        self.table.column("#6",anchor=tk.CENTER)
        self.table.heading("#6", text="Lugar")
        self.table.column("#7", anchor=tk.CENTER)
        self.table.heading("#7", text="Direccion")
        self.table.column("#8", anchor=tk.CENTER)
        self.table.heading("#8", text="Hora")
        self.table.column("#9", anchor=tk.CENTER,stretch=False, minwidth=0, width=0)
        self.table.heading("#9", text="Descripcion")
        self.table.column("#10", anchor=tk.CENTER,stretch=False, minwidth=0, width=0)
        self.table.heading("#10", text="imagen")

        self.table.grid(row=1, column=0,padx=20, pady=20,sticky="nsew")

        self.scrollable_frame_horizontal = customtkinter.CTkScrollbar(self.frame_table,command=self.table.xview,orientation="horizontal")
        self.scrollable_frame_horizontal.grid(row=2, column=0,sticky="ew")
        self.table.configure(xscrollcommand=self.scrollable_frame_horizontal.set)

        self.scrollable_frame_vertical = customtkinter.CTkScrollbar(self.frame_table,command=self.table.yview,orientation="vertical")
        self.scrollable_frame_vertical.grid(row=1, column=1,sticky="ns")
        self.table.configure(xscrollcommand=self.scrollable_frame_vertical.set)

        self.insert_table()
    
    def get_evento_table(self):
        indice = self.table.focus()
        evento_row = self.table.item(indice)
        if indice:
            return evento_row["values"]
        else:
            return None

    def event_info(self,event=None):
        evento_row = self.get_evento_table()
        event_level_info = EventoInfo(evento_row)
        event_level_info.mainloop()

    