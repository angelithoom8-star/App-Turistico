 

import os
import webbrowser
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.audio import SoundLoader
from PIL import Image as PILImage, ImageDraw, ImageFont
from kivy_garden.mapview import MapView

# Ajustar ventana
Window.size = (360, 640)

# ========= GENERAR IMÁGENES SI NO EXISTEN =========
categorias = [
    "turismo", "cultura", "alojamiento", "transporte",
    "gastronomia", "eventos", "compras", "rutas", "servicios"
]

try:
    font = ImageFont.truetype("arial.ttf", 30)
except:
    font = ImageFont.load_default()

for categoria in categorias:
    for i in range(1, 5):
        filename = f"{categoria}{i}.png"
        if not os.path.exists(filename):
            img = PILImage.new("RGB", (400, 300), (50*i % 255, 100*i % 255, 150*i % 255))
            draw = ImageDraw.Draw(img)
            texto = f"{categoria.capitalize()} {i}"
            w, h = draw.textsize(texto, font=font)
            draw.text(((400-w)/2, (300-h)/2), texto, fill="white", font=font)
            img.save(filename)

# ========= DATOS DE CONTENIDO =========
contenido_ejemplo = {
    "turismo": ("Sección Turismo",
                [("turismo1.png","Turismo 1"),
                 ("turismo2.png","Turismo 2"),
                 ("turismo3.png","Turismo 3"),
                 ("turismo4.png","Turismo 4")]),
    "cultura": ("Sección Cultura",
                [("cultura1.png","Música 1"),
                 ("cultura2.png","Música 2"),
                 ("cultura3.png","Música 3"),
                 ("cultura4.png","Música 4")]),
    "alojamiento": ("Sección Alojamiento",
                [("alojamiento1.png","Alojamiento 1"),
                 ("alojamiento2.png","Alojamiento 2"),
                 ("alojamiento3.png","Alojamiento 3"),
                 ("alojamiento4.png","Alojamiento 4")]),
    "transporte": ("Sección Transporte",
                [("transporte1.png","Transporte 1"),
                 ("transporte2.png","Transporte 2"),
                 ("transporte3.png","Transporte 3"),
                 ("transporte4.png","Transporte 4")]),
    "gastronomia": ("Sección Gastronomía",
                [("gastronomia1.png","Gastronomía 1"),
                 ("gastronomia2.png","Gastronomía 2"),
                 ("gastronomia3.png","Gastronomía 3"),
                 ("gastronomia4.png","Gastronomía 4")]),
    "eventos": ("Sección Eventos",
                [("eventos1.png","Evento 1"),
                 ("eventos2.png","Evento 2"),
                 ("eventos3.png","Evento 3"),
                 ("eventos4.png","Evento 4")]),
    "compras": ("Sección Compras",
                [("compras1.png","Compras 1"),
                 ("compras2.png","Compras 2"),
                 ("compras3.png","Compras 3"),
                 ("compras4.png","Compras 4")]),
    "rutas": ("Sección Rutas",
                [("rutas1.png","Ruta 1"),
                 ("rutas2.png","Ruta 2"),
                 ("rutas3.png","Ruta 3"),
                 ("rutas4.png","Ruta 4")]),
    "servicios": ("Sección Servicios",
                [("servicios1.png","Servicio 1"),
                 ("servicios2.png","Servicio 2"),
                 ("servicios3.png","Servicio 3"),
                 ("servicios4.png","Servicio 4")]),
}

# ========= KV DESIGN =========
kv = """
ScreenManager:
    MenuScreen:
    CategoriaScreen:

<MenuScreen>:
    name: "menu"
    BoxLayout:
        orientation: "vertical"
        spacing: dp(10)
        padding: dp(20)

        Label:
            text: "PALMAR GRANDE"
            font_size: '24sp'
            size_hint_y: None
            height: dp(40)

        Label:
            text: "Ubicación"
            font_size: '20sp'
            size_hint_y: None
            height: dp(30)
            halign: 'center'
            valign: 'middle'
            text_size: self.size

        MapView:
            lat: -28.055
            lon: -58.029
            zoom: 12
            size_hint_y: 0.4

        Button:
            text: "Ir a Palmar Grande"
            size_hint_y: None
            height: dp(50)
            background_color: (0.3, 0.6, 1, 1)
            on_release: app.ir_a_palmar()

        GridLayout:
            cols: 3
            rows: 3
            spacing: dp(10)
            size_hint_y: None
            height: dp(240)

            Button:
                text: "Turismo"
                background_color: (0.6,0.4,1,1)
                on_release: root.mostrar_categoria("turismo")
            Button:
                text: "Cultura"
                background_color: (0.2,0.7,0.7,1)
                on_release: root.mostrar_categoria("cultura")
            Button:
                text: "Alojamiento"
                background_color: (0.6,0.4,1,1)
                on_release: root.mostrar_categoria("alojamiento")
            Button:
                text: "Transporte"
                background_color: (0.2,0.7,0.7,1)
                on_release: root.mostrar_categoria("transporte")
            Button:
                text: "Gastronomía"
                background_color: (0.6,0.4,1,1)
                on_release: root.mostrar_categoria("gastronomia")
            Button:
                text: "Eventos"
                background_color: (0.2,0.7,0.7,1)
                on_release: root.mostrar_categoria("eventos")
            Button:
                text: "Compras"
                background_color: (0.6,0.4,1,1)
                on_release: root.mostrar_categoria("compras")
            Button:
                text: "Rutas"
                background_color: (0.2,0.7,0.7,1)
                on_release: root.mostrar_categoria("rutas")
            Button:
                text: "Servicios"
                background_color: (0.6,0.4,1,1)
                on_release: root.mostrar_categoria("servicios")

<CategoriaScreen>:
    name: "categoria"
    BoxLayout:
        orientation: "vertical"

        BoxLayout:
            size_hint_y: None
            height: dp(50)
            Button:
                text: "Volver"
                on_release: root.volver_menu()

        Label:
            id: titulo_categoria
            text: ""
            font_size: '20sp'
            size_hint_y: None
            height: dp(40)
            halign: 'center'
            valign: 'middle'
            text_size: self.size

        MapView:
            lat: -28.055
            lon: -58.029
            zoom: 12
            size_hint_y: 0.3

        ScrollView:
            do_scroll_x: False
            BoxLayout:
                id: content_box
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)
                padding: dp(10)
"""

# ========= IMAGEN BOTÓN PARA POPUP SOLO CON DESCRIPCIÓN Y BOTÓN CERRAR =========
class ImageButton(ButtonBehavior, Image):
    def __init__(self, desc, source_image, **kwargs):
        super().__init__(**kwargs)
        self.desc = desc
        self.source_image = source_image

    def on_release(self):
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        content.add_widget(Label(
            text=self.desc,
            font_size='16sp',
            halign='center',
            valign='middle',
            text_size=(300, None)
        ))
        close_button = Button(text="Cerrar", size_hint=(1, 0.3))
        content.add_widget(close_button)
        popup = Popup(title="Información", content=content, size_hint=(0.9, 0.4))
        close_button.bind(on_release=popup.dismiss)
        popup.open()

# ========= SCREENS =========
class MenuScreen(Screen):
    def mostrar_categoria(self, categoria):
        categoria_screen = self.manager.get_screen("categoria")
        categoria_screen.cargar_contenido(categoria)
        categoria_screen.ids.titulo_categoria.text = contenido_ejemplo[categoria][0]

        # Reproducir música solo en Cultura
        if categoria == "cultura":
            if categoria_screen.sound:
                categoria_screen.sound.stop()
            categoria_screen.sound = SoundLoader.load("cultura.mp3")
            if categoria_screen.sound:
                categoria_screen.sound.loop = True
                categoria_screen.sound.play()
        else:
            if categoria_screen.sound:
                categoria_screen.sound.stop()
                categoria_screen.sound = None

        self.manager.current = "categoria"

class CategoriaScreen(Screen):
    sound = None

    def cargar_contenido(self, categoria):
        self.ids.content_box.clear_widgets()
        _, elementos = contenido_ejemplo[categoria]
        for img_path, desc in elementos:
            self.ids.content_box.add_widget(ImageButton(source_image=img_path, desc=desc, size_hint_y=None, height=200))
            self.ids.content_box.add_widget(Label(text=desc, size_hint_y=None, height=30))

    def volver_menu(self):
        if self.sound:
            self.sound.stop()
            self.sound = None
        self.manager.current = "menu"

# ========= APP =========
class TurismoApp(App):
    def build(self):
        return Builder.load_string(kv)

    def ir_a_palmar(self):
        lat, lon = -27.942, -57.901
        url = f"https://www.google.com/maps/dir/?api=1&destination={lat},{lon}&travelmode=driving"
        webbrowser.open(url)

    def on_stop(self):
        # Detener música si la app se cierra
        categoria_screen = self.root.get_screen("categoria")
        if categoria_screen.sound:
            categoria_screen.sound.stop()
            categoria_screen.sound = None

if __name__ == "__main__":
    TurismoApp().run()
