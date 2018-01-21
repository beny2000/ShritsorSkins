from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<FirstScreen>:
    BoxLayout:
        id: box_layout

        TextInput:
            id: text_input
            text: 'text'

        Button:
            id: view_teams
            text: 'Change Screens'
            size: (100,100)
            size_hint: (1, None)
            on_press: root.some_function()
            on_press: root.manager.current = 'second_screen'


<SecondScreen>:
    BoxLayout:

        Button:
            id: back_to_input
            size: (100,100)
            size_hint: (1, None)
            text: 'Back to  first screen'
            on_press: root.manager.current = 'first_screen'
""")

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)
        self.some_text = ''

    def some_function(self,*args):
        self.some_text = self.ids['text_input'].text


class SecondScreen(FirstScreen,Screen):
    def __init__(self,  **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        self.remove_widget(self.ids.box_layout)
        lbl = Label(text= self.ids['text_input'].text)
        self.add_widget(lbl)


class MyApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(FirstScreen(name='first_screen'))
        self.sm.add_widget(SecondScreen(name='second_screen'))

        return self.sm

if __name__ == '__main__':
    MyApp().run()
