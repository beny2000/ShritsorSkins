from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class TestApp(App):
    def build(self):
        self.x = TextInput(input_filter = 'str')
        self.x.bind(on_text_validate=self.r)
        return self.x
    def r(self):
        print(self.x)
TestApp().run()
