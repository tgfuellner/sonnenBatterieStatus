#!/usr/bin/python3

import json2table
import requests
from collections import OrderedDict

url = 'http://192.168.0.115:8080/api/v1/status'

r = requests.get(url)
stateAll = r.json()

state = OrderedDict()
state['SOC'] = stateAll['USOC']
state['Production'] = str(stateAll['Production_W'])+'W'
state['Consumption'] = str(stateAll['Consumption_W'])+'W'
state['GridFeedIn'] = str(stateAll['GridFeedIn_W'])+'W'
state['Timestamp'] = stateAll['Timestamp']


print("""<!DOCTYPE html>
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
""")

build_direction = "LEFT_TO_RIGHT"
print(json2table.convert(state, build_direction=build_direction)) 

print("""</body>
</html>""")
