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
        id: box_layout
            Button:
            id: view_teams
            text: 'Change Screens'
            size: (100,100)
            size_hint: (1, None)
            on_press: root.manager.current = 'output'
        
        
<OutputScreen>:
    BoxLayout:

        Button:
            id: back_to_input
            size: (100,100)
            size_hint: (1, None)
            text: 'Back to Names'
            on_press: root.manager.current = 'input'
""")

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)
        self.layout = GridLayout(cols=5)
        self.txt_input1 = TextInput(text='Ben',size=(100, 100), size_hint=(1, None),multiline=False)
        self.layout.add_widget(self.txt_input1)
        self.add_widget(self.layout)

        
    def some_function(self,*args):
        self.some_list = [self.txt_input1.text,self.txt_input2.text]
        
class SecondScreen(FirstScreen,Screen):
    def __init__(self,  **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        self.remove_widget(self.layout)
        self.main_layout = GridLayout(cols=2)
        lbl = Label(text=self.some_list, size=(100,100), size_hint=(1,None))
        self.self.main_layout.add_widget(lbl)
        self.add_widget(self.main_layout)
                
class MyApp(InputScreen,App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(InputScreen(name='first_screen'))
        self.sm.add_widget(SecondScreen(name='second_screen'))
        
        
        return self.sm

if __name__ == '__main__':
    MyApp().run()
