#!/usr/bin/python3

import json2table
import requests
from collections import OrderedDict

url = 'http://192.168.0.115:8080/api/v1/status'
port = 8080

def makeTable(environ, start_response):
    r = requests.get(url)
    stateAll = r.json()

    state = OrderedDict()
    state['SOC'] = str(stateAll['USOC'])+'%'
    state['Production'] = str(stateAll['Production_W'])+'W'
    state['Consumption'] = str(stateAll['Consumption_W'])+'W'
    state['GridFeedIn'] = str(stateAll['GridFeedIn_W'])+'W'
    state['Timestamp'] = stateAll['Timestamp']

    build_direction = "LEFT_TO_RIGHT"
    state = json2table.convert(state, build_direction=build_direction) 

    start_response('200 OK', [('Content-Type', 'text/html')])

    return [b"""
    <html>
    <head>
    <style>
    table {
      border-collapse: collapse;
    }

    th, td {
      text-align: left;
      padding: 8px;
    }

    tr:nth-child(even) {background-color: #f2f2f2;}
    </style>
    </head>
    <body>

    %(table)s

    </body>
    </html>""" % {b"table": state.encode('utf-8')}]




if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('', port, makeTable)
    print("Serving on port {} ...".format(port))
    srv.serve_forever()
