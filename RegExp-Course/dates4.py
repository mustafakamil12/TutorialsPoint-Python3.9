import re
text='Dates are 22-06-1999,22-12-1999,12-04-1999,12-04-1963'

pattern=r'\b\d{2}-\d{2}-1999\b'
regex=re.compile(pattern)

dates=regex.findall(text)
print(dates)