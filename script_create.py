import requests
import json

url = 'https://smartoffice1i844796trial.hanatrial.ondemand.com/SmartOffice/rest'

headers = {'Content-Type': 'application/json'}
# Bathroom
json_data = json.dumps({'id': '2CM', 'occupied': 'false'}, sort_keys=True, indent=4, separators=(',', ': '))
r = requests.post(url + '/bathroom', data=json_data, headers=headers)
print (r)

json_data = json.dumps({'id': '2EM', 'occupied': 'false'}, sort_keys=True, indent=4, separators=(',', ': '))
r = requests.post(url + '/bathroom', data=json_data, headers=headers)
print (r)

json_data = json.dumps({'id': '2CF', 'occupied': 'false'}, sort_keys=True, indent=4, separators=(',', ': '))
r = requests.post(url + '/bathroom', data=json_data, headers=headers)
print (r)

json_data = json.dumps({'id': '2EF', 'occupied': 'false'}, sort_keys=True, indent=4, separators=(',', ': '))
r = requests.post(url + '/bathroom', data=json_data, headers=headers)
print (r)

# ParkingLot

json_data = json.dumps({'id': 'vaga1', 'occupied': 'false'}, sort_keys=True, indent=4, separators=(',', ': '))
r = requests.post(url + '/parkingLot', data=json_data, headers=headers)
print (r)

json_data = json.dumps({'id': 'vaga2', 'occupied': 'false'}, sort_keys=True, indent=4, separators=(',', ': '))
r = requests.post(url + '/parkingLot', data=json_data, headers=headers)
print (r)

json_data = json.dumps({'id': 'vaga3', 'occupied': 'false'}, sort_keys=True, indent=4, separators=(',', ': '))
r = requests.post(url + '/parkingLot', data=json_data, headers=headers)
print (r)

# Noise Sensor
    
json_data = json.dumps({'id': '1', 'name': '1', 'level': '0'}, sort_keys=True, indent=4, separators=(',', ': '))
r = requests.post(url + '/noiseSensor', data=json_data, headers=headers)
print (r)

# Light Sensor
    
json_data = json.dumps({'id': '1', 'level': '0'}, sort_keys=True, indent=4, separators=(',', ': '))
r = requests.post(url + '/lightSensor', data=json_data, headers=headers)
print (r)

# Temperature Sensor

json_data = json.dumps({'id': '1', 'value': '24'}, sort_keys=True, indent=4, separators=(',', ': '))
r = requests.post(url + '/temperature', data=json_data, headers=headers)
print (r)

