from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from algorthim import Players

Builder.load_string("""            
<HelpScreen>
    BoxLayout:
        id: help_layout
        orientation: 'vertical'
        
        Label:
            text: '*some help text*'
            
        Button:
            id: back
            size_hint: (1, None)
            text: 'Back'
            on_press: root.manager.current = 'main'
""")

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.players_dick = {}
        self.game_list = []
        
        self.input_page()
        
    def input_page(self,*args):
        self.input_page_layout = BoxLayout(orientation= 'vertical')
        
        self.input_layout = GridLayout(cols=5, size_hint_y=None)
        self.input_scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        self.txt_input1 = TextInput(text='Name', size_hint=(1, None),multiline=False)
        self.input_layout.add_widget(self.txt_input1)
        self.txt_input2 = TextInput(text='0', size_hint=(1, None),multiline=False)
        self.input_layout.add_widget(self.txt_input2)
        self.label_1 = Label(text='', size_hint=(0.2, None))
        self.input_layout.add_widget(self.label_1)
        self.txt_input3 = TextInput(text='Name', size_hint=(1, None),multiline=False)
        self.input_layout.add_widget(self.txt_input3)
        self.txt_input4 = TextInput(text='0', size_hint=(1, None),multiline=False)
        self.input_layout.add_widget(self.txt_input4)
        self.input_layout.bind(minimum_height=self.input_layout.setter('height'))
        self.input_scroll.add_widget(self.input_layout)
        self.input_page_layout.add_widget(self.input_scroll)
        
        self.btns()
        self.input_page_layout.add_widget(self.btn_layout)
        self.add_widget(self.input_page_layout)
        
    def btns(self):
        self.btn_layout = BoxLayout()
        btn_add_new_players = Button(text='Add New \n players', size_hint=(1,None))
        btn_view_teams = Button(text='View \n Teams', size_hint=(1,None))
        btn_new_teams = Button(text='Make New \n Teams', size_hint=(1,None))
        btn_help = Button(text='Help', size_hint=(1,None))
        btn_add_new_players.bind(on_press=self.new_players)
        btn_add_new_players.bind(on_press=self.update_dick)
        btn_view_teams.bind(on_press=self.make_teams)
        btn_new_teams.bind(on_press=self.new_teams)
        btn_new_teams.bind(on_press=self.input_page)
        btn_help.bind(on_press = self.to_help)
        self.btn_layout.add_widget(btn_add_new_players)
        self.btn_layout.add_widget(btn_view_teams)
        self.btn_layout.add_widget(btn_new_teams)
        self.btn_layout.add_widget(btn_help)
        
        
    def to_help(self, *args):
        self.manager.current = 'help'

    def new_players(self,*args):
        self.txt_input1 = TextInput(text='Name', size_hint=(1, None),multiline=False)
        self.input_layout.add_widget(self.txt_input1)
        self.txt_input2 = TextInput(text='0', size_hint=(1, None),multiline=False)
        self.input_layout.add_widget(self.txt_input2)
        self.label_1 = Label(text='', size_hint=(1, None))
        self.input_layout.add_widget(self.label_1)
        self.txt_input3 = TextInput(text='Name', size_hint=(1, None),multiline=False)
        self.input_layout.add_widget(self.txt_input3)
        self.txt_input4 = TextInput(text='0', size_hint=(1, None),multiline=False)
        self.input_layout.add_widget(self.txt_input4)
        
        
    def update_dick(self,*args):
        self.players_dick.update({self.txt_input1.text:int(self.txt_input2.text), self.txt_input3.text:int(self.txt_input4.text)})
        
    def new_teams(self,*args):    
        self.players_dick = {}
        self.remove_widget(self.output_page_layout)
        
    def make_teams(self,*args):
        self.update_dick()
        game = Players(self.players_dick)
        self.game_list = game.team_maker()
        self.remove_widget(self.input_page_layout)
        self.put_names()
        
        print(self.game_list)
        return self.game_list
    
    def put_names(self,*args):
        self.output_page_layout = BoxLayout(orientation= 'vertical')
        
        self.output_layout = GridLayout(cols=2, size_hint_y=None)
        self.output_scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))   
        
        shirts_lbl = Label(text="Shirts", size_hint=(1,None))
        skins_lbl = Label(text="Skins", size_hint=(1,None))
        self.output_layout.add_widget(skins_lbl)
        self.output_layout.add_widget(shirts_lbl)
            
        self.team1 = self.game_list[0]
        self.team2 = self.game_list[1]
        n = max(len(self.team2), len(self.team1))
            
        for i in range(n):
            if self.game_list[0][i] == 'Name':
                lbl = Label(text='', size_hint=(1,None))
            else:
                lbl = Label(text=self.game_list[0][i], size_hint=(1,None))    
            self.output_layout.add_widget(lbl)
                
            if self.game_list[1][i] == 'Name':
                lbl1 = Label(text='', size_hint=(1,None))
            else:
                lbl1 = Label(text=self.game_list[1][i], size_hint=(1,None))
            self.output_layout.add_widget(lbl1)
                 
        #self.input_page_layout.add_widget(self.output_layout)
        #self.add_widget(self.input_page_layout)
        
        #self.output_page_layout.add_widget(self.output_layout)
        self.output_layout.bind(minimum_height=self.output_layout.setter('height'))
        self.output_scroll.add_widget(self.output_layout)
        self.output_page_layout.add_widget(self.output_scroll)
        
        self.btns()
        self.output_page_layout.add_widget(self.btn_layout)
        self.add_widget(self.output_page_layout)
        
        
        
 
class HelpScreen(Screen):
    pass
        
        
class MyApp(MainScreen,App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(HelpScreen(name='help'))
        return self.sm

if __name__ == '__main__':
        MyApp().run()