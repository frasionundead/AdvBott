from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class AdvBotApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, I'm Telegram UserBot for sending your advertisements messages", halign="center")


AdvBotApp().run()
