import re
# \s = [\f\n\r\t\v]
# \S = [^\f\n\r\t\v]

if re.search("\w{2,20}\s\w{2,20}","Mustafa Al_Ogaidi"):
    print("full name is valid")