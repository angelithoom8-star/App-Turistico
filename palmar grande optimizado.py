import os
import platform
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
from kivy.uix.video import Video
from kivy_garden.mapview import MapView
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.audio import SoundLoader
from PIL import Image as PILImage, ImageDraw, ImageFont

# ========= CONFIGURACIÓN MULTIPLATAFORMA =========
is_mobile = platform.system() in ["Android", "iOS"]

if not is_mobile:
    Window.size = (360, 640)
Window.clearcolor = (1, 1, 1, 1)

# ========= FUNCIONES DE RENDIMIENTO =========
def optimize_image(image_path, max_size=(512, 512)):
    """Reduce tamaño de imágenes para mejorar el rendimiento móvil"""
    try:
        if os.path.exists(image_path):
            with PILImage.open(image_path) as img:
                img.thumbnail(max_size)
                img.save(image_path, optimize=True, quality=85)
    except Exception:
        pass

# ========= FUENTE SEGURA =========
try:
    font = ImageFont.truetype("arial.ttf", 30)
except:
    font = ImageFont.load_default()

# ========= GENERACIÓN DE IMÁGENES (solo si faltan) =========
categorias = [
    "turismo", "cultura", "alojamiento", "transporte",
    "gastronomia", "eventos", "compras", "rutas", "servicios"
]

max_por_categoria = {
    "turismo": 4, "cultura": 6, "alojamiento": 3, "transporte": 4,
    "gastronomia": 8, "eventos": 5, "compras": 5, "rutas": 4, "servicios": 9,
}

for categoria in categorias:
    for i in range(1, max_por_categoria[categoria] + 1):
        filename = f"{categoria}{i}.png"
        if not os.path.exists(filename):
            img = PILImage.new("RGB", (400, 300), (50*i % 255, 100*i % 255, 150*i % 255))
            draw = ImageDraw.Draw(img)
            texto = f"{categoria.capitalize()} {i}"
            w, h = draw.textsize(texto, font=font)
            draw.text(((400-w)/2, (300-h)/2), texto, fill="white", font=font)
            img.save(filename)
        else:
            optimize_image(filename)

# ========= DATOS DE CONTENIDO (RESUMIDO DEL ORIGINAL) =========
# (Se conserva el mismo contenido original que tenías)
# --- OMITIDO AQUÍ POR BREVEDAD, DEJAR IGUAL EN TU ARCHIVO ---
# contenido_ejemplo = {...}
# nombres_imagenes = {...}

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

        BoxLayout:
            orientation: "horizontal"
            size_hint_y: None
            height: dp(60)
            spacing: dp(10)
            Image:
                source: "logo.png"
                size_hint: None, None
                size: dp(50), dp(50)
                allow_stretch: True
                keep_ratio: True
            Label:
                text: "PALMAR GRANDE"
                font_size: '24sp'
                color: 0,0,0,1
                valign: 'middle'
                halign: 'left'
                text_size: self.size

        Label:
            text: "Ubicación"
            font_size: '20sp'
            size_hint_y: None
            height: dp(30)
            halign: 'center'
            valign: 'middle'
            text_size: self.size
            color: 0,0,0,1

        MapView:
            id: map_view
            lat: -28.055
            lon: -58.029
            zoom: 12
            size_hint_y: 0.4

        Button:
            text: "Ir a Palmar Grande"
            size_hint_y: None
            height: dp(50)
            background_color: (0.3, 0.6, 1, 1)
            color: 1,1,1,1
            bold: True
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
                color: 1,1,1,1
                on_release: root.mostrar_categoria("turismo")
            Button:
                text: "Cultura"
                background_color: (0.2,0.7,0.7,1)
                color: 1,1,1,1
                on_release: root.mostrar_categoria("cultura")
            Button:
                text: "Alojamiento"
                background_color: (0.9,0.6,0.2,1)
                color: 1,1,1,1
                on_release: root.mostrar_categoria("alojamiento")
            Button:
                text: "Transporte"
                background_color: (0.4,0.8,0.4,1)
                color: 1,1,1,1
                on_release: root.mostrar_categoria("transporte")
            Button:
                text: "Gastronomía"
                background_color: (1,0.5,0.5,1)
                color: 1,1,1,1
                on_release: root.mostrar_categoria("gastronomia")
            Button:
                text: "Eventos"
                background_color: (0.5,0.5,1,1)
                color: 1,1,1,1
                on_release: root.mostrar_categoria("eventos")
            Button:
                text: "Compras"
                background_color: (0.7,0.7,0.2,1)
                color: 1,1,1,1
                on_release: root.mostrar_categoria("compras")
            Button:
                text: "Rutas"
                background_color: (0.2,0.6,0.9,1)
                color: 1,1,1,1
                on_release: root.mostrar_categoria("rutas")
            Button:
                text: "Servicios"
                background_color: (0.8,0.3,0.6,1)
                color: 1,1,1,1
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
            color: 0,0,0,1
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

# ========= CLASES =========
class ButtonBehaviorImage(ButtonBehavior, Image):
    pass

class ImageCard(BoxLayout):
    def __init__(self, source_image, desc, index=None, categoria=None, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint_y = None
        self.height = 270
        optimize_image(source_image)  # reducción inmediata

        if "|" in source_image:
            img_path, video_path = source_image.split("|")
            img = ButtonBehaviorImage(source=img_path, allow_stretch=True, keep_ratio=False)
            img.bind(on_release=lambda _: self.abrir_video(video_path))
            self.add_widget(img)
            self.add_widget(Button(text="▶ Play", size_hint=(1, 0.1),
                                   background_color=(0.6,0.4,0.8,1),
                                   on_release=lambda _: self.abrir_video(video_path)))
        else:
            img = ButtonBehaviorImage(source=source_image, allow_stretch=True, keep_ratio=False)
            img.bind(on_release=lambda _: self.mostrar_popup(desc))
            self.add_widget(img)

        nombre_corto = desc.split("\n")[0][:40]
        self.add_widget(Label(text=nombre_corto, font_size='16sp', color=(0,0,0,1), size_hint_y=None, height=30))

    def mostrar_popup(self, desc):
        lbl = Label(text=desc, font_size='16sp', color=(1,1,1,1),
                    size_hint_y=None, halign="center", valign="top", text_size=(300, None))
        lbl.bind(texture_size=lambda _, v: setattr(lbl, "height", v[1]))
        scroll = ScrollView(); scroll.add_widget(lbl)
        content = BoxLayout(orientation="vertical", spacing=10)
        content.add_widget(scroll)
        content.add_widget(Button(text="Cerrar", size_hint_y=None, height=40,
                                  on_release=lambda x: popup.dismiss()))
        popup = Popup(title="Descripción", content=content, size_hint=(0.9, 0.7))
        popup.open()

    def abrir_video(self, video_path):
        vid = Video(source=video_path, state='pause', options={'allow_stretch': True})
        box = BoxLayout(orientation="vertical")
        btn_play_pause = Button(text="Reproducir / Pausar", size_hint_y=None, height=40)
        btn_close = Button(text="Cerrar", size_hint_y=None, height=40)

        popup = Popup(title="Video", content=box, size_hint=(0.95, 0.95))

        def toggle(_): vid.state = 'play' if vid.state == 'pause' else 'pause'
        def close(_):
            vid.state = 'pause'
            popup.dismiss()
            vid.unload()  # libera memoria
        btn_play_pause.bind(on_release=toggle)
        btn_close.bind(on_release=close)

        box.add_widget(vid)
        box.add_widget(btn_play_pause)
        box.add_widget(btn_close)
        popup.open()

class MenuScreen(Screen):
    def on_enter(self):
        # Desactiva el mapa en móviles si es pesado
        if is_mobile:
            self.ids.map_view.disabled = True
            self.ids.map_view.opacity = 0
    def mostrar_categoria(self, categoria):
        self.manager.get_screen("categoria").cargar_categoria(categoria)
        self.manager.current = "categoria"

class CategoriaScreen(Screen):
    def cargar_categoria(self, categoria):
        from threading import Thread
        self.ids.titulo_categoria.text = contenido_ejemplo[categoria][0]
        box = self.ids.content_box
        box.clear_widgets()
        if hasattr(self, 'music') and self.music:
            self.music.stop()
        self.music = None
        if categoria in ["gastronomia", "eventos"]:
            self.music = SoundLoader.load(f"{categoria}.mp3")
            if self.music:
                self.music.loop = True
                self.music.play()
        # carga diferida de imágenes
        def cargar():
            for idx, (img, desc) in enumerate(contenido_ejemplo[categoria][1]):
                card = ImageCard(img, desc, index=idx, categoria=categoria)
                box.add_widget(card)
        Thread(target=cargar).start()

    def volver_menu(self):
        if hasattr(self, 'music') and self.music:
            self.music.stop()
        self.manager.current = "menu"

# ========= APP PRINCIPAL =========
class PalmarApp(App):
    def build(self):
        return Builder.load_string(kv)

    def ir_a_palmar(self):
        try:
            webbrowser.open("https://maps.google.com/?q=Palmar+Grande,+Corrientes,+Argentina")
        except:
            pass

if __name__ == "__main__":
    PalmarApp().run()

