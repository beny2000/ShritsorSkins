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
        self.layout = StackLayout()
        anchor = AnchorLayout()
        self.new_player_btn = Button(text="Add New Players", size=(100, 100), size_hint=(None, None))
        anchor.add_widget(self.new_player_btn)
        self.new_player_btn.bind(on_press=self.new_players)
        self.add_widget(anchor)
        self.names_input(2)

    def names_input(self,num):

        for i in range(int(num)):
            txt_input1 = TextInput(text='Name', size=(100, 100), size_hint=(None, None))
            self.layout.add_widget(txt_input1)
            txt_input2 = TextInput(text='#', size=(100, 100), size_hint=(None, None))
            self.layout.add_widget(txt_input2)
            label_1 = Label(text='', size=(100, 100), size_hint=(None, None))
            self.layout.add_widget(label_1)
            txt_input3 = TextInput(text='name', size=(100, 100), size_hint=(None, None))
            self.layout.add_widget(txt_input3)
            txt_input4 = TextInput(text='#', size=(100, 100), size_hint=(None, None))
            self.layout.add_widget(txt_input4)
            self.players_dick.update({txt_input1:txt_input2})
            self.players_dick.update({txt_input3:txt_input4})
        self.add_widget(self.layout)

    def new_players(self,btn):
        return True

class MyJB(App):
    def build(self):

        parent = Container()

        return parent

if __name__ == '__main__':
    MyJB().run()