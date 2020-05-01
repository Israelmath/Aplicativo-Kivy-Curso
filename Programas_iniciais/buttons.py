from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class ButtonWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__()
        self.padding = 50

        btn = Button(text = 'Click me')
        btn.onrelease = self.print_name
        btn.color = (1,1,1,1)
        btn.background_color = (1,0,1,1)
        # Normalmente o background é da cor cinza, como um botão normal,
        # para excluir esse fundo, basta escrevermos esse código abaixo
        btn.background_normal = ''
        self.add_widget(btn)

    def print_name(self):
        print('Hello, Israel')

class ButtonsApp(App):
    def build(self):

        return ButtonWindow()

if __name__ == '__main__':
    ButtonsApp().run()