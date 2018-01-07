'''
Glossary of Terms:
bind: when and object is binded to a method via a action, means that when the action occurs to the object the method is called. ie
layout: the GUI structure in which the widgets are added to in order to displayed them in a organised way
widget: elements of GUI that preform task. ie TextInput
kivy language: python code with speific implentation for kivy, is used as alternate was to design UI, simialr to CSS
'''

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from algorthim import Players

class MainScreen(Screen):
    """ The Main Screen of the app where the names are inputed and teams are outputed

        Attributes:
            players_dick: dictionary of player names and respective skill rating 
            game_list: matrix of teams where first row is one team and the second row is another 
            current_page: holds which screen (input, output or help) is being currently displayed
            

    """

    def __init__(self, **kwargs):
        '''initilizes attributs and displays input widget on start up'''
        
        super(MainScreen, self).__init__(**kwargs)#inializes screen manager
        
        self.players_dick = {}
        self.game_list = []
        self.current_page = None
        
        self.input_page()#adds and displays all widgets related to input
        
        
    def input_page(self,*args):
        ''' method adds all relvent items(widgets) to screen, needed for the inputing of names, hence input page'''
        self.current_page = 'input'

        #creates layout scructure for widgets
        self.input_page_layout = BoxLayout(orientation= 'vertical') #main layout
        self.input_layout = GridLayout(cols=5, size_hint_y=None)#layout for input widgets
        self.input_scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        
        #creates text input widgets
        self.name_input1 = TextInput(text='Name', size_hint=(1, None),multiline=False) 
        self.skill_input1 = TextInput(text='0', size_hint=(1, None),multiline=False, input_filter= 'int')
        self.separator = Label(text='', size_hint=(0.2, None))
        self.name_input2 = TextInput(text='Name', size_hint=(1, None),multiline=False)
        self.skill_input2 = TextInput(text='0', size_hint=(1, None),multiline=False, input_filter= 'int')
        
        #add widgets to layout for input widgets
        self.input_layout.add_widget(self.name_input1)
        self.input_layout.add_widget(self.skill_input1)
        self.input_layout.add_widget(self.separator)
        self.input_layout.add_widget(self.name_input2)
        self.input_layout.add_widget(self.skill_input2)
        
        #allows widgets to be scroallble with scroll view
        self.input_layout.bind(minimum_height=self.input_layout.setter('height'))
        self.input_scroll.add_widget(self.input_layout)
        self.input_page_layout.add_widget(self.input_scroll)
        
        self.btns()# creates button to page
        
        self.input_page_layout.add_widget(self.btn_layout)#adds btns to main layout
        self.add_widget(self.input_page_layout)# adds layout to window
        
        
    def btns(self):
        '''method creates control buttons'''
        
        self.btn_layout = BoxLayout()#layout for btns
        
        #creates btns
        btn_add_new_players = Button(text='Add New \n players', size_hint=(1,None))
        btn_view_teams = Button(text='View \n Teams', size_hint=(1,None))
        btn_new_teams = Button(text='Make New \n Teams', size_hint=(1,None))
        btn_help = Button(text='Help', size_hint=(1,None))
        
        #binds buttons to methods, so that when button is pressed function is called
        btn_add_new_players.bind(on_press=self.new_players)
        btn_add_new_players.bind(on_press=self.update_dick)
        btn_view_teams.bind(on_press=self.make_teams)
        btn_new_teams.bind(on_press=self.new_teams)
        btn_help.bind(on_press = self.to_help)
        
        #adds btns to layout
        self.btn_layout.add_widget(btn_add_new_players)
        self.btn_layout.add_widget(btn_view_teams)
        self.btn_layout.add_widget(btn_new_teams)
        self.btn_layout.add_widget(btn_help)
        
        
    def to_help(self, *args):
        '''method changes screen to the help menu'''
        
        self.manager.current = 'help'#calls on the screen manger to set the curent screen to help
        self.current_page = 'help'


    def new_players(self,*args):
        '''adds more text input fields to input page '''
        
        #creates pop up in case error ocurs
        popup_btn = Button(text="Error not able add more players \n\n Click anywhere to close")
        popup = Popup(title='Error', content=popup_btn)
        popup_btn.bind(on_press= popup.dismiss)
            
        #make sure that the previous text widgets are not blank
        #fix: skills can be blank
        for i in self.players_dick.values():
            if i == '':
                popup.open()#displays popup
                self.players_dick[i]= 0
                return -1
        for i in self.players_dick.keys():
            if i == '':
                popup.open()
                del self.players_dick[i]
                return -1
        else:
            #creates text input widgets
            self.name_input1 = TextInput(text='Name', size_hint=(1, None),multiline=False)
            self.skill_input1 = TextInput(text='0', size_hint=(1, None),multiline=False, input_filter= 'int')
            self.label_1 = Label(text='', size_hint=(1, None))
            self.name_input2 = TextInput(text='Name', size_hint=(1, None),multiline=False)
            self.skill_input2 = TextInput(text='0', size_hint=(1, None),multiline=False, input_filter= 'int')
            
            #adds widgets to text input layout
            self.input_layout.add_widget(self.name_input1)
            self.input_layout.add_widget(self.skill_input1)
            self.input_layout.add_widget(self.label_1)
            self.input_layout.add_widget(self.name_input2)
            self.input_layout.add_widget(self.skill_input2)
            
            
    def update_dick(self,*args):
        '''method updates the dictonary of names and skills, with the text from the text input widgets'''
        
        if self.skill_input1.text != '' and self.skill_input2.text != '' :
            self.players_dick.update({self.name_input1.text:int(self.skill_input1.text), self.name_input2.text:int(self.skill_input2.text)})
        else:
            self.players_dick = {}
            popup_btn = Button(text="Already making teams \n\n Click anywhere to close")
            popup = Popup(title='Error', content=popup_btn)
            popup_btn.bind(on_press= popup.dismiss)
            popup.open()
        
    def new_teams(self,*args): 
        '''methods returns to input page so that user can input names again, making new teams'''
  
        if self.current_page == 'output': #makes sure that user is not trying to return to the input page while already at the input page
            self.players_dick = {}
            self.remove_widget(self.output_page_layout)#removes output page layout which contains all widgets
            self.input_page()#adds and displays all widgets related to input
        else:
            #creates and displays pop up when error occurs
            popup_btn = Button(text="Already making teams \n\n Click anywhere to close")
            popup = Popup(title='Error', content=popup_btn)
            popup_btn.bind(on_press= popup.dismiss)
            popup.open()
        
        
    def make_teams(self,*args):
        '''where the magic happens: method creates the teams'''
        
        self.update_dick()#gets most recent dictonary of names
        #print(self.players_dick)
        
        #creats pop up if error ocurrs
        popup_btn = Button(text="Error not able to show teams \n\n Click anywhere to close")
        popup = Popup(title='Error', content=popup_btn)
        popup_btn.bind(on_press= popup.dismiss)
        
        #make sure that new names and skill rating are not blank
        #fix: skils can be blank    
        for i in self.players_dick.values():
            if i == '':
                popup.open()
                self.players_dick[i]= 0
                return -1
            
        for i in self.players_dick.keys():
            if i == '':
                popup.open()
                del self.players_dick[i]
                return -1
            
        if len(self.players_dick) != 1 and len(self.players_dick) !=0  and self.current_page != 'output': #make sure that the diconray is not empty and that the input page is being displayed           
            #magic
            game = Players(self.players_dick)#makes diconry object of players class, see algorthim.py
            self.game_list = game.team_maker()#calls team_maker method to make teams with players class object
            
            self.remove_widget(self.input_page_layout)# removes the input layout which contains all the input related widgets
            self.output_names() # displays teams and names
            #print(self.game_list)
        else:
            popup.open()

            
        return self.game_list #not sure why its there to afraid to remove
    
    def output_names(self,*args):
        '''method displays names in their respective teams'''
        
        self.current_page = 'output'
        
        #layouts for output page
        self.output_page_layout = BoxLayout(orientation= 'vertical')#main layout
        self.output_layout = GridLayout(cols=2, size_hint_y=None)#layout for labels
        self.output_scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))   
        
        #creates and adds team name to layout
        shirts_lbl = Label(text="Shirts", size_hint=(1,None))
        skins_lbl = Label(text="Skins", size_hint=(1,None))
        self.output_layout.add_widget(skins_lbl)
        self.output_layout.add_widget(shirts_lbl)
            
        #splits game_list into its two teams     
        self.team1 = self.game_list[0]
        self.team2 = self.game_list[1]
        
        n = max(len(self.team2), len(self.team1))#see which team is longer, for odd num of names case
        
        for i in range(n):
            if self.game_list[0][i] == 'Name':#adds blank label for player with name = 'Name' 
                lbl = Label(text='', size_hint=(1,None))
            else:
                lbl = Label(text=self.game_list[0][i], size_hint=(1,None)) #adds name to team
            self.output_layout.add_widget(lbl)#adds name to display
                
            if self.game_list[1][i] == 'Name':#adds blank label for player with name = 'Name' 
                lbl1 = Label(text='', size_hint=(1,None))
            else:
                lbl1 = Label(text=self.game_list[1][i], size_hint=(1,None))#adds name to team
            self.output_layout.add_widget(lbl1)#adds name to display
                 
        self.output_layout.bind(minimum_height=self.output_layout.setter('height'))#allows scrollable
        self.output_scroll.add_widget(self.output_layout)
        self.output_page_layout.add_widget(self.output_scroll)
        
        self.btns()#creates control btns
        
        self.output_page_layout.add_widget(self.btn_layout)#adds controls btns to page
        self.add_widget(self.output_page_layout)#displays main layout in window
        
        
        
class HelpScreen(Screen):
        help_text =' Welcome to Shirts or Skins Help Menu \n In the textboxes label name, you would type the name of the player and in the textbox with the number 0 in it you would put that players skill. If more player are to be add plase mare sure to fill in the previous box before adding new players. Once all the name and respective skils are inputted you can tap on the view team button which will display the teams. If you would like to make new teams, tapping on the make new teams button will bring you  back to where you can input the players again. If anything is inputted incorrectly or any unallowed buttons are tapped the app will display and error message. If this occurs check to make sure that you did not leave any fields blank or that you did not tap a button that wants to bring to a page that your already on.\n Please report crashes to ben.morgenstern8@gmail.com. With you phone model, android version,what you where doing before the crash. \n\n Creators: Ben Morgenstern & Yasha Bershtatd \n Made with Kivy 1.9.0'

Builder.load_string("""   
<HelpScreen>
    BoxLayout:
        id: help_layout
        orientation: 'vertical'
        
        Label:
            text_size: self.width, None
            size_hint: 1, None
            height: self.texture_size[1]
            text: root.help_text
            padding_x: 10
        
        Label:
            text: ''
            size_hint: (0.7,None)
        Button:
            id: back
            size_hint: (1, None)
            text: 'Back'
            on_press: root.manager.current = 'main'
""") 
        
class MyApp(App):
    ''''class where app is build '''
    def build(self):
        '''builds app by creating object of the two classes and displaying their content, see kivy docs'''
        
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))#adds content of MainScreen class to app
        sm.add_widget(HelpScreen(name='help'))#adds content of HelpScreen class to app
        
        return sm

if __name__ == '__main__':
        MyApp().run()#runs app