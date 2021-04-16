import re


cur_prod = 3
prod_count = 5

y = 0
while y < 2 and cur_prod < prod_count:
    print(y)
    y += 1

arg = '@1'
arg = re.sub('^@','',arg)
print(arg)
