import tkinter as tk
from tkinter.font import BOLD
#import util.generic as utl
import customtkinter
import os
from PIL import Image
from views.map_custom import MapCustom

from views.gui_evento import EventoGui
from views.gui_ubicacion import UbicacionGui
from views.gui_review import ReviewGui
from views.gui_usuario import UsuarioGui

class MasterPanel(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("TOUR MUSICAL")
        self.geometry("1200x600")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo_simple.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Tour_Titulo.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "logo_evento2.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "logo_evento2.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "logo_mapa2.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "logo_mapa2.png")), size=(20, 20))
        
        #Agrego resena
        self.resena_image= customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "logo_resena2.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "logo_resena2.png")), size=(20, 20))
        #agrego boton cuenta
        self.cuenta_image= customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "logo_cuenta2.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "logo_cuenta2.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Menu", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Inicio",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Eventos",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Ubicaciones",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        #boton 4
        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Reseñas",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.resena_image, anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")
        #boton5
        self.frame_5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="MI CUENTA",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.cuenta_image, anchor="w", command=self.frame_5_button_event)
        self.frame_5_button.grid(row=5, column=0, sticky="ew")


        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        #Agregar los frames evento, ubicacion, review y cuenta
        


        #agregar mapa
        self.frame_map = MapCustom(self.home_frame,width=900,height=600)
        self.frame_map.grid(row=1,column=0,padx=20,pady=20)

        # create second frame
        #self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        #prueba
        self.second_frame = EventoGui(self,corner_radius=0)

        # create third frame
        #self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame = UbicacionGui(self,corner_radius=0)


        #crea un cuarto frame
        #self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fourth_frame = ReviewGui(self,corner_radius=0)

        #crea un quinto frame 
        #self.fifth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent") 
        self.fifth_frame = UsuarioGui(self,corner_radius=0)




        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        #4
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        #5
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()
        if name == "frame_5":
            self.fifth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fifth_frame.grid_forget()
            
        

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    #boton4
    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    #boton5
    def frame_5_button_event(self):
        self.select_frame_by_name("frame_5")


    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    

if __name__ == "__main__":
    app = MasterPanel()

    



    app.mainloop()


    
                                  
    """def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Master panel')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("1200x600")
        self.ventana.config(bg='#fcfcfc')      
        #ver
        frame = tk.Frame(self.ventana, bg='white')
        frame.pack(fill='both', expand=True)

        button1 = tk.Button(frame, text='Botón 1')
        button2 = tk.Button(frame, text='Botón 2')

        button1.pack(side='left', padx=10, pady=10)
        button2.pack(side='right', padx=10, pady=10)




        #ver
        #logo =utl.leer_imagen("./imagenes/logo.png", (200, 200))
                        
        #label = tk.Label( self.ventana, image=logo,bg='#E6D884' )
        #label.place(x=0,y=0,relwidth=1, relheight=1)

        self.ventana.update_idletasks()
        width = self.ventana.winfo_width()
        height = self.ventana.winfo_height()
        x = (self.ventana.winfo_screenwidth() - width) // 2
        y = (self.ventana.winfo_screenheight() - height) // 2
        self.ventana.geometry(f"{width}x{height}+{x}+{y}")
        
        self.ventana.mainloop()"""
    
