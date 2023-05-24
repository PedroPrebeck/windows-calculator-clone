import customtkinter as ctk
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
        self.rowconfigure(list(range(MAIN_ROWS)), weight = 1, uniform = 'a')
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
        
        OutputLabel(self, 0, 'se', main_font, self.formula_string)
        OutputLabel(self, 1, 'e', result_font, self.result_string)

class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master = parent, text = '123', font = font, textvariable = string_var)
        self.grid(column = 0, columnspan = MAIN_COLS, row = row, sticky = anchor, padx = 10)

if __name__ == '__main__':
    Calculator(darkdetect.isDark())