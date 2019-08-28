import math
from datetime import datetime

AVAILABLE_ACTIONS = [{'action': 'add', 'admin_required': False,
                      'operator': '+'},
                     {'action': 'subtract', 'admin_required': False,
                      'operator': '-'},
                     {'action': 'multiply', 'admin_required': False,
                      'operator': '*'},
                     {'action': 'divide', 'admin_required': False,
                      'operator': '/'},
                     {'action': 'power', 'admin_required': True,
                      'operator': '**'},
                     {'action': 'sqrt', 'admin_required': True,
                      'operator': 'sqrt'},
                     ]


def get_available_options(action):
    """
    Go through the available options and find it, then return that object
    :param action: string
    :return: list
    """
    return [obj for obj in AVAILABLE_ACTIONS
            if obj['action'] == action.lower()]


def do_calculation(action, x, y):
    """
    This function does all the calculation thig
    :param action: string
    :param x: int
    :param y: int
    :return: int ( the result )
    """
    operator = get_available_options((action))[0]['operator']
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y else 0,
        '**': lambda x, y: x ** y,
        'sqrt': lambda x, y: math.sqrt(int(x))
    }
    return ops[operator](int(x), int(y))


def get_current_month():
    now = datetime.now()
    return now.month


def get_current_year():
    now = datetime.now()
    return now.year


def get_current_date():
    return datetime.now().date()
