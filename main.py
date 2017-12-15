#!/usr/bin/env python3

# ---------- main.py  ----------

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

import kivy

kivy.require('1.10.0')


class CalcGridLayout(GridLayout):

    # Function called when equals is pressed
    def calculate(self, calculation):
        if calculation:

            string = calculation

            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                self.display.text = str(eval(string.replace('&&', 'and').replace('||', 'or').replace('!', 'not ')))
            except Exception:
                self.display.text = "Error"


class RootWidget(BoxLayout):
    '''Create a controller that receives a custom widget from the kv lang file.
    Add an action to be called from a kv file.
    '''

    container = ObjectProperty(None)


class NumConv(BoxLayout):

    def num_conversion(self, input1, output, data):
        try:
            if input1 == 'Decimal':
                if output == 'Decimal':
                    self.display.text = str(int(data))
                elif output == 'Hexadecimal':
                    self.display.text = str(hex(int(data)))
                elif output == 'Octal':
                    self.display.text = str(oct(int(data)))
                elif output == 'Binary':
                    self.display.text = str(bin(int(data)))
            if input1 == 'Hexadecimal':
                if output == 'Decimal':
                    self.display.text = str(int(data, 16))
                elif output == 'Hexadecimal':
                    self.display.text = str(hex(int(data, 16)))
                elif output == 'Octal':
                    self.display.text = str(oct(int(data, 16)))
                elif output == 'Binary':
                    self.display.text = str(bin(int(data, 16)))
            if input1 == 'Octal':
                if output == 'Decimal':
                    self.display.text = str(int(data, 8))
                elif output == 'Hexadecimal':
                    self.display.text = str(hex(int(data, 8)))
                elif output == 'Octal':
                    self.display.text = str(oct(int(data, 8)))
                elif output == 'Binary':
                    self.display.text = str(bin(int(data, 8)))
            if input1 == 'Binary':
                if output == 'Decimal':
                    self.display.text = str(int(data, 2))
                elif output == 'Hexadecimal':
                    self.display.text = str(hex(int(data, 2)))
                elif output == 'Octal':
                    self.display.text = str(oct(int(data, 2)))
                elif output == 'Binary':
                    self.display.text = str(bin(int(data, 2)))
        except Exception:
            self.display.text = "Error"


class CalculatorApp(App):
    '''This is the app itself'''

    def build(self):
        '''This method loads the root.kv file automatically

        :return: none
        '''
        # loading the content of root.kv
        self.root = Builder.load_file('kv_modes/root.kv')

    def screen_select(self, selector):
        '''

        :param selector: character that is dependant on which mode button is toggled.
        :return:
        '''

        filename = selector + '.kv'
        # unload the content of the .kv file
        # reason: may have data from previous calls
        Builder.unload_file('kv_modes/' + filename)
        # clear the container
        self.root.container.clear_widgets()
        # load the .kv file
        selector = Builder.load_file('kv_modes/' + filename)
        # add content of the .kv file to the container
        self.root.container.add_widget(selector)


if __name__ == '__main__':
    '''Start the application'''

    CalculatorApp().run()
