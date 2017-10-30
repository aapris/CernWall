"""
WALL_MODES must be defined like this:
{
    'name': Descriptive name,
    'm':    Mode number,
    'c':    Color code in hex,
    'c2':   Color 2 code in hex,
    'c3':   Color 3 code in hex,
    'bs':   Brightness 0-255,
    't':    Speed 0-255
}

"""

DRIVER_URL = 'http://172.24.1.2/set?'
#DRIVER_URL = '/?'

WALL_MODES = [
    {'name': 'OFF', 'm': 0, 'c': '000000', 'bs': 0, 't': 100, 'description': ''},
    {'name': 'Running lights (default)', 'm': 47, 'c': '4dff20', 'c2': 'ffffcc', 'bs': 100, 't': 100, 'description': ''},
    {'name': 'Color wipe', 'm': 48, 'c': 'ffff33', 'c2': 'ffdd33',  'c3': '4dff20', 't': 250, 'description': ''},
]
