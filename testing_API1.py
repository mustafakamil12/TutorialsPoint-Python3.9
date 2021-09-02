import requests

response = requests.get("http://api.open-notify.org/astros.json")

print(f"response = {response}")
print(type(response))
#print(response.content())
#print(response.text())
#print(response.json())

query = {'lat':'45', 'lon':'180'}
response1 = requests.get("http://api.open-notify.org/astros.json", params=query)
print(response1.json())
