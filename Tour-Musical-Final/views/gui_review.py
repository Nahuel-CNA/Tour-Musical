import tkinter as tk
from tkinter import ttk
import customtkinter
import os
from PIL import Image,ImageTk
from models.serv_review import ServicioReview  # Cambia la importación a la clase correcta

class ReviewGui(customtkinter.CTkFrame):

    def __init__(self, root, corner_radius):

        super().__init__(root, corner_radius)
        self.grid_columnconfigure(0, weight=1)

        image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "forms/assets")

        #image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

        self.ubicacion_large_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "frame_resena.png")), size=(500, 150)) #imagen en el medio de la app
        self.ubicacion_frame_large_image_label = customtkinter.CTkLabel(self, text="", image=self.ubicacion_large_image)
        self.ubicacion_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

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
        self.boton_ver = customtkinter.CTkButton(self.frame_filter,text="VER",fg_color="#A1A892",hover_color="#3bed44")
        self.boton_editar.grid(row=0,column=2,padx=10,pady=10)
        self.boton_eliminar.grid(row=0,column=3,padx=10,pady=10)
        self.boton_ver.grid(row=0,column=4,padx=10,pady=10)

        # Resto del código de inicialización de la GUI

        self.create_table()
       # self.get_and_insert_values()

    def get_and_insert_values(self):
        values = self.get_values()  # Obtener los valores de las revisiones
        for value in values:
            self.table.insert("", tk.END, values=value)  # Insertar los valores en la tabla

    def get_values(self):
        reviewss = ServicioReview()
        lista_reviews = reviewss.get_reviews()
        values = []
        for review in lista_reviews:
            fila_review = []
            fila_review.append(review.id)
            fila_review.append(review.id_evento)
            fila_review.append(review.id_usuario)
            fila_review.append(review.calificacion)
            fila_review.append(review.comentario)
            fila_review.append(review.animo)
            values.append(fila_review)
        return values
        """fila_review = [
                review.id_review,
                review.id_evento,
                review.id_usuario,
                review.calificacion,
                review.comentario,
                review.animo
            ]
            values.append(fila_review)
        return values"""""

    def insert_table(self):
        reviews = self.get_values()
        for review in reviews:
            self.table.insert("", tk.END, values=review)

    def create_table(self):
        self.table = ttk.Treeview(self.frame_table, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=25)
        self.table.column("#1", anchor=tk.CENTER)
        self.table.heading("#1", text="ID Review")
        self.table.column("#2", anchor=tk.CENTER)
        self.table.heading("#2", text="ID Evento")
        self.table.column("#3", anchor=tk.CENTER)
        self.table.heading("#3", text="ID Usuario")
        self.table.column("#4", anchor=tk.CENTER)
        self.table.heading("#4", text="Calificación")
        self.table.column("#5", anchor=tk.CENTER)
        self.table.heading("#5", text="Comentario")
        self.table.column("#6", anchor=tk.CENTER)
        self.table.heading("#6", text="Ánimo")
        self.table.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.insert_table()

# Código para crear la ventana principal y ejecutar la aplicación
"""root = tk.Tk()
root.title("Tabla de Revisiones")
app = ReviewGui(root, corner_radius=10)
app.pack(fill=tk.BOTH, expand=True)
root.mainloop()"""
