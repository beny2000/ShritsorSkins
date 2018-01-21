import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyApp(App):
# layout
    def build(self):
        self.txt = 'What up'
        layout = AnchorLayout(anchor_x = 'right', anchor_y = 'bottom')
        btn1 = Button(text="OK")
        #btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)
        layout2 = AnchorLayout(anchor_x = 'left', anchor_y = 'top')
        btn2 = Button(text="OK")
        layout2.add_widget(btn2)
        return layout+layout2

# button click function
    def buttonClicked(self,btn):
        x = self.txt1.text
        y = self.txt2.text
        t = {x:y}
        self.lbl1.text = "You wrote " + self.txt1.text
# run app
if __name__ == "__main__":
    MyApp().run()