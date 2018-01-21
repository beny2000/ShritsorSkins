from  kivy.uix.popup import Popup
from  kivy.uix.label import Label

popup = Popup(title='Test popup', content=Label(text='Hello world'),
              auto_dismiss=False)
popup.open()