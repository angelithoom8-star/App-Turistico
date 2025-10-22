[app]
title = Palmar Grande
package.name = palmarg
package.domain =org.example
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,mp3,mp4
version = 1.0.0
requirements = python3,kivy,kivy_garden.mapview,pillow,plyer
orientation = portrait
fullscreen = 0
icon.filename = logo_app.jpeg
android.permissions = INTERNET, ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION
android.arch = armeabi-v7a, arm64-v8a
android.ndk_api = 21
android.minapi = 21
android.aab = True
android.extra_args = --ignore-setup-py
android.release_keystore = release.keystore
android.release_keyalias = palmargrande
android.release_keystore_pass = android
android.release_keyalias_pass = android
android.build_tools_version = 33.0.2

[buildozer]
log_level = 2
warn_on_root = 0
