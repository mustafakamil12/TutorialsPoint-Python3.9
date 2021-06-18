from datetime import datetime
from datetime import timedelta

# taking input as the date
Begindatestring = "2020-10-11"

# carry out conversion between string
# to datetime object
Begindate = datetime.strptime(Begindatestring, "%Y-%m-%d")

# print begin date
print("Beginning date")
print(Begindate)

# calculating end date by adding 10 days
Enddate = Begindate + timedelta(days=300)

# printing end date
print("Ending date")
print(Enddate)
