import requests

response = requests.get("http://api.open-notify.org/astros.json")

print(f"response = {response}")
print(type(response))
print(response.headers["date"])
#print(response.content())
#print(response.text())
print(response.json())


# How to filter data
"""
query = {'lat':'45', 'lon':'180'}
response1 = requests.get("http://api.open-notify.org/astros.json", params=query)
print(response1.json())
"""

# Create a new resource
"""
response = requests.post('https://httpbin.org/post', data = {'key':'value'})
"""

# Update an existing resource
"""
requests.put('https://httpbin.org/put', data = {'key':'value'})
"""

# How to use HTTP Basic auth
"""
requests.get('https://api.github.com/user',auth=HTTPBasicAuth('username', 'password'))
"""

# How to use bearer token
"""
my_headers = {'Authorization' : 'Bearer {access_token}'}
response = requests.get('http://httpbin.org/headers', headers=my_headers)
"""

# How to use subsession
"""
session = requests.Session()
session.headers.update({'Authorization': 'Bearer {access_token}'})
response = session.get('https://httpbin.org/headers')
"""

# How to Check for HTTP Errors With Python Requests
"""
response = requests.get("http://api.open-notify.org/astros.json")
if (response.status_code == 200):
    print("The request was a success!")
    # Code here will only run if the request is successful
elif (response.status_code == 404):
    print("Result not found!")
    # Code here will react to failed requests
"""

# How to raise error - the same example above but using try and scratch_products
"""
try:
    response = requests.get('http://api.open-notify.org/astros.json')
    response.raise_for_status()
    # Additional code will only run if the request is successful
except requests.exceptions.HTTPError as error:
    print(error)
    # This code will run if there is a 404 error.
"""

# How to handle TooManyRedirects
"""
try:
    response = requests.get('http://api.open-notify.org/astros.json')
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.TooManyRedirects as error:
    print(error)
"""

# Or we can set the max no of redirection instead of the code above
"""
response = requests.get('http://api.open-notify.org/astros.json', max_redirects=2)
"""

# if there's any error with the line code above u can use the lien below
"""
session = requests.Session()
session.max_redirects = 2
session.get('http://api.open-notify.org/astros.json')
"""

# Or disable redirecting completely within your request options
"""
response = requests.get('http://api.open-notify.org/astros.json', allow_redirects=False)
"""

# Handle ConnectionError
"""
try:
    response = requests.get('http://api.open-notify.org/astros.json')
    # Code here will only run if the request is successful
except requests.ConnectionError as error:
    print(error)
"""

# Handle Timeout
"""
try:
    response = requests.get('http://api.open-notify.org/astros.json', timeout=0.00001)
    # Code here will only run if the request is successful - please note that there's no API request can be done in 0.00001
except requests.Timeout as error:
    print(error)
"""

# How to Make Robust API Requests
"""
try:
    response = requests.get('http://api.open-notify.org/astros.json', timeout=5)
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print("HTTPError")
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print("ConnectionError")
    print(errc)
except requests.exceptions.Timeout as errt:
    print("Timeout")
    print(errt)
except requests.exceptions.RequestException as err:
    print("RequestException")
    print(err)
"""
