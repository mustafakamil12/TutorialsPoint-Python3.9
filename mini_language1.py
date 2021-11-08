python, java, p_num, j_num = ["Python Users", "Java Users", 8.2, 7.5]
print(f"|{python:^16}|{java:^16}|\n|{p_num:^16}|{j_num:^16}|")
print("\n")
print(f"|{python:_^16}|\n|{p_num:^16}|")
print("\n")
print("|", python.center(16, "_"), "|\n|", str(p_num).center(16), "|", sep="")
print("\n")
hours = 47
minutes = 5
quotient, minute = divmod(minutes, 60)
hour = (hours + quotient) % 24
print(f'{hour}:{minute}')
print(f'{hour:02}:{minute:02}')
print("\n")
proxima_centauri = 40208000000000
print(f'The closest star to our own is {proxima_centauri:,} km away.')
print(f'The closest star to our own is {proxima_centauri:_} km away.')
