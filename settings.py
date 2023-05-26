# Size
APP_SIZE = (318,468)
MAIN_ROWS = 11
MAIN_COLS = 12

DARKGRAY = '#202020'
BLACK = '#000000'
WHITE = '#FFFFFF'

# Text
REGULAR_FONT = 'Segoe UI'
SEMIBOLD_FONT = 'Segoe UI Semibold'
LIGHT_FONT = 'Segoe UI Light'
OUTPUT_FONT_SIZE = 46
NORMAL_FONT_SIZE = 24
BUTTON_FONT_SIZE = 14
MATH_FONT_SIZE = 26
NUMBER_FONT_SIZE = 18
MEMORY_FONT_SIZE = 12

STYLING = {
    'gap': 1,
    'corner-radius': 5
}

NUM_POSITIONS = {
    '.': {'col': 6, 'row': 10, 'columnspan': 3},
    0: {'col': 3, 'row': 10, 'columnspan': 3},
    1: {'col': 0, 'row': 9, 'columnspan': 3},
    2: {'col': 3, 'row': 9, 'columnspan': 3},
    3: {'col': 6, 'row': 9, 'columnspan': 3},
    4: {'col': 0, 'row': 8, 'columnspan': 3},
    5: {'col': 3, 'row': 8, 'columnspan': 3},
    6: {'col': 6, 'row': 8, 'columnspan': 3},
    7: {'col': 0, 'row': 7, 'columnspan': 3},
    8: {'col': 3, 'row': 7, 'columnspan': 3},
    9: {'col': 6, 'row': 7, 'columnspan': 3},
}

MATH_POSITIONS = {
    '/': {'col': 9, 'row': 6, 'columnspan': 3, 'character': '÷'},
    '*': {'col': 9, 'row': 7, 'columnspan': 3, 'character': '×'},
    '-': {'col': 9, 'row': 8, 'columnspan': 3, 'character': '-'},
    '=': {'col': 9, 'row': 10, 'columnspan': 3, 'character': '='},
    '+': {'col': 9, 'row': 9, 'columnspan': 3, 'character': '+'},
}

MEM_POSITIONS = {
    'MC': {'col': 0, 'row': 4, 'columnspan': 2, 'text': 'MC'},
    'MR': {'col': 2, 'row': 4, 'columnspan': 2, 'text': 'MR'},
    'M+': {'col': 4, 'row': 4, 'columnspan': 2, 'text': 'M+'},
    'M-': {'col': 6, 'row': 4, 'columnspan': 2, 'text': 'M-'},
    'MS': {'col': 8, 'row': 4, 'columnspan': 2, 'text': 'MS'},
    'M': {'col': 10, 'row': 4, 'columnspan': 2, 'text': 'M'},
}

OPERATORS = {
    'CE': {'col': 3, 'row': 5, 'columnspan': 3, 'text': 'CE'},
    'C': {'col': 6, 'row': 5, 'columnspan': 3, 'text': 'C'},
    'backspace': {'col': 9, 'row': 5, 'columnspan': 3, 'text': '«'},
    'percent': {'col': 0, 'row': 5, 'columnspan': 3, 'text': '%'},
    'inverse': {'col': 0, 'row': 6, 'columnspan': 3, 'text': '1/x'},
    'x2': {'col': 3, 'row': 6, 'columnspan': 3, 'text': 'x²'},
    'square root': {'col': 6, 'row': 6, 'columnspan': 3, 'text': '√'},
    '+/-': {'col': 0, 'row': 10, 'columnspan': 3, 'text': '±'}
}

COLORS = {
    'accent': {'fg': ('#005a9e', '#f266e3'), 'hover': ('#196aa7', '#dc5ecf'), 'text': ('white', 'black')},
    'number': {'fg': ('#f3f3f3', '#3b3b3b'), 'hover': ('#eaeaea', '#323232'), 'text': ('black', 'white')},
    'operator': {'fg': ('#f9f9f9', '#323232'), 'hover': ('#f6f6f6', '#3c3c3c'), 'text': ('black', 'white')},
    'memory': {'fg': ('#202020', '#202020'), 'hover': ('#eaeaea', '#2d2d2d'), 'text': ('black', 'white')},
}

TITLE_BAR_HEX_COLORS = {
    'dark': 0x00FF00FF,
    'light': 0x00FF00FF
}