import re
text='Dates are 22-06-1980,12-12-1984,12-04-1999,12-04-1963'

pattern=r'\b\d{2}-\d{2}-19[89][0-9]\b'
regex=re.compile(pattern)

dates=regex.findall(text)
print(dates)