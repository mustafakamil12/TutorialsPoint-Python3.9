import re
text='Dates are 22-06-1989,12/04/1992,12.04.1963'

pattern=r'\b\d{2}[-/.]\d{2}[-/.]\d{4}\b'
regex=re.compile(pattern)

dates=regex.findall(text)
print(dates)