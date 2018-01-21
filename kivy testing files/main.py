from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        self.layout = BoxLayout()
        btn = Button(text='Hello World')
        btn.bind(on_press=self.new_label)
        self.layout.add_widget(btn)
        return self.layout

    def new_label(self,btn):
        lbl = Label(text = 'New Label')
        self.layout.add_widget(lbl)

TestApp().run()