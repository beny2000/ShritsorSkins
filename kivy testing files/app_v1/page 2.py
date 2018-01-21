from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
#from algor import team_maker

class Container(FloatLayout):
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        self.players_dick = {}
        anchor = AnchorLayout()
        self.new_player_btn = Button(text="New players", size=(100, 100), size_hint=(None, None))
        anchor.add_widget(self.restart)
        #self.new_player_btn.bind(on_press=self.new_players)
        self.add_widget(anchor)
        self.stack1 = StackLayout()
        self.names_input(2)

    def names_input(self,num):

        for i in range(int(num)):
            txt_lbl1 = Label(text='Name', size=(100, 100), size_hint=(None, None))
            self.stack1.add_widget(txt_lbl1)
            txt_lbl2 = Label(text='#', size=(100, 100), size_hint=(None, None))
            self.stack1.add_widget(txt_lbl2)
            label_1 = Label(text='', size=(100, 100), size_hint=(None, None))
            self.stack1.add_widget(label_1)
            txt_lbl3 = Label(text='name', size=(100, 100), size_hint=(None, None))
            self.stack1.add_widget(txt_lbl3)
            txt_lbl4 = Label(text='#', size=(100, 100), size_hint=(None, None))
            self.stack1.add_widget(txt_lbl4)
        self.add_widget(self.stack1)

    def restart(self,btn):
        open('main.py')

class MyJB(App):
    def build(self):

        parent = Container()

        return parent

if __name__ == '__main__':
    MyJB().run()