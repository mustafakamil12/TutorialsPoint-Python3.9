#www.facebook.com/CSxFunda
#program to illustrate the working of split
import re

text='Kalyan is a good boy and he is going to marry Meghana'
pattern=r'\s'

regex=re.compile(pattern)

split_text=regex.split(text)
print(split_text)
