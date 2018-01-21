from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        self.txt = "Hi"
        btn1= Button(text=self.txt)
        btn1.bind(on_press=self.buttonClicked)
        return btn1

    def buttonClicked(self,btn):
        self.txt = "Fuck You"
        btn1= Button(text=self.txt)
        btn1.bind(on_press=self.buttonClicked)
        return 'ass'

TestApp().run()