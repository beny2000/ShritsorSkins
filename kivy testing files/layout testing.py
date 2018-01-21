from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput




class Container(FloatLayout):
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)

        stack1 = StackLayout()
        lbl = Label(text='Name', size=(100, 100), size_hint=(None, None))
        stack1.add_widget(lbl)

        lbl1 = Label(text='#', size=(100, 100), size_hint=(None, None))
        stack1.add_widget(lbl1)
        lbl2 = Label(text='', size=(100, 100), size_hint=(None, None))
        stack1.add_widget(lbl2)
        lbl3 = Label(text='name', size=(100, 100), size_hint=(None, None))
        stack1.add_widget(lbl3)
        lbl4 = Label(text='#', size=(100, 100), size_hint=(None, None))
        stack1.add_widget(lbl4)
        lbl5 = Label(text='name', size=(100, 100), size_hint=(None, None))
        stack1.add_widget(lbl5)
        lbl6 = Label(text='#', size=(100, 100), size_hint=(None, None))
        stack1.add_widget(lbl6)
        #self.lbl1 = Label(text=self.txt)
        self.add_widget(stack1)

class MyJB(App):
    def build(self):

        parent = Container()

        return parent

if __name__ == '__main__':
    MyJB().run()