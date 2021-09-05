import re

address = "#TZ=godric.phoenix@gmail#"
default_match = re.match('#TZ=(\w*)#',address)
print(f"default_match = {default_match}")
