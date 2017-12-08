#!/usr/bin/env python3

# ---------- main.py  ----------

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

import kivy
kivy.require('1.10.0')


class RootWidget(BoxLayout):
    '''Create a controller that receives a custom widget from the kv lang file.
    Add an action to be called from a kv file.
    '''

    container = ObjectProperty(None)


class CalculatorApp(App):

    '''This is the app itself'''

    def build(self):
        '''This method loads the root.kv file automatically

        :rtype: none
        '''
        # loading the content of root.kv
        self.root = Builder.load_file('kv_modes/root.kv')


if __name__ == '__main__':
    '''Start the application'''

    CalculatorApp().run()

