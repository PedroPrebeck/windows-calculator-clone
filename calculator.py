import customtkinter as ctk
from buttons import Button, NumButton, MathButton, MemButton
import darkdetect
from settings import *
try:
    from ctypes import windll, byref, sizeof, c_int, GetLastError
except:
    pass
from ctypes import sizeof

class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        
        super().__init__(fg_color = (WHITE, BLACK))
        ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        self.resizable(False, False)
        self.title('Calculadora')
        self.iconbitmap('empty.ico')
        
        # grid layout
        self.rowconfigure(0, weight = 2, uniform = 'a')
        self.rowconfigure(1, weight = 1, uniform = 'a')
        self.rowconfigure(2, weight = 2, uniform = 'a')
        self.rowconfigure([3, 4], weight = 1, uniform ='a')
        self.rowconfigure(list(range(MAIN_ROWS)[5:]), weight = 2, uniform = 'a')
        self.columnconfigure(list(range(MAIN_COLS)), weight = 1, uniform = 'a')

        # data
        self.result_string = ctk.StringVar(value = '0')
        self.formula_string = ctk.StringVar(value = '')
        
        # widgets
        self.create_widgets()
        
        self.mainloop()         
        
    def create_widgets(self):
        main_font = ctk.CTkFont(family = FONT, size = NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family = FONT, size = OUTPUT_FONT_SIZE)
        memory_font = ctk.CTkFont(family = FONT, size = MEMORY_FONT_SIZE)
        
        OutputLabel(self, 0, 'w', main_font, 'Padrão')
        OutputLabel(self, 1, 'se', main_font, self.formula_string)
        OutputLabel(self, 2, 'e', result_font, self.result_string)

        Button(parent = self,
               func = self.percent, 
               text = OPERATORS['percent']['text'],
               col = OPERATORS['percent']['col'],
               row = OPERATORS['percent']['row'],
               font = main_font,
               columnspan = OPERATORS['percent']['columnspan'],)
        
        Button(parent = self,
               func = self.clear_result, 
               text = OPERATORS['CE']['text'],
               col = OPERATORS['CE']['col'],
               row = OPERATORS['CE']['row'],
               font = main_font,
               columnspan = OPERATORS['CE']['columnspan'],)
        
        Button(parent = self,
               func = self.clear, 
               text = OPERATORS['C']['text'],
               col = OPERATORS['C']['col'],
               row = OPERATORS['C']['row'],
               font = main_font,
               columnspan = OPERATORS['C']['columnspan'],)
        
        Button(parent = self,
               func = self.backspace, 
               text = OPERATORS['backspace']['text'],
               col = OPERATORS['backspace']['col'],
               row = OPERATORS['backspace']['row'],
               font = main_font,
               columnspan = OPERATORS['backspace']['columnspan'],)
        
        Button(parent = self,
               func = self.inverse, 
               text = OPERATORS['inverse']['text'],
               col = OPERATORS['inverse']['col'],
               row = OPERATORS['inverse']['row'],
               font = main_font,
               columnspan = OPERATORS['inverse']['columnspan'],)
        
        Button(parent = self,
               func = self.square, 
               text = OPERATORS['x2']['text'],
               col = OPERATORS['x2']['col'],
               row = OPERATORS['x2']['row'],
               font = main_font,
               columnspan = OPERATORS['x2']['columnspan'],)
        
        Button(parent = self,
               func = self.square_root, 
               text = OPERATORS['square root']['text'],
               col = OPERATORS['square root']['col'],
               row = OPERATORS['square root']['row'],
               font = main_font,
               columnspan = OPERATORS['square root']['columnspan'],)
        
        Button(parent = self,
               func = self.inverted_signal, 
               text = OPERATORS['+/-']['text'],
               col = OPERATORS['+/-']['col'],
               row = OPERATORS['+/-']['row'],
               font = main_font,
               columnspan = OPERATORS['+/-']['columnspan'],)
        
        for mem, data in MEM_POSITIONS.items():
            MemButton(parent = self,
                   text = data['text'],
                   func = self.math_press,
                   col = data['col'],
                   row = data['row'],
                   font = memory_font,
                   columnspan = data['columnspan'],)
        
        for math, data in MATH_POSITIONS.items():
            MathButton(parent = self,
                   text = data['character'],
                   func = self.math_press,
                   col = data['col'],
                   row = data['row'],
                   font = main_font,
                   columnspan = data['columnspan'],)
        
        for num, data in NUM_POSITIONS.items():
            NumButton(parent = self,
                   text = num,
                   func = self.num_press,
                   col = data['col'],
                   row = data['row'],
                   font = main_font,
                   columnspan = data['columnspan'],)

    def num_press(self, value):
        print(value)

    def math_press(self, value):
        print(value)

    def clear(self):
        print('clear')

    def clear_result(self):
        print('clear result')

    def percent(self):
        print('percent')

    def backspace(self):
        print('backspace')

    def inverse(self):
        print('inverse')

    def square(self):
        print('square')

    def square_root(self):
        print('square root')
    
    def inverted_signal(self):
        print('+/-')

class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master = parent, text = 'Padrão', font = font, textvariable = string_var)
        self.grid(column = 0, columnspan = MAIN_COLS, row = row, sticky = anchor, padx = 10)

if __name__ == '__main__':
    #Calculator(darkdetect.isDark())
    Calculator(False)