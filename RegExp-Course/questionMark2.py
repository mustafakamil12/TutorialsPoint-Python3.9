import re
text='values are -12,24,19,-64'

pattern=r'-?\d\d'
regex=re.compile(pattern)

numbers=regex.findall(text)
print(numbers)