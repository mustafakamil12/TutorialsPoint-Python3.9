import re

htmCont = '''
Cecilia Chapman
711-2880 Nulla St.
Mankato Mississippi 96522
(257) 563-7401
Iris Watson
P.O. Box 283 8562 Fusce Rd.
Frederick Nebraska 20620
(372) 587-2335
Celeste Slater
606-3727 Ullamcorper. Street
Roseville NH 11523
(786) 713-8616
Theodore Lowe
Ap #867-859 Sit Rd.
Azusa New York 39531
(793) 151-6230
'''

pdata = re.findall("\(\d{3}\) \d{3}-\d{4}",htmCont)

for item in pdata:
    print(item)