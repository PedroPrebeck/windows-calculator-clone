# Size
APP_SIZE = (324,502)
MAIN_ROWS = 9
MAIN_COLS = 12

# Text
FONT = 'Helvetica'
OUTPUT_FONT_SIZE = 48
NORMAL_FONT_SIZE = 24

STYLING = {
    'gap': 0.5,
    'corner-radius': 0
}

NUM_POSITIONS = {
    '.': {'col': 7, 'row': 9, 'span': 3},
    0: {'col': 4, 'row': 9, 'span': 3},
    1: {'col': 1, 'row': 9, 'span': 3},
    2: {'col': 4, 'row': 8, 'span': 3},
    3: {'col': 7, 'row': 8, 'span': 3},
    4: {'col': 1, 'row': 7, 'span': 3},
    5: {'col': 4, 'row': 7, 'span': 3},
    6: {'col': 7, 'row': 7, 'span': 3},
    7: {'col': 1, 'row': 6, 'span': 3},
    8: {'col': 4, 'row': 6, 'span': 3},
    9: {'col': 7, 'row': 6, 'span': 3},
}

MATH_POSITIONS = {
    '/': {'col': 10, 'row': 5, 'span': 3, 'character': '÷', 'operator': '/', 'image path': None},
    '*': {'col': 10, 'row': 6, 'span': 3, 'character': 'x', 'operator': '*', 'image path': None},
    '-': {'col': 10, 'row': 7, 'span': 3, 'character': '-', 'operator': '-', 'image path': None},
    '=': {'col': 10, 'row': 9, 'span': 3, 'character': '=', 'operator': '=', 'image path': None},
    '+': {'col': 10, 'row': 8, 'span': 3, 'character': '+', 'operator': '+', 'image path': None},
}

OPERATORS = {
    'CE': {'col': 4, 'row': 4, 'span': 3, 'text': 'CE', 'image path': None},
    'C': {'col': 7, 'row': 4, 'span': 3, 'text': 'C', 'image path': None},
    'back': {'col': 10, 'row': 4, 'span': 3}, 'text': '«', 'image path': None,
    'percent': {'col': 1, 'row': 4, 'span': 3, 'text': '%', 'image path': None},
    'inverse': {'col': 1, 'row': 5, 'span': 3, 'text': '1/x', 'image path': None},
    'x2': {'col': 4, 'row': 5, 'span': 3, 'text': 'x²', 'image path': None},
    'square root': {'col': 7, 'row': 5, 'span': 3, 'text': '√', 'image path': None},
    '+/-': {'col': 1, 'row': 9, 'span': 3, 'text': '±', 'image path': None}
}

COLORS = {
    'blue': {'fg': ('#005a9e', '#005a9e'), 'hover': ('#196aa7', '#196aa7'), 'text': ('white', 'white')},
    'lighter-gray': {'fg': ('#f3f3f3', '#f3f3f3'), 'hover': ('#eaeaea', '#eaeaea'), 'text': ('black', 'black')},
    'light-gray': {'fg': ('#f9f9f9', '#f9f9f9'), 'hover': ('#f6f6f6', '#f6f6f6'), 'text': ('black', 'black')}
}

TITLE_BAR_HEX_COLORS = {
    'dark': 0x00F00FF,
    'light': 0x00FF00FF
}

BLACK = '#000000'
WHITE = '#FFFFFF'