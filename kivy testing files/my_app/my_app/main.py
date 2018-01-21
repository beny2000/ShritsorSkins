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
from algorthim import Players
from __builtin__ import False


Builder.load_string("""
<InputScreen>:
    BoxLayout:
        id: box_layout
        Button:
            id: submit
            text: 'Submit Names'
            size: (100,100)
            size_hint: (1, None)
            on_press: root.update_dick()
            
        Button:
            id: help
            text: 'Help'
            size:(100,100)
            size_hint:(1,None)
            on_press: root.manager.current = 'help'
            
        Button:
            id: clear_players
            text: 'Clear Players'
            size:(100,100)
            size_hint:(1,None)
            on_press: root.clear_dick()
            
            
        Button:
            id: view_teams
            text: 'View Teams'
            size: (100,100)
            size_hint: (1, None)
            on_press: root.update_dick()
            on_press: root.make_teams()
            on_press: root.call_class()
            on_press: print(root.players_dick)
            on_press: root.manager.current = 'output'
            
        Button:
            id: add_new_players
            text: 'Add New Players'
            size: (100,100)
            size_hint: (1, None)
            on_press: root.new_players()
            on_press: root.update_dick()
        
        
<OutputScreen>:
    BoxLayout:

        Button:
            id: back_to_input
            size: (100,100)
            size_hint: (1, None)
            text: 'Back to Names'
            on_press: root.manager.current = 'input'
            
        Button:
            id: help
            text: 'Help'
            size:(100,100)
            size_hint:(1,None)
            on_press: root.manager.current = 'help'
            
        
            
<HelpScreen>
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: '*some help text*'
            
        Button:
            id: back_input
            size: (100,100)
            size_hint: (1, None)
            text: 'Back to Names'
            on_press: root.manager.current = 'input'
""")

class InputScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)
        self.sm = ScreenManager()
        self.players_dick = {}
        self.game_list = []
        #self.outputscreen_class = None
        #box_layout = BoxLayout()
        #btn  = Button(text= 'text', size=(100,100), size_hint = (1,None))
        #btn.bind(on_press = self.call_class())
        #self.ids.box_layout.add_widget(btn)
        self.layout = GridLayout(cols=5)
        self.txt_input1 = TextInput(text='Ben',size=(100, 100), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input1)
        self.txt_input2 = TextInput(text='2', size=(100, 100), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input2)
        self.label_1 = Label(text='', size=(100, 100), size_hint=(0.2, None))
        self.layout.add_widget(self.label_1)
        self.txt_input3 = TextInput(text='Max',size=(100, 100), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input3)
        self.txt_input4 = TextInput(text='1',size=(100, 100), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input4)
        self.add_widget(self.layout)

        
    def new_players(self,*args):
        
        self.txt_input1 = TextInput(text='Yasha', size=(100, 100), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input1)
        self.txt_input2 = TextInput(text='3', size=(100, 100), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input2)
        self.label_1 = Label(text='', size=(100, 100), size_hint=(1, None))
        self.layout.add_widget(self.label_1)
        self.txt_input3 = TextInput(text='Noah', size=(100, 100), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input3)
        self.txt_input4 = TextInput(text='4', size=(100, 100), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input4)
        
    def update_dick(self,*args):
        self.players_dick.update({self.txt_input1.text:int(self.txt_input2.text), self.txt_input3.text:int(self.txt_input4.text)})
        
    def clear_dick(self):    
        self.players_dick = {}
        
    def call_class(self):
        self.sm.add_widget(OutputScreen(name='output'))

    
    def make_teams(self,*args):
        game = Players(self.players_dick)
        self.game_list = game.team_maker()
        print(self.game_list)
        return self.game_list
        
class OutputScreen(InputScreen,Screen):
    def __init__(self,  **kwargs):
        super(OutputScreen, self).__init__(**kwargs)
        self.remove_widget(self.layout)
        self.main = GridLayout(cols=2)
        self.shirts_layout = GridLayout(cols=1)
        self.skins_layout = GridLayout(cols=1)
        shirts_lbl = Label(text="Shirts", size=(100,100), size_hint=(1,None))
        skins_lbl = Label(text="Skins", size=(100,100), size_hint=(1,None))
        self.shirts_layout.add_widget(shirts_lbl)
        self.skins_layout.add_widget(skins_lbl)
        
        self.main.add_widget(self.skins_layout)
        self.main.add_widget(self.shirts_layout)
        self.add_widget(self.main)
        #print(self.make_teams())
        
    def put_names(self):
        if len(self.game_list) == 2:
            self.team1 = self.game_list[0]
            self.team2 = self.game_list[1]
    
            for i in self.team1:
                lbl = Label(text=i, size=(100,100), size_hint=(1,None))
                self.shirts_layout.add_widget(lbl)
                
            for i in self.team2:
                lbl1 = Label(text=i, size=(100,100), size_hint=(1,None))
                self.skins_layout.add_widget(lbl1)
                
    
class HelpScreen(Screen):
    pass
        

class MyApp(InputScreen,App):
    def build(self):
        
        self.sm.add_widget(InputScreen(name='input'))
        self.sm.add_widget(OutputScreen(name='output'))
        self.sm.add_widget(HelpScreen(name='help'))
        
        
        return self.sm

if __name__ == '__main__':
    MyApp().run()