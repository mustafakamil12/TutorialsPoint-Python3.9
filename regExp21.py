import re
Temps = "Mustafa | Kamil"

[mintemp,maxtemp]=re.split('\|',Temps)

print(f"mintemp = {mintemp} and maxtemp = {maxtemp}")
