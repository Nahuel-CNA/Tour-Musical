import customtkinter
from PIL import Image
import os

class EventoInfo(customtkinter.CTkToplevel):

    #dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "forms/assets/Eventos")
    dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "forms/assets/Eventos")

    def __init__(self,evento_row):
        super().__init__()
        self.title("Evento")
        self.geometry("700x700")
        self.resizable(0,0)
        self.grid_columnconfigure(0, weight=1)
        self.evento = evento_row
        self.frame_imagen()
        self.frame_info()

    def frame_imagen(self):
        self.evento_image = customtkinter.CTkImage(Image.open(os.path.join(EventoInfo.dir_path, self.evento[9])), size=(500, 300)) #imagen en el medio de la app
        self.evento_frame_image_label = customtkinter.CTkLabel(self, text="", image=self.evento_image)
        self.evento_frame_image_label.grid(row=0, column=0, padx=20, pady=10)
    
    def frame_info(self):
        self.frame_info = customtkinter.CTkFrame(self)
        self.frame_info.grid(row=1,column=0, padx=20, pady=10,sticky="ns")
        self.frame_info.grid_columnconfigure(0, weight=1)

        self.nombre_label = customtkinter.CTkLabel(self.frame_info, text=self.evento[1],font=("Comic Sans MS",30),compound="center")
        self.nombre_label.grid(row=0, column=0,columnspan=2,padx=20, pady=5)
        self.artista_label = customtkinter.CTkLabel(self.frame_info, text=self.evento[2],font=("Comic Sans MS",30),compound="center")
        self.artista_label.grid(row=1, column=0,columnspan=2,padx=20, pady=5)

        self.genero_label_text = customtkinter.CTkLabel(self.frame_info, text="GENERO")
        self.genero_label_text.grid(row=2, column=0, padx=5, pady=5)
        self.genero_label = customtkinter.CTkLabel(self.frame_info, text=self.evento[3])
        self.genero_label.grid(row=2, column=1,pady=5)

        self.lugar_label_text = customtkinter.CTkLabel(self.frame_info, text="LUGAR")
        self.lugar_label_text.grid(row=3, column=0, padx=20, pady=5)
        self.lugar_label = customtkinter.CTkLabel(self.frame_info, text=self.evento[5])
        self.lugar_label.grid(row=3, column=1, padx=20, pady=5)

        self.direccion_label_text = customtkinter.CTkLabel(self.frame_info, text="DIRECCION")
        self.direccion_label_text.grid(row=4, column=0, padx=20, pady=5)
        self.direccion_label = customtkinter.CTkLabel(self.frame_info, text=self.evento[6])
        self.direccion_label.grid(row=4, column=1, padx=20, pady=5)

        self.fecha_label_text = customtkinter.CTkLabel(self.frame_info, text="FECHA")
        self.fecha_label_text.grid(row=5, column=0, padx=20, pady=5)
        self.fecha_label = customtkinter.CTkLabel(self.frame_info, text=self.evento[7])
        self.fecha_label.grid(row=5, column=1, padx=20, pady=5)

        self.descripcion_label_text = customtkinter.CTkLabel(self.frame_info, text="DESCRIPCION")
        self.descripcion_label_text.grid(row=6, column=0, padx=20, pady=5)
        self.descripcion_label = customtkinter.CTkLabel(self.frame_info, text=self.evento[8])
        self.descripcion_label.grid(row=6, column=1, padx=20, pady=5)
        
        
