# -*- coding: utf-8 -*-
"""
    CernWall
    ~~~~~~~~

    A user interface to control the lights of CERN's Classbox restaurant's wood structure,
    written with Flask.

    :copyright: (c) 2017 by Aapo Rista.
    :license: MIT, see LICENSE for more details.
"""

import json
# import requests
from flask import (Flask, Response, request, session, url_for, redirect,
     render_template, abort, g, flash, _app_ctx_stack)
from .cernwall_ui_config import WALL_MODES, DRIVER_URL

# configuration
DEBUG = True
SECRET_KEY = b'Xv!y2L"F4Q8z\n\xec]/'

# Create application
app = Flask('cernwall_ui')
app.config.from_object(__name__)
app.config.from_envvar('CERNWALL_SETTINGS', silent=True)


def format_url(mode):
    """Create a URL from mode parameters."""
    mode['url'] = '{}'.format(DRIVER_URL)
    if 'm' in mode:
        mode['url'] += 'm={}'.format(mode['m'])
    else:
        mode['error'] = 'There are errors in this mode :-('
    if 'c' in mode:
        mode['url'] += '&c={}'.format(mode['c'])
    if 'c2' in mode:
        mode['url'] += '&c2={}'.format(mode['c2'])
    if 't' in mode:
        mode['url'] += '&t={}'.format(mode['t'])
    if 'bs' in mode:
        mode['url'] += '&bs={}'.format(mode['bs'])
    return mode


def build_modes(modes):
    i = 0
    for mode in modes:
        mode['id'] = i
        i += 1
        format_url(mode)
    return modes

@app.route('/')
def index():
    """Show available predefined modes in a web page.
    """
    modes = build_modes(WALL_MODES)
    return render_template('index.html', messages=modes)


@app.route('/modes')
def modes():
    """Show available predefined modes in json format.
    """
    modes = build_modes(WALL_MODES)
    json_modes = []
    for mode in modes:
        json_modes.append({
            'id': mode['id'], 'name': mode['name'], 'description': mode['description'],
            'url': '/setmode?mode={}'.format(mode['id']),
        })
    json_str = json.dumps(json_modes, indent=1)
    return Response(response=json_str, content_type='application/json')


@app.route('/setmode')
def setmode():
    """Set mode calling MCU's web interface
    """
    modes = build_modes(WALL_MODES)
    resp = {'status': 'ERROR', 'message': ''}
    status_code = 200
    try:
        requested_mode = int(request.args.get('mode'))
        resp['message'] = 'Mode {} does not exist'.format(requested_mode)
        for mode in modes:
            if requested_mode == mode['id']:
                resp['status'] = 'OK'
                resp['message'] = ''
                # here call ESP
                print('requests.get({})'.format(mode['url']))
                break
    except ValueError as err:
        status_code = 500
        resp['message'] = str(err)
    json_str = json.dumps(resp, indent=1)
    return Response(response=json_str, status=status_code, content_type='application/json')
