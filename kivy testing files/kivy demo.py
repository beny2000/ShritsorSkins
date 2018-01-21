from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        self.layout = BoxLayout(orientation= 'vertical')
        lbl  = Label(text='This is a label')
        btn = Button(text='This is a button')
        self.layout.add_widget(lbl)
        self.layout.add_widget(btn)
        return self.layout
TestApp().run()
