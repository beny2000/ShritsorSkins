from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<InputScreen>:
    BoxLayout:
        Button:
            id: submit
            text: 'View Teams'
            size: (100,100)
            size_hint: (None, None)
            on_press: root.manager.current = 'output'
            on_press: root.update_dick()
            on_press: print(root.players_dick)
            
        Button:
            id: add_new_players
            text: 'Add New Players'
            size: (100,100)
            size_hint: (None, None)
            on_press: root.new_players()
        

<OutputScreen>:
    BoxLayout:
        Button:
            id: back_input
            size: (100,100)
            size_hint: (None, None)
            text: 'Back to Names'
            on_press: root.manager.current = 'input'
""")


class InputScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)
        self.players_dick = {}
        self.layout = GridLayout(cols=5)
        self.txt_input1 = TextInput(size=(100, 100), size_hint=(None, None),multiline=False)
        self.layout.add_widget(self.txt_input1)
        self.txt_input2 = TextInput(size=(100, 100), size_hint=(None, None),multiline=False)
        self.layout.add_widget(self.txt_input2)
        self.label_1 = Label(text='', size=(100, 100), size_hint=(None, None))
        self.layout.add_widget(self.label_1)
        self.txt_input3 = TextInput(size=(100, 100), size_hint=(None, None),multiline=False)
        self.layout.add_widget(self.txt_input3)
        self.txt_input4 = TextInput(size=(100, 100), size_hint=(None, None),multiline=False)
        self.layout.add_widget(self.txt_input4)
        self.add_widget(self.layout)
        #submit.bind(on_press=up)
        
    def new_players(self,*args):
        
        self.txt_input1 = TextInput(text='Name', size=(100, 100), size_hint=(None, None),multiline=False)
        self.layout.add_widget(self.txt_input1)
        self.txt_input2 = TextInput(text='#', size=(100, 100), size_hint=(None, None),multiline=False)
        self.layout.add_widget(self.txt_input2)
        self.label_1 = Label(text='', size=(100, 100), size_hint=(None, None))
        self.layout.add_widget(self.label_1)
        self.txt_input3 = TextInput(text='name', size=(100, 100), size_hint=(None, None),multiline=False)
        self.layout.add_widget(self.txt_input3)
        self.txt_input4 = TextInput(text='#', size=(100, 100), size_hint=(None, None),multiline=False)
        self.layout.add_widget(self.txt_input4)
        
    def update_dick(self,*args):
        self.players_dick.update({self.txt_input1.text:self.txt_input2.text, self.txt_input3.text:self.txt_input4.text})
        return self.players_dick
        
class OutputScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InputScreen(name='input'))
        sm.add_widget(OutputScreen(name='output'))
        
        return sm

if __name__ == '__main__':
    MyApp().run()