from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class DemoWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__()

        box = BoxLayout(orientation = 'vertical')

        lbl = Label(text = 'Primeiro')
        btn = Button(text= 'Second')
        box.add_widget(lbl)
        box.add_widget(btn)

        self.add_widget(box)

class DemoApp(App):
    def build(self):

        return DemoWindow()

if __name__ == '__main__':
    DemoApp().run()