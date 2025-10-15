

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.mapview import MapView, MapMarker
from kivy.uix.popup import Popup
from kivy.uix.label import Label
Builder.load_string('''
<InicioScreen>:
    BoxLayout:
        orientation: 'vertical'
        MapView:
            id: map_view
            zoom: 5
            lat: -28.055
            lon: -58.029
            size_hint: (1, 1)

<TurismoScreen>:
    BoxLayout:
        Label:
            text: "Pantalla Turismo"

<CulturaScreen>:
    BoxLayout:
        Label:
            text: "Pantalla Cultura"

<AlojamientoScreen>:
    BoxLayout:
        Label:
            text: "Pantalla Alojamiento"

<TransporteScreen>:
    BoxLayout:
        Label:
            text: "Pantalla Transporte"

<GastronomiaScreen>:
    BoxLayout:
        Label:
            text: "Pantalla Gastronomía"

<EventosScreen>:
    BoxLayout:
        Label:
            text: "Pantalla Eventos"

<ComprasScreen>:
    BoxLayout:
        Label:
            text: "Pantalla Compras"

<RutasScreen>:
    BoxLayout:
        Label:
            text: "Pantalla Rutas"

<ServiciosScreen>:
    BoxLayout:
        Label:
            text: "Pantalla Servicios"
''')from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string('''
<InicioScreen>:
    BoxLayout:
        Label:
            text: "Hola Mundo"
''')

class InicioScreen(Screen):
    pass

class TurismoApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InicioScreen(name="inicio"))
        return sm

if __name__ == "__main__":
    TurismoApp().run()



class InicioScreen(Screen):
    pass

class TurismoScreen(Screen):
    pass

class CulturaScreen(Screen):
    pass

class AlojamientoScreen(Screen):
    pass

class TransporteScreen(Screen):
    pass

class GastronomiaScreen(Screen):
    pass

class EventosScreen(Screen):
    pass

class ComprasScreen(Screen):
    pass

class RutasScreen(Screen):
    pass

class ServiciosScreen(Screen):
    pass
if __name__ == "__main__":
    TurismoApp().run()
