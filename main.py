from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Red"

        return (
            MDScreen(
                MDRectangleFlatButton(
                    text="Hello, World",
                    pos_hint={"center_x": 0.9, "center_y": 0.9},
                )
            )
        )


MainApp().run()
from kivy.lang import Builder

from kivymd.app import MDApp


class Test(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(
            '''
MDScreen:

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Mail'
            icon: 'gmail'
            badge_icon: "numeric-10"

            MDLabel:
                text: 'Mail'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Twitter'
            icon: 'twitter'
            badge_icon: "numeric-5"

            MDLabel:
                text: 'Twitter'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'LinkedIN'
            icon: 'linkedin'

            MDLabel:
                text: 'LinkedIN'
                halign: 'center'
'''
        )


Test().run()