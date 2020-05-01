from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.base import EventLoop

EventLoop.ensure_window()

import os

class GalleryWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__()

        # im = Image(source = 'imgs/Owl.jpg')
        # print('Image Width: ', im.texture_size[0])
        # print('Image Height: ', im.texture_size[1])
        # print('Image Size: ', im.texture_size)
        # self.add_widget(im)

class GalleryApp(App):
    def build(self):

        return GalleryWindow()

if __name__ == '__main__':
    GalleryApp().run()