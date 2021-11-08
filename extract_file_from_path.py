import re
string = "input_new/survey/argentina-attributes.csv"

#test = re.findall(r'[^\/]+(?=\.)',string) # or re.findall(r'([^\/]+)\.',string)

test = re.match(r'[^\\/:*?"<>|\r\n]+$',string)
print(test)
