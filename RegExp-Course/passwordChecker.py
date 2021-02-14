import re
pwd=input('Enter the password: ')

pattern1=r'^.{8,32}$'
pattern2=r'[^A-Za-z0-9#@*!&]'
pattern3=r'^.*[A-Z].*$'
pattern4=r'^.*[a-z].*$'
pattern5=r'^.*[0-9].*$'
pattern6=r'^.*[#@*!&].*$'
pattern7=r'^.*(.)\1{2,}.*$'

if not re.search(pattern1,pwd):
    print('Length is not between 8 and 32 characters')
elif re.search(pattern2,pwd):
    print('Password contains an invalid character')
elif not re.search(pattern3,pwd):
    print('Password should contain at least one Uppercase Letter')
elif not re.search(pattern4,pwd):
    print('Password should contain at least one Lowercase Letter')
elif not re.search(pattern5,pwd):
    print('Password should contain at least one digit')
elif not re.search(pattern6,pwd):
    print('Password should contain at least one special character [#@*!&]')
elif re.search(pattern7,pwd):
    print('Password should not contain sequential identical characters')
else:
    print(pwd + ' is valid password')
