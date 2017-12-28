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
from kivy.clock import Clock
from algorthim import Players
from distutils.fancy_getopt import fancy_getopt

#on_press: root.manager.current = 'output'
Builder.load_string("""
<InputScreen>:
    BoxLayout:
         
        Button:
            id: add_new_players
            text: 'Add New Players'
            size: (100,100)
            size_hint: (1, None)
            on_press: root.new_players()
            on_press: root.update_dick()
        
        Button:
            id: submit
            text: 'Submit Names'
            size: (100,100)
            size_hint: (1, None)
            on_press: root.update_dick()
            
        Button:
            id: view_teams
            text: 'View Teams'
            size: (100,100)
            size_hint: (1, None)
            on_press: root.remove_widget(root.layout)
            on_press: root.put_names()
            on_press: root.update_dick()
            on_press: root.make_teams()
            on_press: print(root.players_dick)
            
        Button:
            id: new_teams
            text: 'Make new Teams'
            size: (100,100)
            size_hint: (1, None)
            on_press: root.remove_widget(root.layout1)
            on_press: root.clear_dick()
            on_press: root.add_input()    
            
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
        self.players_dick = {}
        self.game_list = ['test value']
        self.add_input()
        
    def add_input(self):
        
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
        if self.change_screens == True:
            return True
        else:
            return False
        
    def clear(self):
        self.remove_widget(self.layout)

    def make_teams(self,*args):
        game = Players(self.players_dick)
        self.game_list = game.team_maker()
        print(self.game_list)
        return self.game_list
    
    def put_names(self):
        self.layout1 = GridLayout(cols=2)
        self.shirts_layout = GridLayout(cols=1)
        self.skins_layout = GridLayout(cols=1)
        shirts_lbl = Label(text="Shirts", size=(100,100), size_hint=(1,None))
        skins_lbl = Label(text="Skins", size=(100,100), size_hint=(1,None))
        self.layout1.add_widget(skins_lbl)
        self.layout1.add_widget(shirts_lbl)
        
        self.team1 = self.game_list[0]
        self.team2 = self.game_list[1]
        n = max(len(self.team2), len(self.team1))
        #print(n)
        for i in range(n):
                
            if self.game_list[0][i] == 'Name':
                lbl = Label(text='', size=(100,100), size_hint=(1,None))
            else:
                lbl = Label(text=self.game_list[0][i], size=(100,100), size_hint=(1,None))    
            
            self.layout1.add_widget(lbl)
            
                
            if self.game_list[1][i] == 'Name':
                lbl1 = Label(text='', size=(100,100), size_hint=(1,None))
            else:
                lbl1 = Label(text=self.game_list[1][i], size=(100,100), size_hint=(1,None))   
            
            self.layout1.add_widget(lbl1)
                
        self.add_widget(self.layout1)
 
        
class HelpScreen(Screen):
    pass
        
        
class MyApp(InputScreen,App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(InputScreen(name='input'))
        self.sm.add_widget(HelpScreen(name='help'))
        
        return self.sm

if __name__ == '__main__':
    
        MyApp().run()