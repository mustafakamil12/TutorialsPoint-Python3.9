t = """Track,Artist,Album,Time
Songname 1,Artist 1,Album 1,7:15
Songname 1,Artist 2,Album 2,6:27
"""
with open("t.txt","w") as w:
    w.write(t)


import csv

with open('t.txt', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for idx, row in enumerate(csv_reader):
        if idx == 0:
            print("-"*65)

        # string format mini language:
        #  {:<20} means take the n-th provided value and right align in 20 spaces
        print("|{:^20}|{:^15}|{:^20}|{:^5}|".format(*row))  # *row == row element wise
        if idx == 0:
            print("-"*65)
    print("-"*65)
