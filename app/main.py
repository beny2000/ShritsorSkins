from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from algorthim import Players
from kivy.uix.boxlayout import BoxLayout

Builder.load_string("""
<MainScreen>:
    BoxLayout:
         
        Button:
            id: add_new_players
            text: 'Add New Players'
            size: (200,200)

            size_hint: (1, None)
            text_size_hint: (1, None)
            on_press: root.new_players()
            on_press: root.update_dick()
        
        Button:
            id: submit
            text: 'Submit Names'
            size: (200,200)
            size_hint: (1, None)
            on_press: root.make_teams()
            
            on_press: print(root.players_dick)
            
        Button:
            id: new_teams
            text: 'Make new Teams'
            size: (200,200)

            size_hint: (1, None)
            on_press: root.new_teams()
            on_press: root.add_input()   
            
        Button:
            id: help
            text: 'Help'
            size:(200,200)
            size_hint:(1,None)
            on_press: root.manager.current = 'help'            
        
            
<HelpScreen>
    BoxLayout:
        orientation: 'vertical'
        
        Label:
            text: '*some help text*'
            
        Button:
            id: back
            size: (200,200)
            size_hint: (1, None)
            text: 'Back'
            on_press: root.manager.current = 'main'
""")

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.main_box = BoxLayout(orientation= 'vertical')
        self.players_dick = {}
        self.game_list = []
        self.add_input()
        
    def add_input(self):
        self.layout = GridLayout(cols=5)
        self.txt_input1 = TextInput(text='Ben',size=(200, 200), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input1)
        self.txt_input2 = TextInput(text='2', size=(200, 200), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input2)
        self.label_1 = Label(text='', size=(200, 200), size_hint=(0.2, None))
        self.layout.add_widget(self.label_1)
        self.txt_input3 = TextInput(text='Max',size=(200, 200), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input3)
        self.txt_input4 = TextInput(text='1',size=(200, 200), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input4)
        self.add_widget(self.layout)
        
    def new_players(self,*args):
        self.txt_input1 = TextInput(text='Yasha', size=(200, 200), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input1)
        self.txt_input2 = TextInput(text='3', size=(200, 200), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input2)
        self.label_1 = Label(text='', size=(200, 200), size_hint=(1, None))
        self.layout.add_widget(self.label_1)
        self.txt_input3 = TextInput(text='Noah', size=(200, 200), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input3)
        self.txt_input4 = TextInput(text='4', size=(200, 200), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input4)
        
    def update_dick(self,*args):
        self.players_dick.update({self.txt_input1.text:int(self.txt_input2.text), self.txt_input3.text:int(self.txt_input4.text)})
        
    def new_teams(self):    
        self.players_dick = {}
        self.remove_widget(self.layout1)
        
    def make_teams(self,*args):
        self.update_dick()
        game = Players(self.players_dick)
        self.game_list = game.team_maker()
        self.remove_widget(self.layout)
        self.put_names()
        
        print(self.game_list)
        return self.game_list
    
    def put_names(self):
        self.layout1 = GridLayout(cols=2)
        self.shirts_layout = GridLayout(cols=1)
        self.skins_layout = GridLayout(cols=1)
            
        shirts_lbl = Label(text="Shirts", size=(200,200), size_hint=(1,None))
        skins_lbl = Label(text="Skins", size=(200,200), size_hint=(1,None))
        self.layout1.add_widget(skins_lbl)
        self.layout1.add_widget(shirts_lbl)
            
        self.team1 = self.game_list[0]
        self.team2 = self.game_list[1]
        n = max(len(self.team2), len(self.team1))
            
        for i in range(n):
            if self.game_list[0][i] == 'Name':
                lbl = Label(text='', size=(200,200), size_hint=(1,None))
            else:
                lbl = Label(text=self.game_list[0][i], size=(200,200), size_hint=(1,None))    
            self.layout1.add_widget(lbl)
                
            if self.game_list[1][i] == 'Name':
                lbl1 = Label(text='', size=(200,200), size_hint=(1,None))
            else:
                lbl1 = Label(text=self.game_list[1][i], size=(200,200), size_hint=(1,None))
            self.layout1.add_widget(lbl1)
                 
        self.add_widget(self.layout1)
        
 
        
class HelpScreen(Screen):
    pass
        
        
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(HelpScreen(name='help'))
        return sm

if __name__ == '__main__':
        MyApp().run()
