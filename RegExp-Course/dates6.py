import re
text='Dates are 22-01-1980,12-12-1984,12-05-1999,12-04-1963'

pattern=r'\b\d{2}-(?:0[13578]|1[02])-\d{4}\b'
regex=re.compile(pattern)

dates=regex.findall(text)
print(dates)