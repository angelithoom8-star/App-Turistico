
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
contenido_ejemplo = {
    "turismo": ("Sección Turismo",
                [("turismo1.png", "Estero Santa Lucía\n\n*Descripción técnica:* Ecosistema de humedal compuesto por lagunas, esteros y pastizales, ideal para el ecoturismo. Se puede realizar avistaje de aves, paseos en bote y caminatas interpretativas.\n*Actividad destacada:* Excursión guiada por los esteros y contacto con biodiversidad autóctona."),
                 ("turismo2.png", "Parque Nacional Mburucuyá\n\n*Descripción técnica:* Área protegida de más de 17.000 hectáreas que conserva ambientes de selva, pastizales y esteros. Ofrece senderos interpretativos, centro de visitantes y observación de fauna nativa.\n*Ubicación:* Ruta Provincial Nº 86, km 46.\n*Actividad destacada:* Senderismo, fotografía de flora y fauna."),
                 ("turismo3.png", "Murales Urbanos\n\n*Descripción técnica:* Intervenciones artísticas sobre muros públicos que reflejan identidad local, tradiciones y paisajes culturales.\n*Ubicación:* Centro de la localidad y entrada de Palmar Grande.\n*Actividad destacada:* Recorrido autoguiado de arte urbano."),
                 ("turismo4.png", "Cañada Fragosa\n\n*Descripción técnica:* Paisaje natural con cursos de agua y vegetación autóctona, ideal para actividades de esparcimiento, fotografía y picnic.\n*Acceso:* Ruta 87 desde Palmar Grande hasta Mburucuyá.")]),

    "cultura": ("Sección Cultura",
                [("cultura1.png", "Bailes Típicos\n\n*Descripción técnica:* Expresiones folklóricas regionales que incluyen danzas tradicionales como el chamamé, la zamba y la chacarera, acompañadas de vestimenta típica y música en vivo."),
                 ("cultura2.png", "Caminata con la Cruz José de los Milagros\n\n*Descripción técnica:* Peregrinación religiosa con fuerte contenido espiritual, realizada el 6 de octubre.\n*Hora de salida:* 00:00 hs\n*Actividad destacada:* Recorrido a pie, oración colectiva, devoción popular."),
                 ("cultura3.png", "Desfile Gaucho (11 de noviembre)\n\n*Descripción técnica:* Representación cultural de la tradición rural, donde jinetes participan en desfiles a caballo con vestimenta típica.\n*Ruta:* Desde Caa Catí hasta Mburucuyá."),
                 ("cultura4.png", "Ángeles Somos\n\n*Fecha:* 1 de noviembre\n*Descripción técnica:* Celebración religiosa donde niños recorren casas cantando coplas tradicionales y recolectan golosinas.\n*Actividad destacada:* Transmisión oral, participación infantil."),
                 ("cultura5.png", "Destrezas Criollas\n\n*Fecha:* 17 de agosto\n*Descripción técnica:* Competencias ecuestres que incluyen doma, jineteadas y carreras de sortijas. Promueven la identidad campesina y el espíritu gaucho.\n*Ubicación:* Establecimiento 'La Milagrosa'."),
                 ("cultura6.png|cultura.mp4", "Video Cultural - Disfruta de los eventos y tradiciones locales.")]),

    "alojamiento": ("Sección Alojamiento",
                [("alojamiento1.png", "Josecito Soloaga\n\n*Ubicación:* Av. Madariaga\n*Descripción técnica:* Hospedaje familiar de tipo rural, con ambiente tranquilo y atención personalizada. Ideal para el descanso y el turismo de naturaleza.")]),

    "transporte": ("Sección Transporte",
                [("transporte1.png", "Colectivo Rápido Bus\n\n*Salida:* 5:00 hs – *Regreso:* 13:00 hs\n*Descripción técnica:* Servicio de transporte interurbano que conecta localidades vecinas. Funciona lunes, miércoles y viernes."),
                 ("transporte2.png", "Remis Juan Gonzales – Cel: 3781-408745\n*Descripción técnica:* Transporte privado con chofer, ideal para traslados turísticos o por demanda. Servicio puerta a puerta."),
                 ("transporte3.png", "Remis Horacio Vedoya – Cel: 3781-609821\n*Descripción técnica:* Transporte privado con chofer, ideal para traslados turísticos o por demanda. Servicio puerta a puerta."),
                 ("transporte4.png", "Remis Cristian Barrios – Cel: 3794-771158\n*Descripción técnica:* Transporte privado con chofer, ideal para traslados turísticos o por demanda. Servicio puerta a puerta.")]),

    "gastronomia": ("Sección Gastronomía",
                [("gastronomia1.png", "Asado: Un método de cocción y una comida festiva, generalmente de carne, preparada a la parrilla o al fuego."),
                 ("gastronomia2.png", "Empanada: Una masa rellena, que puede ser horneada o frita, con una variedad de sabores, predominantemente salados."),
                 ("gastronomia3.png", "Chipacito: Pequeños bollos o panes horneados, populares como snack o acompañamiento, con una textura característica."),
                 ("gastronomia4.png", "Guiso: Un plato sustancioso y caliente, cocinado a fuego lento, popular en climas fríos como comida principal."),
                 ("gastronomia5.png", "Torta frita: Un tipo de masa frita, a menudo consumida como merienda, especialmente popular en días lluviosos."),
                 ("gastronomia6.png", "Mbaypu: Un plato cremoso y consistente, similar a una polenta suave, que se sirve caliente como comida principal o acompañamiento."),
                 ("gastronomia7.png", "Sopa paraguaya: A pesar de su nombre, es un pastel salado horneado, de consistencia firme y muy sabroso, un clásico de la gastronomía paraguaya."),
                 ("gastronomia8.png", "Locro: Un guiso espeso y sustancioso, tradicional en la región andina y el Cono Sur, popular en épocas frías o festividades.")]),

    "eventos": ("Sección Eventos",
            [("eventos1.png", "El quincho es el escenario principal de los festivales musicales que animan la Fiesta Patronal de Palmar Grande los días 2 y 3 de mayo. Este espacio se transforma en el epicentro de los eventos y celebraciones, acogiendo a diversos artistas y a la comunidad en general."),
             ("eventos2.png", "El 1 de mayo, la Estancia La Milagrosa celebra el Día del Trabajador con una jornada de festividades criollas. Desde las 9 de la mañana, se realizan destrezas como volteada de ternero, marcación, pialada de vacuno, prueba de rienda y jineteada en categorías crina y basto, con premios para los ganadores. Al finalizar las destrezas, la celebración continúa con una bailanteada chamamecera."),
             ("eventos3.png", "Fiestas Patronales de Palmar Grande los días 2 y 3 de mayo, en honor a la Santísima Cruz de los Milagros. El primer día se caracteriza por misas, procesiones y festivales musicales nocturnos. El segundo día, la comunidad disfruta de una misa y un almuerzo comunitario, con festivales que resuenan tanto de día como de noche."),
             ("eventos4.png", "Cada 12 de enero, San Jorge 2 se viste de fiesta para celebrar la tradicional Fiesta de la Sandía en el campo de la familia Cabrera, ubicado en la Ruta 13. Desde las 9 de la mañana, los visitantes se maravillan con la sandía más grande y pesada, disfrutan de emocionantes jineteadas y bailan al ritmo de conjuntos musicales hasta las 23hs. ¡Una jornada llena de sabor y tradición!"),
             ("eventos5.png|eventos.mp4", "Video de Eventos - Mira las actividades destacadas.")]),
    
    "compras": ("Sección Compras",
            [("compras1.png", "Mini Mercado Don Pedro\n\nUbicación: Av. San Martín s/n\n\nAlmacén de cercanía con productos de primera necesidad, alimentos y bebidas."),
             ("compras2.png", "Carnicería San Jorge\n\nUbicación: Av. Madariaga\n\nComercio especializado en carnes frescas, embutidos y productos regionales."),
             ("compras3.png", "Despensa y Carnicería\n\nUbicación: Madariaga\n\nTienda mixta que combina productos básicos y carnes locales."),
             ("compras4.png", "Autoservicio Super Jor\n\nUbicación: Av. Caa Catí\n\nSupermercado con variedad de alimentos, bebidas, artículos de limpieza y golosinas."),
             ("compras5.png", "Kiosco Leito\n\nUbicación: Centro del pueblo\n\nPunto de venta de snacks, bebidas y artículos varios.")]),
    
    
    "rutas": ("Sección Rutas",
          [("rutas1.png", "Bienvenidos a Palmar Grande\n\nCartel de ingreso principal que da la bienvenida a visitantes."),
           ("rutas2.png", "Desde Mburucuyá\n\nAcceso por Ruta 86 hasta Palmar Grande. Señalización adecuada hasta sitios turísticos."),
           ("rutas3.png", "Desde Corrientes Capital\n\nRuta 5 → Ruta 75 hasta llegar al pueblo. Vía directa y en buen estado."),
           ("rutas4.png", "Desde Caa Catí\n\nRuta 13 hasta Palmar Grande. Camino de acceso desde el oeste de la provincia.")]),

    

    "servicios": ("Sección Servicios",
              [("servicios5.png", "Municipalidad\n\nUbicación: Av. Caa Catí\n\nSede del gobierno local donde se gestionan trámites administrativos."),
               ("servicios6.png", "Cajero Automático\n\nUbicación: Av. Madariaga\n\nPunto de extracción de dinero y operaciones bancarias."),
               ("servicios7.png", "Sala de Primeros Auxilios\n\nUbicación: Av. Caa Catí\n\nCentro de atención médica básica y emergencias."),
               ("servicios3.png", "Club Deportivo\n\nUbicación: Av. Madariaga\n\nEspacio para práctica de deportes y actividades recreativas."),
               ("servicios4.png", "Comisaría\n\nUbicación: Av. San Martín\n\nDependencia de seguridad pública para atención de emergencias y prevención del delito."),
               ("servicios1.png", "Escuela Primaria N° 414\n\nUbicación: Av. Caa Catí\n\nInstitución educativa de nivel primario y secundario."),
               ("servicios2.png", "DEPEC\n\nUbicación: Av. Madariaga\n\nOrganismo público de servicios comunitarios y supervisión social."),
               ("servicios8.png", "Agua Potable\n\nUbicación: Av. Madariaga\n\nOficina de atención al público para consultas y reclamos sobre el servicio de agua."),
               ("servicios9.png", "Baños publicos\n\nPlaza central Palmar Grande\n\nModulo sanitario con instalaciones para personas con movilidad reducida, damas, caballeros y un área con agua caliente.")]),
                

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

        if "|" in source_image:  # Caso imagen + video
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
