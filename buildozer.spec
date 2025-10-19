[app]
title = Palmar Grande
package.name = palmarg
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas
version = 1.0.0
requirements = python3,kivy,kivy_garden.mapview,pillow,plyer
orientation = portrait
fullscreen = 0
icon.filename = logo_app.jpeg

# Permisos necesarios
android.permissions = INTERNET, ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION

# Arquitecturas Android
android.arch = armeabi-v7a, arm64-v8a

# Nivel de API del NDK
android.ndk_api = 21

# Rutas manuales si usás SDK/NDK personalizado
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653

# Ignorar setup.py si da conflicto
android.extra_args = --ignore-setup-py

# Para generar .aab si querés publicar en Google Play
android.aab = True

# Firma para release (ajustá si tenés tu propio keystore)
android.release_keystore = release.keystore
android.release_keyalias = palmargrande
android.release_keystore_pass = android
android.release_keyalias_pass = android

[buildozer]
log_level = 2
warn_on_root = 0
