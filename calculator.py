import customtkinter as ctk
from buttons import Button, NumButton, MathButton, MemButton
import darkdetect
from settings import *
try:
    from ctypes import windll, byref, sizeof, c_int, GetLastError
except:
    pass
from ctypes import sizeof
from mathparse import mathparse as parser
from decimal import Decimal

class CalculatorFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = (WHITE, DARKGRAY))

        self.rowconfigure(0, weight = 2, uniform = 'a')
        self.rowconfigure(1, weight = 1, uniform = 'a')
        self.rowconfigure(2, weight = 2, uniform = 'a')
        self.rowconfigure([3, 4], weight = 1, uniform ='a')
        self.rowconfigure(list(range(MAIN_ROWS)[5:]), weight = 2, uniform = 'a')
        self.columnconfigure(list(range(MAIN_COLS)), weight = 1, uniform = 'a')

        self.formula_display = ctk.StringVar(value = '')
        self.result_display = ctk.StringVar(value = '0')

        self.current_number_digits = ['0']
        self.first_number = ''
        self.second_number = ''
        self.result = ''

        self.full_operation = []
        self.last_operation = ''

        self.digits_limit = 16

        self.create_widgets()

        self.result_display.trace('w', self.update_output_font_size)

    def update_output_font_size(self, *args):
        num_digits = len(self.result_display.get().replace('.', '').replace(',', ''))
        #print(f'num_digits: {num_digits}')
        MIN_NUM_DIGITS = 10
        MAX_NUM_DIGITS = 16

        font_size = int(((MAX_NUM_DIGITS - num_digits) / (MAX_NUM_DIGITS - MIN_NUM_DIGITS)) * (OUTPUT_FONT_SIZE - MIN_OUTPUT_FONT_SIZE) + MIN_OUTPUT_FONT_SIZE)
        #print(f'font size: {font_size}')

        self.output_font_size = max(min(font_size, OUTPUT_FONT_SIZE), MIN_OUTPUT_FONT_SIZE)
        #print(f'output_font_size: {self.output_font_size}')

        output_font = ctk.CTkFont(family=SEMIBOLD_FONT, size=self.output_font_size)

        self.result_label.configure(font=output_font)

    def create_widgets(self):
        output_font = ctk.CTkFont(family = SEMIBOLD_FONT, size = OUTPUT_FONT_SIZE)
        title_font = ctk.CTkFont(family = SEMIBOLD_FONT, size = NORMAL_FONT_SIZE)
        formula_font = ctk.CTkFont(family = REGULAR_FONT, size = BUTTON_FONT_SIZE)
        operator_font = ctk.CTkFont(family = REGULAR_FONT, size = BUTTON_FONT_SIZE)
        math_font = ctk.CTkFont(family = LIGHT_FONT, size = MATH_FONT_SIZE)
        number_font = ctk.CTkFont(family = REGULAR_FONT, size = NUMBER_FONT_SIZE)
        memory_font = ctk.CTkFont(family = REGULAR_FONT, size = MEMORY_FONT_SIZE)

        OutputLabel(self, 0, 'w', title_font, 'Standard', 'Standard')
        OutputLabel(self, 1, 'se', formula_font, self.formula_display)
        self.result_label = OutputLabel(self, 2, 'e', output_font, self.result_display)

        Button(parent = self,
               func = self.percent, 
               text = OPERATORS['percent']['text'],
               col = OPERATORS['percent']['col'],
               row = OPERATORS['percent']['row'],
               font = operator_font,
               columnspan = OPERATORS['percent']['columnspan'],)

        Button(parent = self,
               func = self.clear_result, 
               text = OPERATORS['CE']['text'],
               col = OPERATORS['CE']['col'],
               row = OPERATORS['CE']['row'],
               font = operator_font,
               columnspan = OPERATORS['CE']['columnspan'],)

        Button(parent = self,
               func = self.clear_everything, 
               text = OPERATORS['C']['text'],
               col = OPERATORS['C']['col'],
               row = OPERATORS['C']['row'],
               font = operator_font,
               columnspan = OPERATORS['C']['columnspan'],)

        Button(parent = self,
               func = self.backspace, 
               text = OPERATORS['backspace']['text'],
               col = OPERATORS['backspace']['col'],
               row = OPERATORS['backspace']['row'],
               font = operator_font,
               columnspan = OPERATORS['backspace']['columnspan'],)

        Button(parent = self,
               func = self.inverse, 
               text = OPERATORS['inverse']['text'],
               col = OPERATORS['inverse']['col'],
               row = OPERATORS['inverse']['row'],
               font = operator_font,
               columnspan = OPERATORS['inverse']['columnspan'],)

        Button(parent = self,
               func = self.square, 
               text = OPERATORS['x2']['text'],
               col = OPERATORS['x2']['col'],
               row = OPERATORS['x2']['row'],
               font = operator_font,
               columnspan = OPERATORS['x2']['columnspan'],)

        Button(parent = self,
               func = self.square_root, 
               text = OPERATORS['square root']['text'],
               col = OPERATORS['square root']['col'],
               row = OPERATORS['square root']['row'],
               font = operator_font,
               columnspan = OPERATORS['square root']['columnspan'],)

        Button(parent = self,
               func = self.inverted_signal, 
               text = OPERATORS['+/-']['text'],
               col = OPERATORS['+/-']['col'],
               row = OPERATORS['+/-']['row'],
               font = operator_font,
               color = 'number',
               columnspan = OPERATORS['+/-']['columnspan'],)

        for mem, data in MEM_POSITIONS.items():
            MemButton(parent = self,
                   text = data['text'],
                   func = self.mem_press,
                   col = data['col'],
                   row = data['row'],
                   font = memory_font,
                   columnspan = data['columnspan'],)

        for math, data in MATH_POSITIONS.items():
            color = 'accent' if math == '=' else 'operator'

            MathButton(parent=self,
                    text = data['character'],
                    operator = math,
                    func = self.math_press,
                    col = data['col'],
                    row = data['row'],
                    font = math_font,
                    columnspan = data['columnspan'],
                    color = color)

        for num, data in NUM_POSITIONS.items():
            NumButton(parent = self,
                   text = num,
                   func = self.num_press,
                   col = data['col'],
                   row = data['row'],
                   font = number_font,
                   columnspan = data['columnspan'],)

    def num_press(self, value):
        MAX_DIGIT_LENGTH = self.digits_limit
        CURRENT_NUMBER_IS_MAX_LENGHT = sum(1 for digit in self.current_number_digits if digit != '.') == MAX_DIGIT_LENGTH
        VALUE_IS_NOT_DECIMAL = value != '.'
        CURRENT_NUMBER_INITIAL_IS_ZERO = self.current_number_digits == ['0'] and VALUE_IS_NOT_DECIMAL
        VALUE_IS_DECIMAL = value == '.'
        CURRENT_NUMBER_IS_EMPTY = not self.current_number_digits
        CURRENT_NUMBER_IS_DECIMAL = '.' in self.current_number_digits

        if CURRENT_NUMBER_IS_MAX_LENGHT:
            return

        if CURRENT_NUMBER_INITIAL_IS_ZERO:
            self.current_number_digits.pop(0)

        if VALUE_IS_DECIMAL and CURRENT_NUMBER_IS_EMPTY:
            self.current_number_digits.append('0')

        if VALUE_IS_DECIMAL and CURRENT_NUMBER_IS_DECIMAL:
            return

        #print(f'num press {value}')
        self.current_number_digits.append(str(value))
        #print(f'current_number_digits {self.current_number_digits}')
        current_number = ''.join(self.current_number_digits)
        #print(f'current_number {current_number}')

        if '.' in current_number:
            integer_part, decimal_part = current_number.split('.')
            integer_part_formatted = "{:,}".format(int(integer_part))
            #print(f'integer_part_formatted {integer_part_formatted}')
            current_number_formatted = f"{integer_part_formatted}.{decimal_part[:MAX_DIGIT_LENGTH - len(integer_part_formatted.replace(',', ''))]}"
        else:
            current_number_formatted = "{:,}".format(int(current_number))
        #print(f'current_number_formated {current_number_formatted}')

        self.result_display.set(current_number_formatted)
        #print(f'result_display {self.result_display.get()}')

    def math_press(self, value):
        print(f'math press {value}')
        current_number = ''.join(self.current_number_digits)
        if not self.first_number:
            self.first_number = current_number
            print(f'first_number {self.first_number}')
            self.full_operation.append(self.first_number)
            self.full_operation.append(value)
            print(f'full_operation {self.full_operation}')
            self.formula_display.set(' '.join(self.full_operation))
            print(f'formula_display: {self.formula_display.get()}')
            self.current_number_digits = []
            print(f'current_number_digits {self.current_number_digits}')
        else:
            self.second_number = current_number
            print(f'second_number {self.second_number}')
            self.full_operation.append(self.second_number)
            print(f'full_operation {self.full_operation}')
            formula = ' '.join(self.full_operation)
            print(f'formula {formula}')
            result = Decimal(str(parser.parse(formula)))
            self.result = result
            print(f'formula_result {self.result}')
            if value == '=':
                self.formula_display.set(formula + ' =')
                self.result_display.set(self.result)
            else:
                self.formula_display.set(f'{self.result} {value}')
                self.result_display.set(self.result)
            self.last_operation = ' '.join(self.full_operation[-2:])
            self.full_operation.clear()
            self.current_number_digits.clear()
            self.first_number = None
            self.result = None





    def percent(self):
        print('percent')

    def clear_result(self):
        print('clear result')

    def clear_everything(self):
        print('clear everything')

    def inverted_signal(self):
        print('inverted signal')

    def mem_press(self, value):
        print(value)

    def backspace(self):
        print('backspace')

    def inverse(self):
        print('inverse')

    def square(self):
        print('square')

    def square_root(self):
        print('square root')

class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        super().__init__(fg_color = (WHITE, DARKGRAY))
        ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        self.resizable(False, False)
        self.title('Calculadora')
        self.iconbitmap('empty.ico')       

        calculator_frame = CalculatorFrame(self)
        calculator_frame.pack(fill = 'both', expand = True, padx = 3, pady = 3)

        self.mainloop()

class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var, text = ''):
        super().__init__(master = parent, text = text, font = font, textvariable = string_var)
        self.grid(column = 0, columnspan = MAIN_COLS, row = row, sticky = anchor, padx = 10)

if __name__ == '__main__':
    Calculator(darkdetect.isDark())