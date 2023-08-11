import tkinter
import tkintermapview
import customtkinter

from PIL import Image, ImageTk
import os


class MapCustom(customtkinter.CTkFrame):

    

    def __init__(self, root, width, height):
        super().__init__(root, width, height)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.map_widget = tkintermapview.TkinterMapView(self, width=1200, height=700, corner_radius=0)
        self.map_widget.grid(row=0, column=0, sticky="nsew")
        
        self.map_widget.set_position(-24.8531288, -65.4977050)
        #-24.72279803947432, -65.426856820208
        self.map_widget.set_zoom(12)

        self.load_markers()

        #agregado de marcadores
    def load_markers(self):  
        image_names = [
            "Mana.png",
            "Marco_Solis.png",
            "Montero.png",
            "Palavecino.png"
            ]
        
        image_paths = [os.path.join("forms/assets/Eventos", name) for name in image_names]
        images = [Image.open(path).resize((300, 200)) for path in image_paths]
        image_tk_objects = [ImageTk.PhotoImage(image) for image in images]
        
        positions = [
            {"lat": -24.82905124713856, "lon": -65.43447009070401, "text": "Rayando El Sol Tour"},
            {"lat": -24.78860454503634, "lon": -65.40953047417509, "text": "El Buki 2023 - World Tour"},
            {"lat": -24.78963851316605, "lon": -65.40887380421306, "text": "Homenaje al ultimo rey"},
            {"lat": -24.908130371682038, "lon": -65.64688169151162, "text": "Festival Patrio"}
            ]
        
        markers = []
        
        for i, pos in enumerate(positions):
            marker = self.map_widget.set_marker(pos["lat"], pos["lon"], text=pos["text"], image=image_tk_objects[i],
                                           image_zoom_visibility=(0, float("inf")), command=self.click_marker_event)
            markers.append(marker)
            marker.hide_image(True)
    
    def click_marker_event(self, marker):
        if marker.image_hidden:
            marker.hide_image(False)
        else:
            marker.hide_image(True)

    

    


    """def __init__(self,root,width,height):
        super().__init__(root,width,height)
        self.grid_columnconfigure(0, weight=1)
        self.map_widget = tkintermapview.TkinterMapView(self, width=900,height=600, corner_radius=0)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.map_widget.set_position(-24.72279803947432, -65.426856820208)
        self.map_widget.set_zoom(12)"""
   
                                      
