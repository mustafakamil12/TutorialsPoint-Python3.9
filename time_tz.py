import datetime
from datetime import date
from datetime import datetime

strDate = '2021-10-21T10:56:59Z'

objDate = datetime.strptime(strDate, '%Y-%m-%dT%H:%M:%Sz')
print(f"objDate = {objDate}")

print(f" seconds = {objDate.timestamp()}")
