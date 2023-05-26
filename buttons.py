from customtkinter import CTkButton
from settings import *

class Button(CTkButton):
    def __init__(self, parent, text, func, col, row, font, columnspan, color = 'operator'):
        super().__init__(
            master = parent,
            command = func,
            text = text,
            corner_radius = STYLING['corner-radius'],
            font = font,
            fg_color = COLORS[color]['fg'],
            hover_color = COLORS[color]['hover'],
            text_color = COLORS[color]['text'],)
        self.grid(column = col, row = row, sticky = 'NSEW', columnspan = columnspan, padx = STYLING['gap'], pady = STYLING['gap'])

class NumButton(CTkButton):
    def __init__(self, parent, text, func, col, row, font, columnspan, color = 'number'):
        super().__init__(
            master = parent,
            text = text,
            command = lambda: func(text),
            corner_radius = STYLING['corner-radius'],
            font = font,
            fg_color = COLORS[color]['fg'],
            hover_color = COLORS[color]['hover'],
            text_color = COLORS[color]['text'],)
        self.grid(column = col, row = row, sticky = 'NSEW', columnspan = columnspan, padx = STYLING['gap'], pady = STYLING['gap'])

class MathButton(CTkButton):
    def __init__(self, parent, text, operator, func, col, row, font, columnspan, color = 'operator'):
        super().__init__(
            master = parent,
            text = text,
            command = lambda: func(operator),
            corner_radius = STYLING['corner-radius'],
            font = font,
            fg_color = COLORS[color]['fg'],
            hover_color = COLORS[color]['hover'],
            text_color = COLORS[color]['text'],)
        self.grid(column = col, row = row, sticky = 'NSEW', columnspan = columnspan, padx = STYLING['gap'], pady = STYLING['gap'])

class MemButton(CTkButton):
    def __init__(self, parent, text, func, col, row, font, columnspan, color = 'memory'):
        super().__init__(
            master = parent,
            text = text,
            command = lambda: func(text),
            corner_radius = STYLING['corner-radius'],
            font = font,
            fg_color = COLORS[color]['fg'],
            hover_color = COLORS[color]['hover'],
            text_color = COLORS[color]['text'])
        self.grid(column = col, row = row, sticky = 'NSEW', columnspan = columnspan)