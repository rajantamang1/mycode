#!/usr/bin/env python3

import requests

result = requests.get('http://api.open-notify.org/astros.json')
response = result.json()
print(f"People in space: {response['number']}")
for total in response["people"]:
    
    print(f"{total['name']} on the {total['craft']}")
