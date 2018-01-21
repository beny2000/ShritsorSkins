from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MyWidget>:
    label_widget: label_widget
    BoxLayout:
        Button:
            text: 'Add Button'
            on_press: root.add_widget(label_widget)
        Button:
            text: 'Remove Button'
            on_press: root.remove_widget(label_widget)
        Label:
            id: label_widget
            text: 'widget'
""")

# Declare both screens
class MyWidget(BoxLayout):
    pass

# Create the screen manager

class TestApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    TestApp().run()