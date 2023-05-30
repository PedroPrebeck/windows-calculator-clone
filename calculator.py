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
        
        self.formula_string = ctk.StringVar(value = '')
        self.result_string = ctk.StringVar(value = '0')
        self.display_nums = []
        self.full_operation = []
        self.last_operation = []
        self.last_percent = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        output_font = ctk.CTkFont(family = SEMIBOLD_FONT, size = OUTPUT_FONT_SIZE)
        title_font = ctk.CTkFont(family = SEMIBOLD_FONT, size = NORMAL_FONT_SIZE)
        formula_font = ctk.CTkFont(family = REGULAR_FONT, size = BUTTON_FONT_SIZE)
        operator_font = ctk.CTkFont(family = REGULAR_FONT, size = BUTTON_FONT_SIZE)
        math_font = ctk.CTkFont(family = LIGHT_FONT, size = MATH_FONT_SIZE)
        number_font = ctk.CTkFont(family = REGULAR_FONT, size = NUMBER_FONT_SIZE)
        memory_font = ctk.CTkFont(family = REGULAR_FONT, size = MEMORY_FONT_SIZE)
        
        OutputLabel(self, 0, 'w', title_font, 'Standard', 'Standard')
        OutputLabel(self, 1, 'se', formula_font, self.formula_string)
        OutputLabel(self, 2, 'e', output_font, self.result_string)

        # percent
        Button(parent = self,
               func = self.percent, 
               text = OPERATORS['percent']['text'],
               col = OPERATORS['percent']['col'],
               row = OPERATORS['percent']['row'],
               font = operator_font,
               columnspan = OPERATORS['percent']['columnspan'],)
        
        # clear result
        Button(parent = self,
               func = self.clear_result, 
               text = OPERATORS['CE']['text'],
               col = OPERATORS['CE']['col'],
               row = OPERATORS['CE']['row'],
               font = operator_font,
               columnspan = OPERATORS['CE']['columnspan'],)
        
        # clear everything
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
        self.last_percent = 0
        if self.formula_string.get() and self.formula_string.get()[-1] == '=':
            self.clear_everything()
            
        if self.display_nums == [] and self.full_operation == [] and value == 0:
            return

        if self.display_nums == ['undefined']:
            self.display_nums.clear()
            self.full_operation.clear()

        if len(self.display_nums) < 11:
            self.display_nums.append(str(value))
            full_number = ''.join(self.display_nums)
            self.result_string.set(full_number)

    def math_press(self, value):
        def perform_sum():
            formula = ' '.join(self.full_operation)
            result = float(parser.parse(formula))
            
            if result.is_integer():
                result = int(result)
            else:
                digits_before_decimal = len(str(int(result)))
                round_to = 11 - digits_before_decimal
                result = int(round(result, max(round_to,0))) if round(result, max(round_to,0)).is_integer() else round(result, max(round_to,0))

            self.formula_string.set(formula + ' =')
            self.result_string.set(result)
            self.last_operation = ' '.join(self.full_operation[-2:])
            self.full_operation.clear()
            self.display_nums = [str(result)]

        current_number = ''.join(self.display_nums)
        if not current_number:
            return
        
        if value == '=' and self.full_operation == []:
            self.full_operation.append(current_number)
            self.full_operation.extend(self.last_operation.split()[-2:])
            self.formula_string.set(' '.join(self.full_operation))
            perform_sum()
            return

        self.full_operation.append(current_number)

        if value != '=' or not self.full_operation:
            self.full_operation.append(value)
            self.display_nums.clear()
            self.formula_string.set(' '.join(self.full_operation))
        else:
            perform_sum()
    
    def mem_press(self, value):
        print(value)

    def clear_result(self):
        if self.full_operation == []:
            self.clear_everything()
            return
        self.result_string.set(0)
        self.display_nums.clear()

    def clear_everything(self):
        self.result_string.set(0)
        self.formula_string.set('')
        self.display_nums.clear()
        self.full_operation.clear()
        self.last_operation = ''
        self.last_percent = 0
        
    # TODO: if the number is too small it will convert to scientific 
    #       notation and the parser will not recognize it as a number
    def percent(self):
        if self.full_operation:
            print('aqui 1')
            last_operator = self.full_operation[-1]
            current_number = Decimal(''.join(self.display_nums))

            if last_operator == '+' or last_operator == '-':
                previous_number = Decimal(self.full_operation[-2])
                percent_value = previous_number * current_number * Decimal('0.01')
                decimal_percent_value = Decimal(str(percent_value))
                if decimal_percent_value == decimal_percent_value.to_integral_value():
                    percent_value = int(decimal_percent_value)
                else:
                    percent_value = decimal_percent_value
                self.display_nums.clear()
                self.display_nums.append(str(percent_value))
                self.formula_string.set(' '.join(self.full_operation) + ' ' + ''.join(self.display_nums))
            elif last_operator == '*' or last_operator == '/':
                current_number = Decimal(''.join(self.display_nums))
                percent_value = current_number * Decimal('0.01')
                self.display_nums.clear()
                self.display_nums.append(str(percent_value))
                self.formula_string.set(' '.join(self.full_operation) + ' ' + ''.join(self.display_nums))
        elif self.last_percent == 0:
            current_number = Decimal(''.join(self.display_nums))
            self.last_percent = current_number * Decimal('0.01')
            percent_value = current_number * self.last_percent
            percent_value = percent_value
            digits_before_decimal = len(str(int(percent_value)))
            round_to = 11 - digits_before_decimal
            decimal_percent_value = Decimal(str(percent_value))
            if decimal_percent_value == decimal_percent_value.to_integral_value():
                percent_value = int(round(decimal_percent_value, max(round_to,0)))
            else:
                percent_value = round(percent_value, max(round_to,0)).normalize()
            self.display_nums.clear()
            self.display_nums.append(str(percent_value))
            self.result_string.set(str(percent_value))
            self.formula_string.set(str(percent_value))
        else:
            print('aqui 3')
            current_number = Decimal(''.join(self.display_nums))
            percent_value = Decimal(current_number * self.last_percent)
            digits_before_decimal = len(str(int(percent_value)))
            round_to = 11 - digits_before_decimal
            digits_before_decimal = len(str(int(percent_value)))
            round_to = 11 - digits_before_decimal
            decimal_percent_value = Decimal(str(percent_value))
            if decimal_percent_value == decimal_percent_value.to_integral_value():
                percent_value = int(round(decimal_percent_value, max(round_to,0)))
            else:
                percent_value = round(percent_value, max(round_to,0)).normalize()
            self.display_nums.clear()
            self.display_nums.append(str(percent_value))
            self.result_string.set(str(percent_value))
            self.formula_string.set(str(percent_value))


    def backspace(self):
        print('backspace')

    def inverse(self):
        print('inverse')

    def square(self):
        print('square')

    def square_root(self):
        print('square root')
    
    def inverted_signal(self):
        current_number = float(''.join(self.display_nums))
        if current_number.is_integer():
            current_number = int(current_number)
        if current_number:
            self.display_nums.clear()
            self.display_nums.append(str(current_number * -1))
            self.result_string.set(''.join(self.display_nums))

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
    #Calculator(False)