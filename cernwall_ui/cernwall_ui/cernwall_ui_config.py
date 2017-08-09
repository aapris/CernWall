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
    {'name': 'Running lights', 'm': 47, 'c': '4dff20', 'c2': 'ffffcc', 'bs': 100, 't': 100, 'description': ''},
#    {'name': 'Color wipe', 'm': 48, 'c': 'ffff20', 'c2': 'ff0000', 'bs': 250, 't': 250, 'description': ''},
    {'name': 'Color wipe', 'm': 48, 'c': 'ffff20', 'c2': 'ff0000', 't': 250, 'description': ''},
    #    {'name': 'this has error', 'c': '008800', 'bs': 150, 't': 100, 'description': ''},
    {'name': 'Color Wipe 3',   'm': 3,  'c': 'ffff20', 'bs': 250,  't': 250, 'description': ''},
#    {'name': 'Color Wipe',     'm': 3,  'c': '4dff20', 'bs': 250, 't': 180, 'description': ''},
#    {'name': 'Color Wipe Y', 'm': 3, 'c': 'ff6e00', 'bs': 250, 't': 180, 'description': ''},
#    {'name': 'Color Wipe',     'm': 3,  'c': '4dff20', 'bs': 250, 't': 200, 'description': ''},
#    {'name': 'Color Wipe G',     'm': 3,  'c': '4dff20', 'bs': 250, 't': 180, 'description': ''},
    {'name': 'Running lights', 'm': 15, 'c': '4dff20', 'bs': 100, 't': 100, 'description': ''},
]
