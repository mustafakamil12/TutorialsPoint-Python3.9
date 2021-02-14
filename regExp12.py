import re

# \w [a-zA-Z0-9_]
# \W [^a-zA-Z0-9_]

phn = "210-712-3989"

if re.search("\w{3}-\w{3}-\w{4}", phn):
    print("It's a phone number")
else:
    print("It's not a phone number")