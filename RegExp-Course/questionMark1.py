import re
text='words are rise, risen'

pattern=r'risen?'
regex=re.compile(pattern)

numbers=regex.findall(text)
print(numbers)