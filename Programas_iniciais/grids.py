from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class DemoWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__()

        grid = GridLayout(rows = 2)

        for x in range(6):
            grid.add_widget(Button(text = 'x'))
        
        self.add_widget(grid)

class DemoApp(App):
    def build(self):

        return DemoWindow()

if __name__ == '__main__':
    DemoApp().run()