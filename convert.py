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
