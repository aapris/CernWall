"""
WALL_MODES must be defined like this:
{
    'name': Descriptive name,
    'm':    Mode number,
    'c':    Color code in hex,
    'bs':   Brightness 0-255,
    't':    Speed 0-255
}

"""

DRIVER_URL = 'http://172.24.1.2/set?'
#DRIVER_URL = '/?'

WALL_MODES = [
    {'name': 'OFF', 'm': 0, 'c': '000000', 'bs': 0, 't': 100, 'description': ''},
    {'name': 'Running lights (default)', 'm': 47, 'c': '4dff20', 'c2': 'ffffcc', 'bs': 100, 't': 100, 'description': ''},
    {'name': 'Another example mode', 'm': 8, 'bs': 100, 't': 100, 'description': 'Do not use this'},
    {'name': 'Color wipe', 'm': 48, 'c': 'ffff20', 'c2': 'ff0000', 't': 250, 'description': ''},
]
