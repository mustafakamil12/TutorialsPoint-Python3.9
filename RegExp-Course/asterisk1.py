import re
text='abababc ababc abc c'

pattern=r'(ab)*c'
regex=re.compile(pattern)
results=regex.findall(text)

print(results)