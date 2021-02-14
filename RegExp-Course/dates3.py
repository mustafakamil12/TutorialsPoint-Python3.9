import re
text='Dates are 22-06-89,22-11-1984,12/04/1992,12.04.1963,12/04/1963'

pattern=r'\b\d{2}-\d{2}-\d{2}(?:\d{2})?\b'
regex=re.compile(pattern)

dates=regex.findall(text)
print(dates)