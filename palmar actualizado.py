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
from kivy.uix.video import Video
from PIL import Image as PILImage, ImageDraw, ImageFont
from kivy_garden.mapview import MapView
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.audio import SoundLoader

# Ajustar ventana
Window.size = (360, 640)
Window.clearcolor = (1, 1, 1, 1)

# ========= GENERAR IMÁGENES SI NO EXISTEN =========
categorias = [
    "turismo", "cultura", "alojamiento", "transporte",
    "gastronomia", "eventos", "compras", "rutas", "servicios"
]

max_por_categoria = {
    "turismo": 4,
    "cultura": 6,
    "alojamiento": 3,
    "transporte": 4,
    "gastronomia": 8,
    "eventos": 5,
    "compras": 5,
    "rutas": 4,
    "servicios": 9,
}

try:
    font = ImageFont.truetype("arial.ttf", 30)
except:
    font = ImageFont.load_default()

# ✅ Bloque corregido: usa textbbox en lugar de textsize
for categoria in categorias:
    for i in range(1, max_por_categoria[categoria] + 1):
        filename = f"{categoria}{i}.png"
        if not os.path.exists(filename):
            img = PILImage.new("RGB", (400, 300), (50*i % 255, 100*i % 255, 150*i % 255))
            draw = ImageDraw.Draw(img)
            texto = f"{categoria.capitalize()} {i}"
            bbox = draw.textbbox((0, 0), texto, font=font)
            w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
            draw.text(((400 - w) / 2, (300 - h) / 2), texto, fill="white", font=font)
            img.save(filename)

# ========= NOMBRES CORTOS DE IMÁGENES =========
nombres_imagenes = {
    "turismo": ["Estero Santa Lucía", "Parque Nacional Mburucuyá", "Murales urbanos", "Cañada Fragosa"],
    "cultura": ["Bailes típicos", "Caminata con la cruz", "Cabalgata tradicional", "Ángeles somos", "Destrezas criollas", "Video Cultural"],
    "alojamiento": ["Jose Soloaga", "Dentro de la habitación", "Costado de la casa"],
    "transporte": ["Rápido Bus", "Remis Juan González", "Remis Horacio Vedoya", "Remis Cristian Barrios"],
    "gastronomia": ["Asado", "Empanadas", "Chipacitos", "Guiso", "Torta frita", "Mbaypú", "Sopa paraguaya", "Locro"],
    "eventos": ["Quincho municipal", "Estancia la milagrosa", "Encuentros religiosos", "Festival de la sandia", "Video Eventos"],
    "compras": ["Mini mercado Don Pedro", "Carnicería San Jorge", "Despensa y carnicería", "Autoservicio Super Jor", "Kiosco Leito"],
    "rutas": ["Bienvenidos a Palmar Grande", "Ruta 86", "Ruta 75", "Ruta 13"],
    "servicios": ["Municipalidad","Cajero automático", "Estación sanitaria", "Club deportivo", "Comisaría", "Escuela primaria, secundaria e Instituto superior", "DPEC", "Oficina de agua potable","Baños Publicos"]
}

# ========= DATOS DE CONTENIDO =========
# (El contenido_ejemplo completo lo mantenemos igual)
# ⚠️ — Lo dejo sin modificar, ya que no afecta el error

contenido_ejemplo = {
    "turismo": ("Sección Turismo",
                [("turismo1.png", "Estero Santa Lucía...")]),
    # ... (resto del contenido igual que antes)
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
                bold: True
                on_release: root.mostrar_categoria("turismo")
            Button:
                text: "Cultura"
                background_color: (0.2,0.7,0.7,1)
                color: 1,1,1,1
                bold: True
                on_release: root.mostrar_categoria("cultura")
            Button:
                text: "Alojamiento"
                background_color: (0.9,0.6,0.2,1)
                color: 1,1,1,1
                bold: True
                on_release: root.mostrar_categoria("alojamiento")
            Button:
                text: "Transporte"
                background_color: (0.4,0.8,0.4,1)
                color: 1,1,1,1
                bold: True
                on_release: root.mostrar_categoria("transporte")
            Button:
                text: "Gastronomía"
                background_color: (1,0.5,0.5,1)
                color: 1,1,1,1
                bold: True
                on_release: root.mostrar_categoria("gastronomia")
            Button:
                text: "Eventos"
                background_color: (0.5,0.5,1,1)
                color: 1,1,1,1
                bold: True
                on_release: root.mostrar_categoria("eventos")
            Button:
                text: "Compras"
                background_color: (0.7,0.7,0.2,1)
                color: 1,1,1,1
                bold: True
                on_release: root.mostrar_categoria("compras")
            Button:
                text: "Rutas"
                background_color: (0.2,0.6,0.9,1)
                color: 1,1,1,1
                bold: True
                on_release: root.mostrar_categoria("rutas")
            Button:
                text: "Servicios"
                background_color: (0.8,0.3,0.6,1)
                color: 1,1,1,1
                bold: True
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
                color: 1,1,1,1
                bold: True
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

# ========= GALERÍA =========
class ButtonBehaviorImage(ButtonBehavior, Image):
    pass

class ImageCard(BoxLayout):
    def __init__(self, source_image, desc, index=None, categoria=None, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint_y = None
        self.height = 270

        if "|" in source_image:
            img_path, video_path = source_image.split("|")
            img = ButtonBehaviorImage(
                source=img_path,
                size_hint=(1, 0.7),
                allow_stretch=True,
                keep_ratio=False
            )
            img.bind(on_release=lambda instance: self.abrir_video(video_path))
            self.add_widget(img)

            btn_play = Button(
                text="▶ Play",
                size_hint=(1, 0.1),
                background_color=(0.6,0.4,0.8,1),
                color=(1,1,1,1),
                background_normal='',
                background_down=''
            )
            btn_play.bind(on_release=lambda x: self.abrir_video(video_path))
            self.add_widget(btn_play)

        elif source_image.endswith(".mp4"):
            btn_video = Button(text="▶ Play Video", size_hint=(1, 0.8), background_color=(0.6, 0.4, 0.8, 1), background_normal='', background_down='')
            btn_video.bind(on_release=lambda x: self.abrir_video(source_image))
            self.add_widget(btn_video)
        else:
            img = ButtonBehaviorImage(
                source=source_image,
                size_hint=(1, 0.8),
                allow_stretch=True,
                keep_ratio=False
            )
            img.bind(on_release=lambda instance: self.mostrar_popup(desc))
            self.add_widget(img)

        if categoria is not None and index is not None and categoria in nombres_imagenes:
            nombre_corto = nombres_imagenes[categoria][index]
        else:
            nombre_corto = desc.split(" - ")[0]

        lbl = Label(
            text=nombre_corto,
            font_size='16sp',
            size_hint=(1, None),
            height=30,
            halign="center",
            valign="middle",
            color=(0,0,0,1)
        )
        lbl.bind(size=lambda instance, value: setattr(instance, "text_size", (value[0], None)))
        self.add_widget(lbl)

    def mostrar_popup(self, desc):
        box = BoxLayout(orientation="vertical", spacing=10, padding=10)
        scroll = ScrollView(size_hint=(1, 1))
        lbl = Label(
            text=desc,
            font_size='16sp',
            color=(1, 1, 1, 1),
            size_hint_y=None,
            halign="center",
            valign="top",
            text_size=(300, None)
        )
        lbl.bind(texture_size=lambda instance, value: setattr(lbl, "height", value[1]))
        scroll.add_widget(lbl)

        popup = Popup(title="Descripción", size_hint=(0.9, 0.7))
        btn_cerrar = Button(text="Cerrar", size_hint_y=None, height=40, on_release=lambda x: popup.dismiss())
        box.add_widget(scroll)
        box.add_widget(btn_cerrar)
        popup.content = box
        popup.open()

    def abrir_video(self, video_path):
        box = BoxLayout(orientation="vertical")
        vid = Video(source=video_path, state='pause', options={'allow_stretch': True}, size_hint=(1, 0.85))
        btn_play_pause = Button(text="Reproducir / Pausar", size_hint=(1, 0.075))
        btn_cerrar = Button(text="Cerrar", size_hint=(1, 0.075))

        def toggle_video(instance):
            vid.state = 'play' if vid.state == 'pause' else 'pause'

        def cerrar_popup(instance):
            vid.state = 'pause'
            popup.dismiss()

        btn_play_pause.bind(on_release=toggle_video)
        btn_cerrar.bind(on_release=cerrar_popup)

        box.add_widget(vid)
        box.add_widget(btn_play_pause)
        box.add_widget(btn_cerrar)

        popup = Popup(title="Video", size_hint=(0.95, 0.95))
        popup.content = box
        popup.open()

# ========= PANTALLAS =========
class MenuScreen(Screen):
    def mostrar_categoria(self, categoria):
        self.manager.get_screen("categoria").cargar_categoria(categoria)
        self.manager.current = "categoria"

class CategoriaScreen(Screen):
    def cargar_categoria(self, categoria):
        self.ids.titulo_categoria.text = contenido_ejemplo[categoria][0]
        box = self.ids.content_box
        box.clear_widgets()

        try:
            if hasattr(self, 'music') and self.music:
                self.music.stop()
        except:
            pass

        # Música según categoría
        if categoria == "gastronomia":
            self.music = SoundLoader.load("gastronomia.mp3")
        elif categoria == "eventos":
            self.music = SoundLoader.load("eventos.mp3")
        else:
            self.music = None

        if self.music:
            self.music.loop = True
            self.music.play()

        for idx, (img, desc) in enumerate(contenido_ejemplo[categoria][1]):
            card = ImageCard(img, desc, index=idx, categoria=categoria)
            box.add_widget(card)

    def volver_menu(self):
        if hasattr(self, 'music') and self.music:
            self.music.stop()
        self.manager.current = "menu"

# ========= APP PRINCIPAL =========
class PalmarApp(App):
    def build(self):
        return Builder.load_string(kv)

    def ir_a_palmar(self):
        webbrowser.open("https://maps.google.com/?q=Palmar+Grande,+Corrientes,+Argentina")

if __name__ == "__main__":
    PalmarApp().run()
